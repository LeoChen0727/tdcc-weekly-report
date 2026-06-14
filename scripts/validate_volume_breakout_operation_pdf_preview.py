from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
PREVIEW_CSV = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.csv"
PREVIEW_MD = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.md"
SPEC_MD = ROOT / "docs" / "specs" / "volume_breakout_operation_pdf_table_spec.md"

REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "display_order",
    "stock_id",
    "stock_display",
    "operation_status_zh",
    "stop_basis_zh",
    "sample_size",
    "win_rate_zh",
    "median_return_zh",
    "pdf_note_zh",
}

FORBIDDEN_DISPLAY_TEXT = [
    "median",
    "signal_low",
    "next_open",
    "pullback_5ma_confirmed",
    "pullback_10ma_confirmed",
    "next_day_continuation_confirmed",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def main() -> int:
    for path in [PREVIEW_CSV, PREVIEW_MD, SPEC_MD]:
        if not path.exists():
            fail(f"missing required file: {path}")
    preview = read_csv(PREVIEW_CSV)
    if preview.empty:
        fail(f"{PREVIEW_CSV} has no rows")
    missing = sorted(REQUIRED_COLUMNS - set(preview.columns))
    if missing:
        fail(f"{PREVIEW_CSV} missing columns: {missing}")

    bad_models = sorted(set(preview["model_id"].astype(str)) - {"volume_range_breakout"})
    if bad_models:
        fail(f"volume breakout operation artifact must not include other models: {bad_models}")
    bad_views = sorted(set(preview["pdf_view"].astype(str)) - {"highlight", "full"})
    if bad_views:
        fail(f"invalid pdf_view values: {bad_views}")
    bad_sections = sorted(set(preview["pdf_section"].astype(str)) - {"confirmed_operation", "pending_confirmation"})
    if bad_sections:
        fail(f"invalid pdf_section values: {bad_sections}")

    display_cols = [
        "operation_status_zh",
        "quality_status_zh",
        "trigger_zh",
        "entry_basis_zh",
        "entry_price_status_zh",
        "stop_basis_zh",
        "exit_rule_zh",
        "pending_age_zh",
        "pending_group_zh",
        "pending_confirmation_zh",
        "tdcc_status_zh",
        "win_rate_zh",
        "avg_return_zh",
        "median_return_zh",
        "confidence_zh",
        "pdf_note_zh",
    ]
    display_text = "\n".join(
        preview[col].astype(str).str.cat(sep="\n") for col in display_cols if col in preview.columns
    )
    for token in FORBIDDEN_DISPLAY_TEXT:
        if token in display_text:
            fail(f"forbidden display token leaked: {token}")

    md_text = PREVIEW_MD.read_text(encoding="utf-8", errors="replace")
    if "中位數報酬" not in md_text:
        fail("preview markdown must display 中位數報酬")
    if "最低價" not in display_text:
        fail("preview stop display must use 日期最低價 wording")

    confirmed = preview[preview["pdf_section"].astype(str).eq("confirmed_operation")]
    highlight_confirmed = confirmed[confirmed["pdf_view"].astype(str).eq("highlight")]
    if len(highlight_confirmed) > 10:
        fail("highlight confirmed rows must be at most 10")
    if not highlight_confirmed.empty:
        samples = pd.to_numeric(highlight_confirmed["sample_size"], errors="coerce")
        if samples.isna().any() or (samples < 10).any():
            fail("highlight confirmed rows must have sample_size >= 10")
        med = pd.to_numeric(
            highlight_confirmed["median_return_zh"]
            .astype(str)
            .str.replace("%", "", regex=False)
            .str.replace("+", "", regex=False),
            errors="coerce",
        )
        if med.isna().any() or (med <= 0).any():
            fail("highlight confirmed rows must have positive 中位數報酬")

    full_pending = preview[
        preview["pdf_view"].astype(str).eq("full")
        & preview["pdf_section"].astype(str).eq("pending_confirmation")
    ]
    if full_pending.duplicated("stock_id").any():
        fail("full pending preview must be de-duplicated by stock_id")

    print(
        "volume breakout operation artifact validation passed "
        f"rows={len(preview)} highlight_confirmed={len(highlight_confirmed)} "
        f"full_pending={len(full_pending)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
