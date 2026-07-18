from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract, require_dataset_id
from tracking_utils import LATEST_DIR, now_text, read_csv


HISTORY_DIR = Path("output/history/surge_model")

REQUIRED_FILES = [
    HISTORY_DIR / "daily_stock_feature_panel.csv",
    HISTORY_DIR / "surge_event_labels.csv",
    HISTORY_DIR / "pre_surge_event_study.csv",
    HISTORY_DIR / "non_surge_control_sample.csv",
    LATEST_DIR / "surge_model_feature_importance_latest.md",
    LATEST_DIR / "surge_model_feature_importance_latest.csv",
    LATEST_DIR / "surge_model_score_latest.md",
    LATEST_DIR / "surge_model_score_latest.csv",
    LATEST_DIR / "surge_precondition_candidates_latest.md",
    LATEST_DIR / "surge_precondition_candidates_latest.csv",
    LATEST_DIR / "surge_model_backtest_latest.md",
    LATEST_DIR / "surge_model_backtest_latest.csv",
    LATEST_DIR / "surge_model_chatgpt_packet_latest.md",
]

FEATURE_REQUIRED_COLUMNS = [
    "trade_date",
    "stock_id",
    "stock_name",
    "close",
    "price_ret_20d",
    "distance_ma20_pct",
    "volume_ratio_20d",
    "surge_precondition_score",
    "surge_watch_label",
]

LABEL_REQUIRED_COLUMNS = [
    "trade_date",
    "stock_id",
    "future_max_ret_5d",
    "future_max_ret_10d",
    "future_max_ret_20d",
    "surge_5d",
    "surge_10d",
    "surge_20d",
    "mature_5d",
    "mature_10d",
    "mature_20d",
]


def bool_series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(False, index=df.index)
    return df[column].astype(str).str.lower().isin({"true", "1", "yes", "y"})


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    errors: list[str] = []
    warnings: list[str] = []
    status: dict[str, object] = {"generated_at": now_text()}
    contract = load_research_tdcc_dataset_contract()
    status["source_tdcc_dataset_id"] = contract.dataset_id

    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"missing file: {path.as_posix()}")
        elif path.stat().st_size == 0:
            errors.append(f"empty file: {path.as_posix()}")

    feature = read_csv(HISTORY_DIR / "daily_stock_feature_panel.csv", dtype=str, keep_default_na=False)
    labels = read_csv(HISTORY_DIR / "surge_event_labels.csv", dtype=str, keep_default_na=False)
    candidates = read_csv(LATEST_DIR / "surge_precondition_candidates_latest.csv", dtype=str, keep_default_na=False)
    backtest = read_csv(LATEST_DIR / "surge_model_backtest_latest.csv", dtype=str, keep_default_na=False)
    for label, frame in (
        ("surge feature panel", feature),
        ("surge labels", labels),
        ("surge candidates", candidates),
        ("surge backtest", backtest),
    ):
        try:
            require_dataset_id(frame, contract, label=label)
        except RuntimeError as exc:
            errors.append(str(exc))

    if feature.empty:
        errors.append("feature panel is empty")
    else:
        missing = [col for col in FEATURE_REQUIRED_COLUMNS if col not in feature.columns]
        if missing:
            errors.append("feature panel missing columns: " + ",".join(missing))
        status["feature_panel_rows"] = len(feature)
        status["feature_panel_dates"] = feature["trade_date"].nunique() if "trade_date" in feature.columns else 0

    if labels.empty:
        errors.append("labels csv is empty")
    else:
        missing = [col for col in LABEL_REQUIRED_COLUMNS if col not in labels.columns]
        if missing:
            errors.append("labels missing columns: " + ",".join(missing))
        mature_5 = int(bool_series(labels, "mature_5d").sum())
        mature_10 = int(bool_series(labels, "mature_10d").sum())
        mature_20 = int(bool_series(labels, "mature_20d").sum())
        status["mature_5d_count"] = mature_5
        status["mature_10d_count"] = mature_10
        status["mature_20d_count"] = mature_20
        if mature_10 == 0:
            warnings.append("mature_10d_count is 0; backtest must remain not_ready")

    if candidates.empty:
        errors.append("surge candidates csv is empty")
    elif "surge_precondition_score" not in candidates.columns:
        errors.append("surge candidates missing surge_precondition_score")

    if backtest.empty:
        errors.append("backtest csv is empty")
    elif "segment" not in backtest.columns:
        errors.append("backtest missing segment column")

    packet = LATEST_DIR / "surge_model_chatgpt_packet_latest.md"
    if packet.exists():
        text = packet.read_text(encoding="utf-8", errors="replace")
        line_count = len(text.splitlines())
        status["packet_line_count"] = line_count
        if line_count < 30:
            errors.append("surge packet appears too short or single-line compressed")
        if "tuning_status = not_ready" not in text:
            warnings.append("surge packet does not explicitly mark tuning_status = not_ready")
        if "Top Surge Precondition Candidates" not in text:
            errors.append("surge packet missing Top Surge Precondition Candidates section")
        if contract.dataset_id not in text or "source_tdcc_dataset_id" not in text:
            errors.append("surge packet lacks canonical TDCC dataset lineage")

    validation_status = "pass" if not errors else "fail"
    status["status"] = validation_status
    status["errors"] = errors
    status["warnings"] = warnings

    json_path = LATEST_DIR / "surge_model_validation_latest.json"
    md_path = LATEST_DIR / "surge_model_validation_latest.md"
    json_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(
        "\n".join(
            [
                "# Surge Model Validation Latest",
                "",
                f"generated_at: {status['generated_at']}",
                f"status: {validation_status}",
                "",
                "## Errors",
                "\n".join(f"- {item}" for item in errors) if errors else "- none",
                "",
                "## Warnings",
                "\n".join(f"- {item}" for item in warnings) if warnings else "- none",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Saved: {json_path}")
    print(f"Saved: {md_path}")
    if errors:
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
