from __future__ import annotations

import subprocess
from pathlib import Path

from scripts import repair_recent_daily_price_gaps as repair
from scripts import validate_recent_structured_source_repair_workflow as validator


def _texts() -> tuple[str, str, str]:
    return (
        validator.RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
        validator.HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
        validator.DAILY_FULL_WORKFLOW.read_text(encoding="utf-8"),
    )


def test_current_workflows_pass_data_only_catch_up_contract() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert validator.validate(recent_text, replay_text, daily_full_text) == []


def test_historical_replay_freshness_staging_is_exact_and_fail_closed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    command = validator.HISTORICAL_REPLAY_FRESHNESS_STAGE_COMMAND
    assert validator.validate(recent_text, replay_text, daily_full_text) == []

    mutants = {
        "missing_csv": "git add output/latest/data_freshness_latest.md",
        "missing_md": "git add output/latest/data_freshness_latest.csv",
        "broad_directory": "git add output/latest/",
        "glob": "git add output/latest/data_freshness_latest.*",
        "conditional_carrier": f"if true; then {command}; fi",
        "extra_market_session": (
            f"{command} output/latest/market_session_status_latest.json"
        ),
        "extra_release": f"{command} output/latest/daily_authority_release_latest.json",
    }
    for label, replacement in mutants.items():
        errors = validator.validate(
            recent_text,
            replay_text.replace(command, replacement, 1),
            daily_full_text,
        )
        assert errors, label

    duplicate = replay_text.replace(command, f"{command}\n          {command}", 1)
    assert validator.validate(recent_text, duplicate, daily_full_text)

    wrong_step = replay_text.replace(
        f"- name: {validator.HISTORICAL_REPLAY_FRESHNESS_STAGE_STEP}",
        "- name: Wrong artifact-family staging step",
        1,
    )
    assert validator.validate(recent_text, wrong_step, daily_full_text)


def test_repair_contract_is_not_locked_to_unrelated_workflow_bytes() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert validator.validate(
        recent_text + "\n# unrelated workflow comment\n",
        replay_text,
        daily_full_text,
    ) == []


def test_reusable_replay_concurrency_and_result_gate_are_minimal_and_fail_closed() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert "caller_concurrency_identity" not in recent_text
    assert "caller_concurrency_identity" not in replay_text
    assert validator.validate(recent_text, replay_text, daily_full_text) == []

    self_colliding = replay_text.replace(
        "group: historical-structured-source-replay-${{ github.ref }}",
        "group: daily-full-pipeline-${{ github.ref }}",
        1,
    )
    errors = validator.validate(recent_text, self_colliding, daily_full_text)
    assert any("self-collide" in error for error in errors)

    permissive_required = recent_text.replace(
        'if [ "$STRUCTURED_REPLAY_RESULT" != success ]; then',
        'if [ "$STRUCTURED_REPLAY_RESULT" != failure ]; then',
        1,
    )
    errors = validator.validate(permissive_required, replay_text, daily_full_text)
    assert any("must succeed before resume" in error for error in errors)

    caller_ceremony = recent_text.replace(
        "      expected_main_sha:",
        "      caller_concurrency_identity: fixed\n      expected_main_sha:",
        1,
    )
    errors = validator.validate(caller_ceremony, replay_text, daily_full_text)
    assert any("identity ceremony" in error for error in errors)


def test_repair_trading_date_boundary_includes_current_day_by_default() -> None:
    assert repair.latest_trading_date_on_or_before("20260820", set()) == "20260820"
    assert (
        repair.latest_trading_date_on_or_before(
            "20260820",
            set(),
            include_as_of_date=False,
        )
        == "20260819"
    )


def test_repair_continuity_must_bind_target_date_and_precede_commit() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    missing_date = recent_text.replace(
        exact_continuity,
        "python scripts/validate_daily_price_history_continuity.py",
        1,
    )
    errors = validator.validate(missing_date, replay_text, daily_full_text)
    assert any("bind the exact REPAIR_TARGET_DATE" in error for error in errors)

    moved_after_commit = recent_text.replace(exact_continuity, "echo deferred-continuity", 1).replace(
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"',
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"\n'
        f"            {exact_continuity}",
        1,
    )
    errors = validator.validate(moved_after_commit, replay_text, daily_full_text)
    assert any("before commit/push" in error for error in errors)


def test_repair_safety_validators_must_be_direct_shell_commands() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    staged_validator = (
        "python scripts/validate_recent_daily_price_repair_staged_paths.py \\"
    )
    for carrier in (
        f"echo '{exact_continuity}'",
        f"printf '%s\\n' '{exact_continuity}'",
        f"cat <<'EOF'\n          {exact_continuity}\n          EOF",
        f'result="$({exact_continuity})"',
    ):
        invalid = recent_text.replace(exact_continuity, carrier, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("one direct command" in error for error in errors)

    for carrier in (
        f"echo {staged_validator}",
        f"printf '%s\\n' '{staged_validator}'",
        f"cat <<'EOF'\n              {staged_validator}\n              EOF",
        f'result="$({staged_validator})"',
    ):
        invalid = recent_text.replace(staged_validator, carrier, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)


def test_repair_safety_gates_reject_dead_shell_control_flow() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    staged_validator = (
        "python scripts/validate_recent_daily_price_repair_staged_paths.py \\"
    )
    history_stage = "git add data/stock_price_history/"
    mutations = (
        recent_text.replace(
            continuity,
            f"if false; then\n          {continuity}\n          fi",
            1,
        ),
        recent_text.replace(
            staged_validator,
            f"if false; then\n          {staged_validator}",
            1,
        ).replace(
            '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"',
            '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"\n          fi',
            1,
        ),
        recent_text.replace(
            history_stage,
            f"if false; then\n          {history_stage}\n          fi",
            1,
        ),
        recent_text.replace(continuity, f"false && {continuity}", 1),
        recent_text.replace(
            history_stage,
            f"case never in always) {history_stage} ;; esac",
            1,
        ),
    )
    for invalid in mutations:
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            marker in error
            for error in errors
            for marker in (
                "one direct command",
                "staged-path validator",
                "exact unconditional staging step",
            )
        )


def test_repair_safety_steps_reject_skip_metadata_and_permissive_persist() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_step = "      - name: Validate exact staged current-day source recovery bundle\n"
    for metadata in (
        "        if: ${{ false }}\n",
        "        continue-on-error: true\n",
        "        shell: pwsh\n",
    ):
        invalid = recent_text.replace(staged_step, staged_step + metadata, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)

    permissive_commit = recent_text.replace(
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"',
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle" || true',
        1,
    )
    assert permissive_commit != recent_text
    errors = validator.validate(permissive_commit, replay_text, daily_full_text)
    assert any("unconditional fail-closed domain-commit" in error for error in errors)


def test_repair_rejects_duplicate_or_interposed_critical_steps() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_step = validator._step_block(
        validator._job_block(recent_text, "repair-recent-daily-price-gaps"),
        "Validate exact staged current-day source recovery bundle",
    )
    duplicate = recent_text.replace(staged_step, staged_step + staged_step, 1)
    errors = validator.validate(duplicate, replay_text, daily_full_text)
    assert any("must exist exactly once" in error for error in errors)

    staged_marker = "      - name: Validate exact staged current-day source recovery bundle\n"
    malicious_step = (
        "      - name: Premature remote mutation\n"
        "        run: |\n"
        '          git commit -m "premature"\n'
        "          git push origin HEAD:main\n\n"
    )
    interposed = recent_text.replace(
        staged_marker, malicious_step + staged_marker, 1
    )
    errors = validator.validate(interposed, replay_text, daily_full_text)
    assert any("exact adjacent" in error for error in errors)
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_unnamed_interposed_git_write_step() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_marker = "      - name: Validate exact staged current-day source recovery bundle\n"
    unnamed_write = (
        "      - run: |\n"
        '          git commit -m "premature unnamed"\n'
        "          git push origin HEAD:main\n\n"
    )
    invalid = recent_text.replace(
        staged_marker, unnamed_write + staged_marker, 1
    )
    errors = validator.validate(invalid, replay_text, daily_full_text)
    assert any("every step" in error for error in errors)
    assert any("exact adjacent" in error for error in errors)
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_safety_metadata_after_run_block() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    job_block = validator._job_block(recent_text, "repair-recent-daily-price-gaps")
    step_name = "Validate exact staged current-day source recovery bundle"
    staged_block = validator._step_block(job_block, step_name)
    assert staged_block
    for metadata in (
        "        if: ${{ false }}",
        "        continue-on-error: true",
        "        shell: pwsh",
    ):
        invalid_block = staged_block.rstrip() + f"\n{metadata}\n"
        invalid = recent_text.replace(staged_block, invalid_block, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)


def test_repair_rejects_job_level_bypass_metadata() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    job_marker = "  repair-recent-daily-price-gaps:\n"
    for metadata in (
        "    if: ${{ false }}\n",
        "    continue-on-error: true\n",
        '    "if": ${{ false }}\n',
        "    'continue-on-error': true\n",
    ):
        invalid = recent_text.replace(job_marker, job_marker + metadata, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            "job must be unconditional" in error
            or "canonical unquoted YAML" in error
            for error in errors
        )


def test_repair_rejects_git_write_in_any_other_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    rogue_job = (
        "\n  rogue-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized repository write\n"
        "        run: |\n"
        '          git commit -m "cross-job write"\n'
        "          git push origin HEAD:main\n"
    )
    errors = validator.validate(
        recent_text + rogue_job, replay_text, daily_full_text
    )
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_multiline_git_write_in_any_other_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    rogue_job = (
        "\n  rogue-multiline-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized multiline repository write\n"
        "        run: |\n"
        "          git \\\n"
        '            commit -m "cross-job write"\n'
        "          git \\\n"
        "            push origin HEAD:main\n"
    )
    errors = validator.validate(
        recent_text + rogue_job, replay_text, daily_full_text
    )
    assert any("globally unique" in error for error in errors)


def test_required_history_staging_failure_cannot_be_swallowed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    safe_stage = "git add data/stock_price_history/"
    assert safe_stage in {line.strip() for line in recent_text.splitlines()}
    assert f"{safe_stage} || true" not in recent_text

    permissive = recent_text.replace(safe_stage, f"{safe_stage} || true", 1)
    errors = validator.validate(permissive, replay_text, daily_full_text)
    assert any("must not swallow" in error for error in errors)

    missing = recent_text.replace(safe_stage, "echo skip-history-stage", 1)
    errors = validator.validate(missing, replay_text, daily_full_text)
    assert any("fail closed while staging" in error for error in errors)


def test_direct_replay_or_model_work_is_rejected() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replay_script = "replay_historical_structured" + "_sources.py"
    model_script = "build_daily_candidate_model" + "_layer.py"
    recent_text += (
        f"\nrun: python scripts/{replay_script}\n"
        f"run: python scripts/{model_script}\n"
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("must not bypass" in error for error in errors)
    assert any("must remain data-only" in error for error in errors)


def test_missing_pinned_bundle_checkout_or_ancestry_gate_is_rejected() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        "Checkout published source-bundle commit for structured catch-up planning",
        "Checkout stale source",
        1,
    ).replace(
        'git merge-base --is-ancestor "$local_sha" "$remote_main_sha"',
        'git merge-base --is-ancestor "$remote_main_sha" "$local_sha"',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("immutable source-bundle" in error for error in errors)
    assert any("current-main ancestor" in error for error in errors)


def test_reusable_workflow_definition_and_post_plan_drift_gates_are_required() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        '"$local_replay_workflow_blob_sha" != "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        '"$local_replay_workflow_blob_sha" = "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        1,
    ).replace(
        'git merge-base --is-ancestor "$local_sha" "$remote_main_sha_after_plan"',
        'git merge-base --is-ancestor "$remote_main_sha_after_plan" "$local_sha"',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("pinned reusable workflow definition drift" in error for error in errors)
    assert any("revalidate pinned ancestry" in error for error in errors)


def test_runtime_static_blocks_and_unbounded_or_nonordinary_publish_are_rejected() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        "      - name: Repair recent daily price gaps",
        "      - name: Validate workflow automation boundaries\n"
        "        run: python scripts/validate_repo_production_inventory.py\n\n"
        "      - name: Repair recent daily price gaps",
        1,
    ).replace("for push_attempt in 1 2 3", "for push_attempt in 1 2 4", 1)
    replay_text = replay_text.replace(
        "      - name: Replay structured objective sources in ascending order",
        "      - name: Validate repository automation boundaries\n"
        "        run: python scripts/validate_daily_production_boundaries.py\n\n"
        "      - name: Replay structured objective sources in ascending order",
        1,
    ).replace('git merge --no-edit "$remote_main_sha"', "git rebase origin/main", 1)
    assert "for push_attempt in 1 2 4" in recent_text
    assert "git rebase origin/main" in replay_text

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("must not execute repo-static" in error for error in errors)
    assert any("publication retries must be bounded" in error for error in errors)
    assert any("ordinary merge" in error for error in errors)


def test_all_moving_main_overlap_checks_are_rename_safe_and_counted() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    safe = '["git", "diff", "--name-only", "--no-renames", "-z"'
    unsafe = '["git", "diff", "--name-only", "-z"'
    staged_safe = "git diff --cached --name-only --no-renames -z"
    staged_unsafe = "git diff --cached --name-only -z"
    assert recent_text.count(safe) == 2
    assert replay_text.count(safe) == 2
    assert recent_text.count(staged_safe) == 2
    assert replay_text.count(staged_safe) == 1

    recent_first_unsafe = recent_text.replace(safe, unsafe, 1)
    recent_last_unsafe = unsafe.join(recent_text.rsplit(safe, 1))
    replay_first_unsafe = replay_text.replace(safe, unsafe, 1)
    replay_last_unsafe = unsafe.join(replay_text.rsplit(safe, 1))
    for invalid_recent, invalid_replay in (
        (recent_first_unsafe, replay_text),
        (recent_last_unsafe, replay_text),
        (recent_text, replay_first_unsafe),
        (recent_text, replay_last_unsafe),
    ):
        errors = validator.validate(invalid_recent, invalid_replay, daily_full_text)
        assert any("rename" in error for error in errors)
    for invalid_recent, invalid_replay in (
        (recent_text.replace(staged_safe, staged_unsafe, 1), replay_text),
        (staged_unsafe.join(recent_text.rsplit(staged_safe, 1)), replay_text),
        (recent_text, replay_text.replace(staged_safe, staged_unsafe, 1)),
    ):
        errors = validator.validate(invalid_recent, invalid_replay, daily_full_text)
        assert any("staged" in error and "rename" in error for error in errors)


def test_no_renames_diff_exposes_staged_old_path_overlap(tmp_path: Path) -> None:
    root = tmp_path / "rename-overlap"
    root.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
    subprocess.run(["git", "config", "diff.renames", "true"], cwd=root, check=True)
    staged_old = root / "output" / "latest" / "data_freshness_latest.csv"
    staged_old.parent.mkdir(parents=True)
    staged_old.write_text("status\nready\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "base"], cwd=root, check=True, capture_output=True)
    base_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    renamed = root / "docs" / "renamed_freshness.csv"
    renamed.parent.mkdir(parents=True)
    subprocess.run(
        ["git", "mv", staged_old.relative_to(root).as_posix(), renamed.relative_to(root).as_posix()],
        cwd=root,
        check=True,
    )
    subprocess.run(["git", "commit", "-m", "rename"], cwd=root, check=True, capture_output=True)
    head_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    changed = {
        item.decode("utf-8")
        for item in subprocess.check_output(
            ["git", "diff", "--name-only", "--no-renames", "-z", base_sha, head_sha, "--"],
            cwd=root,
        ).split(b"\0")
        if item
    }

    assert staged_old.relative_to(root).as_posix() in changed
    assert changed & {staged_old.relative_to(root).as_posix()}


def test_staged_and_moving_main_renames_share_the_old_path(tmp_path: Path) -> None:
    root = tmp_path / "staged-rename-overlap"
    root.mkdir()
    subprocess.run(["git", "init", "-b", "main"], cwd=root, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=root, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
    subprocess.run(["git", "config", "diff.renames", "true"], cwd=root, check=True)
    old_relative = Path("output/latest/data_freshness_latest.csv")
    old_path = root / old_relative
    old_path.parent.mkdir(parents=True)
    old_path.write_text("status\nready\n", encoding="utf-8")
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "base"], cwd=root, check=True, capture_output=True)
    base_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    remote_new = Path("docs/remote_freshness.csv")
    (root / remote_new).parent.mkdir(parents=True)
    subprocess.run(["git", "mv", old_relative.as_posix(), remote_new.as_posix()], cwd=root, check=True)
    subprocess.run(["git", "commit", "-m", "remote rename"], cwd=root, check=True, capture_output=True)
    remote_sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    subprocess.run(["git", "checkout", "--detach", base_sha], cwd=root, check=True, capture_output=True)
    staged_new = Path("archive/staged_freshness.csv")
    (root / staged_new).parent.mkdir(parents=True)
    subprocess.run(["git", "mv", old_relative.as_posix(), staged_new.as_posix()], cwd=root, check=True)
    staged = {
        item.decode("utf-8")
        for item in subprocess.check_output(
            ["git", "diff", "--cached", "--name-only", "--no-renames", "-z"],
            cwd=root,
        ).split(b"\0")
        if item
    }
    moving = {
        item.decode("utf-8")
        for item in subprocess.check_output(
            ["git", "diff", "--name-only", "--no-renames", "-z", base_sha, remote_sha, "--"],
            cwd=root,
        ).split(b"\0")
        if item
    }

    assert old_relative.as_posix() in staged
    assert old_relative.as_posix() in moving
    assert staged & moving == {old_relative.as_posix()}


def test_publish_convergence_structures_reject_exact_critical_bypasses() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    source_final = '''          if [ "$published" != true ] && \\
             [[ "$candidate_published_head_sha" =~ ^[0-9a-f]{40}$ ]] && \\
             fetch_main_bounded && \\
             git merge-base --is-ancestor "$source_bundle_commit_sha" "$candidate_published_head_sha" && \\
             git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_main_sha"; then
            published=true
            published_head_sha="$candidate_published_head_sha"
          fi
'''
    reservation_final = '''          if [ "$reservation_published" != true ] && \\
             [[ "$reservation_candidate_head_sha" =~ ^[0-9a-f]{40}$ ]] && \\
             fetch_reservation_main_bounded && \\
             git merge-base --is-ancestor "$reservation_commit_sha" "$reservation_candidate_head_sha" && \\
             git merge-base --is-ancestor "$reservation_candidate_head_sha" "$remote_main_sha"; then
            reservation_published=true
            reservation_published_head_sha="$reservation_candidate_head_sha"
          fi
'''
    historical_final = '''          if [ "$published" != true ] && \\
             [[ "$candidate_published_head_sha" =~ ^[0-9a-f]{40}$ ]] && \\
             fetch_main_bounded && \\
             git merge-base --is-ancestor "$output_commit_sha" "$candidate_published_head_sha" && \\
             git merge-base --is-ancestor "$candidate_published_head_sha" "$remote_main_sha"; then
            published=true
            published_head_sha="$candidate_published_head_sha"
          fi
'''
    source_first_ancestor = '''               git merge-base --is-ancestor "$source_bundle_commit_sha" "$candidate_published_head_sha" && \\
'''
    source_merge = '''            if ! git merge-base --is-ancestor "$remote_main_sha" HEAD; then
              git merge --no-edit "$remote_main_sha"
            fi
'''
    source_push_success = '''            if git push origin HEAD:main; then
              published=true
              published_head_sha="$candidate_published_head_sha"
              break
            fi
'''
    reservation_push_success = '''            if git push origin HEAD:main; then
              reservation_published=true
              reservation_published_head_sha="$reservation_candidate_head_sha"
              break
            fi
'''
    historical_push_success = '''            if git push origin HEAD:refs/heads/main; then
              published=true
              published_head_sha="$candidate_published_head_sha"
              break
            fi
'''
    dead_merge = '''            if ! git merge-base --is-ancestor "$remote_main_sha" HEAD; then
              if false; then
                git merge --no-edit "$remote_main_sha"
              fi
            fi
'''
    mutations = (
        (recent_text.replace(source_final, "", 1), replay_text, "post-loop"),
        (recent_text.replace(reservation_final, "", 1), replay_text, "post-loop"),
        (recent_text, replay_text.replace(historical_final, "", 1), "post-loop"),
        (recent_text.replace(source_merge, dead_merge, 1), replay_text, "ordinary merge"),
        (recent_text.replace(source_first_ancestor, "", 1), replay_text, "candidate ancestor"),
        (recent_text.replace(source_push_success, "            git push origin HEAD:main\n", 1), replay_text, "push-exit-zero"),
        (recent_text.replace(reservation_push_success, "            git push origin HEAD:main\n", 1), replay_text, "push-exit-zero"),
        (recent_text, replay_text.replace(historical_push_success, "            git push origin HEAD:refs/heads/main\n", 1), "push-exit-zero"),
    )
    for mutated_recent, mutated_replay, expected in mutations:
        assert mutated_recent != recent_text or mutated_replay != replay_text
        errors = validator.validate(mutated_recent, mutated_replay, daily_full_text)
        assert any(expected in error for error in errors), (expected, errors)


def test_repair_domain_commit_is_exactly_one_above_pinned_base() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    for token in (
        'if [ "$head_before_commit" != "$REPAIR_BASE_SHA" ]; then',
        'source_bundle_commit_count="$(git rev-list --count "$REPAIR_BASE_SHA..$source_bundle_commit_sha")"',
        'echo "::error::Repair must create exactly one source-bundle domain commit above REPAIR_BASE_SHA."',
    ):
        mutated = recent_text.replace(token, "disabled-exact-domain-commit", 1)
        assert mutated != recent_text
        errors = validator.validate(mutated, replay_text, daily_full_text)
        assert any("domain-commit" in error for error in errors)


def test_reusable_replay_rejects_inherited_or_extra_secrets() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    named_mapping = (
        "    secrets:\n"
        "      PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: "
        "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
    )
    for replacement in (
        "    secrets: inherit",
        named_mapping + "\n      OTHER_SECRET: ${{ secrets.OTHER_SECRET }}",
    ):
        invalid = recent_text.replace(named_mapping, replacement, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("must pass exactly the named" in error for error in errors)


def test_raw_repair_requires_immutable_base_push_mode() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        'git push origin HEAD:main',
        'bash scripts/ci_push_with_retry.sh main 5',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("rebase or retry" in error for error in errors)


def test_structured_replay_limit_is_independent_from_raw_repair_limit() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        "MAX_REPLAY_DATES: ${{ inputs.max_structured_replay_dates }}",
        "MAX_REPLAY_DATES: ${{ inputs.max_repair_dates }}",
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("narrower raw repair limit" in error for error in errors)


def test_reusable_replay_entrypoint_and_secret_are_required() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replay_text = replay_text.replace("workflow_call:", "disabled_workflow_call:", 1).replace(
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY:",
        "MISSING_PRODUCTION_WRITER_SECRET:",
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("reusable workflow entrypoint" in error for error in errors)
    assert any("production writer secret" in error for error in errors)


def test_reusable_replay_outputs_and_successful_caller_wiring_are_exact() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replay_mutations = (
        replay_text.replace(
            "value: ${{ jobs.replay-historical-structured-sources.outputs.published_head_sha }}",
            "value: ${{ jobs.replay-historical-structured-sources.outputs.domain_output_commit_sha }}",
            1,
        ),
        replay_text.replace(
            "published_head_sha: ${{ steps.publish_replay.outputs.published_head_sha }}",
            "published_head_sha: ${{ steps.other.outputs.published_head_sha }}",
            1,
        ),
        replay_text.replace("id: publish_replay", "id: hidden_publish", 1),
    )
    for mutated_replay in replay_mutations:
        errors = validator.validate(recent_text, mutated_replay, daily_full_text)
        assert any("output" in error or "publish step" in error for error in errors)

    caller_mutations = (
        recent_text.replace(
            'resume_published_base_sha="$REPLAY_PUBLISHED_HEAD_SHA"',
            'resume_published_base_sha="$REPAIR_PUBLISHED_HEAD_SHA"',
            1,
        ),
        recent_text.replace(
            "ref: ${{ steps.resolve_resume_head.outputs.resume_published_base_sha }}",
            "ref: ${{ needs.repair-recent-daily-price-gaps.outputs.published_head_sha }}",
            1,
        ),
        recent_text.replace(
            'git merge-base --is-ancestor "$REPLAY_DOMAIN_OUTPUT_COMMIT_SHA" "$resume_base_sha"',
            'git merge-base --is-ancestor "$resume_base_sha" "$REPLAY_DOMAIN_OUTPUT_COMMIT_SHA"',
            1,
        ),
    )
    for mutated_recent in caller_mutations:
        errors = validator.validate(mutated_recent, replay_text, daily_full_text)
        assert any("replay" in error or "resume" in error for error in errors)


def test_failed_recovery_retry_requires_exact_expected_event_head() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    for token in (
        "failed-recovery retry requires recovery_expected_head_sha",
        "if expected_head and event_head != expected_head:",
    ):
        mutated_daily = daily_full_text.replace(token, "disabled-exact-retry-head", 1)
        errors = validator.validate(recent_text, replay_text, mutated_daily)
        assert any("exact reviewed event head" in error or "different from its exact" in error for error in errors)


def test_resume_identity_polling_and_current_day_contract_fail_closed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    assert daily_full_text.count("github.run_attempt == 1") == 1
    assert daily_full_text.count("recovery dispatch requires github.run_attempt=1") == 1
    invalid_recent = recent_text.replace(
        "for completion_poll in $(seq 1 240)",
        "while true",
        1,
    ).replace(
        "gh workflow run daily_full_pipeline.yml",
        "gh workflow run other.yml",
        1,
    )
    invalid_daily = daily_full_text.replace(
        "recovery source bundle inputs must be all-or-none",
        "recovery inputs optional",
        1,
    ).replace(
        "recovery dispatch requires github.run_attempt=1",
        "recovery rerun attempts are allowed",
        1,
    ).replace(
        "if: github.run_attempt == 1 && needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'",
        "if: needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, invalid_daily)

    assert any("completion polling must be bounded" in error for error in errors)
    assert any("dispatch Daily Full exactly once" in error for error in errors)
    assert any("unapproved workflow dispatch" in error for error in errors)
    assert any("reject partial recovery identities" in error for error in errors)
    assert any("reject rerun attempts" in error for error in errors)
    assert any("independently reject rerun attempts" in error for error in errors)


def test_resume_requires_completed_authority_shortcut_and_durable_date_reservation() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace("authority-status", "authority-check-disabled").replace(
        'correlation_id="daily-source-${SOURCE_TRADING_DATE}"',
        'correlation_id="daily-source-${GITHUB_RUN_ID}"',
        1,
    ).replace("reject_existing_recovery_run", "accept_existing_recovery_run")

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("completed authority" in error for error in errors)
    assert any("per trading date" in error for error in errors)
    assert any("before POST" in error for error in errors)


def test_completed_authority_shortcut_requires_zero_raw_and_structured_changes() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        'if [ "$REPAIR_ACTION_COUNT" = 0 ] && [ "$STRUCTURED_REPLAY_REQUIRED" != true ]; then',
        "if true; then",
        1,
        ).replace(
            '--source-bundle-sha "$SOURCE_BUNDLE_SHA"',
            '--source-bundle-sha "$UNBOUND_BUNDLE_SHA"',
        )

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("true zero-change" in error for error in errors)
    assert any("exact immutable bundle identity" in error for error in errors)


def test_daily_full_recovery_is_bound_to_event_sha_and_actual_production_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "recovery event SHA mismatch",
        "recovery event SHA accepted",
        1,
    ).replace(
        "      - name: Materialize immutable recovery source bundle for production",
        "      - name: Disabled immutable recovery source bundle for production",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("ref-resolution drift" in error for error in errors)
    assert any("production job must materialize" in error for error in errors)


def test_daily_full_recovery_requires_exact_durable_reservation_inputs() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        '-f recovery_reservation_sha256="$reservation_sha256"',
        '-f recovery_reservation_sha256=""',
        1,
    )
    invalid_daily = daily_full_text.replace(
        "python -B scripts/daily_source_recovery_bundle.py verify-reservation",
        "python -B scripts/daily_source_recovery_bundle.py skip-reservation",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, invalid_daily)

    assert any("durable reservation SHA" in error for error in errors)
    assert any("canonical reservation verifier" in error for error in errors)


def test_daily_full_materializes_before_identity_and_validators() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    materialize = "      - name: Materialize immutable recovery source bundle for production"
    download = "      - name: Download market-session preflight evidence"
    invalid_daily = daily_full_text.replace(materialize, "__MATERIALIZE__", 1)
    invalid_daily = invalid_daily.replace(download, materialize, 1).replace(
        "__MATERIALIZE__", download, 1
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("before artifact identity" in error for error in errors)


def test_daily_full_requires_retained_runtime_boundary_after_materialization() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    boundary = "      - name: Validate daily production boundaries"
    materialize = "      - name: Materialize immutable recovery source bundle for production"

    missing_boundary = daily_full_text.replace(
        boundary,
        "      - name: Skip daily production boundaries",
        1,
    )
    errors = validator.validate(recent_text, replay_text, missing_boundary)
    assert any("before artifact identity" in error for error in errors)

    moved_before_materialize = daily_full_text.replace(materialize, "__MATERIALIZE__", 1)
    moved_before_materialize = moved_before_materialize.replace(
        boundary,
        materialize,
        1,
    ).replace("__MATERIALIZE__", boundary, 1)
    errors = validator.validate(recent_text, replay_text, moved_before_materialize)
    assert any("before artifact identity" in error for error in errors)


def test_recovery_daily_full_uses_a_non_deadlocking_correlation_scoped_group() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "group: ${{ inputs.recovery_retry_of_run_id != '' && format('daily-full-retry-{0}', inputs.recovery_source_bundle_trading_date) || inputs.recovery_correlation_id != '' && format('daily-full-recovery-{0}', inputs.recovery_correlation_id) || format('daily-full-pipeline-{0}', github.ref) }}",
        "group: daily-full-pipeline-${{ github.ref }}",
        1,
    )
    assert invalid_daily != daily_full_text

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("deadlocking" in error for error in errors)


def test_repair_holds_normal_production_lock_for_entire_recovery_chain() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        "  repair-recent-daily-price-gaps:\n    runs-on: ubuntu-latest",
        "  repair-recent-daily-price-gaps:\n    runs-on: ubuntu-latest\n"
        "    concurrency:\n      group: daily-full-pipeline-${{ github.ref }}",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("entire workflow" in error for error in errors)


def test_resume_prerequisite_and_dispatch_uncertainty_persist_terminal_state() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace("fail_recovery() {", "log_failure() {", 1).replace(
        "dispatch_result=uncertain",
        "dispatch_result=success",
        1,
    )
    assert invalid_recent != recent_text

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("persist a terminal state" in error for error in errors)
    assert any("uncertain dispatch acknowledgement" in error for error in errors)


def test_mutable_fetch_cannot_run_for_recovery_bundle() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''",
        "if: always()",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("skip exactly the fetch" in error for error in errors)


def test_each_mutable_source_step_is_individually_recovery_gated() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "      - name: Fetch latest official daily price\n"
        "        if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''",
        "      - name: Fetch latest official daily price\n        if: always()",
        1,
    ).replace(
        "      - name: Install dependencies\n        run: |",
        "      - name: Install dependencies\n"
        "        if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''\n        run: |",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("Fetch latest official daily price" in error for error in errors)
