from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, read_csv  # noqa: E402
from validate_daily_operation_adapter_protected_fields import validate_adapter_frame  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_NAME = "daily_published_model_snapshot_manifest.csv"
SNAPSHOT_REPOSITORY_PATH = Path("output/history/daily_model_snapshots")
REQUIRED_MANIFEST_COLUMNS = {"snapshot_report_date", "artifact_id", "snapshot_path", "snapshot_sha256"}
MODEL_ID = "price_pullback_23ema"
OPERATION_MODULE_ID = "price_pullback_23ema_prev20_breakout_stop_v1"
APPROVAL_VERSION = "price_pullback_23ema_operation_v1_20260703"
BUY_FILTER_ID = "v1_gate_return20_tdcc_high_obv"
ENTRY_RULE_ID = "signal_date_next_open"
STOP_LOSS_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
EXIT_RULE_ID = "close_prev20_high_break_next_open"
OUT_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_section_latest.csv"
OUT_MD = OUT_CSV.with_suffix(".md")
AUDIT_CSV = LATEST_DIR / "daily_price_pullback_23ema_operation_evidence_audit_latest.csv"
AUDIT_MD = AUDIT_CSV.with_suffix(".md")
SECTION_EMPTY_NOTE_ZH = {
    "confirmed_operation": "本日無股票推薦",
    "active_operation": "目前無操作中追蹤列",
}
RANK_COLUMNS = ("model_rank", "display_rank", "model_rank_overall")
PROOF_COLUMNS = (
    "confirmation_source_artifact", "confirmation_source_sha256",
    "confirmation_row_sha256", "confirmation_snapshot_revision",
    "confirmation_snapshot_report_date",
)
# These fields describe the new lifecycle row, rather than the frozen confirmation.
ACTIVE_MUTABLE_COLUMNS = {
    "pdf_view", "pdf_section", "pdf_section_zh", "display_order",
    "operation_asof_date", "operation_source_date_status", "operation_status",
    "operation_status_zh", "buy_rank_eligible", "row_action_status",
    "daily_signal_date", "daily_model_signal_count", "adapter_source", "generated_at",
    "entry_date", "entry_price", "target_price", "stop_loss_price",
    "stop_loss_label_zh", "stop_confirmed_days", "operation_age_days",
    "realized_exit_date", "realized_exit_reason", "pdf_note_zh", *PROOF_COLUMNS,
}

REQUIRED_COLUMNS = {
    *RANK_COLUMNS, *PROOF_COLUMNS,
    "model_id",
    "model_name_zh",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "report_line",
    "display_order",
    "stock_id",
    "stock_display",
    "operation_quality",
    "row_action_status",
    "buy_rank_eligible",
    "signal_date",
    "entry_rule_id",
    "entry_basis_zh",
    "stop_loss_rule_id",
    "stop_basis_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "planned_holding_days",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "technical_package_win_rate_zh",
    "technical_package_avg_return_zh",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "buy_filter_id",
    "adapter_source_status",
}

REQUIRED_AUDIT_COLUMNS = {
    "model_id",
    "operation_asof_date",
    "stock_id",
    "signal_date",
    "operation_lifecycle_state",
    "audit_status",
    "included_in_daily_adapter",
    "reason",
}


def validate_mirror(path: Path, errors: list[str]) -> None:
    mirror = DOCS_LATEST_DIR / path.name
    if not mirror.exists():
        errors.append(f"missing docs/latest mirror: {mirror}")
        return
    if path.read_bytes() != mirror.read_bytes():
        errors.append(f"docs/latest mirror differs: {mirror}")


def validate_files() -> list[str]:
    errors: list[str] = []
    for path in [OUT_CSV, OUT_MD, AUDIT_CSV, AUDIT_MD]:
        if not path.exists():
            errors.append(f"missing price_pullback operation adapter artifact: {path}")
        else:
            validate_mirror(path, errors)
    return errors


def validate_section(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if df.empty:
        return [f"empty price_pullback operation adapter: {OUT_CSV}"]
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        return [f"price_pullback operation adapter missing columns: {missing}"]
    models = sorted(set(df["model_id"].astype(str)))
    if models != [MODEL_ID]:
        errors.append(f"price_pullback adapter must contain only {MODEL_ID}, got {models}")
    errors.extend(validate_adapter_frame(df, MODEL_ID))
    views = set(df["pdf_view"].astype(str))
    if views != {"highlight", "full"}:
        errors.append(f"price_pullback adapter must contain highlight and full views, got {sorted(views)}")
    sections = set(df["pdf_section"].astype(str))
    if sections != {"confirmed_operation", "active_operation"}:
        errors.append(f"price_pullback adapter must contain confirmed_operation and active_operation only, got {sorted(sections)}")
    for view in ["highlight", "full"]:
        for section in ["confirmed_operation", "active_operation"]:
            part = df[(df["pdf_view"].astype(str).eq(view)) & (df["pdf_section"].astype(str).eq(section))]
            if part.empty:
                errors.append(f"price_pullback adapter missing view/section: {view}/{section}")
            if part["row_type"].astype(str).eq("empty_state").any():
                empty = part[part["row_type"].astype(str).eq("empty_state")]
                expected = SECTION_EMPTY_NOTE_ZH[section]
                if not empty["stock_display"].astype(str).eq(expected).all():
                    errors.append(f"{view}/{section} empty_state must use {expected!r}")
    expected = {
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": OPERATION_MODULE_ID,
        "approval_version": APPROVAL_VERSION,
        "operation_directive_level": "approved_daily_operation_guidance",
        "buy_filter_id": BUY_FILTER_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "stop_loss_rule_id": STOP_LOSS_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "adapter_source_status": "ready",
    }
    for col, value in expected.items():
        unexpected = sorted(set(df[col].astype(str)) - {value})
        if unexpected:
            errors.append(f"price_pullback adapter {col} must be {value!r}, got {unexpected}")
    buy_rows = df[df["buy_rank_eligible"].astype(str).eq("True")]
    bad_buy = buy_rows[
        ~(
            buy_rows["pdf_section"].astype(str).eq("confirmed_operation")
            & buy_rows["row_type"].astype(str).eq("data")
            & buy_rows["row_action_status"].astype(str).eq("confirmed_buy_candidate")
        )
    ]
    if not bad_buy.empty:
        errors.append("buy_rank_eligible=True must be limited to confirmed_operation data rows")
    if df.astype(str).agg("|".join, axis=1).str.contains("intraday", case=False, regex=False).any():
        errors.append("price_pullback operation adapter must not use intraday execution semantics")
    if df["row_type"].astype(str).eq("data").any():
        data = df[df["row_type"].astype(str).eq("data")]
        if data["operation_quality"].astype(str).isin(["", "empty_state"]).any():
            errors.append("price_pullback data rows must expose operation_quality")
        confirmed = data[data["pdf_section"].astype(str).eq("confirmed_operation")]
        active = data[data["pdf_section"].astype(str).eq("active_operation")]
        if not confirmed.empty and not active.empty:
            confirmed_keys = set(
                tuple(item)
                for item in confirmed[["pdf_view", "report_line", "stock_id"]]
                .astype(str)
                .itertuples(index=False, name=None)
            )
            active_keys = set(
                tuple(item)
                for item in active[["pdf_view", "report_line", "stock_id"]]
                .astype(str)
                .itertuples(index=False, name=None)
            )
            overlap = sorted(confirmed_keys & active_keys)
            if overlap:
                errors.append(f"price_pullback stock cannot be both confirmed and active in the same view/report line: {overlap}")
    return errors


def validate_confirmation_bindings(
    frame: pd.DataFrame,
    *,
    repository_root: Path,
    snapshot_dir: Path | None = None,
    manifest_path: Path | None = None,
) -> list[str]:
    """Independently bind active rows to immutable, originally buy-ranked r1 rows.

    This checks saved-input consumption, not PIT coverage or backtest returns.
    No production selector, lifecycle, or confirmation-reader function is imported.
    """
    required = {"pdf_section", "row_type", "stock_id", "signal_date", "report_line",
                "operation_asof_date", *RANK_COLUMNS, *PROOF_COLUMNS}
    if not required.issubset(frame.columns):
        return [f"confirmation binding missing columns: {sorted(required - set(frame.columns))}"]
    data = frame.fillna("").astype(str)
    data = data[data["row_type"].eq("data")]
    errors: list[str] = []
    for _, row in data.iterrows():
        if not all(re.fullmatch(r"[1-9][0-9]*", row[field]) for field in RANK_COLUMNS):
            errors.append(f"23EMA data row missing original rank: {row['stock_id']}")
    active = data[data["pdf_section"].eq("active_operation")]
    if active.empty:
        return errors
    root = Path(repository_root).resolve()
    directory = Path(snapshot_dir or root / SNAPSHOT_REPOSITORY_PATH).resolve()
    manifest_file = Path(manifest_path or directory / MANIFEST_NAME)
    try:
        manifest = pd.read_csv(manifest_file, dtype=str, keep_default_na=False)
        missing = REQUIRED_MANIFEST_COLUMNS - set(manifest.columns)
        if missing:
            return errors + [f"confirmation manifest missing columns: {sorted(missing)}"]
        revision_columns = {"snapshot_revision", "supersedes_snapshot_sha256", "revision_reason"}
        present = revision_columns & set(manifest.columns)
        if present and present != revision_columns:
            return errors + ["confirmation manifest has a partial revision schema"]
        if not present:
            manifest = manifest.assign(snapshot_revision="r1", supersedes_snapshot_sha256="",
                                       revision_reason="legacy_v1_manifest")
        elif manifest["snapshot_revision"].eq("").any():
            return errors + ["confirmation manifest has a blank snapshot_revision"]
    except (OSError, ValueError, RuntimeError) as exc:
        return errors + [f"cannot validate original confirmations: {exc}"]
    for _, row in active.iterrows():
        identity = (row["stock_id"], row["signal_date"], row["report_line"])
        prefix = f"23EMA original confirmation {identity}"
        date = row["confirmation_snapshot_report_date"]
        if (re.fullmatch(r"[0-9]{8}", date) is None or date != row["signal_date"]
                or date >= row["operation_asof_date"]
                or row["confirmation_snapshot_revision"] != "r1"):
            errors.append(f"{prefix}: invalid original revision/date")
            continue
        matches = manifest[
            manifest["artifact_id"].eq("price_pullback_23ema_operation_section")
            & manifest["snapshot_report_date"].eq(date)
            & manifest["snapshot_revision"].eq("r1")
        ]
        if len(matches) != 1:
            errors.append(f"{prefix}: requires exactly one manifest r1")
            continue
        original_manifest = matches.iloc[0]
        sha = str(original_manifest["snapshot_sha256"])
        name = Path(str(original_manifest["snapshot_path"]).replace("\\", "/")).name
        expected_name = f"daily_price_pullback_23ema_operation_section_{date}_r1_{sha[:12]}.csv"
        legacy = (original_manifest["revision_reason"] == "legacy_v1_manifest"
                  and name == f"daily_price_pullback_23ema_operation_section_{date}.csv")
        relative = (SNAPSHOT_REPOSITORY_PATH / name).as_posix()
        if (re.fullmatch(r"[0-9a-f]{64}", sha) is None
                or str(original_manifest["supersedes_snapshot_sha256"])
                or (name != expected_name and not legacy)
                or str(original_manifest["snapshot_path"]).replace("\\", "/") != relative
                or row["confirmation_source_artifact"] != relative):
            errors.append(f"{prefix}: original source path/hash identity mismatch")
            continue
        path = (directory / name).resolve()
        if not path.is_relative_to(directory):
            errors.append(f"{prefix}: original source escapes approved snapshot directory")
            continue
        try:
            payload = path.read_bytes()
            lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
            accepted_hashes = {hashlib.sha256(item).hexdigest()
                               for item in (payload, lf, lf.replace(b"\n", b"\r\n"))}
            if (sha not in accepted_hashes
                    or hashlib.sha256(lf).hexdigest() != row["confirmation_source_sha256"]):
                errors.append(f"{prefix}: original source SHA-256 mismatch")
                continue
            reader = csv.DictReader(io.StringIO(lf.decode("utf-8-sig"), newline=""))
            originals = [item for item in reader if (
                item.get("model_id") == MODEL_ID and item.get("row_type") == "data"
                and item.get("pdf_section") in {"confirmed_operation", "confirmed_unranked_operation"}
                and tuple(item.get(field, "") for field in ("stock_id", "signal_date", "report_line")) == identity
            )]
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{prefix}: cannot read original source: {exc}")
            continue
        views = {item.get("pdf_view"): item for item in originals}
        if len(originals) != 2 or set(views) != {"full", "highlight"}:
            errors.append(f"{prefix}: original confirmation requires unique full/highlight pair")
            continue
        original = views["full"]
        if ({key: value for key, value in original.items() if key != "pdf_view"}
                != {key: value for key, value in views["highlight"].items() if key != "pdf_view"}):
            errors.append(f"{prefix}: original full/highlight values conflict")
            continue
        if (original.get("pdf_section") != "confirmed_operation"
                or original.get("buy_rank_eligible") != "True"
                or original.get("operation_asof_date") != date
                or not all(re.fullmatch(r"[1-9][0-9]*", original.get(field, "")) for field in RANK_COLUMNS)):
            errors.append(f"{prefix}: original confirmation was not buy-ranked")
            continue
        row_sha = hashlib.sha256(json.dumps(original, ensure_ascii=False, sort_keys=True,
                                           separators=(",", ":")).encode("utf-8")).hexdigest()
        if row_sha != row["confirmation_row_sha256"]:
            errors.append(f"{prefix}: original row SHA-256 mismatch")
        changed = sorted(field for field, value in original.items()
                         if field not in ACTIVE_MUTABLE_COLUMNS and row.get(field, "") != value)
        if changed:
            errors.append(f"{prefix}: frozen confirmation fields changed: {changed}")
    return errors


def validate_audit(audit: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if audit.empty:
        return [f"empty price_pullback operation audit: {AUDIT_CSV}"]
    missing = sorted(REQUIRED_AUDIT_COLUMNS - set(audit.columns))
    if missing:
        return [f"price_pullback operation audit missing columns: {missing}"]
    models = sorted(set(audit["model_id"].astype(str)))
    if models != [MODEL_ID]:
        errors.append(f"price_pullback audit must contain only {MODEL_ID}, got {models}")
    return errors


def main() -> int:
    errors = validate_files()
    section = read_csv(OUT_CSV, dtype=str).fillna("") if OUT_CSV.exists() else pd.DataFrame()
    audit = read_csv(AUDIT_CSV, dtype=str).fillna("") if AUDIT_CSV.exists() else pd.DataFrame()
    if not section.empty:
        errors.extend(validate_section(section))
        errors.extend(validate_confirmation_bindings(section, repository_root=ROOT))
    if not audit.empty:
        errors.extend(validate_audit(audit))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("price_pullback_23ema operation section validation passed")
    print(f"validated_output={OUT_CSV}")
    print(f"rows={len(section)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
