from __future__ import annotations

import csv
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_text, write_csv  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "daily_model_background_data_registry.csv"
PRODUCTION_INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
LIFECYCLE_INVENTORY = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
ARTIFACT_LINEAGE = ROOT / "config" / "report_artifact_lineage.csv"

OUTPUT_CSV = RESEARCH_LATEST_DIR / "daily_model_background_data_cleanup_audit_latest.csv"
OUTPUT_MD = RESEARCH_LATEST_DIR / "daily_model_background_data_cleanup_audit_latest.md"
DOCS_OUTPUT_CSV = DOCS_LATEST_DIR / OUTPUT_CSV.name
DOCS_OUTPUT_MD = DOCS_LATEST_DIR / OUTPUT_MD.name

SCAN_DIRS = [
    ".github/workflows",
    "scripts",
    "tests",
    "config",
    "docs",
    "rules",
]

TEXT_SUFFIXES = {".csv", ".md", ".py", ".txt", ".yml", ".yaml", ".json", ".toml", ".ps1", ".sh"}
MAX_SCAN_BYTES = 2_500_000
MAX_REF_DISPLAY = 8


def rel_to_root(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def split_list(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return [{key: str(value or "").strip() for key, value in row.items()} for row in reader]


def path_prefix(pattern: str) -> str:
    normalized = pattern.replace("\\", "/").strip()
    if not normalized:
        return ""
    for marker in ["*", "?", "["]:
        if marker in normalized:
            normalized = normalized.split(marker, 1)[0]
    return normalized.rstrip("/")


def basename_token(pattern: str) -> str:
    prefix = path_prefix(pattern)
    if not prefix:
        return ""
    name = Path(prefix).name
    if name in {"", ".", ".."}:
        name = Path(prefix).parent.name
    return name


def artifact_matches(pattern: str) -> list[str]:
    normalized = pattern.replace("\\", "/").strip()
    if not normalized:
        return []
    if any(marker in normalized for marker in ["*", "?", "["]):
        return sorted(rel_to_root(path) for path in ROOT.glob(normalized))
    path = ROOT / normalized
    return [rel_to_root(path)] if path.exists() else []


def path_exists(path_text: str) -> bool:
    text = path_text.replace("\\", "/").strip()
    if not text or text == "not_implemented":
        return False
    return (ROOT / text).exists()


def compact_refs(paths: Iterable[str]) -> str:
    unique = sorted({path for path in paths if path})
    shown = unique[:MAX_REF_DISPLAY]
    suffix = f";...(+{len(unique) - MAX_REF_DISPLAY})" if len(unique) > MAX_REF_DISPLAY else ""
    return ";".join(shown) + suffix


def tokens_for_row(row: dict[str, str]) -> list[str]:
    tokens: set[str] = set()
    for field in ["data_family_id", "producer", "artifact_path", "validator"]:
        value = row.get(field, "")
        if value and value != "not_implemented":
            tokens.add(value.replace("\\", "/"))
            prefix = path_prefix(value)
            if prefix:
                tokens.add(prefix)
            base = basename_token(value)
            if base and len(base) >= 4:
                tokens.add(base)

    for field in ["source_artifacts"]:
        for value in split_list(row.get(field, "")):
            if value and value != "not_implemented":
                tokens.add(value.replace("\\", "/"))
                prefix = path_prefix(value)
                if prefix:
                    tokens.add(prefix)
                base = basename_token(value)
                if base and len(base) >= 4:
                    tokens.add(base)

    # Avoid noisy one-word tokens. Path-like tokens and data_family_id are enough
    # to identify real dependencies without matching generic words such as data.
    return sorted(token for token in tokens if len(token) >= 4 and token not in {"*.csv", "*.md", "*.py"})


def iter_scan_files() -> Iterable[Path]:
    for directory in SCAN_DIRS:
        base = ROOT / directory
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if path.stat().st_size > MAX_SCAN_BYTES:
                continue
            yield path


def scan_repo_references(tokens: list[str]) -> dict[str, list[str]]:
    refs = {
        "workflow": [],
        "inventory": [],
        "lineage": [],
        "docs": [],
        "scripts_tests": [],
        "config": [],
    }
    if not tokens:
        return refs

    inventory_paths = {rel_to_root(PRODUCTION_INVENTORY), rel_to_root(LIFECYCLE_INVENTORY)}
    lineage_path = rel_to_root(ARTIFACT_LINEAGE)
    registry_path = rel_to_root(REGISTRY)

    for path in iter_scan_files():
        rel = rel_to_root(path)
        if rel == registry_path:
            continue
        try:
            text = path.read_text(encoding="utf-8-sig", errors="ignore")
        except OSError:
            continue
        if not any(token in text for token in tokens):
            continue
        if rel.startswith(".github/workflows/"):
            refs["workflow"].append(rel)
        elif rel in inventory_paths:
            refs["inventory"].append(rel)
        elif rel == lineage_path:
            refs["lineage"].append(rel)
        elif rel.startswith("docs/") or rel.startswith("rules/"):
            refs["docs"].append(rel)
        elif rel.startswith("scripts/") or rel.startswith("tests/"):
            refs["scripts_tests"].append(rel)
        elif rel.startswith("config/"):
            refs["config"].append(rel)
    return refs


def deletion_decision(
    row: dict[str, str],
    dependency_count: int,
) -> tuple[str, str, str, bool]:
    data_family_id = row["data_family_id"]
    scope = row["scope"]
    cleanup_status = row["cleanup_status"]
    retention_policy = row["retention_policy"]

    if cleanup_status == "blocked_missing_source_or_validator":
        return (
            "not_applicable_missing_family",
            f"{data_family_id} has no deletable artifact; source or validator is missing.",
            "build dated source and validator before any formal model gate",
            False,
        )

    if cleanup_status != "deprecated_candidate":
        if scope in {"shared_replay_evidence", "shared_replay_source"}:
            decision = "retain_historical_replay_evidence"
            next_step = "do not delete; preserve replay and parity audit trail"
        elif scope == "shared_objective":
            decision = "retain_shared_objective_source"
            next_step = "reuse only with point-in-time rules; do not convert to model gate by itself"
        elif scope == "latest_only_context":
            decision = "retain_latest_only_context"
            next_step = "do not use as historical point-in-time label"
        elif scope == "model_specific":
            decision = "retain_model_specific_semantics"
            next_step = "keep with owning model contract; do not reuse across unrelated models"
        elif scope == "model_research_output":
            decision = "retain_model_research_evidence"
            next_step = "keep until superseded by explicit approved operation or cleanup PR"
        else:
            decision = "retain_registered_active_family"
            next_step = "no cleanup action"
        return (
            decision,
            f"registry cleanup_status={cleanup_status}; retention_policy={retention_policy}.",
            next_step,
            False,
        )

    if dependency_count > 0:
        return (
            "blocked_deprecated_candidate_has_dependencies",
            "registry marks deprecated_candidate but active references still exist.",
            "remove or migrate dependencies in a reviewed cleanup PR before deleting artifacts",
            False,
        )

    return (
        "eligible_for_cleanup_pr",
        "registry marks deprecated_candidate and audit found no active references.",
        "open explicit cleanup PR with validator evidence before deleting artifacts",
        True,
    )


def build_audit_rows() -> list[dict[str, str]]:
    generated_at = now_text()
    rows = read_csv_rows(REGISTRY)
    audit_rows: list[dict[str, str]] = []
    for row in rows:
        tokens = tokens_for_row(row)
        refs = scan_repo_references(tokens)
        artifact_paths = artifact_matches(row.get("artifact_path", ""))
        dependency_count = (
            len(set(refs["workflow"]))
            + len(set(refs["inventory"]))
            + len(set(refs["lineage"]))
            + len(set(refs["scripts_tests"]))
            + len(set(refs["config"]))
        )
        decision, reason, next_step, deletion_allowed = deletion_decision(row, dependency_count)
        audit_rows.append(
            {
                "generated_at": generated_at,
                "data_family_id": row["data_family_id"],
                "scope": row["scope"],
                "owner_lane": row["owner_lane"],
                "cleanup_status": row["cleanup_status"],
                "retention_policy": row["retention_policy"],
                "artifact_path": row["artifact_path"],
                "artifact_match_count": str(len(artifact_paths)),
                "producer": row["producer"],
                "producer_exists": str(path_exists(row["producer"])),
                "validator": row["validator"],
                "validator_exists": str(path_exists(row["validator"])),
                "workflow_reference_count": str(len(set(refs["workflow"]))),
                "inventory_reference_count": str(len(set(refs["inventory"]))),
                "lineage_reference_count": str(len(set(refs["lineage"]))),
                "script_test_reference_count": str(len(set(refs["scripts_tests"]))),
                "config_reference_count": str(len(set(refs["config"]))),
                "docs_reference_count": str(len(set(refs["docs"]))),
                "workflow_references": compact_refs(refs["workflow"]),
                "inventory_references": compact_refs(refs["inventory"]),
                "lineage_references": compact_refs(refs["lineage"]),
                "script_test_references": compact_refs(refs["scripts_tests"]),
                "config_references": compact_refs(refs["config"]),
                "docs_references": compact_refs(refs["docs"]),
                "artifact_examples": compact_refs(artifact_paths),
                "deletion_decision": decision,
                "deletion_allowed": str(deletion_allowed),
                "decision_reason": reason,
                "required_next_step": next_step,
            }
        )
    return audit_rows


def write_markdown(df: pd.DataFrame) -> str:
    summary = df["deletion_decision"].value_counts().sort_index().reset_index()
    summary.columns = ["deletion_decision", "rows"]
    deletion_allowed = int(df["deletion_allowed"].astype(str).str.lower().eq("true").sum())
    deprecated_candidates = int(df["cleanup_status"].astype(str).eq("deprecated_candidate").sum())
    lines = [
        "# Daily Model Background Data Cleanup Audit",
        "",
        f"- generated_at: `{df['generated_at'].iloc[0] if not df.empty else now_text()}`",
        f"- registry: `{rel_to_root(REGISTRY)}`",
        f"- rows: `{len(df)}`",
        f"- deletion_allowed_rows: `{deletion_allowed}`",
        f"- deprecated_candidate_rows: `{deprecated_candidates}`",
        "",
        "This audit is a deletion gate. It does not delete artifacts. A data family",
        "can move to a cleanup PR only when the registry marks it",
        "`deprecated_candidate` and dependency checks do not find active workflow,",
        "inventory, lineage, validator, replay, parity, or promotion references.",
        "",
        "## Decision Summary",
        "",
        markdown_table(summary, ["deletion_decision", "rows"]),
        "",
        "## Data Family Decisions",
        "",
        markdown_table(
            df,
            [
                "data_family_id",
                "scope",
                "cleanup_status",
                "deletion_decision",
                "deletion_allowed",
                "required_next_step",
            ],
        ),
        "",
        "## Dependency Counts",
        "",
        markdown_table(
            df,
            [
                "data_family_id",
                "artifact_match_count",
                "workflow_reference_count",
                "inventory_reference_count",
                "lineage_reference_count",
                "script_test_reference_count",
                "docs_reference_count",
            ],
        ),
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = build_audit_rows()
    df = pd.DataFrame(rows)
    write_csv(df, OUTPUT_CSV)
    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_MD.write_text(write_markdown(df), encoding="utf-8", newline="\n")

    write_csv(df, DOCS_OUTPUT_CSV)
    DOCS_OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_OUTPUT_MD.write_text(OUTPUT_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")

    deletion_allowed = int(df["deletion_allowed"].astype(str).str.lower().eq("true").sum()) if not df.empty else 0
    print(f"built_background_cleanup_audit_rows={len(df)}")
    print(f"deletion_allowed_rows={deletion_allowed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
