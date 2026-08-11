from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
RECENT_REPAIR_WORKFLOW = ROOT / ".github" / "workflows" / "repair_recent_daily_price_gaps.yml"
HISTORICAL_REPLAY_WORKFLOW = (
    ROOT / ".github" / "workflows" / "historical_structured_source_replay.yml"
)


def _job_block(text: str, job_name: str) -> str:
    pattern = re.compile(
        rf"(?ms)^  {re.escape(job_name)}:\s*\n(.*?)(?=^  [A-Za-z0-9_-]+:\s*$|\Z)"
    )
    match = pattern.search(text)
    return match.group(0) if match else ""


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


def validate(recent_text: str, replay_text: str) -> list[str]:
    errors: list[str] = []
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
        'export CI_PUSH_EXPECTED_REMOTE_SHA="$REPAIR_BASE_SHA"': (
            "raw repair push helper must use immutable-base mode"
        ),
        "python scripts/validate_recent_daily_price_repair_staged_paths.py": (
            "raw repair must validate an exact data-only staged index before commit"
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
    reusable_job = _job_block(recent_text, "replay-structured-objective-sources")
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
        "gh workflow run": "must not self-dispatch GitHub Actions",
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
    if "git add output/latest/data_freshness_latest" in replay_text:
        errors.append(
            "historical structured-source replay must not independently publish the authoritative freshness surface"
        )
    if "write_files=False" not in (ROOT / "scripts" / "repair_recent_daily_price_gaps.py").read_text(
        encoding="utf-8"
    ):
        errors.append("recent repair market-session preflight must be decision-only with write_files=False")

    ordered = (
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
    if not errors:
        errors.extend(
            validate(
                RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
                HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
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
