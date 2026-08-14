from __future__ import annotations

import hashlib
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
RECENT_REPAIR_WORKFLOW = ROOT / ".github" / "workflows" / "repair_recent_daily_price_gaps.yml"
HISTORICAL_REPLAY_WORKFLOW = (
    ROOT / ".github" / "workflows" / "historical_structured_source_replay.yml"
)
DAILY_FULL_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RECENT_REPAIR_WORKFLOW_CANONICAL_SHA256 = (
    "51b9863503985d3d18ff064d2a29705a13e7f97baa6fd5de4d91951d20c53841"
)


def _canonical_text_sha256(text: str) -> str:
    canonical = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _job_block(text: str, job_name: str) -> str:
    pattern = re.compile(
        rf"(?ms)^  {re.escape(job_name)}:\s*\n(.*?)(?=^  [A-Za-z0-9_-]+:\s*$|\Z)"
    )
    match = pattern.search(text)
    return match.group(0) if match else ""


def _step_blocks(job_block: str, step_name: str) -> list[str]:
    pattern = re.compile(
        rf"(?ms)^      - name: {re.escape(step_name)}\s*\n(.*?)(?=^      - |\Z)"
    )
    return [match.group(0) for match in pattern.finditer(job_block)]


def _step_block(job_block: str, step_name: str) -> str:
    blocks = _step_blocks(job_block, step_name)
    return blocks[0] if len(blocks) == 1 else ""


def _step_item_blocks(job_block: str) -> list[str]:
    return [
        match.group(0)
        for match in re.finditer(r"(?ms)^      - .*?(?=^      - |\Z)", job_block)
    ]


def _step_names(job_block: str) -> list[str]:
    names: list[str] = []
    for block in _step_item_blocks(job_block):
        match = re.match(r"^      - name: (.+?)\s*$", block.splitlines()[0])
        names.append(match.group(1) if match else "")
    return names


def _step_run_executable_lines(job_block: str, step_name: str) -> list[str]:
    block = _step_block(job_block, step_name)
    lines = block.splitlines()
    try:
        run_index = next(
            index
            for index, line in enumerate(lines)
            if re.fullmatch(r"        run:\s*\|\s*", line)
        )
    except StopIteration:
        return []
    executable: list[str] = []
    heredoc_delimiter = ""
    for raw_line in lines[run_index + 1 :]:
        if raw_line.strip() and not raw_line.startswith("          "):
            break
        line = raw_line[10:].strip() if raw_line.startswith("          ") else ""
        if heredoc_delimiter:
            if line == heredoc_delimiter:
                heredoc_delimiter = ""
            continue
        if not line or line.startswith("#"):
            continue
        executable.append(line)
        heredoc = re.search(
            r"<<-?\s*(?:'([^']+)'|\"([^\"]+)\"|([A-Za-z_][A-Za-z0-9_]*))",
            line,
        )
        if heredoc:
            heredoc_delimiter = next(
                value for value in heredoc.groups() if value is not None
            )
    return executable


def _has_unique_exact_command(
    lines: list[str],
    expected_lines: tuple[str, ...],
    *,
    command_marker: str,
) -> bool:
    matching_blocks = sum(
        tuple(lines[index : index + len(expected_lines)]) == expected_lines
        for index in range(len(lines) - len(expected_lines) + 1)
    )
    marker_lines = [line for line in lines if command_marker in line]
    return matching_blocks == 1 and marker_lines == [expected_lines[0]]


def _step_has_exact_contract(
    job_block: str,
    step_name: str,
    *,
    metadata_lines: tuple[str, ...],
    executable_lines: tuple[str, ...],
) -> bool:
    block = _step_block(job_block, step_name)
    if not block:
        return False
    lines = block.splitlines()
    try:
        run_index = lines.index("        run: |")
    except ValueError:
        return False
    observed_metadata = tuple(line for line in lines[1:run_index] if line.strip())
    run_tail_is_shell_only = all(
        not line.strip() or line.startswith("          ")
        for line in lines[run_index + 1 :]
    )
    return (
        observed_metadata == metadata_lines
        and run_tail_is_shell_only
        and _step_run_executable_lines(job_block, step_name) == list(executable_lines)
    )


def _job_mapping(block: str, section: str) -> dict[str, str]:
    mapping: dict[str, str] = {}
    lines = block.splitlines()
    marker = f"    {section}:"
    in_section = False
    for line in lines:
        if not in_section:
            if line == marker:
                in_section = True
            continue
        if re.match(r"^    \S", line):
            break
        match = re.match(r"^      ([A-Za-z0-9_]+):\s*(.*?)\s*$", line)
        if match:
            mapping[match.group(1)] = match.group(2).strip("'\"")
    return mapping


def validate(recent_text: str, replay_text: str, daily_full_text: str) -> list[str]:
    errors: list[str] = []
    observed_recent_sha = _canonical_text_sha256(recent_text)
    if observed_recent_sha != RECENT_REPAIR_WORKFLOW_CANONICAL_SHA256:
        errors.append(
            "recent repair workflow canonical SHA-256 mismatch: "
            f"expected={RECENT_REPAIR_WORKFLOW_CANONICAL_SHA256} "
            f"observed={observed_recent_sha}"
        )
    workflow_call_marker = "\n  workflow_call:\n"
    workflow_dispatch_marker = "\n  workflow_dispatch:\n"
    if workflow_call_marker not in replay_text:
        errors.append("historical replay must expose a reusable workflow entrypoint")
        workflow_call_block = ""
    else:
        workflow_call_block = replay_text.split(workflow_call_marker, 1)[1]
        workflow_call_block = workflow_call_block.split(workflow_dispatch_marker, 1)[0]
    replay_required = {
        "secrets:\n      PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY:\n        required: true": (
            "reusable replay must declare only the production writer secret"
        ),
        "price_history_high_water_date:": (
            "reusable replay must preserve the raw price/history high-water"
        ),
        "expected_main_sha:": "reusable replay must bind to an immutable main SHA",
    }
    recent_required = {
        "group: daily-full-pipeline-${{ github.ref }}": (
            "raw repair must serialize with Daily Full Pipeline"
        ),
        "plan-structured-objective-source-catch-up:": (
            "structured catch-up planning must run in a separate fresh job"
        ),
        "max_structured_replay_dates:": (
            "structured catch-up must have an independent bounded replay limit"
        ),
        'default: "10"': (
            "structured catch-up default must cover the confirmed eight-session outage"
        ),
        "MAX_REPLAY_DATES: ${{ inputs.max_structured_replay_dates }}": (
            "planner must not inherit the narrower raw repair limit"
        ),
        "needs: repair-recent-daily-price-gaps": (
            "structured planning must wait for raw price/history persistence"
        ),
        "Checkout current main for structured catch-up planning": (
            "structured catch-up planning must fresh-checkout current main"
        ),
        "permissions:\n      contents: read": (
            "structured planner must use a read-only GitHub token"
        ),
        "persist-credentials: false": (
            "structured planner checkout must not persist credentials"
        ),
        "Verify and capture caller-pinned workflow definitions": (
            "raw repair must verify the exact dispatch SHA before data work"
        ),
        '"$checkout_sha" != "$remote_main_sha"': (
            "raw repair checkout must equal current remote main"
        ),
        'echo "REPAIR_BASE_SHA=$checkout_sha"': (
            "raw repair must bind outputs to an immutable base SHA"
        ),
        'git rev-parse "${CALLER_SHA}:.github/workflows/repair_recent_daily_price_gaps.yml"': (
            "raw repair must resolve its caller-pinned workflow definition blob"
        ),
        'git rev-parse "${CALLER_SHA}:.github/workflows/historical_structured_source_replay.yml"': (
            "raw repair must resolve the caller-pinned reusable definition blob"
        ),
        'git rev-parse HEAD:.github/workflows/repair_recent_daily_price_gaps.yml': (
            "raw repair must resolve its checked-out workflow definition blob"
        ),
        'git rev-parse HEAD:.github/workflows/historical_structured_source_replay.yml': (
            "raw repair must resolve the checked-out reusable definition blob"
        ),
        '"$checkout_repair_blob_sha" != "$repair_blob_sha"': (
            "raw repair must reject caller/checkout workflow definition drift"
        ),
        '"$checkout_replay_blob_sha" != "$replay_blob_sha"': (
            "raw repair must reject caller/checkout reusable definition drift"
        ),
        'remote_main_sha" != "$REPAIR_BASE_SHA"': (
            "raw repair must reject remote-main drift before committing outputs"
        ),
        'git push origin HEAD:main': (
            "raw repair must publish one fail-closed source-bundle commit without rebase/retry"
        ),
        "python scripts/validate_recent_daily_price_repair_staged_paths.py": (
            "raw repair must validate an exact data-only staged index before commit"
        ),
        '--target-date "$REPAIR_TARGET_DATE"': (
            "staged repair validation must bind the exact target date"
        ),
        '--source-base-sha "$REPAIR_BASE_SHA"': (
            "staged repair validation must bind the exact source base SHA"
        ),
        '--manifest-path "${{ steps.source_bundle.outputs.manifest_path }}"': (
            "staged repair validation must bind the exact bundle manifest path"
        ),
        '--manifest-sha256 "${{ steps.source_bundle.outputs.manifest_sha256 }}"': (
            "staged repair validation must bind the exact bundle manifest SHA"
        ),
        '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"': (
            "staged repair validation must bind the canonical bundle identity"
        ),
        "python scripts/plan_historical_structured_source_replay.py": (
            "recent repair must use the canonical bounded planner"
        ),
        'local_sha="$(git rev-parse HEAD)"': (
            "planner must capture its local immutable source"
        ),
        'remote_main_sha="$(git rev-parse origin/main)"': (
            "planner must capture origin/main"
        ),
        'if [ -z "$local_sha" ] || [ "$local_sha" != "$remote_main_sha" ]; then': (
            "planner must reject main drift before authorizing replay"
        ),
        "CALLER_REPAIR_WORKFLOW_BLOB_SHA: ${{ needs.repair-recent-daily-price-gaps.outputs.caller_repair_workflow_blob_sha }}": (
            "planner must consume the caller-pinned repair workflow blob"
        ),
        "CALLER_REPLAY_WORKFLOW_BLOB_SHA: ${{ needs.repair-recent-daily-price-gaps.outputs.caller_replay_workflow_blob_sha }}": (
            "planner must consume the caller-pinned reusable workflow blob"
        ),
        "remote_repair_workflow_blob_sha=\"$(git rev-parse origin/main:.github/workflows/repair_recent_daily_price_gaps.yml)\"": (
            "planner must resolve the fresh-main repair workflow blob"
        ),
        "remote_replay_workflow_blob_sha=\"$(git rev-parse origin/main:.github/workflows/historical_structured_source_replay.yml)\"": (
            "planner must resolve the fresh-main reusable workflow blob"
        ),
        '"$remote_repair_workflow_blob_sha" != "$CALLER_REPAIR_WORKFLOW_BLOB_SHA"': (
            "planner must reject repair workflow definition drift"
        ),
        '"$remote_replay_workflow_blob_sha" != "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"': (
            "planner must reject reusable workflow definition drift"
        ),
        'remote_main_sha_after_plan="$(git ls-remote origin refs/heads/main': (
            "planner must recheck remote main after all local validation"
        ),
        '"$remote_main_sha_after_plan" != "$local_sha"': (
            "planner must reject remote-main drift even for a no-op plan"
        ),
        "replay-structured-objective-sources:": (
            "recent repair must contain a dedicated structured replay job"
        ),
        "needs: plan-structured-objective-source-catch-up": (
            "structured replay must consume only the fresh planner result"
        ),
        "if: needs.plan-structured-objective-source-catch-up.outputs.should_replay == 'true'": (
            "structured replay must run only for an approved gap plan"
        ),
        "uses: ./.github/workflows/historical_structured_source_replay.yml": (
            "recent repair must reuse the hardened replay workflow"
        ),
        "repair_market_index_base_date: \"\"": (
            "automatic catch-up must not invent a base repair"
        ),
        "Build immutable current-day source recovery bundle": (
            "recent repair must build a durable date-scoped source bundle before commit"
        ),
        "python -B scripts/daily_source_recovery_bundle.py build": (
            "recent repair must use the canonical source bundle builder"
        ),
        "git add output/latest/official_price_fetch_latest.json": (
            "recent repair must stage the date-bound official fetch status"
        ),
        "git add output/latest/official_price_fetch_latest.md": (
            "recent repair must stage the date-bound human-readable fetch status"
        ),
        'git add output/history/daily_source_bundles/"$REPAIR_TARGET_DATE"/': (
            "recent repair must stage the immutable source bundle in the same source commit"
        ),
        "resume-daily-full-from-source-bundle:": (
            "recent repair must contain one bounded Daily Full resume job"
        ),
        "fail_recovery() {": (
            "resume uncertainty and downstream prerequisite failures must persist a terminal state"
        ),
        "STRUCTURED_PLAN_RESULT: ${{ needs.plan-structured-objective-source-catch-up.result }}": (
            "resume must observe the structured plan result even when it failed"
        ),
        "STRUCTURED_REPLAY_RESULT: ${{ needs.replay-structured-objective-sources.result }}": (
            "resume must observe the structured replay result even when it failed or was skipped"
        ),
        "source_bundle_commit_sha": "resume must retain the immutable source commit identity",
        "REPAIR_ACTION_COUNT: ${{ needs.repair-recent-daily-price-gaps.outputs.repair_action_count }}": (
            "resume must receive the exact raw repair action count"
        ),
        "STRUCTURED_REPLAY_REQUIRED: ${{ needs.plan-structured-objective-source-catch-up.outputs.should_replay }}": (
            "resume must distinguish a structured replay from a no-op plan"
        ),
        'if [ "$REPAIR_ACTION_COUNT" = 0 ] && [ "$STRUCTURED_REPLAY_REQUIRED" != true ]; then': (
            "completed authority may suppress dispatch only for a true zero-change recovery"
        ),
        "authority-status": (
            "resume must prove whether the current date already has completed authority"
        ),
        '--source-commit-sha "$SOURCE_BUNDLE_COMMIT_SHA"': (
            "authority shortcut must bind the exact immutable bundle commit"
        ),
        '--source-bundle-sha "$SOURCE_BUNDLE_SHA"': (
            "authority shortcut must bind the exact immutable bundle identity"
        ),
        "--to resume_not_required": (
            "completed same-date authority must use the no-dispatch terminal path"
        ),
        'correlation_id="daily-source-${SOURCE_TRADING_DATE}"': (
            "resume must use one durable display-title reservation per trading date"
        ),
        "reject_existing_recovery_run": (
            "resume must reject an existing same-date Daily Full run before POST"
        ),
        "python -B scripts/daily_source_recovery_bundle.py reserve": (
            "resume must persist an append-only date-scoped reservation before POST"
        ),
        'git add -- output/history/daily_source_recovery_reservations/"${SOURCE_TRADING_DATE}.json"': (
            "resume must stage only the durable reservation path"
        ),
        'git push origin HEAD:main': (
            "resume must publish the reservation with a direct fail-closed push"
        ),
        '--resume-reservation-path "$reservation_path"': (
            "resume state must retain the durable reservation path"
        ),
        '--resume-reservation-sha256 "$reservation_sha256"': (
            "resume state must retain the durable reservation SHA"
        ),
        "baseline_run_id=\"$(python - \"$existing_runs\"": (
            "resume must capture the pre-dispatch Daily Full baseline run id"
        ),
        "dispatch_started_at=\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"": (
            "resume must preserve its exact dispatch execution time"
        ),
        "expected_title=\"Daily Full Pipeline | recovery=${correlation_id}\"": (
            "resume must use an exact unique display title"
        ),
        "resume_head_sha=\"$(git rev-parse origin/main)\"": (
            "resume must bind the dispatch to an exact current-main head SHA"
        ),
        '-f recovery_expected_head_sha="$resume_head_sha"': (
            "resume must pass the reserved event head SHA to Daily Full"
        ),
        '-f recovery_reservation_path="$reservation_path"': (
            "resume must pass the exact durable reservation path to Daily Full"
        ),
        '-f recovery_reservation_sha256="$reservation_sha256"': (
            "resume must pass the exact durable reservation SHA to Daily Full"
        ),
        "--resume-workflow-run-attempt 1": "resume must bind the correlated run to attempt 1",
        "for poll_attempt in $(seq 1 30)": "resume correlation polling must be bounded",
        "for completion_poll in $(seq 1 240)": "resume completion polling must be bounded",
        "for api_attempt in 1 2 3": "resume API retries must be bounded",
        "select_correlated_run": "resume must use the exact correlation contract",
        "--to confirm_source_gate": "successful resume must close the source-gate state machine",
    }
    for literal, purpose in replay_required.items():
        if literal not in workflow_call_block:
            errors.append(f"{purpose}: missing {literal!r}")
    replay_runtime_required = {
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: ${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}": (
            "reusable replay must receive the production writer secret only in its writer job"
        ),
        'if [ -z "${PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}" ]': (
            "reusable replay must fail closed when the production writer secret is unavailable"
        ),
        'if [ "$head_before_commit" != "$REPLAY_BASE_SHA" ]; then': (
            "reusable replay must reject commits created before its only output commit"
        ),
        'git rev-list --count "$REPLAY_BASE_SHA..HEAD"': (
            "reusable replay must prove exactly one commit above its immutable base"
        ),
    }
    for literal, purpose in replay_runtime_required.items():
        if literal not in replay_text:
            errors.append(f"{purpose}: missing {literal!r}")
    for literal, purpose in recent_required.items():
        if literal not in recent_text:
            errors.append(f"{purpose}: missing {literal!r}")

    if recent_text.count(
        "uses: ./.github/workflows/historical_structured_source_replay.yml"
    ) != 1:
        errors.append("recent repair must call the reusable replay workflow exactly once")
    authority_start = recent_text.find(
        "python -B scripts/daily_source_recovery_bundle.py authority-status"
    )
    authority_end = recent_text.find('--output "$authority_path"', authority_start)
    authority_call = (
        recent_text[authority_start : authority_end + len('--output "$authority_path"')]
        if authority_start >= 0 and authority_end >= authority_start
        else ""
    )
    for literal, purpose in {
        '--source-commit-sha "$SOURCE_BUNDLE_COMMIT_SHA"': "exact immutable bundle commit",
        '--manifest-path "$SOURCE_BUNDLE_MANIFEST_PATH"': "exact immutable manifest path",
        '--manifest-sha256 "$SOURCE_BUNDLE_MANIFEST_SHA256"': "exact immutable manifest SHA",
        '--source-bundle-sha "$SOURCE_BUNDLE_SHA"': "exact immutable bundle identity",
    }.items():
        if literal not in authority_call:
            errors.append(f"authority shortcut must bind the {purpose}")
    reusable_job = _job_block(recent_text, "replay-structured-objective-sources")
    repair_job = _job_block(recent_text, "repair-recent-daily-price-gaps")
    if "    concurrency:" in repair_job:
        errors.append(
            "recent repair must hold the shared Daily Full concurrency lock for the entire workflow"
        )
    forbidden_job_keys = {"if", "continue-on-error"}
    for line in repair_job.splitlines():
        match = re.match(r"^    (\S[^:\n]*?)\s*:", line)
        if not match:
            continue
        raw_key = match.group(1).strip()
        if raw_key.startswith(("'", '"', "?")):
            errors.append(
                "recent repair job keys must use canonical unquoted YAML spelling"
            )
            continue
        if raw_key in forbidden_job_keys:
            errors.append(
                "recent repair job must be unconditional and fail closed; forbidden "
                f"job key: {raw_key}"
            )
    expected_secrets = {
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY": (
            "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
        )
    }
    if _job_mapping(reusable_job, "secrets") != expected_secrets:
        errors.append(
            "recent repair reusable replay job must pass exactly the named production "
            "writer secret and must not inherit or add secrets"
        )

    forbidden = {
        "python scripts/replay_historical_structured_sources.py": (
            "must not bypass the reusable replay workflow"
        ),
        "actions/github-script": "must not self-dispatch GitHub Actions",
        "build_daily_candidate_model_layer.py": "must remain data-only",
        "research_backtest_pipeline": "must remain data-only",
        "generate_chatgpt_side_daily_reports.py": "must remain data-only",
        "git add output/latest/all_candidates": "must not stage candidate outputs",
        "git add output/history/daily_model": "must not stage model outputs",
        "git add published_reports": "must not stage published reports",
        "git add chatgpt_side_outputs": "must not stage PDF outputs",
        "git add output/latest/market_session_status_latest.json": (
            "must not publish the authoritative market-session surface"
        ),
    }
    for literal, purpose in forbidden.items():
        if literal in recent_text:
            errors.append(f"recent structured-source catch-up {purpose}: found {literal!r}")
    if "ci_push_with_retry.sh" in recent_text:
        errors.append("recent source-bundle commit must not rebase or retry a post-validation push")
    if recent_text.count("gh workflow run daily_full_pipeline.yml") != 1:
        errors.append("recent recovery must dispatch Daily Full exactly once")
    uncertainty_failures = (
        "Unable to list existing Daily Full recovery runs after bounded API retries",
        "Daily Full recovery run already exists for this trading date",
        "Daily Full recovery dispatch reservation already exists for this trading date",
        "Durable recovery reservation staged path set is not exact",
        "Durable Daily Full recovery reservation push failed or is uncertain",
        "Durable recovery reservation commit does not equal remote main",
        "Daily Full dispatch command failed or is uncertain",
        "Unable to list Daily Full runs after bounded API retries",
        "Daily Full run correlation is ambiguous or invalid",
        "No unique Daily Full run matched the bounded dispatch window",
        "Unable to poll Daily Full completion after bounded API retries",
        "Daily Full completion identity changed or is invalid",
    )
    for message in uncertainty_failures:
        if f'fail_recovery "{message}' not in recent_text:
            errors.append(
                "recent recovery must persist every dispatch/API/correlation uncertainty "
                f"as terminal: missing {message!r}"
            )
    other_dispatches = [
        line.strip()
        for line in recent_text.splitlines()
        if "gh workflow run" in line and "daily_full_pipeline.yml" not in line
    ]
    if other_dispatches:
        errors.append(f"recent recovery contains an unapproved workflow dispatch: {other_dispatches}")
    if "git add output/latest/data_freshness_latest" in replay_text:
        errors.append(
            "historical structured-source replay must not independently publish the authoritative freshness surface"
        )
    if "write_files=False" not in (ROOT / "scripts" / "repair_recent_daily_price_gaps.py").read_text(
        encoding="utf-8"
    ):
        errors.append("recent repair market-session preflight must be decision-only with write_files=False")
    repair_script = (ROOT / "scripts" / "repair_recent_daily_price_gaps.py").read_text(
        encoding="utf-8"
    )
    if "publish_official_price_evidence_transaction" not in repair_script:
        errors.append(
            "current-day repair must publish official price CSV/JSON/MD through the canonical transaction"
        )
    for literal, message in {
        "deferred_transaction=True": (
            "current-day repair must defer official latest commit until confirmation and continuity pass"
        ),
        "commit_official_price_evidence_transaction": (
            "current-day repair must durably commit the deferred official latest transaction"
        ),
        "recover_official_price_evidence_transaction": (
            "current-day repair must roll back failed deferred official latest transactions"
        ),
    }.items():
        if literal not in repair_script:
            errors.append(f"{message}: missing {literal!r}")
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    repair_job = _job_block(recent_text, "repair-recent-daily-price-gaps")
    exact_env_metadata = (
        "        env:",
        "          REPAIR_TARGET_DATE: ${{ steps.repair_result.outputs.target_end_date }}",
    )
    expected_target_date_identity = (
        'if [[ ! "$REPAIR_TARGET_DATE" =~ ^20[0-9]{6}$ ]]; then',
        'echo "::error::Recent repair target date is invalid or missing: $REPAIR_TARGET_DATE"',
        "exit 1",
        "fi",
    )
    expected_staged_validation = (
        "python scripts/validate_recent_daily_price_repair_staged_paths.py \\",
        '--target-date "$REPAIR_TARGET_DATE" \\',
        '--source-base-sha "$REPAIR_BASE_SHA" \\',
        '--manifest-path "${{ steps.source_bundle.outputs.manifest_path }}" \\',
        '--manifest-sha256 "${{ steps.source_bundle.outputs.manifest_sha256 }}" \\',
        '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"',
    )
    expected_stage = (
        'git config user.name "github-actions"',
        'git config user.email "github-actions@github.com"',
        "git add data/daily_price/ || true",
        "git add data/stock_price_history/",
        "git add output/latest/recent_daily_price_gap_repair_latest.* || true",
        "git add output/latest/repair_daily_price_range_latest.* || true",
        "git add output/latest/repair_daily_price_range_check_code_latest.csv || true",
        "git add output/latest/stock_price_history_manifest.* || true",
        "git add output/latest/daily_price_history_continuity_latest.* || true",
        "git add output/latest/official_daily_price_latest.csv",
        "git add output/latest/official_price_fetch_latest.json",
        "git add output/latest/official_price_fetch_latest.md",
        "git add docs/latest/stock_price_history_manifest.* || true",
        'git add output/history/daily_source_bundles/"$REPAIR_TARGET_DATE"/"${{ steps.source_bundle.outputs.release_id }}"/',
        "git status --short",
        "if git diff --cached --quiet; then",
        'echo "::error::Immutable source bundle produced no staged commit."',
        "exit 1",
        "fi",
    )
    expected_persist = (
        'remote_main_sha="$(git ls-remote origin refs/heads/main | awk \'{print $1}\')"',
        'if [ -z "$remote_main_sha" ] || [ "$remote_main_sha" != "$REPAIR_BASE_SHA" ]; then',
        'echo "::error::Remote main drifted during recent price repair; refusing to commit or rebase stale outputs."',
        "exit 1",
        "fi",
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"',
        "git push origin HEAD:main",
        'local_sha="$(git rev-parse HEAD)"',
        'remote_main_sha="$(git ls-remote origin refs/heads/main | awk \'{print $1}\')"',
        'if [ -z "$remote_main_sha" ] || [ "$local_sha" != "$remote_main_sha" ]; then',
        'echo "::error::Remote main does not equal the persisted recent price repair commit."',
        "exit 1",
        "fi",
        'echo "source_bundle_commit_sha=$local_sha" >> "$GITHUB_OUTPUT"',
    )
    history_stage = "git add data/stock_price_history/"
    if f"{history_stage} || true" in recent_text:
        errors.append(
            "recent repair must not swallow required stock-price history staging failure"
        )
    elif not _step_has_exact_contract(
        repair_job,
        "Stage exact current-day source recovery bundle",
        metadata_lines=(),
        executable_lines=expected_stage,
    ):
        errors.append(
            "recent repair must use the exact unconditional staging step and fail "
            "closed while staging required stock-price history"
        )
    if not _step_has_exact_contract(
        repair_job,
        "Validate repaired target-date identity",
        metadata_lines=exact_env_metadata,
        executable_lines=expected_target_date_identity,
    ):
        errors.append(
            "recent repair target-date identity must be one unconditional exact step"
        )
    if not _step_has_exact_contract(
        repair_job,
        "Validate exact repaired target-date continuity",
        metadata_lines=exact_env_metadata,
        executable_lines=(exact_continuity,),
    ):
        errors.append(
            "recent repair continuity validation must be one direct command, bind "
            "the exact REPAIR_TARGET_DATE, and run before commit/push"
        )
    staged_validator_is_exact = _step_has_exact_contract(
        repair_job,
        "Validate exact staged current-day source recovery bundle",
        metadata_lines=(),
        executable_lines=expected_staged_validation,
    )
    if not staged_validator_is_exact:
        errors.append(
            "recent repair staged-path validator must be one exact direct command"
        )
    critical_step_names = (
        "Summarize recent repair result",
        "Validate repaired target-date identity",
        "Validate exact repaired target-date continuity",
        "Build immutable current-day source recovery bundle",
        "Upload recent daily price gap repair evidence",
        "Stage exact current-day source recovery bundle",
        "Validate exact staged current-day source recovery bundle",
        "Commit repaired recent daily price gaps",
    )
    observed_step_names = _step_names(repair_job)
    if any(not name for name in observed_step_names):
        errors.append(
            "recent repair requires every step to be explicitly named so ordering and "
            "write boundaries remain auditable"
        )
    critical_indices: list[int] = []
    for name in critical_step_names:
        if observed_step_names.count(name) != 1:
            errors.append(
                f"recent repair critical step must exist exactly once: {name}"
            )
        else:
            critical_indices.append(observed_step_names.index(name))
    if len(critical_indices) != len(critical_step_names) or critical_indices != list(
        range(critical_indices[0], critical_indices[0] + len(critical_indices))
    ):
        errors.append(
            "recent repair must keep the exact adjacent continuity, bundle, stage, "
            "validation, and persistence step sequence"
        )
    if not _step_has_exact_contract(
        repair_job,
        "Commit repaired recent daily price gaps",
        metadata_lines=("        id: persist_bundle",),
        executable_lines=expected_persist,
    ):
        errors.append(
            "recent repair must use one exact fail-closed commit/push step"
        )
    normalized_git_scan_text = re.sub(
        r"\\[ \t]*\r?\n[ \t]*", " ", recent_text
    )
    git_write_lines = [
        line.strip()
        for line in normalized_git_scan_text.splitlines()
        if re.search(
            r"\bgit(?:\s+(?:-[^\s]+\s+\S+))*\s+(?:commit|push)\b",
            line,
        )
    ]
    expected_git_write_lines = [
        expected_persist[5],
        expected_persist[6],
        'git commit -m "Reserve Daily Full recovery for ${SOURCE_TRADING_DATE}"',
        "if ! git push origin HEAD:main; then",
    ]
    if git_write_lines != expected_git_write_lines:
        errors.append(
            "recent repair Git commit/push commands must be globally unique and "
            "confined to the exact persistence and recovery-reservation steps"
        )

    daily_full_required = {
        "run-name: ${{ inputs.recovery_correlation_id != '' && format('Daily Full Pipeline | recovery={0}', inputs.recovery_correlation_id) || 'Daily Full Pipeline' }}": (
            "Daily Full must expose the exact recovery display-title contract"
        ),
        "recovery_expected_head_sha:": "Daily Full must declare the reserved event head input",
        "recovery_reservation_path:": "Daily Full must declare the durable reservation path input",
        "recovery_reservation_sha256:": "Daily Full must declare the durable reservation SHA input",
        "recovery event SHA mismatch": "Daily Full must reject ref-resolution drift before source work",
        "recovery correlation id must equal the date-scoped bundle identity": (
            "Daily Full must reject arbitrary recovery concurrency identities"
        ),
        "ref: ${{ github.sha }}": "Daily Full preflight must checkout its immutable event SHA",
        "group: ${{ inputs.recovery_correlation_id != '' && format('daily-full-recovery-{0}', inputs.recovery_correlation_id) || format('daily-full-pipeline-{0}', github.ref) }}": (
            "Daily Full recovery must avoid deadlocking behind the repair workflow while normal runs remain serialized"
        ),
        "recovery_source_bundle_commit_sha:": "Daily Full must declare immutable source commit input",
        "recovery_source_bundle_manifest_path:": "Daily Full must declare exact manifest path input",
        "recovery_source_bundle_manifest_sha256:": "Daily Full must declare exact manifest SHA input",
        "recovery_source_bundle_sha:": "Daily Full must declare canonical bundle identity input",
        "recovery_source_bundle_trading_date:": "Daily Full must declare exact recovery date input",
        "recovery source bundle inputs must be all-or-none": (
            "Daily Full must reject partial recovery identities"
        ),
        "recovery dispatch requires github.run_attempt=1": (
            "Daily Full must reject rerun attempts for a reserved recovery dispatch"
        ),
        "Materialize immutable recovery source bundle for preflight": (
            "Daily Full preflight must materialize the immutable source bundle"
        ),
        "Verify durable recovery dispatch reservation": (
            "Daily Full must reject recovery dispatches without an exact reservation commit"
        ),
        "verify-reservation": "Daily Full must use the canonical reservation verifier",
        "Materialize immutable recovery source bundle for production": (
            "Daily Full production must independently rematerialize the immutable source bundle"
        ),
        "materialize_market_session_preflight_artifact": (
            "Daily Full must carry and validate preflight identity through the canonical helper"
        ),
        "if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''": (
            "mutable price acquisition must be skipped for a verified recovery bundle"
        ),
    }
    for literal, purpose in daily_full_required.items():
        if literal not in daily_full_text:
            errors.append(f"{purpose}: missing {literal!r}")
    if daily_full_text.count("python -B scripts/daily_source_recovery_bundle.py verify \\") != 2:
        errors.append("Daily Full must verify the immutable source bundle exactly twice")
    if daily_full_text.count("if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''") != 3:
        errors.append("Daily Full must skip exactly the fetch, inspect, and repair mutable source steps")
    daily_full_job = _job_block(daily_full_text, "daily-full-pipeline")
    preflight_job = _job_block(daily_full_text, "market-session-preflight")
    pdf_job = _job_block(daily_full_text, "daily-pdf-dfkai-replay")
    production_required = {
        "if: github.run_attempt == 1 && needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'": (
            "production job must independently reject rerun attempts"
        ),
        "RECOVERY_EXPECTED_HEAD_SHA: ${{ inputs.recovery_expected_head_sha }}": (
            "production job must receive the reserved event SHA"
        ),
        "RECOVERY_SOURCE_BUNDLE_COMMIT_SHA: ${{ inputs.recovery_source_bundle_commit_sha }}": (
            "production job must receive the immutable bundle commit"
        ),
        "RECOVERY_RESERVATION_PATH: ${{ inputs.recovery_reservation_path }}": (
            "production job must receive the exact reservation path"
        ),
        "RECOVERY_RESERVATION_SHA256: ${{ inputs.recovery_reservation_sha256 }}": (
            "production job must receive the exact reservation SHA"
        ),
        "RECOVERY_SOURCE_BUNDLE_MANIFEST_PATH: ${{ inputs.recovery_source_bundle_manifest_path }}": (
            "production job must receive the exact bundle manifest path"
        ),
        "RECOVERY_SOURCE_BUNDLE_MANIFEST_SHA256: ${{ inputs.recovery_source_bundle_manifest_sha256 }}": (
            "production job must receive the exact bundle manifest SHA"
        ),
        "RECOVERY_SOURCE_BUNDLE_SHA: ${{ inputs.recovery_source_bundle_sha }}": (
            "production job must receive the canonical bundle SHA"
        ),
        "RECOVERY_SOURCE_BUNDLE_TRADING_DATE: ${{ inputs.recovery_source_bundle_trading_date }}": (
            "production job must receive the exact bundle trading date"
        ),
        "Materialize immutable recovery source bundle for production": (
            "production job must materialize the immutable bundle before validators and producers"
        ),
        "materialize_market_session_preflight_artifact": (
            "production job must verify the downloaded preflight identity through the canonical helper"
        ),
    }
    for literal, purpose in production_required.items():
        if literal not in daily_full_job:
            errors.append(f"{purpose}: missing {literal!r} from daily-full-pipeline job")
    if daily_full_job.count("if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''") != 3:
        errors.append("Daily Full production job must skip exactly its three mutable source steps")
    for step_name in (
        "Fetch latest official daily price",
        "Inspect official daily price fetch result",
        "Repair missing daily price source files",
    ):
        step = _step_block(daily_full_job, step_name)
        if "if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''" not in step:
            errors.append(
                f"Daily Full mutable source step must be recovery-gated: {step_name}"
            )
    if "Materialize immutable recovery source bundle for production" in pdf_job:
        errors.append("PDF replay job must not materialize the Daily Full recovery source bundle")
    reservation_position = preflight_job.find("Verify durable recovery dispatch reservation")
    preflight_materialize_position = preflight_job.find(
        "Materialize immutable recovery source bundle for preflight"
    )
    if (
        reservation_position < 0
        or preflight_materialize_position < 0
        or reservation_position >= preflight_materialize_position
    ):
        errors.append(
            "Daily Full preflight must verify the durable reservation before bundle materialization"
        )
    production_order = (
        "Materialize immutable recovery source bundle for production",
        "Download market-session preflight evidence",
        "Validate market-session preflight artifact identity",
        "Capture pre-run freshness baseline",
        "Validate Apps Script workflow triggers",
    )
    positions = [daily_full_job.find(literal) for literal in production_order]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append(
            "Daily Full production must materialize the immutable bundle before artifact identity and all validators"
        )

    ordered = (
        "Build immutable current-day source recovery bundle",
        "Commit repaired recent daily price gaps",
        "plan-structured-objective-source-catch-up:",
        "Checkout current main for structured catch-up planning",
        "Plan bounded structured objective-source catch-up",
        "git fetch origin main",
        "remote_repair_workflow_blob_sha=",
        "remote_replay_workflow_blob_sha=",
        "python scripts/plan_historical_structured_source_replay.py",
        "remote_main_sha_after_plan=",
        "replay-structured-objective-sources:",
        "uses: ./.github/workflows/historical_structured_source_replay.yml",
        "resume-daily-full-from-source-bundle:",
        "Verify bundle and dispatch exactly one Daily Full resume",
        "reject_existing_recovery_run",
        "python -B scripts/daily_source_recovery_bundle.py reserve",
        'git push origin HEAD:main',
        "gh workflow run daily_full_pipeline.yml",
    )
    cursor = -1
    for literal in ordered:
        position = recent_text.find(literal, cursor + 1)
        if position < 0:
            errors.append(
                "recent structured-source catch-up order is incomplete or invalid: "
                f"expected {literal!r} after position {cursor}"
            )
            break
        cursor = position
    return errors


def main() -> int:
    errors: list[str] = []
    if not RECENT_REPAIR_WORKFLOW.exists():
        errors.append(f"missing workflow: {RECENT_REPAIR_WORKFLOW}")
    if not HISTORICAL_REPLAY_WORKFLOW.exists():
        errors.append(f"missing workflow: {HISTORICAL_REPLAY_WORKFLOW}")
    if not DAILY_FULL_WORKFLOW.exists():
        errors.append(f"missing workflow: {DAILY_FULL_WORKFLOW}")
    if not errors:
        errors.extend(
            validate(
                RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
                HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
                DAILY_FULL_WORKFLOW.read_text(encoding="utf-8"),
            )
        )
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] recent structured-source repair workflow contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
