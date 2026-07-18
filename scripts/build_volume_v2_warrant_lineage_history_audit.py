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
from typing import Any, Iterable

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
MANIFEST_PATH = SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv"
OUTPUT_CSV = ROOT / "output" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.csv"
OUTPUT_MD = ROOT / "output" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.md"
DOCS_CSV = ROOT / "docs" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.csv"
DOCS_MD = ROOT / "docs" / "latest" / "volume_v2_warrant_lineage_history_audit_latest.md"

AUDIT_VERSION = "volume_v2_warrant_lineage_history_audit_v2"
CURRENT_SOURCE_RESOLUTION = "current_worktree_exact_source_files"
PUBLISHED_PENDING_SOURCE_RESOLUTION = (
    "published_snapshot_exact_current_sources_pending_commit"
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
    "snapshot_report_date",
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


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).strip()
    return "" if text.lower() == "nan" else text


def normalize_stock_id(value: Any) -> str:
    text = normalize_text(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = re.sub(r"[^0-9]", "", text)
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def normalize_warrant_signal(value: Any) -> str:
    return normalize_text(value).lower()


def canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {str(key): normalize_text(value) for key, value in values.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return sha256_bytes(payload)


def read_csv_bytes(payload: bytes, source: str) -> pd.DataFrame:
    try:
        return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False)
    except Exception as exc:  # pragma: no cover - defensive source diagnostic
        raise RuntimeError(f"failed to parse CSV source {source}: {exc}") from exc


def run_git(root: Path, *args: str, allow_failure: bool = False) -> bytes:
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


def git_blob(root: Path, commit_sha: str, repo_path: str) -> bytes:
    return run_git(root, "show", f"{commit_sha}:{repo_path}")


def find_snapshot_commits(
    root: Path,
    snapshot_path: str,
    expected_sha256: str,
) -> list[str]:
    commits = run_git(root, "log", "--format=%H", "--", snapshot_path).decode(
        "ascii", errors="strict"
    ).split()
    matches: list[str] = []
    for commit_sha in commits:
        payload = run_git(
            root,
            "show",
            f"{commit_sha}:{snapshot_path}",
            allow_failure=True,
        )
        if payload and expected_sha256 in manifest_v1_sha256_candidates(payload):
            matches.append(commit_sha)
    return matches


def find_snapshot_commit(
    root: Path,
    snapshot_path: str,
    expected_sha256: str,
) -> str:
    matches = find_snapshot_commits(root, snapshot_path, expected_sha256)
    if len(matches) != 1:
        raise RuntimeError(
            "snapshot SHA must resolve to exactly one history commit: "
            f"path={snapshot_path} sha256={expected_sha256} matches={matches}"
        )
    return matches[0]


def resolve_paired_source_commit(
    root: Path,
    pipeline_commit_sha: str,
    snapshot_commit_sha: str,
    expected_formal_sha256: str,
) -> tuple[str, str]:
    pipeline_payload = run_git(
        root,
        "show",
        f"{pipeline_commit_sha}:{FORMAL_SOURCE_PATH}",
        allow_failure=True,
    )
    if pipeline_payload and sha256_bytes(pipeline_payload) == expected_formal_sha256:
        return pipeline_commit_sha, "manifest_pipeline_commit_exact_source_blob"
    snapshot_commit_payload = git_blob(root, snapshot_commit_sha, FORMAL_SOURCE_PATH)
    if sha256_bytes(snapshot_commit_payload) != expected_formal_sha256:
        raise RuntimeError(
            "neither pipeline commit nor snapshot history commit contains the exact formal source "
            f"blob: pipeline_commit={pipeline_commit_sha} snapshot_commit={snapshot_commit_sha}"
        )
    return snapshot_commit_sha, "snapshot_history_exact_blob_fallback"


def dispatcher_warrant_source_mode(code_payload: bytes) -> str:
    try:
        tree = ast.parse(code_payload.decode("utf-8"))
    except Exception as exc:
        raise RuntimeError(f"failed to parse production dispatcher source: {exc}") from exc
    target_function: ast.FunctionDef | None = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "append_volume_breakout_signals":
            target_function = node
            break
    if target_function is None:
        raise RuntimeError("production source has no append_volume_breakout_signals function")

    watch_update_lines: list[int] = []
    authoritative_override_lines: list[int] = []
    for node in ast.walk(target_function):
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
                watch_update_lines.append(node.lineno)
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if not isinstance(target, ast.Subscript):
                    continue
                if not isinstance(target.value, ast.Name) or target.value.id != "score_source":
                    continue
                slice_node = target.slice
                if isinstance(slice_node, ast.Constant) and slice_node.value == "warrant_flow_signal":
                    authoritative_override_lines.append(node.lineno)

    if not watch_update_lines and authoritative_override_lines:
        return "canonical_candidate_explicit_allowlist"
    if len(watch_update_lines) != 1:
        raise RuntimeError(
            "dispatcher must have exactly one score_source.update(row.to_dict()) call: "
            f"lines={watch_update_lines}"
        )
    update_line = watch_update_lines[0]
    later_overrides = [line for line in authoritative_override_lines if line > update_line]
    if later_overrides:
        return "canonical_candidate_after_watch_merge"
    return "legacy_watch_overrides_candidate"


def decimal_value(value: Any, field: str) -> Decimal:
    text = normalize_text(value)
    try:
        return Decimal(text)
    except InvalidOperation as exc:
        raise RuntimeError(f"invalid decimal {field}={text!r}") from exc


def decimal_text(value: Decimal, reference: str = "") -> str:
    if value == value.to_integral():
        if "." in reference:
            decimal_places = len(reference.partition(".")[2])
            return f"{value:.{decimal_places}f}"
        return str(value.to_integral())
    normalized = format(value.normalize(), "f")
    return normalized.rstrip("0").rstrip(".") if "." in normalized else normalized


def int_value(value: Any, field: str) -> int:
    number = decimal_value(value, field)
    if number != number.to_integral():
        raise RuntimeError(f"invalid integer {field}={value!r}")
    return int(number)


def truthy(value: Any) -> bool:
    return normalize_text(value).lower() in TRUTHY_VALUES


def first_value(values: dict[str, Any], *names: str) -> str:
    for name in names:
        for candidate in (name, f"{name}_x", f"{name}_y"):
            value = normalize_text(values.get(candidate, ""))
            if value:
                return value
    return ""


def resolved_collision_context(values: dict[str, Any]) -> dict[str, str]:
    if not values:
        return {}
    warrant = first_value(values, "warrant_flow_signal", "warrant_status").lower()
    tdcc_status = first_value(values, "tdcc_status", "tdcc_judgement", "tdcc_judge").lower()
    accumulation = truthy(values.get("tdcc_accumulation_signal", ""))
    downgrade_flags = first_value(values, "downgrade_flags")
    false_breakout = truthy(values.get("false_breakout_risk", ""))
    tdcc_positive = tdcc_status in POSITIVE_TDCC_STATUSES or accumulation
    tdcc_distribution = (
        tdcc_status == "distribution_warning"
        or "tdcc_distribution_warning" in downgrade_flags
    )
    return {
        "warrant_flow_signal": warrant,
        "tdcc_status": tdcc_status,
        "false_breakout_risk": str(false_breakout),
        "tdcc_accumulation_signal": str(accumulation),
        "downgrade_flags": downgrade_flags,
        "tdcc_positive": str(tdcc_positive),
        "tdcc_distribution": str(tdcc_distribution),
    }


def build_collision_contexts(
    candidate_row: pd.Series | None,
    watch_row: pd.Series,
    dispatcher_mode: str,
) -> tuple[dict[str, str], dict[str, str]]:
    candidate_values = candidate_row.to_dict() if candidate_row is not None else {}
    published_values = dict(candidate_values)
    published_values.update(watch_row.to_dict())
    if dispatcher_mode.startswith("canonical_candidate"):
        published_values["warrant_flow_signal"] = first_value(
            candidate_values,
            "warrant_flow_signal",
            "warrant_status",
        )
    published = resolved_collision_context(published_values)
    canonical = resolved_collision_context(candidate_values)
    return published, canonical


def collision_component_effects(
    model_id: str,
    context: dict[str, str],
) -> dict[str, Decimal]:
    policy = MODEL_COLLISION_COMPONENT_POLICY.get(model_id)
    if policy is None:
        raise RuntimeError(f"missing collision component policy for model_id={model_id}")
    warrant_bullish = context.get("warrant_flow_signal", "") in BULLISH_WARRANT_SIGNALS
    tdcc_positive = context.get("tdcc_positive", "False") == "True"
    tdcc_distribution = context.get("tdcc_distribution", "False") == "True"
    false_breakout = context.get("false_breakout_risk", "False") == "True"
    warrant_bonus = policy["warrant_base_bonus"] if warrant_bullish else Decimal("0")
    base_effect = warrant_bonus
    if tdcc_positive:
        base_effect += policy["tdcc_positive_base_bonus"]
    if tdcc_distribution:
        base_effect -= policy["tdcc_distribution_base_penalty"]
    if false_breakout:
        base_effect -= policy["false_breakout_base_penalty"]
    tdcc_score_effect = (
        policy["tdcc_positive_score_bonus"] if tdcc_positive else Decimal("0")
    )
    risk_penalty_effect = Decimal("0")
    if tdcc_distribution:
        risk_penalty_effect += policy["tdcc_distribution_risk_penalty"]
    if false_breakout:
        risk_penalty_effect += policy["false_breakout_risk_penalty"]
    return {
        "warrant_bonus": warrant_bonus,
        "base_model_score": base_effect,
        "tdcc_score": tdcc_score_effect,
        "risk_penalty": risk_penalty_effect,
    }


def clamp_decimal(value: Decimal) -> Decimal:
    return max(Decimal("0"), min(Decimal("100"), value))


def context_json(context: dict[str, str]) -> str:
    return json.dumps(context, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def effects_json(effects: dict[str, Decimal]) -> str:
    serializable = {key: decimal_text(value) for key, value in effects.items()}
    return json.dumps(serializable, sort_keys=True, separators=(",", ":"))


def collision_field_names(
    published: dict[str, str],
    canonical: dict[str, str],
) -> tuple[str, ...]:
    defaults = {
        "warrant_flow_signal": "",
        "tdcc_status": "",
        "false_breakout_risk": "False",
    }
    return tuple(
        field
        for field in COLLISION_FIELDS
        if published.get(field, defaults[field]) != canonical.get(field, defaults[field])
    )


def replay_collision_components(
    formal_row: pd.Series | dict[str, Any],
    model_id: str,
    published_context: dict[str, str],
    canonical_context: dict[str, str],
) -> dict[str, Decimal | str]:
    published_effects = collision_component_effects(model_id, published_context)
    canonical_effects = collision_component_effects(model_id, canonical_context)
    published_base = decimal_value(formal_row.get("base_model_score", ""), "base_model_score")
    published_operation = decimal_value(formal_row.get("operation_score", ""), "operation_score")
    published_tdcc = decimal_value(formal_row.get("tdcc_score", ""), "tdcc_score")
    published_pattern = decimal_value(formal_row.get("pattern_score", ""), "pattern_score")
    published_risk = decimal_value(formal_row.get("risk_penalty", ""), "risk_penalty")
    published_final = decimal_value(formal_row.get("final_rank_score", ""), "final_rank_score")
    base_effect_delta = (
        canonical_effects["base_model_score"] - published_effects["base_model_score"]
    )
    if published_base in {Decimal("0"), Decimal("100")} and base_effect_delta != 0:
        raise RuntimeError(
            "published base_model_score is clamped at a boundary; exact raw component replay is unavailable"
        )
    fixed_base = published_base - published_effects["base_model_score"]
    fixed_tdcc = published_tdcc - published_effects["tdcc_score"]
    fixed_risk = published_risk - published_effects["risk_penalty"]
    if fixed_tdcc < 0 or fixed_risk < 0:
        raise RuntimeError(
            "published components cannot contain the resolved legacy collision effects: "
            f"fixed_tdcc={fixed_tdcc} fixed_risk={fixed_risk}"
        )
    published_replay = clamp_decimal(
        published_base + published_operation + published_tdcc + published_pattern - published_risk
    )
    replay_rounding_gap = published_replay - published_final
    if abs(replay_rounding_gap) > Decimal("0.3"):
        raise RuntimeError(
            "published rounded component formula exceeds replay tolerance: "
            f"replay={published_replay} formal={published_final} gap={replay_rounding_gap}"
        )
    counterfactual_raw_base = fixed_base + canonical_effects["base_model_score"]
    counterfactual_base = clamp_decimal(counterfactual_raw_base)
    counterfactual_tdcc = fixed_tdcc + canonical_effects["tdcc_score"]
    counterfactual_risk = fixed_risk + canonical_effects["risk_penalty"]
    if counterfactual_tdcc < 0 or counterfactual_risk < 0:
        raise RuntimeError("counterfactual component replay produced a negative component")
    final_effect_delta = (
        base_effect_delta
        + canonical_effects["tdcc_score"]
        - published_effects["tdcc_score"]
        - (
            canonical_effects["risk_penalty"]
            - published_effects["risk_penalty"]
        )
    )
    if published_final in {Decimal("0"), Decimal("100")} and final_effect_delta != 0:
        raise RuntimeError(
            "published final_rank_score is clamped at a boundary; exact counterfactual replay is unavailable"
        )
    counterfactual_final = clamp_decimal(published_final + final_effect_delta)
    return {
        "published_effects": effects_json(published_effects),
        "counterfactual_effects": effects_json(canonical_effects),
        "published_base": published_base,
        "counterfactual_base": counterfactual_base,
        "base_delta": counterfactual_base - published_base,
        "published_operation": published_operation,
        "published_tdcc": published_tdcc,
        "counterfactual_tdcc": counterfactual_tdcc,
        "tdcc_delta": counterfactual_tdcc - published_tdcc,
        "published_pattern": published_pattern,
        "published_risk": published_risk,
        "counterfactual_risk": counterfactual_risk,
        "risk_delta": counterfactual_risk - published_risk,
        "published_replay_final": published_replay,
        "published_replay_rounding_gap": replay_rounding_gap,
        "published_final": published_final,
        "counterfactual_final": counterfactual_final,
        "final_delta": counterfactual_final - published_final,
    }


def counterfactual_rank_order(
    frame: pd.DataFrame,
    indexes: Iterable[int],
) -> list[int]:
    index_list = list(indexes)
    unresolved = [
        index
        for index in index_list
        if normalize_text(frame.at[index, "replay_status"]) != "resolved"
    ]
    if unresolved:
        raise RuntimeError(f"counterfactual rank has unresolved component rows: {unresolved}")
    return sorted(
        index_list,
        key=lambda index: (
            -decimal_value(
                frame.at[index, "counterfactual_final_rank_score"],
                "counterfactual_final_rank_score",
            ),
            normalize_stock_id(frame.at[index, "stock_id"]),
            normalize_text(frame.at[index, "source_row_index"]),
        ),
    )


def first_candidate_lookup(candidates: pd.DataFrame) -> dict[str, tuple[int, pd.Series]]:
    lookup: dict[str, tuple[int, pd.Series]] = {}
    for position, (_, row) in enumerate(candidates.iterrows()):
        stock_id = normalize_stock_id(row.get("stock_id", row.get("ticker", "")))
        if stock_id and stock_id not in lookup:
            lookup[stock_id] = (position, row)
    return lookup


def unique_stock_lookup(
    frame: pd.DataFrame,
    source_name: str,
) -> dict[str, tuple[int, pd.Series]]:
    lookup: dict[str, tuple[int, pd.Series]] = {}
    duplicates: list[str] = []
    for position, (_, row) in enumerate(frame.iterrows()):
        stock_id = normalize_stock_id(row.get("stock_id", ""))
        if not stock_id:
            continue
        if stock_id in lookup:
            duplicates.append(stock_id)
        else:
            lookup[stock_id] = (position, row)
    if duplicates:
        raise RuntimeError(
            f"{source_name} has duplicate normalized stock_id rows: {sorted(set(duplicates))}"
        )
    return lookup


def manifest_rows(root: Path) -> pd.DataFrame:
    path = root / MANIFEST_PATH.relative_to(ROOT)
    if not path.exists():
        raise RuntimeError(f"missing snapshot manifest: {path.as_posix()}")
    manifest = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {
        "snapshot_report_date",
        "pipeline_commit_sha",
        "artifact_id",
        "source_path",
        "snapshot_path",
        "snapshot_sha256",
        "row_count",
    }
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise RuntimeError(f"snapshot manifest missing columns: {missing}")
    return manifest


def file_payload(root: Path, repo_path: str) -> bytes:
    path = root / Path(repo_path)
    if not path.exists():
        raise RuntimeError(f"missing current source artifact: {repo_path}")
    return path.read_bytes()


def volume_v2_formal_rows(payload: bytes, source: str) -> pd.DataFrame:
    formal = read_csv_bytes(payload, source)
    if "model_id" not in formal.columns:
        return pd.DataFrame()
    return formal[formal["model_id"].astype(str).isin(VOLUME_V2_MODELS)].copy()


def formal_report_date(formal: pd.DataFrame, source: str) -> str:
    if formal.empty or "signal_date" not in formal.columns:
        return ""
    dates = sorted(
        {
            normalize_text(value)
            for value in formal["signal_date"].tolist()
            if normalize_text(value)
        }
    )
    if len(dates) != 1 or not re.fullmatch(r"\d{8}", dates[0]):
        raise RuntimeError(
            f"volume v2 formal source must contain exactly one YYYYMMDD signal date: "
            f"source={source} dates={dates}"
        )
    return dates[0]


def build_audit_sources(root: Path, manifest: pd.DataFrame) -> list[dict[str, Any]]:
    """Resolve every immutable v2 snapshot plus an unpublished current snapshot.

    A just-published snapshot may not have a Git commit yet inside the producing
    workflow.  In that narrow state it must byte-match the current formal source,
    and all paired sources are pinned from the same working tree.  The next run
    resolves the same snapshot SHA to its immutable Git commit.
    """

    selected = manifest[
        manifest["artifact_id"].astype(str).eq("model_signals_for_report")
    ].copy()
    duplicate_dates = selected["snapshot_report_date"].astype(str).duplicated(keep=False)
    if duplicate_dates.any():
        dates = sorted(
            selected.loc[duplicate_dates, "snapshot_report_date"].astype(str).unique()
        )
        raise RuntimeError(f"duplicate model_signals_for_report manifest dates: {dates}")

    sources: list[dict[str, Any]] = []
    snapshot_dates: set[str] = set()
    current_formal_payload = file_payload(root, FORMAL_SOURCE_PATH)
    current_formal = volume_v2_formal_rows(current_formal_payload, FORMAL_SOURCE_PATH)
    current_report_date = formal_report_date(current_formal, FORMAL_SOURCE_PATH)
    head_sha = run_git(root, "rev-parse", "HEAD").decode("ascii").strip()

    for _, manifest_row in selected.sort_values("snapshot_report_date").iterrows():
        report_date = normalize_text(manifest_row["snapshot_report_date"])
        if not re.fullmatch(r"\d{8}", report_date):
            raise RuntimeError(f"invalid snapshot report date: {report_date!r}")
        if normalize_text(manifest_row["source_path"]) != FORMAL_SOURCE_PATH:
            raise RuntimeError(
                f"unexpected formal source path for {report_date}: {manifest_row['source_path']}"
            )
        snapshot_path = normalize_text(manifest_row["snapshot_path"])
        manifest_snapshot_sha256 = normalize_text(manifest_row["snapshot_sha256"])
        pipeline_commit_sha = normalize_text(manifest_row["pipeline_commit_sha"])
        snapshot_payload = file_payload(root, snapshot_path)
        snapshot_formal = volume_v2_formal_rows(snapshot_payload, snapshot_path)
        if snapshot_formal.empty:
            continue
        if manifest_snapshot_sha256 not in manifest_v1_sha256_candidates(
            snapshot_payload
        ):
            raise RuntimeError(
                f"formal v2 snapshot SHA mismatch: report_date={report_date} path={snapshot_path}"
            )
        canonical_snapshot_sha256 = sha256_bytes(snapshot_payload)
        if formal_report_date(snapshot_formal, snapshot_path) != report_date:
            raise RuntimeError(
                f"formal snapshot signal date differs from manifest: report_date={report_date}"
            )

        matches = find_snapshot_commits(root, snapshot_path, manifest_snapshot_sha256)
        if len(matches) == 1:
            snapshot_commit_sha = matches[0]
            paired_commit_sha, paired_resolution = resolve_paired_source_commit(
                root,
                pipeline_commit_sha,
                snapshot_commit_sha,
                canonical_snapshot_sha256,
            )
            payloads = {
                "formal_payload": git_blob(root, paired_commit_sha, FORMAL_SOURCE_PATH),
                "watch_payload": git_blob(root, paired_commit_sha, WATCH_SOURCE_PATH),
                "candidate_payload": git_blob(root, paired_commit_sha, CANDIDATE_SOURCE_PATH),
                "official_payload": git_blob(
                    root, paired_commit_sha, OFFICIAL_WARRANT_SOURCE_PATH
                ),
                "code_payload": git_blob(root, paired_commit_sha, PRODUCTION_CODE_PATH),
            }
            expected_session_status = "trading_day_snapshot_present"
        elif not matches:
            if (
                report_date != current_report_date
                or canonical_text_bytes(snapshot_payload)
                != canonical_text_bytes(current_formal_payload)
            ):
                raise RuntimeError(
                    "uncommitted formal snapshot must byte-match the same-date current source: "
                    f"report_date={report_date} path={snapshot_path}"
                )
            snapshot_commit_sha = ""
            paired_commit_sha = ""
            paired_resolution = PUBLISHED_PENDING_SOURCE_RESOLUTION
            payloads = {
                "formal_payload": current_formal_payload,
                "watch_payload": file_payload(root, WATCH_SOURCE_PATH),
                "candidate_payload": file_payload(root, CANDIDATE_SOURCE_PATH),
                "official_payload": file_payload(root, OFFICIAL_WARRANT_SOURCE_PATH),
                "code_payload": file_payload(root, PRODUCTION_CODE_PATH),
            }
            expected_session_status = "published_snapshot_pending_commit"
        else:
            raise RuntimeError(
                "snapshot SHA must resolve to at most one history commit: "
                f"path={snapshot_path} sha256={manifest_snapshot_sha256} matches={matches}"
            )
        if sha256_bytes(payloads["formal_payload"]) != canonical_snapshot_sha256:
            raise RuntimeError(
                f"paired formal source does not equal snapshot: report_date={report_date}"
            )
        sources.append(
            {
                "report_date": report_date,
                "expected_session_status": expected_session_status,
                "pipeline_commit_sha": pipeline_commit_sha,
                "snapshot_commit_sha": snapshot_commit_sha,
                "paired_commit_sha": paired_commit_sha,
                "paired_resolution": paired_resolution,
                "snapshot_path": snapshot_path,
                "snapshot_sha256": canonical_snapshot_sha256,
                "manifest_snapshot_sha256": manifest_snapshot_sha256,
                "manifest_row": manifest_row,
                **payloads,
            }
        )
        snapshot_dates.add(report_date)

    if not current_formal.empty:
        if current_report_date in snapshot_dates:
            matching = next(
                source for source in sources if source["report_date"] == current_report_date
            )
            if sha256_bytes(current_formal_payload) != matching["snapshot_sha256"]:
                raise RuntimeError(
                    "current formal source conflicts with its immutable same-date snapshot: "
                    f"report_date={current_report_date}"
                )
        else:
            sources.append(
                {
                    "report_date": current_report_date,
                    "expected_session_status": "current_formal_latest_pending_snapshot",
                    "pipeline_commit_sha": head_sha,
                    "snapshot_commit_sha": "",
                    "paired_commit_sha": "",
                    "paired_resolution": CURRENT_SOURCE_RESOLUTION,
                    "snapshot_path": FORMAL_SOURCE_PATH,
                    "snapshot_sha256": sha256_bytes(current_formal_payload),
                    "manifest_row": None,
                    "formal_payload": current_formal_payload,
                    "watch_payload": file_payload(root, WATCH_SOURCE_PATH),
                    "candidate_payload": file_payload(root, CANDIDATE_SOURCE_PATH),
                    "official_payload": file_payload(root, OFFICIAL_WARRANT_SOURCE_PATH),
                    "code_payload": file_payload(root, PRODUCTION_CODE_PATH),
                }
            )
    return sorted(sources, key=lambda source: source["report_date"])


def build_audit_dataframe(root: Path = ROOT) -> pd.DataFrame:
    root = root.resolve()
    manifest = manifest_rows(root)
    records: list[dict[str, str]] = []

    for source in build_audit_sources(root, manifest):
        report_date = source["report_date"]
        manifest_row = source["manifest_row"]
        snapshot_path = source["snapshot_path"]
        snapshot_sha256 = source["snapshot_sha256"]
        pipeline_commit_sha = source["pipeline_commit_sha"]
        snapshot_commit_sha = source["snapshot_commit_sha"]
        paired_commit_sha = source["paired_commit_sha"]
        paired_resolution = source["paired_resolution"]
        formal_payload = source["formal_payload"]
        watch_payload = source["watch_payload"]
        candidate_payload = source["candidate_payload"]
        official_payload = source["official_payload"]
        code_payload = source["code_payload"]
        formal = read_csv_bytes(formal_payload, FORMAL_SOURCE_PATH)
        watch = read_csv_bytes(watch_payload, WATCH_SOURCE_PATH)
        candidates = read_csv_bytes(candidate_payload, CANDIDATE_SOURCE_PATH)
        official = read_csv_bytes(official_payload, OFFICIAL_WARRANT_SOURCE_PATH)
        formal = formal[formal["model_id"].astype(str).isin(VOLUME_V2_MODELS)].copy()

        candidate_lookup = first_candidate_lookup(candidates)
        official_lookup = unique_stock_lookup(official, OFFICIAL_WARRANT_SOURCE_PATH)
        source_mode = dispatcher_warrant_source_mode(code_payload)
        manifest_sha = (
            canonical_row_sha256(manifest_row) if manifest_row is not None else ""
        )

        for formal_position, (_, formal_row) in enumerate(formal.iterrows()):
            model_id = normalize_text(formal_row.get("model_id"))
            stock_id = normalize_stock_id(formal_row.get("stock_id"))
            signal_date = normalize_text(formal_row.get("signal_date"))
            if signal_date != report_date:
                raise RuntimeError(
                    "formal row signal date differs from audit report date: "
                    f"report_date={report_date} signal_date={signal_date} stock_id={stock_id}"
                )
            source_row_index = normalize_text(formal_row.get("source_row_index"))
            match = re.fullmatch(r"volume_breakout:(\d+)", source_row_index)
            if not match:
                raise RuntimeError(
                    f"invalid volume source_row_index: report_date={report_date} value={source_row_index}"
                )
            watch_position = int(match.group(1))
            if watch_position >= len(watch):
                raise RuntimeError(
                    f"watch source row out of range: report_date={report_date} index={watch_position}"
                )
            watch_row = watch.iloc[watch_position]
            if normalize_stock_id(watch_row.get("stock_id")) != stock_id:
                raise RuntimeError(
                    "watch source row stock mismatch: "
                    f"report_date={report_date} source_row_index={source_row_index} stock_id={stock_id}"
                )
            candidate_item = candidate_lookup.get(stock_id)
            official_item = official_lookup.get(stock_id)
            if candidate_item is None:
                candidate_position: int | None = None
                candidate_row: pd.Series | None = None
            else:
                candidate_position, candidate_row = candidate_item
            if official_item is None:
                official_position: int | None = None
                official_row: pd.Series | None = None
            else:
                official_position, official_row = official_item

            watch_signal = normalize_warrant_signal(watch_row.get("warrant_flow_signal"))
            candidate_signal = (
                normalize_warrant_signal(candidate_row.get("warrant_flow_signal"))
                if candidate_row is not None
                else ""
            )
            official_signal = (
                normalize_warrant_signal(official_row.get("warrant_flow_signal"))
                if official_row is not None
                else ""
            )
            formal_signal = normalize_warrant_signal(formal_row.get("warrant_flow_signal"))
            watch_source_score = normalize_text(watch_row.get("score"))
            candidate_source_score = (
                normalize_text(candidate_row.get("score"))
                if candidate_row is not None
                else ""
            )
            watch_source_rank = normalize_text(watch_row.get("rank"))
            candidate_source_rank = (
                normalize_text(candidate_row.get("rank"))
                if candidate_row is not None
                else ""
            )
            watch_candidate_score_collision = (
                candidate_row is not None
                and watch_source_score != candidate_source_score
            )
            watch_candidate_rank_collision = (
                candidate_row is not None
                and watch_source_rank != candidate_source_rank
            )
            published_context, counterfactual_context = build_collision_contexts(
                candidate_row,
                watch_row,
                source_mode,
            )
            watch_context = resolved_collision_context(watch_row.to_dict())
            candidate_context = resolved_collision_context(
                candidate_row.to_dict() if candidate_row is not None else {}
            )
            score_basis_signal = published_context.get("warrant_flow_signal", "")
            score_source = (
                "canonical_candidate"
                if source_mode == "canonical_candidate_after_watch_merge"
                else "legacy_watch"
            )
            collision_names = collision_field_names(
                watch_context,
                counterfactual_context,
            )
            published_collision_names = collision_field_names(
                published_context,
                counterfactual_context,
            )
            published_effects = collision_component_effects(model_id, published_context)
            counterfactual_effects = collision_component_effects(
                model_id,
                counterfactual_context,
            )
            bonus = WARRANT_BONUS_BY_MODEL[model_id]
            published_bonus = published_effects["warrant_bonus"]
            counterfactual_bonus = counterfactual_effects["warrant_bonus"]
            published_score_text = normalize_text(formal_row.get("final_rank_score"))
            replay_error = ""
            try:
                replay = replay_collision_components(
                    formal_row,
                    model_id,
                    published_context,
                    counterfactual_context,
                )
                replay_status = "resolved"
            except (RuntimeError, KeyError) as exc:
                replay = {}
                replay_status = "unresolved"
                replay_error = normalize_text(exc)

            def replay_decimal(field: str, reference: str = "") -> str:
                value = replay.get(field)
                return decimal_text(value, reference) if isinstance(value, Decimal) else ""

            records.append(
                {
                    "audit_version": AUDIT_VERSION,
                    "snapshot_report_date": report_date,
                    "expected_session_status": source["expected_session_status"],
                    "pipeline_commit_sha": pipeline_commit_sha,
                    "snapshot_commit_sha": snapshot_commit_sha,
                    "paired_source_commit_sha": paired_commit_sha,
                    "paired_source_resolution": paired_resolution,
                    "dispatcher_warrant_source_mode": source_mode,
                    "production_code_sha256": sha256_bytes(code_payload),
                    "formal_snapshot_path": snapshot_path,
                    "formal_snapshot_sha256": snapshot_sha256,
                    "formal_snapshot_manifest_v1_sha256": source.get(
                        "manifest_snapshot_sha256", ""
                    ),
                    "watch_artifact_path": WATCH_SOURCE_PATH,
                    "watch_artifact_sha256": sha256_bytes(watch_payload),
                    "candidate_artifact_path": CANDIDATE_SOURCE_PATH,
                    "candidate_artifact_sha256": sha256_bytes(candidate_payload),
                    "official_warrant_artifact_path": OFFICIAL_WARRANT_SOURCE_PATH,
                    "official_warrant_artifact_sha256": sha256_bytes(official_payload),
                    "manifest_row_sha256": manifest_sha,
                    "formal_row_sha256": canonical_row_sha256(formal_row),
                    "watch_row_sha256": canonical_row_sha256(watch_row),
                    "candidate_row_sha256": (
                        canonical_row_sha256(candidate_row) if candidate_row is not None else ""
                    ),
                    "candidate_row_present": str(candidate_row is not None),
                    "official_warrant_row_sha256": (
                        canonical_row_sha256(official_row) if official_row is not None else ""
                    ),
                    "official_warrant_row_present": str(official_row is not None),
                    "formal_row_number": str(formal_position),
                    "watch_row_number": str(watch_position),
                    "candidate_row_number": (
                        str(candidate_position) if candidate_position is not None else ""
                    ),
                    "official_warrant_row_number": (
                        str(official_position) if official_position is not None else ""
                    ),
                    "signal_date": signal_date,
                    "report_line": normalize_text(formal_row.get("report_line")),
                    "model_id": model_id,
                    "stock_id": stock_id,
                    "source_row_index": source_row_index,
                    "watch_warrant_signal": watch_signal,
                    "candidate_warrant_signal": candidate_signal,
                    "official_warrant_signal": official_signal,
                    "formal_warrant_signal": formal_signal,
                    "watch_source_score": watch_source_score,
                    "candidate_source_score": candidate_source_score,
                    "watch_source_rank": watch_source_rank,
                    "candidate_source_rank": candidate_source_rank,
                    "watch_candidate_score_collision": str(
                        watch_candidate_score_collision
                    ),
                    "watch_candidate_rank_collision": str(
                        watch_candidate_rank_collision
                    ),
                    "canonical_warrant_source_type": (
                        "all_candidates_projection"
                        if candidate_row is not None
                        else "negative_projection_no_candidate_row"
                    ),
                    "published_warrant_score_source": score_source,
                    "published_warrant_basis_signal": score_basis_signal,
                    "watch_tdcc_status": watch_context.get("tdcc_status", ""),
                    "candidate_tdcc_status": candidate_context.get("tdcc_status", ""),
                    "published_tdcc_status": published_context.get("tdcc_status", ""),
                    "counterfactual_tdcc_status": counterfactual_context.get(
                        "tdcc_status", ""
                    ),
                    "watch_false_breakout_risk": watch_context.get(
                        "false_breakout_risk", "False"
                    ),
                    "candidate_false_breakout_risk": candidate_context.get(
                        "false_breakout_risk", "False"
                    ),
                    "published_false_breakout_risk": published_context.get(
                        "false_breakout_risk", "False"
                    ),
                    "counterfactual_false_breakout_risk": counterfactual_context.get(
                        "false_breakout_risk", "False"
                    ),
                    "published_tdcc_positive": published_context.get(
                        "tdcc_positive", "False"
                    ),
                    "counterfactual_tdcc_positive": counterfactual_context.get(
                        "tdcc_positive", "False"
                    ),
                    "published_tdcc_distribution": published_context.get(
                        "tdcc_distribution", "False"
                    ),
                    "counterfactual_tdcc_distribution": counterfactual_context.get(
                        "tdcc_distribution", "False"
                    ),
                    "published_score_context": context_json(published_context),
                    "counterfactual_score_context": context_json(counterfactual_context),
                    "collision_fields": "|".join(collision_names),
                    "published_counterfactual_collision_fields": "|".join(
                        published_collision_names
                    ),
                    "warrant_bonus_points": decimal_text(bonus),
                    "published_warrant_bonus_points": decimal_text(published_bonus),
                    "counterfactual_warrant_bonus_points": decimal_text(
                        counterfactual_bonus
                    ),
                    "published_collision_component_effects": effects_json(
                        published_effects
                    ),
                    "counterfactual_collision_component_effects": effects_json(
                        counterfactual_effects
                    ),
                    "published_base_model_score": normalize_text(
                        formal_row.get("base_model_score")
                    ),
                    "counterfactual_base_model_score": replay_decimal(
                        "counterfactual_base",
                        normalize_text(formal_row.get("base_model_score")),
                    ),
                    "base_model_score_delta": replay_decimal("base_delta"),
                    "published_operation_score": normalize_text(
                        formal_row.get("operation_score")
                    ),
                    "published_tdcc_score": normalize_text(formal_row.get("tdcc_score")),
                    "counterfactual_tdcc_score": replay_decimal(
                        "counterfactual_tdcc",
                        normalize_text(formal_row.get("tdcc_score")),
                    ),
                    "tdcc_score_delta": replay_decimal("tdcc_delta"),
                    "published_pattern_score": normalize_text(
                        formal_row.get("pattern_score")
                    ),
                    "published_risk_penalty": normalize_text(
                        formal_row.get("risk_penalty")
                    ),
                    "counterfactual_risk_penalty": replay_decimal(
                        "counterfactual_risk",
                        normalize_text(formal_row.get("risk_penalty")),
                    ),
                    "risk_penalty_delta": replay_decimal("risk_delta"),
                    "published_component_replay_final_rank_score": replay_decimal(
                        "published_replay_final", published_score_text
                    ),
                    "published_component_replay_rounding_gap": replay_decimal(
                        "published_replay_rounding_gap"
                    ),
                    "published_component_replay_match": str(replay_status == "resolved"),
                    "published_final_rank_score": published_score_text,
                    "counterfactual_final_rank_score": replay_decimal(
                        "counterfactual_final", published_score_text
                    ),
                    "score_delta": replay_decimal("final_delta"),
                    "replay_status": replay_status,
                    "replay_error": replay_error,
                    "published_model_rank": normalize_text(formal_row.get("model_rank")),
                    "counterfactual_model_rank": "",
                    "rank_delta": "",
                    "rank_replay_status": "pending",
                    "watch_candidate_collision": str(watch_signal != candidate_signal),
                    "candidate_official_match": str(candidate_signal == official_signal),
                    "formal_candidate_match": str(formal_signal == candidate_signal),
                    "watch_disposition": (
                        "superseded_advisory_snapshot"
                        if (
                            bool(collision_names)
                            or watch_candidate_score_collision
                            or watch_candidate_rank_collision
                        )
                        else "current_canonical_match"
                    ),
                    "formal_row_disposition": "",
                    "impact_scope": "",
                    "evidence_status": (
                        "complete" if replay_status == "resolved" else "incomplete"
                    ),
                    "reason": "",
                }
            )

    result = pd.DataFrame(records, columns=AUDIT_COLUMNS)
    primary_key = [
        "snapshot_report_date",
        "report_line",
        "model_id",
        "stock_id",
        "source_row_index",
    ]
    if result.duplicated(primary_key, keep=False).any():
        duplicate_rows = result.loc[result.duplicated(primary_key, keep=False), primary_key]
        raise RuntimeError(
            "duplicate audit grain rows: "
            + duplicate_rows.to_dict(orient="records").__repr__()
        )

    group_columns = ["snapshot_report_date", "report_line", "model_id"]
    for _, indexes in result.groupby(group_columns, sort=False).groups.items():
        try:
            ordered = counterfactual_rank_order(result, indexes)
        except RuntimeError:
            for index in indexes:
                result.at[index, "rank_replay_status"] = "unresolved_group_component"
            continue
        for counterfactual_rank, index in enumerate(ordered, start=1):
            published_rank = int_value(
                result.at[index, "published_model_rank"], "published_model_rank"
            )
            result.at[index, "counterfactual_model_rank"] = str(counterfactual_rank)
            result.at[index, "rank_delta"] = str(counterfactual_rank - published_rank)
            result.at[index, "rank_replay_status"] = "resolved"

    for index, row in result.iterrows():
        candidate_match = row["candidate_official_match"] == "True"
        formal_match = row["formal_candidate_match"] == "True"
        replay_resolved = row["replay_status"] == "resolved"
        rank_replay_resolved = row["rank_replay_status"] == "resolved"
        score_changed = (
            replay_resolved and decimal_value(row["score_delta"], "score_delta") != 0
        )
        rank_changed = (
            rank_replay_resolved and int_value(row["rank_delta"], "rank_delta") != 0
        )
        collision = bool(row["collision_fields"])
        source_score_collision = row["watch_candidate_score_collision"] == "True"
        source_rank_collision = row["watch_candidate_rank_collision"] == "True"
        unpaired_watch_score_rank = (
            row["candidate_row_present"] == "False"
            and bool(row["watch_source_score"] or row["watch_source_rank"])
        )

        if not replay_resolved or not rank_replay_resolved:
            disposition = "unreplayable"
            impact_scope = "independent_component_or_rank_replay_unresolved"
            reason = row["replay_error"] or "counterfactual group rank could not be replayed"
        elif source_score_collision or source_rank_collision or unpaired_watch_score_rank:
            disposition = "quarantined"
            impact_scope = "legacy_watch_source_score_rank_effect_unresolved"
            reason = (
                "legacy generic watch merge exposed a source score or rank value whose "
                "formal effect is not independently proven"
            )
        elif not candidate_match or not formal_match:
            disposition = "superseded"
            impact_scope = "formal_warrant_lineage_superseded"
            reason = "formal or candidate warrant value differs from the official canonical row"
        elif score_changed or rank_changed:
            disposition = "superseded"
            impact_scope = (
                "formal_score_and_rank_superseded"
                if rank_changed
                else "formal_score_superseded"
            )
            reason = (
                "legacy collision context changed the independently replayed formal score or rank: "
                f"fields={row['collision_fields']}"
            )
        else:
            disposition = "verified_clean"
            if collision:
                impact_scope = "watch_only_no_formal_score_or_rank_effect"
                reason = (
                    "legacy collision values differ, but independently replayed formal score and "
                    f"rank are unchanged: fields={row['collision_fields']}"
                )
            else:
                impact_scope = "none"
                reason = "published and canonical collision contexts, components, and rank agree"
        result.at[index, "formal_row_disposition"] = disposition
        result.at[index, "impact_scope"] = impact_scope
        result.at[index, "reason"] = reason

    return result[AUDIT_COLUMNS].reset_index(drop=True)


def render_markdown(audit: pd.DataFrame) -> str:
    audit_dates = tuple(
        sorted(audit["snapshot_report_date"].astype(str).drop_duplicates())
    )
    date_rows = audit.groupby("snapshot_report_date", sort=False).size().to_dict()
    watch_superseded = audit[
        audit["watch_disposition"].astype(str).eq("superseded_advisory_snapshot")
    ]
    formal_counts = audit["formal_row_disposition"].value_counts().to_dict()
    score_collisions = int(
        audit["watch_candidate_score_collision"].astype(str).eq("True").sum()
    )
    rank_collisions = int(
        audit["watch_candidate_rank_collision"].astype(str).eq("True").sum()
    )
    replay_resolved = int(audit["replay_status"].astype(str).eq("resolved").sum())
    candidate_absent = int(audit["candidate_row_present"].astype(str).eq("False").sum())
    collision_counts = {
        field: int(
            audit["collision_fields"]
            .astype(str)
            .map(lambda value: field in value.split("|") if value else False)
            .sum()
        )
        for field in COLLISION_FIELDS
    }
    lines = [
        "# Volume v2 warrant lineage history audit",
        "",
        f"- Audit version: `{AUDIT_VERSION}`",
        f"- Audited trading dates: `{', '.join(audit_dates)}`",
        f"- Dynamic source coverage: `{len(audit_dates)}/{len(audit_dates)}`",
        f"- Formal volume v2 rows: `{len(audit)}`",
        f"- Formal verified clean: `{formal_counts.get('verified_clean', 0)}`",
        f"- Formal superseded: `{formal_counts.get('superseded', 0)}`",
        f"- Formal quarantined: `{formal_counts.get('quarantined', 0)}`",
        f"- Formal unreplayable: `{formal_counts.get('unreplayable', 0)}`",
        f"- Superseded advisory watch rows: `{len(watch_superseded)}`",
        f"- Independent component replay resolved: `{replay_resolved}/{len(audit)}`",
        f"- Candidate-absent canonical score contexts: `{candidate_absent}` stored as `{{}}`",
        f"- Warrant collision rows: `{collision_counts['warrant_flow_signal']}`",
        f"- TDCC-status collision rows: `{collision_counts['tdcc_status']}`",
        f"- False-breakout collision rows: `{collision_counts['false_breakout_risk']}`",
        f"- Watch/candidate source score collisions: `{score_collisions}`",
        f"- Watch/candidate source rank collisions: `{rank_collisions}`",
        "- Historical daily snapshots were read only and were not rewritten.",
        "",
        "## Daily coverage",
        "",
        "| Report date | Formal v2 rows | Dispatcher warrant score source |",
        "|---|---:|---|",
    ]
    for report_date in audit_dates:
        modes = sorted(
            audit.loc[
                audit["snapshot_report_date"].astype(str).eq(report_date),
                "dispatcher_warrant_source_mode",
            ].astype(str).unique()
        )
        lines.append(
            f"| {report_date} | {date_rows.get(report_date, 0)} | {', '.join(modes)} |"
        )

    lines.extend(
        [
            "",
            "## Watch collision disposition",
            "",
        ]
    )
    if watch_superseded.empty:
        lines.append("No watch-to-canonical collisions were found.")
    else:
        lines.extend(
            [
                "| Report date | Stock | Model | Collision fields | Published → canonical values | Base | TDCC | Risk | Final | Rank | Disposition |",
                "|---|---|---|---|---|---:|---:|---:|---:|---:|---|",
            ]
        )
        for _, row in watch_superseded.iterrows():
            lines.append(
                "| {snapshot_report_date} | {stock_id} | {model_id} | "
                "{collision_fields} | warrant={watch_warrant_signal}/{published_warrant_basis_signal}→{candidate_warrant_signal}; "
                "tdcc={watch_tdcc_status}/{published_tdcc_status}→{counterfactual_tdcc_status}; "
                "false_breakout={watch_false_breakout_risk}/{published_false_breakout_risk}→{counterfactual_false_breakout_risk} | "
                "{published_base_model_score}→{counterfactual_base_model_score} | "
                "{published_tdcc_score}→{counterfactual_tdcc_score} | "
                "{published_risk_penalty}→{counterfactual_risk_penalty} | "
                "{published_final_rank_score}→{counterfactual_final_rank_score} | "
                "{published_model_rank}→{counterfactual_model_rank} | "
                "{formal_row_disposition} |".format(**row.to_dict())
            )

    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            "The dynamic historical/current coverage replays the legacy candidate-plus-watch collision context "
            "and the canonical candidate-only collision context independently for warrant, TDCC "
            "status, and false-breakout risk. Component deltas are applied to base_model_score, "
            "tdcc_score, and risk_penalty before final_rank_score is clamped, then rank is rebuilt "
            "by score descending, stock_id, and source_row_index. Candidate-absent canonical score "
            "contexts remain empty. Historical snapshots are never rewritten; superseded, "
            "quarantined, or unreplayable rows cannot be used as current formal evidence.",
            "",
        ]
    )
    return "\n".join(lines)


def write_bytes_identically(payload: bytes, paths: Iterable[Path]) -> None:
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


def write_audit_artifacts(
    audit: pd.DataFrame,
    output_csv: Path = OUTPUT_CSV,
    output_md: Path = OUTPUT_MD,
    docs_csv: Path = DOCS_CSV,
    docs_md: Path = DOCS_MD,
) -> None:
    csv_payload = audit.to_csv(index=False, lineterminator="\n").encode("utf-8")
    markdown_payload = render_markdown(audit).encode("utf-8")
    write_bytes_identically(csv_payload, (output_csv, docs_csv))
    write_bytes_identically(markdown_payload, (output_md, docs_md))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the deterministic volume v2 warrant lineage history audit."
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    audit = build_audit_dataframe(root)
    write_audit_artifacts(
        audit,
        root / OUTPUT_CSV.relative_to(ROOT),
        root / OUTPUT_MD.relative_to(ROOT),
        root / DOCS_CSV.relative_to(ROOT),
        root / DOCS_MD.relative_to(ROOT),
    )
    print(
        "volume v2 warrant lineage history audit built: "
        f"dates={audit['snapshot_report_date'].nunique()} rows={len(audit)} "
        "formal_verified_clean="
        f"{int(audit['formal_row_disposition'].eq('verified_clean').sum())} "
        "watch_superseded="
        f"{int(audit['watch_disposition'].eq('superseded_advisory_snapshot').sum())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
