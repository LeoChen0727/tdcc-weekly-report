from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import re
import subprocess
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "output" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.csv"
MD_PATH = ROOT / "output" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.md"
DOCS_CSV_PATH = ROOT / "docs" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.csv"
DOCS_MD_PATH = ROOT / "docs" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.md"
MANIFEST_PATH = ROOT / "output" / "history" / "daily_model_snapshots" / "daily_published_model_snapshot_manifest.csv"

AUDIT_VERSION = "volume_v2_warrant_lineage_history_audit_v5"
CURRENT_SOURCE_RESOLUTION = "current_worktree_exact_source_files"
CURRENT_PENDING_REVISION_SOURCE_RESOLUTION = (
    "current_worktree_pending_same_date_revision_exact_sources"
)
PUBLISHED_PENDING_SOURCE_RESOLUTION = (
    "published_snapshot_exact_current_sources_pending_commit"
)
LEGACY_HISTORY_COMPLETE = "complete"
LEGACY_HISTORY_INCOMPLETE = "incomplete_fail_closed"
LEGACY_REVISION_RECOVERED = "legacy_git_manifest_recovered"
VERSIONED_REVISION_EXACT = "versioned_revision_exact"
CURRENT_REVISION_PENDING = "current_pending_snapshot"
FORMAL_ROW_TYPE = "formal_row"
REVISION_COVERAGE_ROW_TYPE = "revision_coverage"

MANIFEST_IDENTITY_COLUMNS = [
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
    "daily_pdf_ready",
    "artifact_id",
    "source_path",
    "snapshot_path",
    "source_sha256",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
]
REVISION_MANIFEST_COLUMNS = (
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
)
VOLUME_V2_MODELS = frozenset(
    {
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
        "volume_range_breakout_v2_high_position_volume_attack",
    }
)
BULLISH_WARRANT_SIGNALS = frozenset(
    {"call_inflow", "call_strong_inflow", "call_put_bullish"}
)
WARRANT_BONUS_BY_MODEL = {
    "volume_range_breakout_v2_low_position_volume_attack": Decimal("2"),
    "volume_range_breakout_v2_mid_position_momentum_attack": Decimal("2"),
    "volume_range_breakout_v2_high_position_volume_attack": Decimal("0"),
}

COLLISION_FIELDS = (
    "warrant_flow_signal",
    "tdcc_status",
    "false_breakout_risk",
)
POSITIVE_TDCC_STATUSES = frozenset({"strong_accumulation", "mild_accumulation"})
TRUTHY_VALUES = frozenset({"true", "1", "yes", "y", "t"})
MODEL_COLLISION_COMPONENT_POLICY = {
    "volume_range_breakout_v2_low_position_volume_attack": {
        "warrant_base_bonus": Decimal("2"),
        "tdcc_positive_base_bonus": Decimal("4"),
        "tdcc_distribution_base_penalty": Decimal("6"),
        "false_breakout_base_penalty": Decimal("4"),
        "tdcc_positive_score_bonus": Decimal("4"),
        "tdcc_distribution_risk_penalty": Decimal("6"),
        "false_breakout_risk_penalty": Decimal("4"),
    },
    "volume_range_breakout_v2_mid_position_momentum_attack": {
        "warrant_base_bonus": Decimal("2"),
        "tdcc_positive_base_bonus": Decimal("4"),
        "tdcc_distribution_base_penalty": Decimal("6"),
        "false_breakout_base_penalty": Decimal("4"),
        "tdcc_positive_score_bonus": Decimal("4"),
        "tdcc_distribution_risk_penalty": Decimal("6"),
        "false_breakout_risk_penalty": Decimal("4"),
    },
    "volume_range_breakout_v2_high_position_volume_attack": {
        "warrant_base_bonus": Decimal("0"),
        "tdcc_positive_base_bonus": Decimal("0"),
        "tdcc_distribution_base_penalty": Decimal("0"),
        "false_breakout_base_penalty": Decimal("0"),
        "tdcc_positive_score_bonus": Decimal("4"),
        "tdcc_distribution_risk_penalty": Decimal("0"),
        "false_breakout_risk_penalty": Decimal("0"),
    },
}

FORMAL_SOURCE_PATH = "output/latest/daily_candidate_model_signals_for_report_latest.csv"
WATCH_SOURCE_PATH = "output/latest/volume_breakout_watch_latest.csv"
CANDIDATE_SOURCE_PATH = "output/latest/all_candidates_latest.csv"
OFFICIAL_WARRANT_SOURCE_PATH = "output/latest/warrant_flow_latest.csv"
PRODUCTION_CODE_PATH = "scripts/build_daily_candidate_model_layer.py"

AUDIT_COLUMNS = [
    "audit_version",
    "audit_row_type",
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
    "legacy_revision_history_status",
    "legacy_precontract_revision_history_status",
    "revision_formal_row_count",
    "historical_promotion_evidence_eligible",
    "expected_session_status",
    "pipeline_commit_sha",
    "snapshot_commit_sha",
    "paired_source_commit_sha",
    "paired_source_resolution",
    "dispatcher_warrant_source_mode",
    "production_code_sha256",
    "formal_snapshot_path",
    "formal_snapshot_sha256",
    "formal_snapshot_manifest_v1_sha256",
    "watch_artifact_path",
    "watch_artifact_sha256",
    "candidate_artifact_path",
    "candidate_artifact_sha256",
    "official_warrant_artifact_path",
    "official_warrant_artifact_sha256",
    "manifest_row_sha256",
    "formal_row_sha256",
    "watch_row_sha256",
    "candidate_row_sha256",
    "candidate_row_present",
    "official_warrant_row_sha256",
    "official_warrant_row_present",
    "formal_row_number",
    "watch_row_number",
    "candidate_row_number",
    "official_warrant_row_number",
    "signal_date",
    "report_line",
    "model_id",
    "stock_id",
    "source_row_index",
    "watch_warrant_signal",
    "candidate_warrant_signal",
    "official_warrant_signal",
    "formal_warrant_signal",
    "watch_source_score",
    "candidate_source_score",
    "watch_source_rank",
    "candidate_source_rank",
    "watch_candidate_score_collision",
    "watch_candidate_rank_collision",
    "canonical_warrant_source_type",
    "published_warrant_score_source",
    "published_warrant_basis_signal",
    "watch_tdcc_status",
    "candidate_tdcc_status",
    "published_tdcc_status",
    "counterfactual_tdcc_status",
    "watch_false_breakout_risk",
    "candidate_false_breakout_risk",
    "published_false_breakout_risk",
    "counterfactual_false_breakout_risk",
    "published_tdcc_positive",
    "counterfactual_tdcc_positive",
    "published_tdcc_distribution",
    "counterfactual_tdcc_distribution",
    "published_score_context",
    "counterfactual_score_context",
    "collision_fields",
    "published_counterfactual_collision_fields",
    "warrant_bonus_points",
    "published_warrant_bonus_points",
    "counterfactual_warrant_bonus_points",
    "published_collision_component_effects",
    "counterfactual_collision_component_effects",
    "published_base_model_score",
    "counterfactual_base_model_score",
    "base_model_score_delta",
    "published_operation_score",
    "published_tdcc_score",
    "counterfactual_tdcc_score",
    "tdcc_score_delta",
    "published_pattern_score",
    "published_risk_penalty",
    "counterfactual_risk_penalty",
    "risk_penalty_delta",
    "published_component_replay_final_rank_score",
    "published_component_replay_rounding_gap",
    "published_component_replay_match",
    "published_final_rank_score",
    "counterfactual_final_rank_score",
    "score_delta",
    "replay_status",
    "replay_error",
    "published_model_rank",
    "counterfactual_model_rank",
    "rank_delta",
    "rank_replay_status",
    "watch_candidate_collision",
    "candidate_official_match",
    "formal_candidate_match",
    "watch_disposition",
    "formal_row_disposition",
    "impact_scope",
    "evidence_status",
    "reason",
]


def canonical_text_bytes(payload: bytes) -> bytes:
    """Match the repo text-hash contract across Windows and Git blobs."""

    text_payload = payload.decode("utf-8-sig")
    return text_payload.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(canonical_text_bytes(payload)).hexdigest()


def manifest_v1_sha256_candidates(payload: bytes) -> set[str]:
    """Read-only compatibility for immutable raw/LF/CRLF manifest-v1 hashes."""

    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {
        hashlib.sha256(candidate).hexdigest()
        for candidate in (payload, lf, crlf)
    }


def text(value: Any) -> str:
    if value is None:
        return ""
    normalized = str(value).strip()
    return "" if normalized.lower() == "nan" else normalized


def independent_normalize_revision_manifest_schema(
    manifest: pd.DataFrame,
    source: str,
) -> pd.DataFrame:
    """Independently reject partial revision schemas and normalize legacy r1."""

    present = set(REVISION_MANIFEST_COLUMNS) & set(manifest.columns)
    if present and len(present) != len(REVISION_MANIFEST_COLUMNS):
        missing = sorted(set(REVISION_MANIFEST_COLUMNS) - present)
        raise RuntimeError(
            "snapshot manifest has a partial revision schema; "
            "snapshot_revision, supersedes_snapshot_sha256, and revision_reason "
            "must be all present or all absent for legacy r1: "
            f"source={source} present={sorted(present)} missing={missing}"
        )
    normalized = manifest.copy()
    if not present:
        normalized["snapshot_revision"] = "r1"
        normalized["supersedes_snapshot_sha256"] = ""
        normalized["revision_reason"] = "legacy_v1_manifest"
    elif normalized["snapshot_revision"].map(text).eq("").any():
        blank_rows = normalized.index[
            normalized["snapshot_revision"].map(text).eq("")
        ].tolist()
        raise RuntimeError(
            "snapshot manifest snapshot_revision must not be blank when the "
            f"revision schema is present: source={source} rows={blank_rows}"
        )
    return normalized


def normalize_snapshot_revision(value: Any) -> str:
    revision = text(value)
    match = re.fullmatch(r"r([1-9][0-9]*)", revision)
    if not match:
        raise RuntimeError(f"invalid snapshot_revision: {revision!r}")
    return f"r{int(match.group(1))}"


def snapshot_revision_number(value: Any) -> int:
    return int(normalize_snapshot_revision(value)[1:])


def expected_manifest_data_row_count(
    value: Any,
    *,
    report_date: str,
    snapshot_revision: str,
) -> int:
    row_count = text(value)
    if not re.fullmatch(r"0|[1-9][0-9]*", row_count):
        raise RuntimeError(
            "model_signals_for_report manifest row_count must be a nonnegative "
            "integer: "
            f"report_date={report_date} revision={snapshot_revision} "
            f"value={row_count!r}"
        )
    return int(row_count)


def audit_revision_sort_key(value: Any) -> tuple[int, int]:
    revision = text(value)
    legacy_match = re.fullmatch(r"legacy_r([1-9][0-9]*)", revision)
    if legacy_match:
        return (0, int(legacy_match.group(1)))
    return (1, snapshot_revision_number(revision))


def stock_id(value: Any) -> str:
    normalized = text(value)
    if normalized.endswith(".0"):
        normalized = normalized[:-2]
    digits = re.sub(r"[^0-9]", "", normalized)
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def warrant_signal(value: Any) -> str:
    return text(value).lower()


def row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {str(key): text(value) for key, value in values.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256_bytes(payload)


def decimal(value: Any, field: str) -> Decimal:
    normalized = text(value)
    try:
        return Decimal(normalized)
    except InvalidOperation as exc:
        raise ValueError(f"invalid decimal {field}={normalized!r}") from exc


def integer(value: Any, field: str) -> int:
    number = decimal(value, field)
    if number != number.to_integral():
        raise ValueError(f"invalid integer {field}={value!r}")
    return int(number)


def decimal_text(value: Decimal, reference: str = "") -> str:
    if value == value.to_integral():
        if "." in reference:
            places = len(reference.partition(".")[2])
            return f"{value:.{places}f}"
        return str(value.to_integral())
    normalized = format(value.normalize(), "f")
    return normalized.rstrip("0").rstrip(".") if "." in normalized else normalized


def truthy(value: Any) -> bool:
    return text(value).lower() in TRUTHY_VALUES


def first_value(values: dict[str, Any], *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            normalized = text(values.get(candidate, ""))
            if normalized:
                return normalized
    return ""


def resolve_context(values: dict[str, Any]) -> dict[str, str]:
    if not values:
        return {}
    warrant = first_value(values, "warrant_flow_signal", "warrant_status").lower()
    status = first_value(values, "tdcc_status", "tdcc_judgement", "tdcc_judge").lower()
    accumulation = truthy(values.get("tdcc_accumulation_signal", ""))
    downgrade = first_value(values, "downgrade_flags")
    false_breakout = truthy(values.get("false_breakout_risk", ""))
    return {
        "warrant_flow_signal": warrant,
        "tdcc_status": status,
        "false_breakout_risk": str(false_breakout),
        "tdcc_accumulation_signal": str(accumulation),
        "downgrade_flags": downgrade,
        "tdcc_positive": str(status in POSITIVE_TDCC_STATUSES or accumulation),
        "tdcc_distribution": str(
            status == "distribution_warning"
            or "tdcc_distribution_warning" in downgrade
        ),
    }


def resolve_published_and_canonical_contexts(
    candidate_row: pd.Series | None,
    watch_row: pd.Series,
    mode: str,
) -> tuple[dict[str, str], dict[str, str]]:
    candidate_values = candidate_row.to_dict() if candidate_row is not None else {}
    legacy_values = dict(candidate_values)
    legacy_values.update(watch_row.to_dict())
    if mode.startswith("canonical_candidate"):
        legacy_values["warrant_flow_signal"] = first_value(
            candidate_values,
            "warrant_flow_signal",
            "warrant_status",
        )
    return resolve_context(legacy_values), resolve_context(candidate_values)


def independent_collision_effects(
    model_id: str,
    context: dict[str, str],
) -> dict[str, Decimal]:
    policy = MODEL_COLLISION_COMPONENT_POLICY.get(model_id)
    if policy is None:
        raise ValueError(f"missing independent collision policy for {model_id}")
    warrant_on = context.get("warrant_flow_signal", "") in BULLISH_WARRANT_SIGNALS
    positive = context.get("tdcc_positive", "False") == "True"
    distribution = context.get("tdcc_distribution", "False") == "True"
    false_breakout = context.get("false_breakout_risk", "False") == "True"
    warrant_bonus = policy["warrant_base_bonus"] if warrant_on else Decimal("0")
    base = warrant_bonus
    base += policy["tdcc_positive_base_bonus"] if positive else Decimal("0")
    base -= policy["tdcc_distribution_base_penalty"] if distribution else Decimal("0")
    base -= policy["false_breakout_base_penalty"] if false_breakout else Decimal("0")
    tdcc = policy["tdcc_positive_score_bonus"] if positive else Decimal("0")
    risk = Decimal("0")
    risk += policy["tdcc_distribution_risk_penalty"] if distribution else Decimal("0")
    risk += policy["false_breakout_risk_penalty"] if false_breakout else Decimal("0")
    return {
        "warrant_bonus": warrant_bonus,
        "base_model_score": base,
        "tdcc_score": tdcc,
        "risk_penalty": risk,
    }


def clamp(value: Decimal) -> Decimal:
    return min(Decimal("100"), max(Decimal("0"), value))


def context_json(context: dict[str, str]) -> str:
    return json.dumps(context, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def effects_json(effects: dict[str, Decimal]) -> str:
    return json.dumps(
        {key: decimal_text(value) for key, value in effects.items()},
        sort_keys=True,
        separators=(",", ":"),
    )


def differing_fields(
    left: dict[str, str],
    right: dict[str, str],
) -> tuple[str, ...]:
    defaults = {
        "warrant_flow_signal": "",
        "tdcc_status": "",
        "false_breakout_risk": "False",
    }
    return tuple(
        field
        for field in COLLISION_FIELDS
        if left.get(field, defaults[field]) != right.get(field, defaults[field])
    )


def independent_component_replay(
    formal_row: pd.Series | dict[str, Any],
    model_id: str,
    published_context: dict[str, str],
    canonical_context: dict[str, str],
) -> dict[str, Decimal | str]:
    published_effects = independent_collision_effects(model_id, published_context)
    canonical_effects = independent_collision_effects(model_id, canonical_context)
    base = decimal(formal_row.get("base_model_score", ""), "base_model_score")
    operation = decimal(formal_row.get("operation_score", ""), "operation_score")
    tdcc = decimal(formal_row.get("tdcc_score", ""), "tdcc_score")
    pattern = decimal(formal_row.get("pattern_score", ""), "pattern_score")
    risk = decimal(formal_row.get("risk_penalty", ""), "risk_penalty")
    final = decimal(formal_row.get("final_rank_score", ""), "final_rank_score")
    base_delta_raw = canonical_effects["base_model_score"] - published_effects["base_model_score"]
    if base in {Decimal("0"), Decimal("100")} and base_delta_raw != 0:
        raise ValueError("base_model_score boundary prevents exact independent replay")
    fixed_base = base - published_effects["base_model_score"]
    fixed_tdcc = tdcc - published_effects["tdcc_score"]
    fixed_risk = risk - published_effects["risk_penalty"]
    if fixed_tdcc < 0 or fixed_risk < 0:
        raise ValueError("published components do not contain resolved legacy effects")
    published_formula = clamp(base + operation + tdcc + pattern - risk)
    rounding_gap = published_formula - final
    if abs(rounding_gap) > Decimal("0.3"):
        raise ValueError("published rounded component formula exceeds independent tolerance")
    canonical_raw_base = fixed_base + canonical_effects["base_model_score"]
    canonical_base = clamp(canonical_raw_base)
    canonical_tdcc = fixed_tdcc + canonical_effects["tdcc_score"]
    canonical_risk = fixed_risk + canonical_effects["risk_penalty"]
    if canonical_tdcc < 0 or canonical_risk < 0:
        raise ValueError("independent counterfactual replay produced a negative component")
    final_delta = (
        base_delta_raw
        + canonical_effects["tdcc_score"]
        - published_effects["tdcc_score"]
        - (canonical_effects["risk_penalty"] - published_effects["risk_penalty"])
    )
    if final in {Decimal("0"), Decimal("100")} and final_delta != 0:
        raise ValueError("final_rank_score boundary prevents exact independent replay")
    canonical_final = clamp(final + final_delta)
    return {
        "published_effects": effects_json(published_effects),
        "canonical_effects": effects_json(canonical_effects),
        "canonical_base": canonical_base,
        "base_delta": canonical_base - base,
        "canonical_tdcc": canonical_tdcc,
        "tdcc_delta": canonical_tdcc - tdcc,
        "canonical_risk": canonical_risk,
        "risk_delta": canonical_risk - risk,
        "published_formula": published_formula,
        "rounding_gap": rounding_gap,
        "canonical_final": canonical_final,
        "final_delta": canonical_final - final,
    }


def git(root: Path, *args: str, allow_failure: bool = False) -> bytes:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if completed.returncode != 0 and not allow_failure:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {detail}")
    return completed.stdout if completed.returncode == 0 else b""


def blob(root: Path, commit_sha: str, repo_path: str) -> bytes:
    return git(root, "show", f"{commit_sha}:{repo_path}")


def independent_normalized_manifest_identity_frame(
    payload: bytes,
    source: str = "historical snapshot manifest",
) -> pd.DataFrame:
    manifest = independent_normalize_revision_manifest_schema(
        csv_bytes(payload),
        source,
    )
    manifest["snapshot_revision"] = manifest["snapshot_revision"].map(
        normalize_snapshot_revision
    )
    for column in MANIFEST_IDENTITY_COLUMNS:
        if column not in manifest.columns:
            manifest[column] = ""
    return manifest[MANIFEST_IDENTITY_COLUMNS].fillna("")


def independent_manifest_row_identity(
    row: pd.Series | dict[str, Any],
) -> tuple[str, ...]:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    return tuple(text(values.get(column)) for column in MANIFEST_IDENTITY_COLUMNS)


def independent_manifest_history_commits(root: Path) -> list[str]:
    manifest_repo_path = MANIFEST_PATH.relative_to(ROOT).as_posix()
    return git(
        root,
        "log",
        "--reverse",
        "--topo-order",
        "--format=%H",
        "--",
        manifest_repo_path,
    ).decode("ascii", errors="strict").split()


def independent_commit_changed_paths(root: Path, commit_sha: str) -> set[str]:
    return {
        line
        for line in git(
            root,
            "diff-tree",
            "--root",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit_sha,
        )
        .decode("utf-8", errors="strict")
        .splitlines()
        if line
    }


def independent_cached_history_blob(
    root: Path,
    commit_sha: str,
    repo_path: str,
    cache: dict[tuple[str, str], bytes],
) -> bytes:
    key = (commit_sha, repo_path)
    if key not in cache:
        cache[key] = git(
            root,
            "show",
            f"{commit_sha}:{repo_path}",
            allow_failure=True,
        )
    return cache[key]


def independently_resolve_exact_formal_publication(
    root: Path,
    manifest_row: pd.Series,
    snapshot_payload: bytes,
    *,
    commits: list[str],
    manifest_cache: dict[str, pd.DataFrame],
    changed_paths_cache: dict[str, set[str]],
    blob_cache: dict[tuple[str, str], bytes],
) -> tuple[dict[str, Any] | None, bool]:
    report_date = text(manifest_row.get("snapshot_report_date"))
    snapshot_revision = normalize_snapshot_revision(
        manifest_row.get("snapshot_revision")
    )
    target_identity = independent_manifest_row_identity(manifest_row)
    target_canonical_sha = sha256_bytes(snapshot_payload)
    manifest_repo_path = MANIFEST_PATH.relative_to(ROOT).as_posix()
    observations: list[dict[str, Any]] = []
    exact_identity_seen = False

    for commit_sha in commits:
        if commit_sha not in manifest_cache:
            manifest_payload = independent_cached_history_blob(
                root, commit_sha, manifest_repo_path, blob_cache
            )
            if not manifest_payload:
                manifest_cache[commit_sha] = pd.DataFrame(
                    columns=MANIFEST_IDENTITY_COLUMNS
                )
            else:
                manifest_cache[commit_sha] = (
                    independent_normalized_manifest_identity_frame(manifest_payload)
                )
        historical_manifest = manifest_cache[commit_sha]
        matching_key = historical_manifest[
            historical_manifest["snapshot_report_date"].astype(str).eq(report_date)
            & historical_manifest["artifact_id"].astype(str).eq(
                "model_signals_for_report"
            )
            & historical_manifest["snapshot_revision"].astype(str).eq(
                snapshot_revision
            )
        ]
        if matching_key.empty:
            continue
        identities = matching_key.apply(independent_manifest_row_identity, axis=1)
        exact_rows = matching_key[identities.map(lambda value: value == target_identity)]
        if len(exact_rows) > 1:
            raise RuntimeError(
                "publication manifest contains duplicate exact formal rows: "
                f"report_date={report_date} revision={snapshot_revision} "
                f"commit={commit_sha}"
            )
        exact_identity_seen = exact_identity_seen or len(exact_rows) == 1
        if commit_sha not in changed_paths_cache:
            changed_paths_cache[commit_sha] = independent_commit_changed_paths(
                root, commit_sha
            )
        changed_paths = changed_paths_cache[commit_sha]

        for _, historical_row in matching_key.iterrows():
            snapshot_path = text(historical_row.get("snapshot_path"))
            if (
                manifest_repo_path not in changed_paths
                or snapshot_path not in changed_paths
            ):
                continue
            historical_snapshot = independent_cached_history_blob(
                root, commit_sha, snapshot_path, blob_cache
            )
            if not historical_snapshot:
                continue
            manifest_snapshot_sha = text(historical_row.get("snapshot_sha256"))
            if manifest_snapshot_sha not in manifest_v1_sha256_candidates(
                historical_snapshot
            ):
                continue
            if sha256_bytes(historical_snapshot) != target_canonical_sha:
                continue

            identity = independent_manifest_row_identity(historical_row)
            valid = True
            try:
                historical_frame = csv_bytes(historical_snapshot)
                expected_rows = expected_manifest_data_row_count(
                    historical_row.get("row_count"),
                    report_date=report_date,
                    snapshot_revision=snapshot_revision,
                )
                valid = len(historical_frame) == expected_rows
            except RuntimeError:
                valid = False

            payloads: dict[str, bytes] = {}
            for key, repo_path in (
                ("formal_payload", FORMAL_SOURCE_PATH),
                ("watch_payload", WATCH_SOURCE_PATH),
                ("candidate_payload", CANDIDATE_SOURCE_PATH),
                ("official_payload", OFFICIAL_WARRANT_SOURCE_PATH),
                ("code_payload", PRODUCTION_CODE_PATH),
            ):
                payloads[key] = independent_cached_history_blob(
                    root, commit_sha, repo_path, blob_cache
                )
                if not payloads[key]:
                    valid = False
            if payloads.get("formal_payload"):
                valid = valid and (
                    sha256_bytes(payloads["formal_payload"])
                    == sha256_bytes(historical_snapshot)
                )
                try:
                    valid = valid and (
                        formal_artifact_report_date(
                            payloads["formal_payload"], FORMAL_SOURCE_PATH
                        )
                        == report_date
                    )
                except RuntimeError:
                    valid = False
            fingerprint = tuple(
                sha256_bytes(payloads[key]) if payloads.get(key) else ""
                for key in (
                    "formal_payload",
                    "watch_payload",
                    "candidate_payload",
                    "official_payload",
                    "code_payload",
                )
            )
            observations.append(
                {
                    "commit_sha": commit_sha,
                    "identity": identity,
                    "valid": valid,
                    "fingerprint": fingerprint,
                    "snapshot_payload": historical_snapshot,
                    "snapshot_path": snapshot_path,
                    "manifest_row": historical_row,
                    **payloads,
                }
            )

    valid_publications = [
        observation for observation in observations if observation["valid"]
    ]
    exact_publications = [
        observation
        for observation in valid_publications
        if observation["identity"] == target_identity
    ]
    if exact_publications:
        selected = dict(exact_publications[0])
        selected["paired_resolution"] = (
            "manifest_history_first_exact_row_same_commit_sources"
        )
        selected["force_revision_incomplete"] = False
        hidden_lineage = any(
            observation["commit_sha"] != selected["commit_sha"]
            and (
                not observation["valid"]
                or observation["identity"] != target_identity
                or observation["fingerprint"] != selected["fingerprint"]
            )
            for observation in observations
        )
        return selected, hidden_lineage

    if valid_publications:
        selected = dict(valid_publications[0])
        selected["paired_resolution"] = (
            "legacy_same_canonical_publication_fallback_incomplete"
        )
        selected["force_revision_incomplete"] = True
        return selected, True

    if exact_identity_seen or observations:
            raise RuntimeError(
                "no exact formal publication commit found for current manifest row "
                "and no valid same-canonical publication fallback exists: "
                f"report_date={report_date} revision={snapshot_revision}"
            )
    return None, False


def legacy_snapshot_repo_path(report_date: str) -> str:
    return (
        "output/history/daily_model_snapshots/"
        f"daily_candidate_model_signals_for_report_{report_date}.csv"
    )


def independent_distinct_git_path_history(
    root: Path, repo_path: str
) -> list[dict[str, Any]]:
    commits = git(
        root,
        "log",
        "--reverse",
        "--format=%H",
        "--",
        repo_path,
    ).decode("ascii", errors="strict").split()
    history: list[dict[str, Any]] = []
    seen_blob_oids: set[str] = set()
    for commit_sha in commits:
        blob_oid = git(
            root,
            "rev-parse",
            f"{commit_sha}:{repo_path}",
            allow_failure=True,
        ).decode("ascii", errors="strict").strip()
        if not blob_oid or blob_oid in seen_blob_oids:
            continue
        payload = git(
            root,
            "show",
            f"{commit_sha}:{repo_path}",
            allow_failure=True,
        )
        if not payload:
            continue
        seen_blob_oids.add(blob_oid)
        history.append(
            {
                "commit_sha": commit_sha,
                "blob_oid": blob_oid,
                "payload": payload,
                "manifest_sha_candidates": manifest_v1_sha256_candidates(payload),
            }
        )
    return history


def independently_recover_legacy_source(
    root: Path,
    report_date: str,
    legacy_revision: str,
    snapshot_path: str,
    history_entry: dict[str, Any],
) -> dict[str, Any] | None:
    commit_sha = text(history_entry.get("commit_sha"))
    snapshot_payload = history_entry.get("payload", b"")
    if not commit_sha or not isinstance(snapshot_payload, bytes) or not snapshot_payload:
        return None
    manifest_repo_path = MANIFEST_PATH.relative_to(ROOT).as_posix()
    changed_paths = independent_commit_changed_paths(root, commit_sha)
    if manifest_repo_path not in changed_paths or snapshot_path not in changed_paths:
        return None
    manifest_payload = git(
        root,
        "show",
        f"{commit_sha}:{manifest_repo_path}",
        allow_failure=True,
    )
    if not manifest_payload:
        return None
    try:
        historical_manifest = csv_bytes(manifest_payload)
    except Exception:
        return None
    required_columns = {
        "snapshot_report_date",
        "pipeline_commit_sha",
        "artifact_id",
        "source_path",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
    }
    if not required_columns.issubset(historical_manifest.columns):
        return None
    candidates = history_entry["manifest_sha_candidates"]
    matches = historical_manifest[
        historical_manifest["snapshot_report_date"].astype(str).eq(report_date)
        & historical_manifest["artifact_id"].astype(str).eq(
            "model_signals_for_report"
        )
        & historical_manifest["source_path"].astype(str).eq(FORMAL_SOURCE_PATH)
        & historical_manifest["snapshot_path"].astype(str).eq(snapshot_path)
        & historical_manifest["snapshot_sha256"].astype(str).isin(candidates)
    ]
    if len(matches) != 1:
        return None
    historical_manifest_row = matches.iloc[0].copy()
    source_manifest_sha = text(historical_manifest_row.get("source_sha256"))
    snapshot_manifest_sha = text(historical_manifest_row.get("snapshot_sha256"))
    if source_manifest_sha and source_manifest_sha != snapshot_manifest_sha:
        return None
    try:
        expected_rows = int(text(historical_manifest_row.get("row_count")))
        actual_rows = len(csv_bytes(snapshot_payload))
    except Exception:
        return None
    if actual_rows != expected_rows:
        return None
    payloads: dict[str, bytes] = {}
    for key, repo_path in (
        ("formal_payload", FORMAL_SOURCE_PATH),
        ("watch_payload", WATCH_SOURCE_PATH),
        ("candidate_payload", CANDIDATE_SOURCE_PATH),
        ("official_payload", OFFICIAL_WARRANT_SOURCE_PATH),
        ("code_payload", PRODUCTION_CODE_PATH),
    ):
        payload = git(
            root,
            "show",
            f"{commit_sha}:{repo_path}",
            allow_failure=True,
        )
        if not payload:
            return None
        payloads[key] = payload
    if payloads["formal_payload"] != snapshot_payload:
        return None
    try:
        recovered_report_date = formal_artifact_report_date(
            snapshot_payload, snapshot_path
        )
    except Exception:
        return None
    if recovered_report_date != report_date:
        return None
    return {
        "report_date": report_date,
        "snapshot_revision": legacy_revision,
        "revision_number": int(legacy_revision.removeprefix("legacy_r")),
        "supersedes_snapshot_sha256": "",
        "revision_reason": LEGACY_REVISION_RECOVERED,
        "expected_session_status": LEGACY_REVISION_RECOVERED,
        "pipeline_commit_sha": text(
            historical_manifest_row.get("pipeline_commit_sha")
        ),
        "snapshot_commit_sha": commit_sha,
        "paired_commit_sha": commit_sha,
        "paired_resolution": "legacy_git_manifest_recovered_same_commit_exact_sources",
        "snapshot_path": snapshot_path,
        "snapshot_sha256": sha256_bytes(snapshot_payload),
        "manifest_snapshot_sha256": text(
            historical_manifest_row.get("snapshot_sha256")
        ),
        "manifest_row": historical_manifest_row,
        "is_recovered_legacy": True,
        **payloads,
    }


def independently_recover_legacy_sources(
    root: Path,
    selected: pd.DataFrame,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    recovered_sources: list[dict[str, Any]] = []
    date_status: dict[str, str] = {}
    for report_date_value, date_rows in selected.groupby(
        "snapshot_report_date", sort=False
    ):
        report_date = text(report_date_value)
        snapshot_path = legacy_snapshot_repo_path(report_date)
        history = independent_distinct_git_path_history(root, snapshot_path)
        manifested_shas = {
            text(value)
            for value in date_rows["snapshot_sha256"].tolist()
            if text(value)
        }
        incomplete = False
        for position, history_entry in enumerate(history, start=1):
            if manifested_shas & history_entry["manifest_sha_candidates"]:
                continue
            recovered = independently_recover_legacy_source(
                root,
                report_date,
                f"legacy_r{position}",
                snapshot_path,
                history_entry,
            )
            if recovered is None:
                incomplete = True
                continue
            recovered_sources.append(recovered)
        date_status[report_date] = (
            LEGACY_HISTORY_INCOMPLETE if incomplete else LEGACY_HISTORY_COMPLETE
        )
    return recovered_sources, date_status


def csv_bytes(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False)


def snapshot_commit_matches(
    root: Path,
    snapshot_path: str,
    expected_sha256: str,
) -> list[str]:
    commits = git(root, "log", "--format=%H", "--", snapshot_path).decode("ascii").split()
    matches: list[str] = []
    for commit_sha in commits:
        payload = git(root, "show", f"{commit_sha}:{snapshot_path}", allow_failure=True)
        if payload and expected_sha256 in manifest_v1_sha256_candidates(payload):
            matches.append(commit_sha)
    return matches


def dispatcher_mode(code_payload: bytes) -> str:
    tree = ast.parse(code_payload.decode("utf-8"))
    function = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "append_volume_breakout_signals"
        ),
        None,
    )
    if function is None:
        raise RuntimeError("missing append_volume_breakout_signals")
    update_lines: list[int] = []
    override_lines: list[int] = []
    for node in ast.walk(function):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            if (
                isinstance(node.func.value, ast.Name)
                and node.func.value.id == "score_source"
                and node.func.attr == "update"
                and node.args
                and isinstance(node.args[0], ast.Call)
                and isinstance(node.args[0].func, ast.Attribute)
                and isinstance(node.args[0].func.value, ast.Name)
                and node.args[0].func.value.id == "row"
                and node.args[0].func.attr == "to_dict"
            ):
                update_lines.append(node.lineno)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if (
                    isinstance(target, ast.Subscript)
                    and isinstance(target.value, ast.Name)
                    and target.value.id == "score_source"
                    and isinstance(target.slice, ast.Constant)
                    and target.slice.value == "warrant_flow_signal"
                ):
                    override_lines.append(node.lineno)
    if not update_lines and override_lines:
        return "canonical_candidate_explicit_allowlist"
    if len(update_lines) != 1:
        raise RuntimeError(f"unexpected watch update lines: {update_lines}")
    if any(line > update_lines[0] for line in override_lines):
        return "canonical_candidate_after_watch_merge"
    return "legacy_watch_overrides_candidate"


def first_candidate_lookup(frame: pd.DataFrame) -> dict[str, tuple[int, pd.Series]]:
    result: dict[str, tuple[int, pd.Series]] = {}
    for position, (_, row) in enumerate(frame.iterrows()):
        code = stock_id(row.get("stock_id", row.get("ticker", "")))
        if code and code not in result:
            result[code] = (position, row)
    return result


def unique_warrant_lookup(
    frame: pd.DataFrame,
) -> tuple[dict[str, tuple[int, pd.Series]], list[str]]:
    result: dict[str, tuple[int, pd.Series]] = {}
    duplicates: list[str] = []
    for position, (_, row) in enumerate(frame.iterrows()):
        code = stock_id(row.get("stock_id"))
        if not code:
            continue
        if code in result:
            duplicates.append(code)
        else:
            result[code] = (position, row)
    return result, sorted(set(duplicates))


def append_mismatch(
    errors: list[str],
    report_date: str,
    row_key: str,
    field: str,
    actual: Any,
    expected: Any,
) -> None:
    if text(actual) != text(expected):
        errors.append(
            f"{report_date} {row_key} {field} mismatch: actual={actual!r} expected={expected!r}"
        )


def file_blob(root: Path, repo_path: str) -> bytes:
    path = root / Path(repo_path)
    if not path.exists():
        raise RuntimeError(f"missing current source artifact: {repo_path}")
    return path.read_bytes()


def volume_v2_formal_rows(payload: bytes, source: str) -> pd.DataFrame:
    formal = csv_bytes(payload)
    if "model_id" not in formal.columns:
        return pd.DataFrame()
    return formal[formal["model_id"].astype(str).isin(VOLUME_V2_MODELS)].copy()


def formal_report_date(formal: pd.DataFrame, source: str) -> str:
    if formal.empty or "signal_date" not in formal.columns:
        return ""
    dates = sorted(
        {
            text(value)
            for value in formal["signal_date"].tolist()
            if text(value)
        }
    )
    if len(dates) != 1 or not re.fullmatch(r"\d{8}", dates[0]):
        raise RuntimeError(
            "volume v2 formal source must contain exactly one YYYYMMDD signal date: "
            f"source={source} dates={dates}"
        )
    return dates[0]


def formal_artifact_report_date(payload: bytes, source: str) -> str:
    return formal_report_date(csv_bytes(payload), source)


def expected_audit_sources(root: Path, manifest: pd.DataFrame) -> list[dict[str, Any]]:
    manifest = independent_normalize_revision_manifest_schema(
        manifest,
        "current snapshot manifest",
    )
    selected = manifest[
        manifest["artifact_id"].astype(str).eq("model_signals_for_report")
    ].copy()
    selected["snapshot_revision"] = selected["snapshot_revision"].map(
        normalize_snapshot_revision
    )
    selected["_revision_number"] = selected["snapshot_revision"].map(
        snapshot_revision_number
    )
    duplicate_keys = selected.duplicated(
        ["snapshot_report_date", "snapshot_revision"], keep=False
    )
    if duplicate_keys.any():
        keys = selected.loc[
            duplicate_keys, ["snapshot_report_date", "snapshot_revision"]
        ].to_dict(orient="records")
        raise RuntimeError(
            f"duplicate model_signals_for_report manifest revisions: {keys}"
        )
    for report_date, group in selected.groupby("snapshot_report_date", sort=False):
        ordered = group.sort_values("_revision_number")
        numbers = ordered["_revision_number"].astype(int).tolist()
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            raise RuntimeError(
                "model_signals_for_report revisions must be contiguous from r1: "
                f"report_date={report_date} observed={numbers} expected={expected}"
            )
        previous_snapshot_sha = ""
        for _, row in ordered.iterrows():
            revision = normalize_snapshot_revision(row["snapshot_revision"])
            supersedes = text(row.get("supersedes_snapshot_sha256"))
            reason = text(row.get("revision_reason"))
            if revision == "r1":
                if supersedes:
                    raise RuntimeError(
                        "r1 must not declare supersedes_snapshot_sha256: "
                        f"report_date={report_date} value={supersedes}"
                    )
            else:
                if supersedes != previous_snapshot_sha:
                    raise RuntimeError(
                        "supersedes_snapshot_sha256 must equal the immediately previous "
                        "revision snapshot SHA: "
                        f"report_date={report_date} revision={revision} "
                        f"expected={previous_snapshot_sha} observed={supersedes}"
                    )
                if not reason:
                    raise RuntimeError(
                        "revision_reason is required after r1: "
                        f"report_date={report_date} revision={revision}"
                    )
            previous_snapshot_sha = text(row.get("snapshot_sha256"))
    selected = (
        selected.sort_values(["snapshot_report_date", "_revision_number"])
        .drop(columns=["_revision_number"])
        .reset_index(drop=True)
    )
    recovered_sources, legacy_date_status = independently_recover_legacy_sources(
        root, selected
    )
    unresolved_legacy_dates = {
        report_date
        for report_date, status in legacy_date_status.items()
        if status == LEGACY_HISTORY_INCOMPLETE
    }
    publication_commits = independent_manifest_history_commits(root)
    publication_manifest_cache: dict[str, pd.DataFrame] = {}
    publication_changed_paths_cache: dict[str, set[str]] = {}
    publication_blob_cache: dict[tuple[str, str], bytes] = {}

    current_formal_payload = file_blob(root, FORMAL_SOURCE_PATH)
    current_report_date = formal_artifact_report_date(
        current_formal_payload, FORMAL_SOURCE_PATH
    )
    head_sha = git(root, "rev-parse", "HEAD").decode("ascii").strip()
    sources: list[dict[str, Any]] = []
    snapshot_dates: set[str] = set()
    previous_canonical_snapshot_sha_by_date: dict[str, str] = {}

    for _, manifest_row in selected.iterrows():
        report_date = text(manifest_row.get("snapshot_report_date"))
        snapshot_revision = normalize_snapshot_revision(
            manifest_row.get("snapshot_revision")
        )
        if not re.fullmatch(r"\d{8}", report_date):
            raise RuntimeError(f"invalid snapshot report date: {report_date!r}")
        if text(manifest_row.get("source_path")) != FORMAL_SOURCE_PATH:
            raise RuntimeError(
                f"unexpected formal source path for {report_date}: {manifest_row.get('source_path')}"
            )
        snapshot_path = text(manifest_row.get("snapshot_path"))
        manifest_snapshot_sha = text(manifest_row.get("snapshot_sha256"))
        pipeline_sha = text(manifest_row.get("pipeline_commit_sha"))
        snapshot_payload = file_blob(root, snapshot_path)
        snapshot_frame = csv_bytes(snapshot_payload)
        expected_snapshot_rows = expected_manifest_data_row_count(
            manifest_row.get("row_count"),
            report_date=report_date,
            snapshot_revision=snapshot_revision,
        )
        actual_snapshot_rows = len(snapshot_frame)
        if actual_snapshot_rows != expected_snapshot_rows:
            raise RuntimeError(
                "model_signals_for_report manifest row_count differs from raw "
                "snapshot CSV data rows: "
                f"report_date={report_date} revision={snapshot_revision} "
                f"expected={expected_snapshot_rows} actual={actual_snapshot_rows}"
            )
        if manifest_snapshot_sha not in manifest_v1_sha256_candidates(snapshot_payload):
            raise RuntimeError(
                f"formal v2 snapshot SHA mismatch: report_date={report_date} path={snapshot_path}"
            )
        canonical_snapshot_sha = sha256_bytes(snapshot_payload)
        previous_canonical_snapshot_sha = (
            previous_canonical_snapshot_sha_by_date.get(report_date, "")
        )
        if (
            snapshot_revision_number(snapshot_revision) > 1
            and canonical_snapshot_sha == previous_canonical_snapshot_sha
        ):
            raise RuntimeError(
                "model_signals_for_report revision must change the canonical "
                "snapshot payload: "
                f"report_date={report_date} revision={snapshot_revision} "
                f"canonical_sha256={canonical_snapshot_sha}"
            )
        previous_canonical_snapshot_sha_by_date[report_date] = canonical_snapshot_sha
        if formal_report_date(snapshot_frame, snapshot_path) != report_date:
            raise RuntimeError(
                f"formal snapshot signal date differs from manifest: report_date={report_date}"
            )
        publication, hidden_same_canonical_lineage = (
            independently_resolve_exact_formal_publication(
                root,
                manifest_row,
                snapshot_payload,
                commits=publication_commits,
                manifest_cache=publication_manifest_cache,
                changed_paths_cache=publication_changed_paths_cache,
                blob_cache=publication_blob_cache,
            )
        )
        if publication is not None:
            snapshot_commit = text(publication["commit_sha"])
            paired_commit = snapshot_commit
            paired_resolution = text(publication["paired_resolution"])
            payloads = {
                key: publication[key]
                for key in (
                    "formal_payload",
                    "watch_payload",
                    "candidate_payload",
                    "official_payload",
                    "code_payload",
                )
            }
            expected_session_status = "trading_day_snapshot_present"
            if hidden_same_canonical_lineage:
                legacy_date_status[report_date] = LEGACY_HISTORY_INCOMPLETE
        else:
            if (
                report_date != current_report_date
                or canonical_text_bytes(snapshot_payload)
                != canonical_text_bytes(current_formal_payload)
            ):
                raise RuntimeError(
                    "uncommitted formal snapshot must byte-match the same-date current source: "
                    f"report_date={report_date} path={snapshot_path}"
                )
            snapshot_commit = ""
            paired_commit = ""
            paired_resolution = PUBLISHED_PENDING_SOURCE_RESOLUTION
            payloads = {
                "formal_payload": current_formal_payload,
                "watch_payload": file_blob(root, WATCH_SOURCE_PATH),
                "candidate_payload": file_blob(root, CANDIDATE_SOURCE_PATH),
                "official_payload": file_blob(root, OFFICIAL_WARRANT_SOURCE_PATH),
                "code_payload": file_blob(root, PRODUCTION_CODE_PATH),
            }
            expected_session_status = "published_snapshot_pending_commit"
        if sha256_bytes(payloads["formal_payload"]) != canonical_snapshot_sha:
            raise RuntimeError(
                f"paired formal source does not equal snapshot: report_date={report_date}"
            )
        sources.append(
            {
                "report_date": report_date,
                "snapshot_revision": snapshot_revision,
                "revision_number": snapshot_revision_number(snapshot_revision),
                "supersedes_snapshot_sha256": text(
                    manifest_row.get("supersedes_snapshot_sha256")
                ),
                "revision_reason": text(manifest_row.get("revision_reason")),
                "expected_session_status": expected_session_status,
                "pipeline_commit_sha": pipeline_sha,
                "snapshot_commit_sha": snapshot_commit,
                "paired_commit_sha": paired_commit,
                "paired_resolution": paired_resolution,
                "snapshot_path": snapshot_path,
                "snapshot_sha256": canonical_snapshot_sha,
                "manifest_snapshot_sha256": manifest_snapshot_sha,
                "manifest_row": manifest_row,
                "is_recovered_legacy": False,
                "hidden_same_canonical_lineage": hidden_same_canonical_lineage,
                "force_revision_incomplete": bool(
                    publication is not None
                    and publication.get("force_revision_incomplete", False)
                ),
                **payloads,
            }
        )
        snapshot_dates.add(report_date)

    sources.extend(recovered_sources)

    if current_report_date:
        if current_report_date in snapshot_dates:
            matching = max(
                (
                    source
                    for source in sources
                    if source["report_date"] == current_report_date
                    and not source.get("is_recovered_legacy", False)
                ),
                key=lambda source: int(source["revision_number"]),
            )
            if matching.get(
                "manifest_snapshot_sha256", ""
            ) not in manifest_v1_sha256_candidates(current_formal_payload):
                next_revision_number = int(matching["revision_number"]) + 1
                sources.append(
                    {
                        "report_date": current_report_date,
                        "snapshot_revision": f"r{next_revision_number}",
                        "revision_number": next_revision_number,
                        "supersedes_snapshot_sha256": matching.get(
                            "manifest_snapshot_sha256", ""
                        ),
                        "revision_reason": "pending_warrant_formal_sync",
                        "expected_session_status": (
                            "current_formal_latest_pending_snapshot_revision"
                        ),
                        "pipeline_commit_sha": head_sha,
                        "snapshot_commit_sha": "",
                        "paired_commit_sha": "",
                        "paired_resolution": (
                            CURRENT_PENDING_REVISION_SOURCE_RESOLUTION
                        ),
                        "snapshot_path": FORMAL_SOURCE_PATH,
                        "snapshot_sha256": sha256_bytes(current_formal_payload),
                        "manifest_snapshot_sha256": "",
                        "manifest_row": None,
                        "is_recovered_legacy": False,
                        "formal_payload": current_formal_payload,
                        "watch_payload": file_blob(root, WATCH_SOURCE_PATH),
                        "candidate_payload": file_blob(root, CANDIDATE_SOURCE_PATH),
                        "official_payload": file_blob(
                            root, OFFICIAL_WARRANT_SOURCE_PATH
                        ),
                        "code_payload": file_blob(root, PRODUCTION_CODE_PATH),
                    }
                )
        else:
            sources.append(
                {
                    "report_date": current_report_date,
                    "snapshot_revision": "r1",
                    "revision_number": 1,
                    "supersedes_snapshot_sha256": "",
                    "revision_reason": "",
                    "expected_session_status": "current_formal_latest_pending_snapshot",
                    "pipeline_commit_sha": head_sha,
                    "snapshot_commit_sha": "",
                    "paired_commit_sha": "",
                    "paired_resolution": CURRENT_SOURCE_RESOLUTION,
                    "snapshot_path": FORMAL_SOURCE_PATH,
                    "snapshot_sha256": sha256_bytes(current_formal_payload),
                    "manifest_row": None,
                    "is_recovered_legacy": False,
                    "formal_payload": current_formal_payload,
                    "watch_payload": file_blob(root, WATCH_SOURCE_PATH),
                    "candidate_payload": file_blob(root, CANDIDATE_SOURCE_PATH),
                    "official_payload": file_blob(root, OFFICIAL_WARRANT_SOURCE_PATH),
                    "code_payload": file_blob(root, PRODUCTION_CODE_PATH),
                }
            )
            legacy_date_status.setdefault(
                current_report_date,
                (
                    LEGACY_HISTORY_INCOMPLETE
                    if independent_distinct_git_path_history(
                        root, legacy_snapshot_repo_path(current_report_date)
                    )
                    else LEGACY_HISTORY_COMPLETE
                ),
            )

    for source in sources:
        report_date = text(source["report_date"])
        precontract_status = legacy_date_status.get(
            report_date, LEGACY_HISTORY_COMPLETE
        )
        if source.get("is_recovered_legacy", False):
            revision_status = LEGACY_REVISION_RECOVERED
        elif source.get("manifest_row") is None:
            revision_status = CURRENT_REVISION_PENDING
        elif source.get("force_revision_incomplete", False):
            revision_status = LEGACY_HISTORY_INCOMPLETE
        elif text(source["snapshot_path"]) == legacy_snapshot_repo_path(report_date):
            revision_status = (
                LEGACY_HISTORY_INCOMPLETE
                if (
                    precontract_status == LEGACY_HISTORY_INCOMPLETE
                    and (
                        report_date in unresolved_legacy_dates
                        or not source.get("hidden_same_canonical_lineage", False)
                    )
                )
                else LEGACY_HISTORY_COMPLETE
            )
        else:
            revision_status = VERSIONED_REVISION_EXACT
        source["legacy_revision_history_status"] = revision_status
        source["legacy_precontract_revision_history_status"] = precontract_status
    return sorted(
        sources,
        key=lambda source: (
            source["report_date"],
            audit_revision_sort_key(source["snapshot_revision"]),
        ),
    )


def validate(
    root: Path = ROOT,
    csv_path: Path = CSV_PATH,
    md_path: Path = MD_PATH,
    docs_csv_path: Path = DOCS_CSV_PATH,
    docs_md_path: Path = DOCS_MD_PATH,
) -> list[str]:
    root = root.resolve()
    paths = [csv_path, md_path, docs_csv_path, docs_md_path]
    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"missing audit artifact: {path.as_posix()}")
    if errors:
        return errors

    if csv_path.read_bytes() != docs_csv_path.read_bytes():
        errors.append("latest CSV and docs/latest CSV mirror differ")
    if md_path.read_bytes() != docs_md_path.read_bytes():
        errors.append("latest Markdown and docs/latest Markdown mirror differ")

    try:
        audit = pd.read_csv(csv_path, dtype=str, keep_default_na=False)
    except Exception as exc:
        return [*errors, f"failed to parse audit CSV: {exc}"]
    if list(audit.columns) != AUDIT_COLUMNS:
        errors.append(
            f"audit columns differ: actual={list(audit.columns)} expected={AUDIT_COLUMNS}"
        )
        return errors
    if "audited_at" in audit.columns or "generated_at" in audit.columns:
        errors.append("deterministic audit must not contain dynamic timestamp columns")
    if set(audit["audit_version"].astype(str)) != {AUDIT_VERSION}:
        errors.append("unexpected audit_version values")
    unknown_row_types = sorted(
        set(audit["audit_row_type"].astype(str))
        - {FORMAL_ROW_TYPE, REVISION_COVERAGE_ROW_TYPE}
    )
    if unknown_row_types:
        errors.append(f"unknown audit_row_type values: {unknown_row_types}")
    primary_key = [
        "audit_row_type",
        "snapshot_report_date",
        "snapshot_revision",
        "report_line",
        "model_id",
        "stock_id",
        "source_row_index",
    ]
    if audit.duplicated(primary_key, keep=False).any():
        errors.append("audit primary grain is not unique")
    formal_model_ids = set(
        audit.loc[
            audit["audit_row_type"].eq(FORMAL_ROW_TYPE), "model_id"
        ].astype(str)
    )
    if not formal_model_ids.issubset(VOLUME_V2_MODELS):
        errors.append("audit contains a non-volume-v2 model")
    try:
        manifest = pd.read_csv(
            root / MANIFEST_PATH.relative_to(ROOT),
            dtype=str,
            keep_default_na=False,
        )
        sources = expected_audit_sources(root, manifest)
    except Exception as exc:
        return [*errors, f"failed to resolve dynamic audit sources: {exc}"]

    expected_revisions = {
        (source["report_date"], source["snapshot_revision"]) for source in sources
    }
    actual_revisions = set(
        zip(
            audit["snapshot_report_date"].astype(str),
            audit["snapshot_revision"].astype(str),
        )
    )
    if actual_revisions != expected_revisions:
        errors.append(
            "audit report-date/revision coverage differs from dynamic historical/current "
            "sources: "
            f"actual={sorted(actual_revisions)} expected={sorted(expected_revisions)}"
        )
    expected_rows_by_revision = {
        (source["report_date"], source["snapshot_revision"]): len(
            volume_v2_formal_rows(source["formal_payload"], FORMAL_SOURCE_PATH)
        )
        for source in sources
    }
    expected_total_rows = sum(expected_rows_by_revision.values()) + len(sources)
    if len(audit) != expected_total_rows:
        errors.append(
            "audit row count differs from dynamic source coverage: "
            f"actual={len(audit)} expected={expected_total_rows}"
        )
    for (report_date, snapshot_revision), expected_rows in expected_rows_by_revision.items():
        revision_mask = (
            audit["snapshot_report_date"].astype(str).eq(report_date)
            & audit["snapshot_revision"].astype(str).eq(snapshot_revision)
        )
        actual_formal_rows = int(
            (revision_mask & audit["audit_row_type"].eq(FORMAL_ROW_TYPE)).sum()
        )
        actual_coverage_rows = int(
            (
                revision_mask
                & audit["audit_row_type"].eq(REVISION_COVERAGE_ROW_TYPE)
            ).sum()
        )
        if actual_formal_rows != expected_rows:
            errors.append(
                f"{report_date}/{snapshot_revision} formal row count mismatch: "
                f"expected={expected_rows} actual={actual_formal_rows}"
            )
        if actual_coverage_rows != 1:
            errors.append(
                f"{report_date}/{snapshot_revision} revision coverage row count mismatch: "
                f"expected=1 actual={actual_coverage_rows}"
            )

    computed_counterfactual_scores: dict[int, Decimal] = {}
    computed_row_state: dict[int, dict[str, Any]] = {}
    for source in sources:
        report_date = source["report_date"]
        snapshot_revision = source["snapshot_revision"]
        source_label = f"{report_date}/{snapshot_revision}"
        revision_rows = audit[
            audit["snapshot_report_date"].astype(str).eq(report_date)
            & audit["snapshot_revision"].astype(str).eq(snapshot_revision)
        ].copy()
        if revision_rows.empty:
            continue
        coverage_rows = revision_rows[
            revision_rows["audit_row_type"].eq(REVISION_COVERAGE_ROW_TYPE)
        ]
        date_rows = revision_rows[
            revision_rows["audit_row_type"].eq(FORMAL_ROW_TYPE)
        ]
        manifest_row = source["manifest_row"]
        snapshot_path = source["snapshot_path"]
        snapshot_sha = source["snapshot_sha256"]
        pipeline_sha = source["pipeline_commit_sha"]
        recorded = (
            coverage_rows.iloc[0] if not coverage_rows.empty else revision_rows.iloc[0]
        )

        for field in (
            "snapshot_revision",
            "supersedes_snapshot_sha256",
            "revision_reason",
            "legacy_revision_history_status",
            "legacy_precontract_revision_history_status",
            "revision_formal_row_count",
            "pipeline_commit_sha",
            "snapshot_commit_sha",
            "paired_source_commit_sha",
            "paired_source_resolution",
            "dispatcher_warrant_source_mode",
            "production_code_sha256",
            "formal_snapshot_path",
            "formal_snapshot_sha256",
            "formal_snapshot_manifest_v1_sha256",
            "watch_artifact_path",
            "watch_artifact_sha256",
            "candidate_artifact_path",
            "candidate_artifact_sha256",
            "official_warrant_artifact_path",
            "official_warrant_artifact_sha256",
            "manifest_row_sha256",
        ):
            if revision_rows[field].astype(str).nunique() != 1:
                errors.append(
                    f"{source_label} has multiple values for revision-level field {field}"
                )

        append_mismatch(
            errors,
            source_label,
            "revision",
            "snapshot_revision",
            recorded["snapshot_revision"],
            snapshot_revision,
        )
        append_mismatch(
            errors,
            source_label,
            "revision",
            "supersedes_snapshot_sha256",
            recorded["supersedes_snapshot_sha256"],
            source["supersedes_snapshot_sha256"],
        )
        append_mismatch(
            errors,
            source_label,
            "revision",
            "revision_reason",
            recorded["revision_reason"],
            source["revision_reason"],
        )
        append_mismatch(
            errors,
            source_label,
            "revision",
            "legacy_revision_history_status",
            recorded["legacy_revision_history_status"],
            source["legacy_revision_history_status"],
        )
        append_mismatch(
            errors,
            source_label,
            "revision",
            "legacy_precontract_revision_history_status",
            recorded["legacy_precontract_revision_history_status"],
            source["legacy_precontract_revision_history_status"],
        )
        expected_formal_count = expected_rows_by_revision[
            (report_date, snapshot_revision)
        ]
        append_mismatch(
            errors,
            source_label,
            "revision",
            "revision_formal_row_count",
            recorded["revision_formal_row_count"],
            str(expected_formal_count),
        )

        append_mismatch(errors, report_date, "date", "pipeline_commit_sha", recorded["pipeline_commit_sha"], pipeline_sha)
        append_mismatch(errors, report_date, "date", "formal_snapshot_path", recorded["formal_snapshot_path"], snapshot_path)
        append_mismatch(errors, report_date, "date", "formal_snapshot_sha256", recorded["formal_snapshot_sha256"], snapshot_sha)
        append_mismatch(
            errors,
            report_date,
            "date",
            "formal_snapshot_manifest_v1_sha256",
            recorded["formal_snapshot_manifest_v1_sha256"],
            source.get("manifest_snapshot_sha256", ""),
        )
        append_mismatch(
            errors,
            report_date,
            "date",
            "manifest_row_sha256",
            recorded["manifest_row_sha256"],
            row_sha256(manifest_row) if manifest_row is not None else "",
        )
        append_mismatch(
            errors,
            report_date,
            "date",
            "expected_session_status",
            recorded["expected_session_status"],
            source["expected_session_status"],
        )
        append_mismatch(
            errors,
            report_date,
            "date",
            "snapshot_commit_sha",
            recorded["snapshot_commit_sha"],
            source["snapshot_commit_sha"],
        )
        append_mismatch(
            errors,
            report_date,
            "date",
            "paired_source_commit_sha",
            recorded["paired_source_commit_sha"],
            source["paired_commit_sha"],
        )
        append_mismatch(
            errors,
            report_date,
            "date",
            "paired_source_resolution",
            recorded["paired_source_resolution"],
            source["paired_resolution"],
        )
        for field, expected_path in (
            ("watch_artifact_path", WATCH_SOURCE_PATH),
            ("candidate_artifact_path", CANDIDATE_SOURCE_PATH),
            ("official_warrant_artifact_path", OFFICIAL_WARRANT_SOURCE_PATH),
        ):
            append_mismatch(
                errors,
                source_label,
                "revision",
                field,
                recorded[field],
                expected_path,
            )

        if len(coverage_rows) == 1:
            coverage = coverage_rows.iloc[0]
            coverage_expected = {
                "historical_promotion_evidence_eligible": "False",
                "replay_status": "not_applicable_revision_coverage",
                "rank_replay_status": "not_applicable_revision_coverage",
                "formal_row_disposition": "not_applicable_revision_coverage",
                "impact_scope": "revision_coverage_only",
                "evidence_status": (
                    "incomplete"
                    if source["legacy_revision_history_status"]
                    == LEGACY_HISTORY_INCOMPLETE
                    else "complete"
                ),
                "reason": (
                    "revision coverage record; volume v2 formal row count="
                    f"{expected_formal_count}"
                ),
            }
            for field, expected in coverage_expected.items():
                append_mismatch(
                    errors,
                    source_label,
                    "coverage",
                    field,
                    coverage[field],
                    expected,
                )
            for field in (
                "formal_row_sha256",
                "watch_row_sha256",
                "candidate_row_sha256",
                "official_warrant_row_sha256",
                "formal_row_number",
                "watch_row_number",
                "candidate_row_number",
                "official_warrant_row_number",
                "signal_date",
                "report_line",
                "model_id",
                "stock_id",
                "source_row_index",
                "published_model_rank",
                "counterfactual_model_rank",
                "rank_delta",
            ):
                append_mismatch(
                    errors,
                    source_label,
                    "coverage",
                    field,
                    coverage[field],
                    "",
                )

        formal_payload = source["formal_payload"]
        watch_payload = source["watch_payload"]
        candidate_payload = source["candidate_payload"]
        official_payload = source["official_payload"]
        code_payload = source["code_payload"]

        source_hashes = {
            "formal_snapshot_sha256": sha256_bytes(formal_payload),
            "watch_artifact_sha256": sha256_bytes(watch_payload),
            "candidate_artifact_sha256": sha256_bytes(candidate_payload),
            "official_warrant_artifact_sha256": sha256_bytes(official_payload),
            "production_code_sha256": sha256_bytes(code_payload),
        }
        for field, expected in source_hashes.items():
            append_mismatch(errors, report_date, "date", field, recorded[field], expected)
        if source_hashes["formal_snapshot_sha256"] != snapshot_sha:
            errors.append(f"{report_date} paired formal source does not equal snapshot SHA")

        try:
            formal = volume_v2_formal_rows(formal_payload, FORMAL_SOURCE_PATH)
            watch = csv_bytes(watch_payload)
            candidates = csv_bytes(candidate_payload)
            official = csv_bytes(official_payload)
            candidate_lookup = first_candidate_lookup(candidates)
            official_lookup, official_duplicates = unique_warrant_lookup(official)
            mode = dispatcher_mode(code_payload)
        except Exception as exc:
            errors.append(f"{report_date} failed to parse paired sources: {exc}")
            continue
        if official_duplicates:
            errors.append(f"{report_date} official warrant duplicate IDs: {official_duplicates}")
        append_mismatch(errors, report_date, "date", "dispatcher_warrant_source_mode", recorded["dispatcher_warrant_source_mode"], mode)
        if len(formal) != expected_rows_by_revision[(report_date, snapshot_revision)]:
            errors.append(
                f"{source_label} raw formal v2 row count differs from dynamic coverage"
            )

        date_rows_by_position = {
            integer(row["formal_row_number"], "formal_row_number"): (index, row)
            for index, row in date_rows.iterrows()
        }
        if set(date_rows_by_position) != set(range(len(formal))):
            errors.append(f"{report_date} formal_row_number coverage is not contiguous")
            continue

        for formal_position, (_, formal_row) in enumerate(formal.iterrows()):
            audit_index, audit_row = date_rows_by_position[formal_position]
            row_key = f"{audit_row['model_id']}/{audit_row['stock_id']}/{audit_row['source_row_index']}"
            formal_stock = stock_id(formal_row.get("stock_id"))
            source_index = text(formal_row.get("source_row_index"))
            source_match = re.fullmatch(r"volume_breakout:(\d+)", source_index)
            if not source_match:
                errors.append(f"{report_date} {row_key} invalid raw source_row_index")
                continue
            watch_position = int(source_match.group(1))
            if watch_position >= len(watch):
                errors.append(f"{report_date} {row_key} watch row is out of range")
                continue
            watch_row = watch.iloc[watch_position]
            candidate_item = candidate_lookup.get(formal_stock)
            official_item = official_lookup.get(formal_stock)
            candidate_position, candidate_row = (
                candidate_item if candidate_item is not None else (None, None)
            )
            official_position, official_row = (
                official_item if official_item is not None else (None, None)
            )

            raw_watch_signal = warrant_signal(watch_row.get("warrant_flow_signal"))
            raw_candidate_signal = (
                warrant_signal(candidate_row.get("warrant_flow_signal"))
                if candidate_row is not None
                else ""
            )
            raw_official_signal = (
                warrant_signal(official_row.get("warrant_flow_signal"))
                if official_row is not None
                else ""
            )
            raw_formal_signal = warrant_signal(formal_row.get("warrant_flow_signal"))
            raw_watch_source_score = text(watch_row.get("score"))
            raw_candidate_source_score = (
                text(candidate_row.get("score")) if candidate_row is not None else ""
            )
            raw_watch_source_rank = text(watch_row.get("rank"))
            raw_candidate_source_rank = (
                text(candidate_row.get("rank")) if candidate_row is not None else ""
            )
            score_collision = (
                candidate_row is not None
                and raw_watch_source_score != raw_candidate_source_score
            )
            source_rank_collision = (
                candidate_row is not None
                and raw_watch_source_rank != raw_candidate_source_rank
            )
            raw_model_id = text(formal_row.get("model_id"))
            published_context, canonical_context = resolve_published_and_canonical_contexts(
                candidate_row,
                watch_row,
                mode,
            )
            watch_context = resolve_context(watch_row.to_dict())
            candidate_context = resolve_context(
                candidate_row.to_dict() if candidate_row is not None else {}
            )
            watch_collision_fields = differing_fields(watch_context, canonical_context)
            published_collision_fields = differing_fields(
                published_context,
                canonical_context,
            )
            published_effects = independent_collision_effects(
                raw_model_id,
                published_context,
            )
            canonical_effects = independent_collision_effects(
                raw_model_id,
                canonical_context,
            )
            basis_signal = published_context.get("warrant_flow_signal", "")
            basis_source = (
                "canonical_candidate"
                if mode.startswith("canonical_candidate")
                else "legacy_watch"
            )
            bonus = WARRANT_BONUS_BY_MODEL[raw_model_id]
            published_bonus = published_effects["warrant_bonus"]
            canonical_bonus = canonical_effects["warrant_bonus"]
            published_score_text = text(formal_row.get("final_rank_score"))
            replay_error = ""
            try:
                replay = independent_component_replay(
                    formal_row,
                    raw_model_id,
                    published_context,
                    canonical_context,
                )
                replay_status = "resolved"
                counterfactual_score = replay["canonical_final"]
                assert isinstance(counterfactual_score, Decimal)
                computed_counterfactual_scores[audit_index] = counterfactual_score
            except (ValueError, KeyError) as exc:
                replay = {}
                replay_status = "unresolved"
                replay_error = text(exc)

            def replay_text(field: str, reference: str = "") -> str:
                value = replay.get(field)
                return decimal_text(value, reference) if isinstance(value, Decimal) else ""

            expected_fields = {
                "audit_row_type": FORMAL_ROW_TYPE,
                "revision_formal_row_count": str(len(formal)),
                "formal_row_sha256": row_sha256(formal_row),
                "watch_row_sha256": row_sha256(watch_row),
                "candidate_row_sha256": row_sha256(candidate_row) if candidate_row is not None else "",
                "candidate_row_present": str(candidate_row is not None),
                "official_warrant_row_sha256": row_sha256(official_row) if official_row is not None else "",
                "official_warrant_row_present": str(official_row is not None),
                "watch_row_number": str(watch_position),
                "candidate_row_number": str(candidate_position) if candidate_position is not None else "",
                "official_warrant_row_number": str(official_position) if official_position is not None else "",
                "signal_date": text(formal_row.get("signal_date")),
                "report_line": text(formal_row.get("report_line")),
                "model_id": raw_model_id,
                "stock_id": formal_stock,
                "source_row_index": source_index,
                "watch_warrant_signal": raw_watch_signal,
                "candidate_warrant_signal": raw_candidate_signal,
                "official_warrant_signal": raw_official_signal,
                "formal_warrant_signal": raw_formal_signal,
                "watch_source_score": raw_watch_source_score,
                "candidate_source_score": raw_candidate_source_score,
                "watch_source_rank": raw_watch_source_rank,
                "candidate_source_rank": raw_candidate_source_rank,
                "watch_candidate_score_collision": str(score_collision),
                "watch_candidate_rank_collision": str(source_rank_collision),
                "canonical_warrant_source_type": (
                    "all_candidates_projection"
                    if candidate_row is not None
                    else "negative_projection_no_candidate_row"
                ),
                "published_warrant_score_source": basis_source,
                "published_warrant_basis_signal": basis_signal,
                "watch_tdcc_status": watch_context.get("tdcc_status", ""),
                "candidate_tdcc_status": candidate_context.get("tdcc_status", ""),
                "published_tdcc_status": published_context.get("tdcc_status", ""),
                "counterfactual_tdcc_status": canonical_context.get("tdcc_status", ""),
                "watch_false_breakout_risk": watch_context.get(
                    "false_breakout_risk", "False"
                ),
                "candidate_false_breakout_risk": candidate_context.get(
                    "false_breakout_risk", "False"
                ),
                "published_false_breakout_risk": published_context.get(
                    "false_breakout_risk", "False"
                ),
                "counterfactual_false_breakout_risk": canonical_context.get(
                    "false_breakout_risk", "False"
                ),
                "published_tdcc_positive": published_context.get(
                    "tdcc_positive", "False"
                ),
                "counterfactual_tdcc_positive": canonical_context.get(
                    "tdcc_positive", "False"
                ),
                "published_tdcc_distribution": published_context.get(
                    "tdcc_distribution", "False"
                ),
                "counterfactual_tdcc_distribution": canonical_context.get(
                    "tdcc_distribution", "False"
                ),
                "published_score_context": context_json(published_context),
                "counterfactual_score_context": context_json(canonical_context),
                "collision_fields": "|".join(watch_collision_fields),
                "published_counterfactual_collision_fields": "|".join(
                    published_collision_fields
                ),
                "warrant_bonus_points": decimal_text(bonus),
                "published_warrant_bonus_points": decimal_text(published_bonus),
                "counterfactual_warrant_bonus_points": decimal_text(canonical_bonus),
                "published_collision_component_effects": effects_json(published_effects),
                "counterfactual_collision_component_effects": effects_json(
                    canonical_effects
                ),
                "published_base_model_score": text(formal_row.get("base_model_score")),
                "counterfactual_base_model_score": replay_text(
                    "canonical_base", text(formal_row.get("base_model_score"))
                ),
                "base_model_score_delta": replay_text("base_delta"),
                "published_operation_score": text(formal_row.get("operation_score")),
                "published_tdcc_score": text(formal_row.get("tdcc_score")),
                "counterfactual_tdcc_score": replay_text(
                    "canonical_tdcc", text(formal_row.get("tdcc_score"))
                ),
                "tdcc_score_delta": replay_text("tdcc_delta"),
                "published_pattern_score": text(formal_row.get("pattern_score")),
                "published_risk_penalty": text(formal_row.get("risk_penalty")),
                "counterfactual_risk_penalty": replay_text(
                    "canonical_risk", text(formal_row.get("risk_penalty"))
                ),
                "risk_penalty_delta": replay_text("risk_delta"),
                "published_component_replay_final_rank_score": replay_text(
                    "published_formula", published_score_text
                ),
                "published_component_replay_rounding_gap": replay_text("rounding_gap"),
                "published_component_replay_match": str(replay_status == "resolved"),
                "published_final_rank_score": published_score_text,
                "counterfactual_final_rank_score": replay_text(
                    "canonical_final", published_score_text
                ),
                "score_delta": replay_text("final_delta"),
                "replay_status": replay_status,
                "replay_error": replay_error,
                "published_model_rank": text(formal_row.get("model_rank")),
                "watch_candidate_collision": str(raw_watch_signal != raw_candidate_signal),
                "candidate_official_match": str(raw_candidate_signal == raw_official_signal),
                "formal_candidate_match": str(raw_formal_signal == raw_candidate_signal),
                "watch_disposition": (
                    "superseded_advisory_snapshot"
                    if (
                        bool(watch_collision_fields)
                        or score_collision
                        or source_rank_collision
                    )
                    else "current_canonical_match"
                ),
            }
            for field, expected in expected_fields.items():
                append_mismatch(errors, report_date, row_key, field, audit_row[field], expected)
            computed_row_state[audit_index] = {
                "replay_status": replay_status,
                "replay_error": replay_error,
                "watch_collision": bool(watch_collision_fields),
                "source_score_collision": score_collision,
                "source_rank_collision": source_rank_collision,
                "candidate_match": raw_candidate_signal == raw_official_signal,
                "formal_match": raw_formal_signal == raw_candidate_signal,
                "score_changed": (
                    replay_status == "resolved"
                    and replay.get("final_delta") != Decimal("0")
                ),
                "collision_fields": "|".join(watch_collision_fields),
                "candidate_row_present": candidate_row is not None,
                "watch_source_score": raw_watch_source_score,
                "watch_source_rank": raw_watch_source_rank,
                "legacy_revision_history_status": source[
                    "legacy_revision_history_status"
                ],
                "legacy_precontract_revision_history_status": source[
                    "legacy_precontract_revision_history_status"
                ],
                "immutable_paired_source": bool(source["snapshot_commit_sha"])
                and bool(source["paired_commit_sha"]),
            }
            if formal_stock != stock_id(watch_row.get("stock_id")):
                errors.append(f"{report_date} {row_key} watch stock ID differs from formal stock ID")
            if text(audit_row["signal_date"]) != report_date:
                errors.append(f"{report_date} {row_key} signal_date differs from report date")

    group_columns = [
        "snapshot_report_date",
        "snapshot_revision",
        "report_line",
        "model_id",
    ]
    formal_audit = audit[audit["audit_row_type"].eq(FORMAL_ROW_TYPE)]
    expected_ranks: dict[int, int] = {}
    expected_rank_status: dict[int, str] = {}
    for _, indexes in formal_audit.groupby(group_columns, sort=False).groups.items():
        index_list = list(indexes)
        if any(
            computed_row_state.get(index, {}).get("replay_status") != "resolved"
            for index in index_list
        ):
            for index in index_list:
                expected_rank_status[index] = "unresolved_group_component"
            continue
        ordered = sorted(
            index_list,
            key=lambda index: (
                -computed_counterfactual_scores.get(index, Decimal("-Infinity")),
                stock_id(audit.at[index, "stock_id"]),
                text(audit.at[index, "source_row_index"]),
            ),
        )
        for expected_rank, index in enumerate(ordered, start=1):
            expected_ranks[index] = expected_rank
            expected_rank_status[index] = "resolved"

    for index, audit_row in audit.iterrows():
        state = computed_row_state.get(index)
        if state is None:
            continue
        report_date = text(audit_row["snapshot_report_date"])
        row_key = f"{audit_row['model_id']}/{audit_row['stock_id']}"
        rank_status = expected_rank_status.get(index, "unresolved_group_component")
        append_mismatch(
            errors,
            report_date,
            row_key,
            "rank_replay_status",
            audit_row["rank_replay_status"],
            rank_status,
        )
        if rank_status == "resolved":
            expected_rank = expected_ranks[index]
            published_rank = integer(
                audit.at[index, "published_model_rank"], "published_model_rank"
            )
            append_mismatch(
                errors,
                report_date,
                row_key,
                "counterfactual_model_rank",
                audit.at[index, "counterfactual_model_rank"],
                str(expected_rank),
            )
            append_mismatch(
                errors,
                report_date,
                row_key,
                "rank_delta",
                audit.at[index, "rank_delta"],
                str(expected_rank - published_rank),
            )
        else:
            expected_rank = None
            published_rank = integer(
                audit.at[index, "published_model_rank"], "published_model_rank"
            )
            append_mismatch(
                errors,
                report_date,
                row_key,
                "counterfactual_model_rank",
                audit_row["counterfactual_model_rank"],
                "",
            )
            append_mismatch(
                errors,
                report_date,
                row_key,
                "rank_delta",
                audit_row["rank_delta"],
                "",
            )

        unpaired_watch_score_rank = (
            not state["candidate_row_present"]
            and bool(state["watch_source_score"] or state["watch_source_rank"])
        )
        rank_changed = expected_rank is not None and expected_rank != published_rank
        legacy_revision_incomplete = (
            state["legacy_revision_history_status"] == LEGACY_HISTORY_INCOMPLETE
        )
        if state["replay_status"] != "resolved" or rank_status != "resolved":
            disposition = "unreplayable"
            impact = "independent_component_or_rank_replay_unresolved"
            reason = (
                state["replay_error"]
                or "counterfactual group rank could not be replayed"
            )
        elif legacy_revision_incomplete:
            disposition = "quarantined"
            impact = "legacy_revision_history_incomplete_fail_closed"
            reason = (
                "the date-only precontract snapshot path contains a Git blob revision "
                "without exact same-commit manifest and paired-source recovery evidence"
            )
        elif (
            state["source_score_collision"]
            or state["source_rank_collision"]
            or unpaired_watch_score_rank
        ):
            disposition = "quarantined"
            impact = "legacy_watch_source_score_rank_effect_unresolved"
            reason = (
                "legacy generic watch merge exposed a source score or rank value whose "
                "formal effect is not independently proven"
            )
        elif not state["candidate_match"] or not state["formal_match"]:
            disposition = "superseded"
            impact = "formal_warrant_lineage_superseded"
            reason = "formal or candidate warrant value differs from the official canonical row"
        elif state["score_changed"] or rank_changed:
            disposition = "superseded"
            impact = (
                "formal_score_and_rank_superseded"
                if rank_changed
                else "formal_score_superseded"
            )
            reason = (
                "legacy collision context changed the independently replayed formal score or rank: "
                f"fields={state['collision_fields']}"
            )
        else:
            disposition = "verified_clean"
            impact = (
                "watch_only_no_formal_score_or_rank_effect"
                if state["watch_collision"]
                else "none"
            )
            reason = (
                "legacy collision values differ, but independently replayed formal score and "
                f"rank are unchanged: fields={state['collision_fields']}"
                if state["watch_collision"]
                else "published and canonical collision contexts, components, and rank agree"
            )
        append_mismatch(
            errors,
            report_date,
            row_key,
            "formal_row_disposition",
            audit_row["formal_row_disposition"],
            disposition,
        )
        append_mismatch(
            errors,
            report_date,
            row_key,
            "impact_scope",
            audit_row["impact_scope"],
            impact,
        )
        append_mismatch(
            errors,
            report_date,
            row_key,
            "reason",
            audit_row["reason"],
            reason,
        )
        evidence_status = (
            "incomplete"
            if (
                state["replay_status"] != "resolved"
                or rank_status != "resolved"
                or legacy_revision_incomplete
            )
            else "complete"
        )
        append_mismatch(
            errors,
            report_date,
            row_key,
            "evidence_status",
            audit_row["evidence_status"],
            evidence_status,
        )
        promotion_eligible = (
            state["legacy_precontract_revision_history_status"]
            == LEGACY_HISTORY_COMPLETE
            and not legacy_revision_incomplete
            and disposition == "verified_clean"
            and evidence_status == "complete"
            and state["immutable_paired_source"]
        )
        append_mismatch(
            errors,
            report_date,
            row_key,
            "historical_promotion_evidence_eligible",
            audit_row["historical_promotion_evidence_eligible"],
            str(promotion_eligible),
        )

    allowed_dispositions = {
        "verified_clean",
        "superseded",
        "quarantined",
        "unreplayable",
        "not_applicable_revision_coverage",
    }
    unknown_dispositions = sorted(
        set(audit["formal_row_disposition"].astype(str)) - allowed_dispositions
    )
    if unknown_dispositions:
        errors.append(f"unknown formal row dispositions: {unknown_dispositions}")
    for _, row in audit.iterrows():
        disposition = text(row.get("formal_row_disposition"))
        evidence_status = text(row.get("evidence_status"))
        row_key = f"{row.get('snapshot_report_date')}/{row.get('model_id')}/{row.get('stock_id')}"
        lineage_incomplete_quarantine = (
            disposition == "quarantined"
            and text(row.get("impact_scope"))
            == "legacy_revision_history_incomplete_fail_closed"
        )
        if lineage_incomplete_quarantine:
            if evidence_status != "incomplete":
                errors.append(
                    f"{row_key} incomplete legacy revision quarantine requires incomplete evidence"
                )
        elif disposition in {"verified_clean", "superseded", "quarantined"}:
            if evidence_status != "complete":
                errors.append(
                    f"{row_key} disposition={disposition} requires complete evidence"
                )
        elif disposition == "unreplayable" and evidence_status != "incomplete":
            errors.append(f"{row_key} unreplayable disposition requires incomplete evidence")
    allowed_revision_history_statuses = {
        LEGACY_HISTORY_COMPLETE,
        LEGACY_HISTORY_INCOMPLETE,
        LEGACY_REVISION_RECOVERED,
        VERSIONED_REVISION_EXACT,
        CURRENT_REVISION_PENDING,
    }
    unknown_revision_history_statuses = sorted(
        set(audit["legacy_revision_history_status"].astype(str))
        - allowed_revision_history_statuses
    )
    if unknown_revision_history_statuses:
        errors.append(
            "unknown legacy_revision_history_status values: "
            f"{unknown_revision_history_statuses}"
        )
    unknown_precontract_statuses = sorted(
        set(audit["legacy_precontract_revision_history_status"].astype(str))
        - {LEGACY_HISTORY_COMPLETE, LEGACY_HISTORY_INCOMPLETE}
    )
    if unknown_precontract_statuses:
        errors.append(
            "unknown legacy_precontract_revision_history_status values: "
            f"{unknown_precontract_statuses}"
        )
    unknown_promotion_values = sorted(
        set(audit["historical_promotion_evidence_eligible"].astype(str))
        - {"True", "False"}
    )
    if unknown_promotion_values:
        errors.append(
            "historical_promotion_evidence_eligible must be boolean text: "
            f"{unknown_promotion_values}"
        )
    absent_contexts = formal_audit.loc[
        formal_audit["candidate_row_present"].astype(str).eq("False"),
        "counterfactual_score_context",
    ]
    if not absent_contexts.empty and set(absent_contexts.astype(str)) != {"{}"}:
        errors.append("candidate-absent rows must retain empty canonical score contexts")
    resolved = formal_audit["replay_status"].astype(str).eq("resolved")
    rounding_gap = pd.to_numeric(
        formal_audit.loc[resolved, "published_component_replay_rounding_gap"],
        errors="coerce",
    )
    if rounding_gap.isna().any() or bool(rounding_gap.abs().gt(0.3).any()):
        errors.append("resolved component replay rounding gap exceeds the 0.3 display bound")
    if not formal_audit.loc[resolved, "published_component_replay_match"].astype(str).eq("True").all():
        errors.append("resolved published component formulas must match within rounding tolerance")
    if not formal_audit.loc[~resolved, "published_component_replay_match"].astype(str).eq("False").all():
        errors.append("unresolved published component formulas must be marked unmatched")

    markdown = md_path.read_text(encoding="utf-8")
    formal_counts = (
        formal_audit["formal_row_disposition"].astype(str).value_counts().to_dict()
    )
    watch_superseded = int(
        formal_audit["watch_disposition"]
        .astype(str)
        .eq("superseded_advisory_snapshot")
        .sum()
    )
    replay_resolved = int(resolved.sum())
    candidate_absent = int(
        formal_audit["candidate_row_present"].astype(str).eq("False").sum()
    )
    incomplete_precontract_dates = audit.loc[
        audit["legacy_precontract_revision_history_status"]
        .astype(str)
        .eq(LEGACY_HISTORY_INCOMPLETE),
        "snapshot_report_date",
    ].nunique()
    promotion_eligible = int(
        formal_audit["historical_promotion_evidence_eligible"]
        .astype(str)
        .eq("True")
        .sum()
    )
    collision_counts = {
        field: int(
            formal_audit["collision_fields"]
            .astype(str)
            .map(lambda value: field in value.split("|") if value else False)
            .sum()
        )
        for field in COLLISION_FIELDS
    }
    required_markdown = (
        f"Formal volume v2 rows: `{len(formal_audit)}`",
        f"Formal verified clean: `{formal_counts.get('verified_clean', 0)}`",
        f"Formal superseded: `{formal_counts.get('superseded', 0)}`",
        f"Formal quarantined: `{formal_counts.get('quarantined', 0)}`",
        f"Legacy precontract history incomplete dates: `{incomplete_precontract_dates}`",
        f"Historical promotion evidence eligible rows: `{promotion_eligible}/{len(formal_audit)}`",
        f"Superseded advisory watch rows: `{watch_superseded}`",
        f"Independent component replay resolved: `{replay_resolved}/{len(formal_audit)}`",
        f"Candidate-absent canonical score contexts: `{candidate_absent}` stored as `{{}}`",
        f"Warrant collision rows: `{collision_counts['warrant_flow_signal']}`",
        f"TDCC-status collision rows: `{collision_counts['tdcc_status']}`",
        f"False-breakout collision rows: `{collision_counts['false_breakout_risk']}`",
        "Watch/candidate source score collisions: "
        f"`{int(formal_audit['watch_candidate_score_collision'].astype(str).eq('True').sum())}`",
        "Watch/candidate source rank collisions: "
        f"`{int(formal_audit['watch_candidate_rank_collision'].astype(str).eq('True').sum())}`",
        "Historical daily snapshots were read only and were not rewritten.",
    )
    for token in required_markdown:
        if token not in markdown:
            errors.append(f"Markdown audit missing required token: {token}")
    revision_count = len(expected_revisions)
    coverage_tokens = (
        f"Dynamic source coverage: `{revision_count}/{revision_count}` revisions",
        f"Paired snapshot coverage: `{revision_count}/{revision_count}` revisions",
    )
    if not any(token in markdown for token in coverage_tokens):
        errors.append(
            "Markdown audit missing dynamic coverage token: "
            f"expected_one_of={coverage_tokens}"
        )
    if "audited_at" in markdown or "generated_at" in markdown:
        errors.append("deterministic Markdown must not contain a generated timestamp")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the deterministic volume v2 warrant lineage history audit."
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--csv", type=Path)
    parser.add_argument("--md", type=Path)
    parser.add_argument("--docs-csv", type=Path)
    parser.add_argument("--docs-md", type=Path)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    errors = validate(
        root,
        args.csv or root / CSV_PATH.relative_to(ROOT),
        args.md or root / MD_PATH.relative_to(ROOT),
        args.docs_csv or root / DOCS_CSV_PATH.relative_to(ROOT),
        args.docs_md or root / DOCS_MD_PATH.relative_to(ROOT),
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"volume v2 warrant lineage history audit validation failed: errors={len(errors)}")
        return 1
    print(
        "volume v2 warrant lineage history audit validation passed: "
        "dynamic_historical_and_current_coverage=verified"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
