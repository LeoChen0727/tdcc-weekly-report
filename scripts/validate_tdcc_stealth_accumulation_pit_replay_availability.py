from __future__ import annotations

import argparse
import csv
import fnmatch
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "tdcc_stealth_accumulation"
MODEL_NAME_ZH = "TDCC潛伏吸籌模型"
ARTIFACT_VERSION = "tdcc_stealth_accumulation_pit_replay_availability_audit_v1"
ARTIFACT_NAME = f"{ARTIFACT_VERSION}.csv"
DEFAULT_ARTIFACT = ROOT / "output" / "research" / MODEL_ID / ARTIFACT_NAME
AVAILABILITY_STATE = (
    "partial_inputs_available_selector_replay_not_formally_available"
)
BASE_BLOCKERS = (
    "phase_classifier_unresolved",
    "full_historical_selector_replay_unavailable",
    "model_semantic_sha_unavailable_from_snapshot_contract",
    "formal_operation_decision_required",
    "mutable_price_source_unpinned",
)
ZERO_SAMPLE_BLOCKER = "no_published_tdcc_stealth_signal_rows"

AUDIT_FIELDS = [
    "artifact_version",
    "source_commit_sha",
    "model_id",
    "model_name_zh",
    "source_family",
    "source_role",
    "source_path",
    "source_hash_basis",
    "source_sha256",
    "source_file_count",
    "source_row_count",
    "source_unique_date_count",
    "source_date_min",
    "source_date_max",
    "source_unique_stock_count",
    "source_target_model_row_count",
    "source_target_unique_identity_count",
    "source_target_duplicate_row_count",
    "source_noncanonical_row_count",
    "source_transport_normalized_hash_count",
    "selector_required_input_count",
    "selector_present_input_count",
    "selector_missing_input_count",
    "selector_missing_inputs",
    "declared_semantic_item_count",
    "declared_semantic_sha256",
    "published_target_row_count",
    "source_status",
    "coverage_status",
    "coverage_detail",
    "pit_status",
    "availability_state",
    "selector_replay_allowed",
    "performance_metrics_allowed",
    "formal_use",
    "trade_eligible",
    "promotion_evidence_allowed",
    "promotion_status",
    "blockers",
]

SOURCE_FAMILY_ORDER = (
    "published_snapshot_manifest",
    "published_all_candidates_snapshots",
    "published_model_signal_snapshots",
    "legacy_candidate_signal_log",
    "tdcc_weekly_holder_snapshots",
    "tdcc_date_versioned_raw_snapshots",
    "tdcc_latest_dataset_manifest",
    "tdcc_dataset_manifests",
    "tdcc_rebuilt_signal_snapshot",
    "tdcc_per_stock_raw_history",
    "tdcc_per_stock_normalized_history",
    "daily_price_date_snapshots",
    "stock_price_history",
    "stock_model_contract_registry",
    "model_semantic_ownership_registry",
    "shared_semantic_registry",
)

MANIFEST_PATH = (
    "output/history/daily_model_snapshots/"
    "daily_published_model_snapshot_manifest.csv"
)
LEGACY_SIGNAL_LOG_PATH = (
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
)
TDCC_SIGNAL_SNAPSHOT_PATH = "output/history/tdcc_signals/tdcc_signal_snapshot.csv"
TDCC_LATEST_DATASET_MANIFEST_PATH = "output/latest/tdcc_dataset_manifest_latest.json"
SEMANTIC_OWNERSHIP_PATH = "config/daily_model_semantic_ownership.csv"
SHARED_SEMANTIC_PATH = "config/daily_model_shared_semantic_registry.csv"
STOCK_MODEL_CONTRACT_PATH = "config/stock_model_contract_registry.csv"
MANIFEST_ARTIFACT_ID = "model_signals_for_report"
ALL_CANDIDATES_ARTIFACT_ID = "all_candidates_source_rows"
SNAPSHOT_SELECTOR_COVERAGE_CONTRACT = {
    ALL_CANDIDATES_ARTIFACT_ID: (50, 26, 24),
    MANIFEST_ARTIFACT_ID: (50, 6, 44),
}
MANIFEST_REQUIRED_FIELDS = {
    "snapshot_report_date",
    "snapshot_revision",
    "artifact_id",
    "snapshot_path",
    "snapshot_sha256",
    "row_count",
    "column_count",
}

FAMILY_CONTRACTS = {
    "published_snapshot_manifest": (
        "published_revision_inventory",
        MANIFEST_PATH,
        "revision_inventory_only",
        "partial_membership_pit_only",
    ),
    "published_all_candidates_snapshots": (
        "historical_selector_input_coverage_probe",
        "output/history/daily_model_snapshots/all_candidates_*.csv",
        "selector_input_surface_has_26_of_50_required_columns_not_full_replay",
        "partial_selector_input_coverage_only",
    ),
    "published_model_signal_snapshots": (
        "as_published_membership_source",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv",
        "exact_as_published_membership_only_not_selector_replay",
        "published_membership_pit_only",
    ),
    "legacy_candidate_signal_log": (
        "legacy_discovery_lead",
        LEGACY_SIGNAL_LOG_PATH,
        "rewritten_cumulative_log_not_pit",
        "not_formal_selector_pit",
    ),
    "tdcc_weekly_holder_snapshots": (
        "objective_tdcc_weekly_snapshots",
        "output/history/tdcc/tdcc_holder_ratio_*.csv",
        "weekly_objective_snapshots_coverage_varies_by_date",
        "partial_objective_source_history",
    ),
    "tdcc_date_versioned_raw_snapshots": (
        "objective_tdcc_raw_snapshots",
        "output/history/tdcc/tdcc_latest_ratio_raw_*.csv",
        "date_versioned_raw_available_only_for_partial_period",
        "partial_objective_source_history",
    ),
    "tdcc_latest_dataset_manifest": (
        "current_tdcc_dataset_lineage",
        TDCC_LATEST_DATASET_MANIFEST_PATH,
        "current_manifest_sources_verified_but_not_event_time_full_history",
        "current_dataset_binding_only",
    ),
    "tdcc_dataset_manifests": (
        "tdcc_dataset_lineage",
        "output/history/tdcc/tdcc_dataset_manifest_*.json",
        "versioned_dataset_manifests_cover_only_recent_dates",
        "partial_dataset_lineage",
    ),
    "tdcc_rebuilt_signal_snapshot": (
        "derived_tdcc_signal_history",
        TDCC_SIGNAL_SNAPSHOT_PATH,
        "full_history_rebuild_bound_to_current_dataset_not_event_time",
        "not_event_time_immutable",
    ),
    "tdcc_per_stock_raw_history": (
        "derived_tdcc_per_stock_history",
        "data/tdcc_stock_history_raw/*.csv",
        "per_stock_history_not_event_time_manifest_bound",
        "not_event_time_immutable",
    ),
    "tdcc_per_stock_normalized_history": (
        "derived_tdcc_normalized_history",
        "data/tdcc_stock_history/*.csv",
        "available_current_aggregate_with_stale_rows_not_pit",
        "not_event_time_immutable",
    ),
    "daily_price_date_snapshots": (
        "objective_daily_price_history",
        "data/daily_price/[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].csv",
        "date_versioned_price_files_adjustment_basis_unverified",
        "price_lineage_not_formally_pinned",
    ),
    "stock_price_history": (
        "mutable_aggregate_price_history",
        "data/stock_price_history/*.csv",
        "mutable_aggregate_price_files_unpinned",
        "price_lineage_not_formally_pinned",
    ),
    "stock_model_contract_registry": (
        "selector_required_input_contract",
        STOCK_MODEL_CONTRACT_PATH,
        "current_50_input_contract_not_bound_to_each_historical_snapshot",
        "historical_semantic_binding_unavailable",
    ),
    "model_semantic_ownership_registry": (
        "current_model_semantic_inventory",
        SEMANTIC_OWNERSHIP_PATH,
        "current_semantic_registry_not_bound_to_historical_snapshots",
        "historical_semantic_binding_unavailable",
    ),
    "shared_semantic_registry": (
        "current_shared_semantic_inventory",
        SHARED_SEMANTIC_PATH,
        "current_shared_semantics_not_bound_to_historical_snapshots",
        "historical_semantic_binding_unavailable",
    ),
}


def _text(value: Any) -> str:
    return "" if value is None else str(value).replace("\ufeff", "").strip()


def _normal_relative_path(value: str | Path) -> str:
    text = str(value).replace("\\", "/").strip()
    while text.startswith("./"):
        text = text[2:]
    candidate = Path(text)
    if not text or candidate.is_absolute() or any(
        part in {"", ".", ".."} for part in text.split("/")
    ):
        raise RuntimeError(f"unsafe repository-relative source path: {value!r}")
    return text


def _git_blob_oid(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()  # noqa: S324 - Git identity.


class SourceAccess:
    def __init__(self, root: Path, source_ref: str = "HEAD") -> None:
        self.root = root.resolve()
        self.source_ref = source_ref
        self._git_entries: dict[str, str] | None = None
        self._resolved_commit_sha: str | None = None

    def resolved_commit_sha(self) -> str:
        if self._resolved_commit_sha is not None:
            return self._resolved_commit_sha
        if not self.source_ref:
            self._resolved_commit_sha = ""
            return self._resolved_commit_sha
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--verify", f"{self.source_ref}^{{commit}}"],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
            value = result.stdout.strip().lower()
        except (OSError, subprocess.CalledProcessError) as exc:
            raise RuntimeError(
                f"failed to resolve source_ref: {self.source_ref}"
            ) from exc
        if re.fullmatch(r"[0-9a-f]{40}", value) is None:
            raise RuntimeError(f"source_ref did not resolve to a commit: {self.source_ref}")
        self._resolved_commit_sha = value
        return value

    def _load_git_entries(self) -> dict[str, str]:
        if self._git_entries is not None:
            return self._git_entries
        commit_sha = self.resolved_commit_sha()
        if not commit_sha:
            self._git_entries = {}
            return self._git_entries
        try:
            result = subprocess.run(
                ["git", "ls-tree", "-r", "--full-tree", commit_sha],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
            )
        except (OSError, subprocess.CalledProcessError) as exc:
            raise RuntimeError(
                f"failed to inventory source commit tree: {commit_sha}"
            ) from exc
        entries: dict[str, str] = {}
        for line in result.stdout.splitlines():
            if "\t" not in line:
                continue
            metadata, path = line.split("\t", 1)
            parts = metadata.split()
            if len(parts) == 3 and parts[1] == "blob":
                entries[path.replace("\\", "/")] = parts[2]
        self._git_entries = entries
        return entries

    def list_paths(self, prefix: str, pattern: str = "*") -> list[str]:
        normalized_prefix = _normal_relative_path(prefix).rstrip("/")
        paths: set[str] = set()
        if self.resolved_commit_sha():
            prefix_with_slash = f"{normalized_prefix}/"
            for path in self._load_git_entries():
                if path == normalized_prefix or path.startswith(prefix_with_slash):
                    paths.add(path)
        else:
            physical_root = self.root / Path(normalized_prefix)
            if physical_root.is_file():
                paths.add(normalized_prefix)
            elif physical_root.is_dir():
                for path in physical_root.rglob("*"):
                    if path.is_file():
                        paths.add(path.relative_to(self.root).as_posix())
        return sorted(
            path for path in paths if fnmatch.fnmatchcase(Path(path).name, pattern)
        )

    def exists(self, relative_path: str) -> bool:
        path = _normal_relative_path(relative_path)
        if self.resolved_commit_sha():
            return path in self._load_git_entries()
        return (self.root / Path(path)).is_file()

    def read_bytes(self, relative_path: str) -> bytes:
        path = _normal_relative_path(relative_path)
        physical = self.root / Path(path)
        commit_sha = self.resolved_commit_sha()
        if not commit_sha and physical.is_file():
            return physical.read_bytes()
        if path not in self._load_git_entries():
            raise RuntimeError(f"missing source file: {path}")
        try:
            return subprocess.run(
                ["git", "show", f"{commit_sha}:{path}"],
                cwd=self.root,
                check=True,
                capture_output=True,
            ).stdout
        except (OSError, subprocess.CalledProcessError) as exc:
            raise RuntimeError(f"failed to read tracked source file: {path}") from exc

    def read_many(self, relative_paths: Iterable[str]) -> dict[str, bytes]:
        normalized = [_normal_relative_path(path) for path in relative_paths]
        payloads: dict[str, bytes] = {}
        tracked: list[str] = []
        entries = self._load_git_entries()
        for path in normalized:
            physical = self.root / Path(path)
            if not self.resolved_commit_sha() and physical.is_file():
                payloads[path] = physical.read_bytes()
            elif path in entries:
                tracked.append(path)
            else:
                raise RuntimeError(f"missing source file: {path}")
        if tracked:
            commit_sha = self.resolved_commit_sha()
            request = "".join(f"{commit_sha}:{path}\n" for path in tracked).encode(
                "utf-8"
            )
            try:
                result = subprocess.run(
                    ["git", "cat-file", "--batch"],
                    cwd=self.root,
                    input=request,
                    check=True,
                    capture_output=True,
                )
            except (OSError, subprocess.CalledProcessError) as exc:
                raise RuntimeError("failed to batch-read tracked source files") from exc
            stream = io.BytesIO(result.stdout)
            for path in tracked:
                header = stream.readline().decode("utf-8", errors="replace").strip()
                parts = header.split()
                if len(parts) != 3 or parts[1] != "blob":
                    raise RuntimeError(f"failed to batch-read tracked source file: {path}")
                size = int(parts[2])
                payloads[path] = stream.read(size)
                if stream.read(1) != b"\n":
                    raise RuntimeError(f"invalid git cat-file framing for: {path}")
        return {path: payloads[path] for path in normalized}

    def blob_oid(self, relative_path: str) -> str:
        path = _normal_relative_path(relative_path)
        physical = self.root / Path(path)
        if not self.resolved_commit_sha() and physical.is_file():
            return _git_blob_oid(physical.read_bytes())
        oid = self._load_git_entries().get(path, "")
        if not oid:
            raise RuntimeError(f"missing source file: {path}")
        return oid


def _read_csv_payload(payload: bytes, path: str) -> tuple[list[str], list[dict[str, str]]]:
    try:
        reader = csv.DictReader(
            io.StringIO(payload.decode("utf-8-sig"), newline=""), strict=True
        )
        fields = [_text(field) for field in (reader.fieldnames or [])]
        if not fields or any(not field for field in fields) or len(fields) != len(set(fields)):
            raise RuntimeError(f"source CSV has invalid or duplicate header: {path}")
        rows: list[dict[str, str]] = []
        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise RuntimeError(
                    f"source CSV row width mismatch at {path}:{row_number}"
                )
            rows.append({_text(key): _text(value) for key, value in row.items()})
    except (UnicodeDecodeError, csv.Error) as exc:
        raise RuntimeError(f"failed to parse source CSV {path}: {exc}") from exc
    return fields, rows


def _read_csv(access: SourceAccess, path: str) -> tuple[list[str], list[dict[str, str]]]:
    return _read_csv_payload(access.read_bytes(path), path)


def _raw_sha256(access: SourceAccess, path: str) -> str:
    return hashlib.sha256(access.read_bytes(path)).hexdigest()


def _family_sha256(access: SourceAccess, paths: Iterable[str]) -> str:
    digest = hashlib.sha256()
    ordered = sorted(paths)
    for offset in range(0, len(ordered), 64):
        payloads = access.read_many(ordered[offset : offset + 64])
        for path in ordered[offset : offset + 64]:
            digest.update(path.encode("utf-8"))
            digest.update(b"\t")
            digest.update(hashlib.sha256(payloads[path]).hexdigest().encode("ascii"))
            digest.update(b"\n")
    return digest.hexdigest()


def _hash_contract(access: SourceAccess, paths: list[str]) -> tuple[str, str]:
    if not paths:
        return "", ""
    if len(paths) == 1:
        return "raw_file_sha256", _raw_sha256(access, paths[0])
    return (
        "sorted_path_tab_raw_file_sha256_lf_aggregate_sha256",
        _family_sha256(access, paths),
    )


def _date_from_filename(path: str, prefix: str) -> str:
    match = re.fullmatch(rf"{re.escape(prefix)}([0-9]{{8}})\.[^.]+", Path(path).name)
    return match.group(1) if match else ""


def _row_dates(rows: list[dict[str, str]], candidates: tuple[str, ...]) -> set[str]:
    for field in candidates:
        if rows and field in rows[0]:
            return {
                value
                for row in rows
                if re.fullmatch(r"[0-9]{8}", value := _text(row.get(field)))
            }
    return set()


def _row_stocks(rows: list[dict[str, str]]) -> set[str]:
    for field in ("stock_id", "code", "ticker"):
        if rows and field in rows[0]:
            return {_text(row.get(field)) for row in rows if _text(row.get(field))}
    return set()


def _hash_candidates(payload: bytes) -> set[str]:
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {hashlib.sha256(candidate).hexdigest() for candidate in (payload, lf, crlf)}


def _utf8_text_lf_normalized_sha256(payload: bytes) -> str:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RuntimeError("TDCC manifest-bound source is not UTF-8 text") from exc
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _revision_number(value: str) -> int:
    match = re.fullmatch(r"r([1-9][0-9]*)", _text(value))
    if match is None:
        raise RuntimeError(f"invalid snapshot_revision: {value!r}")
    return int(match.group(1))


def _selector_required_inputs(access: SourceAccess) -> set[str]:
    if not access.exists(STOCK_MODEL_CONTRACT_PATH):
        raise RuntimeError("missing stock model contract registry")
    fields, rows = _read_csv(access, STOCK_MODEL_CONTRACT_PATH)
    if not {"model_id", "input_columns"}.issubset(fields):
        raise RuntimeError("stock model contract registry missing model_id/input_columns")
    target = [row for row in rows if row.get("model_id") == MODEL_ID]
    if len(target) != 1:
        raise RuntimeError(
            f"stock model contract registry must contain exactly one {MODEL_ID} row"
        )
    inputs = {
        value.strip()
        for value in target[0]["input_columns"].split(";")
        if value.strip()
    }
    if len(inputs) != 50:
        raise RuntimeError(
            f"{MODEL_ID} selector input contract must contain exactly 50 columns"
        )
    return inputs


def _published_metrics(
    access: SourceAccess, selector_inputs: set[str]
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    if not access.exists(MANIFEST_PATH):
        empty = {
            "paths": [], "row_count": 0, "dates": set(), "stocks": set(),
            "target_count": 0,
        }
        return empty, dict(empty), dict(empty)
    fields, rows = _read_csv(access, MANIFEST_PATH)
    missing = sorted(MANIFEST_REQUIRED_FIELDS - set(fields))
    if missing:
        raise RuntimeError(f"published snapshot manifest missing fields: {missing}")
    scoped_by_artifact = {
        artifact_id: [row for row in rows if row.get("artifact_id") == artifact_id]
        for artifact_id in (MANIFEST_ARTIFACT_ID, ALL_CANDIDATES_ARTIFACT_ID)
    }
    if not all(scoped_by_artifact.values()):
        raise RuntimeError(
            "published snapshot manifest must contain model_signals_for_report "
            "and all_candidates_source_rows"
        )

    def select(artifact_id: str) -> dict[str, Any]:
        grouped: dict[str, list[dict[str, str]]] = {}
        for row in scoped_by_artifact[artifact_id]:
            report_date = _text(row.get("snapshot_report_date"))
            if re.fullmatch(r"[0-9]{8}", report_date) is None:
                raise RuntimeError(f"invalid snapshot_report_date: {report_date!r}")
            grouped.setdefault(report_date, []).append(row)
        selected_paths: list[str] = []
        selected_rows: list[dict[str, str]] = []
        selected_field_sets: list[set[str]] = []
        transport_normalized_hash_count = 0
        for report_date in sorted(grouped):
            revisions = grouped[report_date]
            numbers = [_revision_number(row["snapshot_revision"]) for row in revisions]
            if len(numbers) != len(set(numbers)):
                raise RuntimeError(f"duplicate snapshot revision for {report_date}")
            selected = max(
                revisions, key=lambda row: _revision_number(row["snapshot_revision"])
            )
            path = _normal_relative_path(selected["snapshot_path"])
            payload = access.read_bytes(path)
            expected_sha = _text(selected["snapshot_sha256"]).lower()
            if re.fullmatch(r"[0-9a-f]{64}", expected_sha) is None:
                raise RuntimeError(f"invalid snapshot SHA-256: {path}")
            if expected_sha not in _hash_candidates(payload):
                raise RuntimeError(f"snapshot SHA-256 mismatch: {path}")
            if hashlib.sha256(payload).hexdigest() != expected_sha:
                transport_normalized_hash_count += 1
            snapshot_fields, snapshot_rows = _read_csv(access, path)
            required_fields = {"signal_date", "stock_id"}
            if artifact_id == MANIFEST_ARTIFACT_ID:
                required_fields.add("model_id")
            missing_fields = sorted(required_fields - set(snapshot_fields))
            if missing_fields:
                raise RuntimeError(
                    f"{artifact_id} snapshot missing required columns "
                    f"at {path}: {missing_fields}"
                )
            for row_number, snapshot_row in enumerate(snapshot_rows, start=2):
                signal_date = _text(snapshot_row.get("signal_date"))
                stock_id = _text(snapshot_row.get("stock_id"))
                if re.fullmatch(r"[0-9]{8}", signal_date) is None:
                    raise RuntimeError(
                        f"{artifact_id} snapshot identity signal_date is invalid "
                        f"at {path}:{row_number}: {signal_date!r}"
                    )
                if signal_date != report_date:
                    raise RuntimeError(
                        f"{artifact_id} snapshot identity signal_date does not "
                        f"match manifest report date at {path}:{row_number}"
                    )
                if not stock_id:
                    raise RuntimeError(
                        f"{artifact_id} snapshot identity stock_id is blank "
                        f"at {path}:{row_number}"
                    )
                if (
                    artifact_id == MANIFEST_ARTIFACT_ID
                    and not _text(snapshot_row.get("model_id"))
                ):
                    raise RuntimeError(
                        f"{artifact_id} snapshot identity model_id is blank "
                        f"at {path}:{row_number}"
                    )
            try:
                row_count = int(_text(selected["row_count"]))
                column_count = int(_text(selected["column_count"]))
            except ValueError as exc:
                raise RuntimeError(f"invalid snapshot coverage count: {path}") from exc
            if row_count != len(snapshot_rows) or column_count != len(snapshot_fields):
                raise RuntimeError(f"snapshot coverage count mismatch: {path}")
            selected_paths.append(path)
            selected_rows.extend(snapshot_rows)
            selected_field_sets.append(set(snapshot_fields))
        fields_present_every_date = (
            set.intersection(*selected_field_sets) if selected_field_sets else set()
        )
        selector_present = selector_inputs & fields_present_every_date
        target_count = (
            sum(row.get("model_id") == MODEL_ID for row in selected_rows)
            if artifact_id == MANIFEST_ARTIFACT_ID else None
        )
        target_rows = (
            [row for row in selected_rows if row.get("model_id") == MODEL_ID]
            if artifact_id == MANIFEST_ARTIFACT_ID else []
        )
        target_identities = {
            (_text(row.get("signal_date")), _text(row.get("stock_id")))
            for row in target_rows
            if _text(row.get("signal_date")) and _text(row.get("stock_id"))
        }
        return {
            "paths": selected_paths,
            "row_count": len(selected_rows),
            "dates": set(grouped),
            "stocks": _row_stocks(selected_rows),
            "target_count": target_count,
            "target_unique_identity_count": (
                len(target_identities)
                if artifact_id == MANIFEST_ARTIFACT_ID else None
            ),
            "target_duplicate_row_count": (
                len(target_rows) - len(target_identities)
                if artifact_id == MANIFEST_ARTIFACT_ID else None
            ),
            "selector_required_count": len(selector_inputs),
            "selector_present_count": len(selector_present),
            "selector_missing_count": len(selector_inputs - selector_present),
            "selector_missing_inputs": ";".join(
                sorted(selector_inputs - selector_present)
            ),
            "transport_normalized_hash_count": transport_normalized_hash_count,
        }

    snapshots = select(MANIFEST_ARTIFACT_ID)
    all_candidates = select(ALL_CANDIDATES_ARTIFACT_ID)
    for artifact_id, metrics in (
        (ALL_CANDIDATES_ARTIFACT_ID, all_candidates),
        (MANIFEST_ARTIFACT_ID, snapshots),
    ):
        observed = (
            metrics["selector_required_count"],
            metrics["selector_present_count"],
            metrics["selector_missing_count"],
        )
        expected = SNAPSHOT_SELECTOR_COVERAGE_CONTRACT[artifact_id]
        if observed != expected:
            raise RuntimeError(
                f"{artifact_id} selector input coverage drift: "
                f"expected={expected} actual={observed}"
            )
    target_count = int(snapshots["target_count"])
    signal_manifest_rows = scoped_by_artifact[MANIFEST_ARTIFACT_ID]
    signal_dates = {
        _text(row.get("snapshot_report_date")) for row in signal_manifest_rows
    }
    return (
        {
            "paths": [MANIFEST_PATH],
            "row_count": len(signal_manifest_rows),
            "dates": signal_dates,
            "stocks": set(),
            "target_count": target_count,
        },
        all_candidates,
        snapshots,
    )


def _csv_metrics(
    access: SourceAccess,
    path: str,
    *,
    target_model_rows: bool = False,
) -> dict[str, Any]:
    if not access.exists(path):
        return {
            "paths": [], "row_count": 0, "dates": set(), "stocks": set(),
            "target_count": 0 if target_model_rows else None,
        }
    _, rows = _read_csv(access, path)
    scoped_rows = (
        [row for row in rows if row.get("model_id") == MODEL_ID]
        if target_model_rows else rows
    )
    target_identities = {
        (_text(row.get("signal_date")), _text(row.get("stock_id")))
        for row in scoped_rows
        if _text(row.get("signal_date")) and _text(row.get("stock_id"))
    }
    return {
        "paths": [path],
        "row_count": len(rows),
        "dates": _row_dates(scoped_rows, ("signal_date", "date")),
        "stocks": _row_stocks(scoped_rows),
        "target_count": (
            len(scoped_rows)
            if target_model_rows else None
        ),
        "target_unique_identity_count": (
            len(target_identities) if target_model_rows else None
        ),
        "target_duplicate_row_count": (
            len(scoped_rows) - len(target_identities) if target_model_rows else None
        ),
    }


def _dated_metrics(
    access: SourceAccess,
    directory: str,
    pattern: str,
    prefix: str,
    *,
    read_rows: bool,
) -> dict[str, Any]:
    paths = [
        path for path in access.list_paths(directory, pattern)
        if _date_from_filename(path, prefix)
    ]
    dates = {_date_from_filename(path, prefix) for path in paths}
    row_count = 0
    stocks: set[str] = set()
    identities: set[tuple[str, str]] = set()
    field_orders: set[tuple[str, ...]] = set()
    if read_rows:
        for offset in range(0, len(paths), 64):
            batch = paths[offset : offset + 64]
            payloads = access.read_many(batch)
            for path in batch:
                fields, current = _read_csv_payload(payloads[path], path)
                field_orders.add(tuple(fields))
                row_count += len(current)
                stocks.update(_row_stocks(current))
                identities.update(
                    (_text(row.get("date")), _text(row.get("stock_id") or row.get("code")))
                    for row in current
                    if _text(row.get("date"))
                    and _text(row.get("stock_id") or row.get("code"))
                )
    return {
        "paths": paths,
        "row_count": row_count if read_rows else None,
        "dates": dates,
        "stocks": stocks,
        "identities": identities,
        "schema_variant_count": len(field_orders) if read_rows else None,
        "target_count": None,
    }


def _per_stock_metrics(
    access: SourceAccess, directory: str, *, read_rows: bool = False
) -> dict[str, Any]:
    paths = [
        path for path in access.list_paths(directory, "*.csv")
        if re.fullmatch(r"[0-9]{4,6}\.csv", Path(path).name)
    ]
    row_count = 0
    dates: set[str] = set()
    identities: set[tuple[str, str]] = set()
    if read_rows:
        for offset in range(0, len(paths), 64):
            batch = paths[offset : offset + 64]
            payloads = access.read_many(batch)
            for path in batch:
                _, rows = _read_csv_payload(payloads[path], path)
                row_count += len(rows)
                stock_from_path = Path(path).stem
                for row in rows:
                    date = _text(row.get("date") or row.get("as_of_date"))
                    stock = _text(row.get("stock_id") or row.get("code")) or stock_from_path
                    if date:
                        dates.add(date)
                    if date and stock:
                        identities.add((date, stock))
    return {
        "paths": paths,
        "row_count": row_count if read_rows else None,
        "dates": dates,
        "stocks": {Path(path).stem for path in paths},
        "identities": identities,
        "target_count": None,
    }


def _is_supported_daily_price_security_id(value: str) -> bool:
    return len(value) == 4 or (
        value.startswith("00") and 5 <= len(value) <= 6
    )


def _daily_price_identifier_field(fields: list[str], path: str) -> str:
    present = [field for field in ("stock_id", "code", "ticker") if field in fields]
    if len(present) != 1:
        raise RuntimeError(
            "daily price source must provide exactly one security identifier field "
            f"for {path}: {present}"
        )
    return present[0]


def _daily_price_metrics(access: SourceAccess) -> dict[str, Any]:
    all_paths = access.list_paths("data/daily_price", "*.csv")
    canonical_by_date = {
        match.group(1): path
        for path in all_paths
        if (match := re.fullmatch(r"([0-9]{8})\.csv", Path(path).name))
    }
    alias_by_date = {
        match.group(1): path
        for path in all_paths
        if (match := re.fullmatch(r"daily_price_([0-9]{8})\.csv", Path(path).name))
    }
    missing_canonical = sorted(set(alias_by_date) - set(canonical_by_date))
    if missing_canonical:
        raise RuntimeError(
            "daily price aliases have no canonical date-only files: "
            + ";".join(missing_canonical)
        )
    for offset in range(0, len(alias_by_date), 64):
        dates = sorted(alias_by_date)[offset : offset + 64]
        paths = [alias_by_date[date] for date in dates] + [
            canonical_by_date[date] for date in dates
        ]
        payloads = access.read_many(paths)
        for date in dates:
            if payloads[alias_by_date[date]] != payloads[canonical_by_date[date]]:
                raise RuntimeError(f"daily price alias differs from canonical file: {date}")
    canonical_paths = [canonical_by_date[date] for date in sorted(canonical_by_date)]
    row_count = 0
    raw_instruments: set[str] = set()
    stocks: set[str] = set()
    schema_file_counts = {"stock_id": 0, "code": 0, "ticker": 0}
    for offset in range(0, len(canonical_paths), 32):
        batch = canonical_paths[offset : offset + 32]
        payloads = access.read_many(batch)
        for path in batch:
            fields, rows = _read_csv_payload(payloads[path], path)
            row_count += len(rows)
            identifier_field = _daily_price_identifier_field(fields, path)
            schema_file_counts[identifier_field] += 1
            for row_number, row in enumerate(rows, start=2):
                identifier = _text(row.get(identifier_field))
                if re.fullmatch(r"[0-9]{4,6}", identifier) is None:
                    raise RuntimeError(
                        "daily price source has malformed security identifier "
                        f"at {path}:{row_number}: {identifier!r}"
                    )
                raw_instruments.add(identifier)
                if _is_supported_daily_price_security_id(identifier):
                    stocks.add(identifier)
    return {
        "paths": canonical_paths,
        "row_count": row_count,
        "dates": set(canonical_by_date),
        "stocks": stocks,
        "target_count": None,
        "coverage_detail": (
            f"canonical_date_file_count={len(canonical_paths)};"
            f"prefixed_alias_count={len(alias_by_date)};"
            "prefixed_aliases_byte_identical=True;"
            f"raw_unique_instrument_count={len(raw_instruments)};"
            f"supported_security_count={len(stocks)};"
            "excluded_unsupported_instrument_count="
            f"{len(raw_instruments - stocks)};"
            f"ticker_schema_file_count={schema_file_counts['ticker']};"
            f"stock_id_schema_file_count={schema_file_counts['stock_id']};"
            f"code_schema_file_count={schema_file_counts['code']};"
            "malformed_identifier_count=0;"
            "price_date_presence_is_not_market_calendar_proof"
        ),
    }


def _tdcc_latest_dataset_manifest_metrics(access: SourceAccess) -> dict[str, Any]:
    path = TDCC_LATEST_DATASET_MANIFEST_PATH
    if not access.exists(path):
        return {
            "paths": [], "row_count": 0, "dates": set(), "stocks": set(),
            "target_count": None,
        }
    try:
        payload = json.loads(access.read_bytes(path).decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise RuntimeError("invalid latest TDCC dataset manifest JSON") from exc
    if not isinstance(payload, dict):
        raise RuntimeError("latest TDCC dataset manifest must be an object")
    if payload.get("hash_mode") != "utf8_text_lf_normalized_sha256":
        raise RuntimeError("latest TDCC dataset manifest hash_mode is unsupported")
    snapshots = payload.get("snapshots")
    history_dates = payload.get("history_dates")
    required_dates = payload.get("required_dates")
    if not isinstance(snapshots, list) or not isinstance(history_dates, list):
        raise RuntimeError("latest TDCC dataset manifest coverage arrays are missing")
    if not isinstance(required_dates, list):
        raise RuntimeError("latest TDCC dataset manifest required_dates is missing")
    if int(payload.get("snapshot_count", -1)) != len(snapshots):
        raise RuntimeError("latest TDCC dataset manifest snapshot_count mismatch")
    accepted_exception_count = 0
    for item in snapshots:
        if not isinstance(item, dict):
            raise RuntimeError("latest TDCC dataset manifest snapshot row is invalid")
        source_path = _normal_relative_path(_text(item.get("path")))
        source_payload = access.read_bytes(source_path)
        expected_sha = _text(item.get("sha256")).lower()
        if re.fullmatch(r"[0-9a-f]{64}", expected_sha) is None:
            raise RuntimeError(f"latest TDCC manifest has invalid source SHA: {source_path}")
        if expected_sha != _utf8_text_lf_normalized_sha256(source_payload):
            raise RuntimeError(f"latest TDCC manifest source SHA mismatch: {source_path}")
        missing_ids = item.get("current_universe_missing_stock_ids", [])
        if not isinstance(missing_ids, list):
            raise RuntimeError("latest TDCC manifest missing-stock list is invalid")
        accepted_exception_count += len(missing_ids)
    def exact_dates(values: list[Any], field: str) -> set[str]:
        normalized = [_text(value) for value in values]
        invalid = [
            value for value in normalized
            if re.fullmatch(r"[0-9]{8}", value) is None
        ]
        if invalid:
            raise RuntimeError(
                f"latest TDCC dataset manifest {field} contains invalid dates: {invalid}"
            )
        if len(normalized) != len(set(normalized)):
            raise RuntimeError(
                f"latest TDCC dataset manifest {field} contains duplicate dates"
            )
        return set(normalized)

    dates = exact_dates(history_dates, "history_dates")
    required = exact_dates(required_dates, "required_dates")
    if not required <= dates:
        raise RuntimeError(
            "latest TDCC dataset manifest required_dates must be a subset of history_dates"
        )
    current_stock_count = int(payload.get("current_stock_count", 0))
    return {
        "paths": [path],
        "row_count": len(snapshots),
        "dates": dates,
        "stocks": set(),
        "unique_stock_count": current_stock_count,
        "target_count": None,
        "required_dates": required,
        "coverage_detail": (
            f"required_snapshot_count={len(required)};"
            f"history_snapshot_count={len(dates)};"
            f"accepted_exception_count={accepted_exception_count};"
            "declared_snapshot_sha256_verified=True;"
            "current_dataset_manifest_is_not_event_time_full_history"
        ),
    }


def _semantic_metrics(access: SourceAccess) -> dict[str, Any]:
    metrics = _csv_metrics(access, SEMANTIC_OWNERSHIP_PATH)
    if metrics["paths"]:
        _, rows = _read_csv(access, SEMANTIC_OWNERSHIP_PATH)
        target = [row for row in rows if row.get("model_id") == MODEL_ID]
        if len(target) != 1:
            raise RuntimeError(
                "semantic ownership registry must contain exactly one "
                f"{MODEL_ID} row"
            )
        metrics["row_count"] = len(target)
        metrics["target_count"] = len(target)
        item_count = _text(target[0].get("semantic_item_count"))
        semantic_sha = _text(target[0].get("semantic_sha256")).lower()
        if not item_count.isdigit() or int(item_count) <= 0:
            raise RuntimeError("semantic ownership row has invalid semantic_item_count")
        if re.fullmatch(r"[0-9a-f]{64}", semantic_sha) is None:
            raise RuntimeError("semantic ownership row has invalid semantic_sha256")
        metrics["declared_semantic_item_count"] = item_count
        metrics["declared_semantic_sha256"] = semantic_sha
    else:
        metrics["target_count"] = 0
    return metrics


def _shared_semantic_metrics(access: SourceAccess) -> dict[str, Any]:
    metrics = _csv_metrics(access, SHARED_SEMANTIC_PATH)
    if metrics["paths"]:
        fields, rows = _read_csv(access, SHARED_SEMANTIC_PATH)
        if "consumer_models" not in fields:
            raise RuntimeError("shared semantic registry missing consumer_models")
        target = [
            row
            for row in rows
            if MODEL_ID
            in {value.strip() for value in row["consumer_models"].split(";")}
        ]
        metrics["row_count"] = len(target)
        metrics["target_count"] = len(target)
        metrics["declared_semantic_item_count"] = str(len(target))
    else:
        metrics["target_count"] = 0
    return metrics


def _stock_model_contract_metrics(access: SourceAccess) -> dict[str, Any]:
    metrics = _csv_metrics(access, STOCK_MODEL_CONTRACT_PATH)
    if metrics["paths"]:
        fields, rows = _read_csv(access, STOCK_MODEL_CONTRACT_PATH)
        if not {"model_id", "input_columns"}.issubset(fields):
            raise RuntimeError(
                "stock model contract registry missing model_id/input_columns"
            )
        target = [row for row in rows if row.get("model_id") == MODEL_ID]
        if len(target) != 1:
            raise RuntimeError(
                f"stock model contract registry must contain exactly one {MODEL_ID} row"
            )
        required = {
            value.strip()
            for value in target[0]["input_columns"].split(";")
            if value.strip()
        }
        if len(required) != 50:
            raise RuntimeError(
                f"{MODEL_ID} selector input contract must contain exactly 50 columns"
            )
        metrics.update(
            {
                "row_count": 1,
                "target_count": 1,
                "selector_required_count": 50,
                "selector_present_count": 50,
                "selector_missing_count": 0,
            }
        )
    else:
        metrics["target_count"] = 0
    return metrics


def _expected_rows(root: Path, source_ref: str) -> list[dict[str, str]]:
    access = SourceAccess(root, source_ref)
    selector_inputs = _selector_required_inputs(access)
    manifest, all_candidates, snapshots = _published_metrics(
        access, selector_inputs
    )
    published_target_count = int(snapshots["target_count"])
    blockers = BASE_BLOCKERS + (
        (ZERO_SAMPLE_BLOCKER,) if published_target_count == 0 else ()
    )
    legacy = _csv_metrics(access, LEGACY_SIGNAL_LOG_PATH, target_model_rows=True)
    weekly = _dated_metrics(
        access, "output/history/tdcc", "tdcc_holder_ratio_*.csv",
        "tdcc_holder_ratio_", read_rows=True,
    )
    raw = _dated_metrics(
        access, "output/history/tdcc", "tdcc_latest_ratio_raw_*.csv",
        "tdcc_latest_ratio_raw_", read_rows=True,
    )
    latest_dataset = _tdcc_latest_dataset_manifest_metrics(access)
    dataset_manifests = _dated_metrics(
        access, "output/history/tdcc", "tdcc_dataset_manifest_*.json",
        "tdcc_dataset_manifest_", read_rows=False,
    )
    rebuilt_signal = _csv_metrics(access, TDCC_SIGNAL_SNAPSHOT_PATH)
    per_stock_raw = _per_stock_metrics(
        access, "data/tdcc_stock_history_raw", read_rows=True
    )
    per_stock_normalized = _per_stock_metrics(
        access, "data/tdcc_stock_history", read_rows=True
    )
    daily_price = _daily_price_metrics(access)
    stock_price = _per_stock_metrics(
        access, "data/stock_price_history", read_rows=True
    )

    canonical_identities = set(weekly.get("identities", set()))
    normalized_identities = set(per_stock_normalized.get("identities", set()))
    noncanonical_identities = sorted(normalized_identities - canonical_identities)
    per_stock_normalized["noncanonical_row_count"] = len(noncanonical_identities)
    per_stock_normalized["coverage_detail"] = (
        f"normalized_tdcc_history_has_{len(noncanonical_identities)}_noncanonical_rows;"
        "noncanonical_identities="
        + ";".join(f"{date}|{stock}" for date, stock in noncanonical_identities)
    )

    required_tdcc_dates = set(latest_dataset.get("required_dates", set()))
    missing_raw_dates = sorted(required_tdcc_dates - set(raw["dates"]))
    raw["coverage_detail"] = (
        "required_date_missing="
        + (";".join(missing_raw_dates) or "none")
        + f";schema_variant_count={raw.get('schema_variant_count', 0)}"
    )

    published_dates = set(snapshots["dates"])
    if published_dates:
        date_min, date_max = min(published_dates), max(published_dates)
        observed_price_dates = {
            date for date in daily_price["dates"] if date_min <= date <= date_max
        }
    else:
        observed_price_dates = set()
    missing_published_dates = sorted(observed_price_dates - published_dates)
    snapshot_coverage_detail = (
        f"selected_snapshot_dates={len(published_dates)};"
        f"observed_price_dates_in_range={len(observed_price_dates)};"
        "missing_published_snapshot_dates="
        + (";".join(missing_published_dates) or "none")
        + ";price_date_presence_is_not_market_calendar_proof"
    )
    snapshots["coverage_detail"] = (
        snapshot_coverage_detail
        + f";transport_normalized_hash_count={snapshots['transport_normalized_hash_count']}"
        + ";non_transport_hash_mismatch_count=0"
    )
    all_candidates["coverage_detail"] = (
        snapshot_coverage_detail
        + f";transport_normalized_hash_count={all_candidates['transport_normalized_hash_count']}"
        + ";non_transport_hash_mismatch_count=0"
    )
    manifest["coverage_detail"] = (
        f"signal_revision_count={manifest['row_count']};"
        f"selected_date_count={len(published_dates)}"
    )

    metrics_by_family = {
        "published_snapshot_manifest": manifest,
        "published_all_candidates_snapshots": all_candidates,
        "published_model_signal_snapshots": snapshots,
        "legacy_candidate_signal_log": legacy,
        "tdcc_weekly_holder_snapshots": weekly,
        "tdcc_date_versioned_raw_snapshots": raw,
        "tdcc_latest_dataset_manifest": latest_dataset,
        "tdcc_dataset_manifests": dataset_manifests,
        "tdcc_rebuilt_signal_snapshot": rebuilt_signal,
        "tdcc_per_stock_raw_history": per_stock_raw,
        "tdcc_per_stock_normalized_history": per_stock_normalized,
        "daily_price_date_snapshots": daily_price,
        "stock_price_history": stock_price,
        "stock_model_contract_registry": _stock_model_contract_metrics(access),
        "model_semantic_ownership_registry": _semantic_metrics(access),
        "shared_semantic_registry": _shared_semantic_metrics(access),
    }
    expected: list[dict[str, str]] = []
    for family in SOURCE_FAMILY_ORDER:
        role, source_path, coverage, pit = FAMILY_CONTRACTS[family]
        metrics = metrics_by_family[family]
        paths = list(metrics["paths"])
        dates = sorted(metrics["dates"])
        stocks = set(metrics["stocks"])
        hash_basis, source_sha = _hash_contract(access, paths)
        target_count = metrics.get("target_count")
        available = bool(paths)
        expected.append(
            {
                "artifact_version": ARTIFACT_VERSION,
                "source_commit_sha": access.resolved_commit_sha(),
                "model_id": MODEL_ID,
                "model_name_zh": MODEL_NAME_ZH,
                "source_family": family,
                "source_role": role,
                "source_path": source_path,
                "source_hash_basis": hash_basis,
                "source_sha256": source_sha,
                "source_file_count": str(len(paths)),
                "source_row_count": (
                    "" if metrics.get("row_count") is None
                    else str(metrics["row_count"])
                ),
                "source_unique_date_count": str(len(dates)),
                "source_date_min": dates[0] if dates else "",
                "source_date_max": dates[-1] if dates else "",
                "source_unique_stock_count": str(
                    metrics.get("unique_stock_count", len(stocks))
                ),
                "source_target_model_row_count": (
                    "" if target_count is None else str(target_count)
                ),
                "source_target_unique_identity_count": (
                    "" if metrics.get("target_unique_identity_count") is None
                    else str(metrics["target_unique_identity_count"])
                ),
                "source_target_duplicate_row_count": (
                    "" if metrics.get("target_duplicate_row_count") is None
                    else str(metrics["target_duplicate_row_count"])
                ),
                "source_noncanonical_row_count": (
                    "" if metrics.get("noncanonical_row_count") is None
                    else str(metrics["noncanonical_row_count"])
                ),
                "source_transport_normalized_hash_count": (
                    "" if metrics.get("transport_normalized_hash_count") is None
                    else str(metrics["transport_normalized_hash_count"])
                ),
                "selector_required_input_count": (
                    "" if metrics.get("selector_required_count") is None
                    else str(metrics["selector_required_count"])
                ),
                "selector_present_input_count": (
                    "" if metrics.get("selector_present_count") is None
                    else str(metrics["selector_present_count"])
                ),
                "selector_missing_input_count": (
                    "" if metrics.get("selector_missing_count") is None
                    else str(metrics["selector_missing_count"])
                ),
                "selector_missing_inputs": _text(
                    metrics.get("selector_missing_inputs")
                ),
                "declared_semantic_item_count": _text(
                    metrics.get("declared_semantic_item_count")
                ),
                "declared_semantic_sha256": _text(
                    metrics.get("declared_semantic_sha256")
                ),
                "published_target_row_count": str(published_target_count),
                "source_status": "available" if available else "missing",
                "coverage_status": coverage if available else "missing_source",
                "coverage_detail": _text(metrics.get("coverage_detail")),
                "pit_status": pit if available else "unavailable",
                "availability_state": AVAILABILITY_STATE,
                "selector_replay_allowed": "False",
                "performance_metrics_allowed": "False",
                "formal_use": "False",
                "trade_eligible": "False",
                "promotion_evidence_allowed": "False",
                "promotion_status": "blocked",
                "blockers": ";".join(blockers),
            }
        )
    return expected


def _read_artifact(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise RuntimeError(f"missing availability audit artifact: {path.as_posix()}")
    try:
        text = path.read_bytes().decode("utf-8-sig")
        header_reader = csv.reader(io.StringIO(text, newline=""), strict=True)
        header = next(header_reader, [])
        dict_reader = csv.DictReader(io.StringIO(text, newline=""), strict=True)
        rows: list[dict[str, str]] = []
        for row_number, row in enumerate(dict_reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise RuntimeError(
                    f"availability audit row width mismatch at row {row_number}"
                )
            rows.append({_text(key): _text(value) for key, value in row.items()})
    except (UnicodeDecodeError, csv.Error) as exc:
        raise RuntimeError(f"failed to read availability audit artifact: {exc}") from exc
    return [_text(field) for field in header], rows


def validate(
    *,
    repository_root: Path = ROOT,
    artifact_path: Path = DEFAULT_ARTIFACT,
    source_ref: str = "",
) -> list[str]:
    errors: list[str] = []
    try:
        fields, rows = _read_artifact(artifact_path)
    except RuntimeError as exc:
        return [str(exc)]
    if fields != AUDIT_FIELDS:
        errors.append(
            "availability audit header/order mismatch: "
            f"expected={AUDIT_FIELDS!r} actual={fields!r}"
        )
        return errors
    if len(fields) != len(set(fields)):
        errors.append("availability audit header contains duplicate columns")
        return errors
    prohibited = {
        "event_id",
        "signal_event_id",
        "entry_date",
        "exit_date",
        "realized_return",
        "return_pct",
        "win_count",
        "win_rate",
        "average_return",
        "median_return",
    }
    present_prohibited = sorted(prohibited & set(fields))
    if present_prohibited:
        errors.append(f"availability audit contains performance/event fields: {present_prohibited}")
        return errors
    recorded_commits = {row.get("source_commit_sha", "") for row in rows}
    if len(recorded_commits) != 1:
        errors.append("availability audit source_commit_sha must be identical on every row")
        return errors
    recorded_commit = next(iter(recorded_commits))
    if recorded_commit and re.fullmatch(r"[0-9a-f]{40}", recorded_commit) is None:
        errors.append("availability audit source_commit_sha is not a 40-hex commit")
        return errors
    if source_ref and recorded_commit:
        requested_commit = SourceAccess(
            repository_root.resolve(), source_ref
        ).resolved_commit_sha()
        if not requested_commit or requested_commit != recorded_commit:
            errors.append(
                "availability audit source_commit_sha does not match requested source_ref"
            )
            return errors
    effective_source_ref = recorded_commit or source_ref or "HEAD"
    try:
        expected = _expected_rows(repository_root.resolve(), effective_source_ref)
    except RuntimeError as exc:
        return [f"source availability recomputation failed: {exc}"]
    if len(rows) != len(expected):
        errors.append(
            f"availability audit row count mismatch: expected={len(expected)} actual={len(rows)}"
        )
        return errors
    if tuple(row.get("source_family", "") for row in rows) != SOURCE_FAMILY_ORDER:
        errors.append("availability audit source family order mismatch")
    false_fields = (
        "selector_replay_allowed",
        "performance_metrics_allowed",
        "formal_use",
        "trade_eligible",
        "promotion_evidence_allowed",
    )
    for index, (actual, wanted) in enumerate(zip(rows, expected, strict=True), start=2):
        family = wanted["source_family"]
        for field in AUDIT_FIELDS:
            if actual.get(field, "") != wanted[field]:
                errors.append(
                    f"row {index} {family} {field} mismatch: "
                    f"expected={wanted[field]!r} actual={actual.get(field, '')!r}"
                )
        for field in false_fields:
            if actual.get(field) != "False":
                errors.append(f"row {index} {family} {field} must be False")
        if actual.get("promotion_status") != "blocked":
            errors.append(f"row {index} {family} promotion_status must be blocked")
    return errors


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the independent TDCC stealth accumulation PIT replay "
            "source-availability audit."
        )
    )
    parser.add_argument("--repository-root", type=Path, default=ROOT)
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--source-ref", default="")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    root = args.repository_root.resolve()
    artifact = args.artifact or (
        root / "output" / "research" / MODEL_ID / ARTIFACT_NAME
    )
    errors = validate(
        repository_root=root,
        artifact_path=artifact,
        source_ref=args.source_ref,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_tdcc_stealth_pit_replay_availability_audit={artifact.as_posix()}")
    print(f"availability_state={AVAILABILITY_STATE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
