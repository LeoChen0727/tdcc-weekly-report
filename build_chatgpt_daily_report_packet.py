from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re
import shutil
from typing import Any

import pandas as pd


REPO_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"

LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
REPORT_MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
PDF_KLINE_STATUS_JSON = LATEST_DIR / "pdf_kline_chart_status_latest.json"
PDF_KLINE_STATUS_MD = LATEST_DIR / "pdf_kline_chart_status_latest.md"
FIXED_PDF_MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"
FIXED_PDF_VALIDATION_JSON = LATEST_DIR / "daily_market_report_validation_latest.json"
DAILY_SIGNAL_LOG = Path("output/history/daily_signals/daily_candidate_signal_log.csv")
DAILY_SIGNAL_PERFORMANCE = Path("output/history/daily_signals/daily_candidate_signal_performance.csv")
DAILY_SIGNAL_SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
DAILY_SIGNAL_WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
DAILY_SIGNAL_MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"
CHIP_FLOW_STREAK_CSV = LATEST_DIR / "chip_flow_positive_streak_latest.csv"
CHIP_FLOW_STREAK_MD = LATEST_DIR / "chip_flow_positive_streak_latest.md"
CHIP_FLOW_STATUS_JSON = LATEST_DIR / "chip_flow_source_status_latest.json"
INSTITUTIONAL_FLOW_CSV = LATEST_DIR / "institutional_investor_flow_latest.csv"
WARRANT_MARKET_MD = LATEST_DIR / "warrant_market_report_latest.md"
WARRANT_MARKET_PDF = LATEST_DIR / "warrant_market_report_latest.pdf"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_SECTOR_HEAT_CSV = LATEST_DIR / "warrant_sector_heat_latest.csv"
WARRANT_SIGNAL_PERFORMANCE_MD = LATEST_DIR / "warrant_signal_performance_latest.md"

SUMMARY_LATEST_MD = LATEST_DIR / "daily_market_summary_latest.md"
FULL_LATEST_MD = LATEST_DIR / "daily_market_full_latest.md"
SUMMARY_LATEST_PDF = LATEST_DIR / "daily_market_summary_latest.pdf"
FULL_LATEST_PDF = LATEST_DIR / "daily_market_full_latest.pdf"
CURATED_REPORT_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_REPORT_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"

SUMMARY_CN_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
FULL_CN_MD = LATEST_DIR / "完整候選股清單_完整版.md"
SUMMARY_CN_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
FULL_CN_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

PACKET_LATEST_OLD = LATEST_DIR / "CHATGPT_DAILY_REPORT_PACKET.txt"
PACKET_LATEST = LATEST_DIR / "chatgpt_daily_report_packet_latest.txt"
PACKET_MANIFEST = LATEST_DIR / "chatgpt_daily_report_packet_manifest.json"


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_date(value: Any) -> str:
    if value is None:
        return ""

    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass

    text = str(value).strip()
    digits = re.sub(r"[^0-9]", "", text)

    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]

    return ""


def safe_read_text(path: Path) -> str:
    if not path.exists():
        return ""

    for enc in ["utf-8", "utf-8-sig", "cp950"]:
        try:
            return path.read_text(encoding=enc)
        except Exception:
            pass

    return ""


def safe_copy(src: Path, dst: Path) -> bool:
    if not src.exists():
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    return True


def raw_url(path: Path, ref: str = "main") -> str:
    return f"https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/{ref}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    elif path.as_posix().startswith("output/latest/"):
        rel = path.relative_to("output").as_posix()
    else:
        rel = path.as_posix()
    return f"https://LeoChen0727.github.io/tdcc-weekly-report/{rel}"


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    return {}


def extract_data_freshness() -> dict[str, Any]:
    result = {
        "main_price_date": "",
        "report_ready": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "stock_monitor_date": "",
        "warrant_flow_date": "",
        "report_ready_note": "",
    }

    if DATA_FRESHNESS_CSV.exists():
        try:
            df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str)
            if not df.empty:
                row = df.iloc[0].to_dict()
                result["main_price_date"] = normalize_date(row.get("main_price_date", ""))
                result["report_ready"] = str(row.get("report_ready", "")).strip()
                result["all_candidates_date"] = normalize_date(row.get("all_candidates_date", ""))
                result["official_price_fetch_date"] = normalize_date(row.get("official_price_fetch_date", ""))
                result["stock_monitor_date"] = normalize_date(row.get("stock_monitor_price_date", ""))
                result["warrant_flow_date"] = normalize_date(row.get("warrant_flow_date", ""))
                result["report_ready_note"] = str(row.get("report_ready_note", "")).strip()
                return result
        except Exception:
            pass

    text = safe_read_text(DATA_FRESHNESS_MD)

    m = re.search(r"主資料日期[：:\s`]*([0-9/\-]{8,10})", text)
    if m:
        result["main_price_date"] = normalize_date(m.group(1))

    m = re.search(r"是否可產出正式每日報告[：:\s`]*(True|False|true|false)", text)
    if m:
        result["report_ready"] = m.group(1)

    return result


def extract_main_meta() -> dict[str, Any]:
    freshness = extract_data_freshness()
    manifest = read_json(REPORT_MANIFEST_JSON)

    main_date = (
        normalize_date(manifest.get("main_price_date", ""))
        or normalize_date(manifest.get("price_date", ""))
        or normalize_date(manifest.get("date", ""))
        or freshness.get("main_price_date", "")
    )

    report_ready = (
        str(manifest.get("report_ready", "")).strip()
        or str(manifest.get("ready", "")).strip()
        or freshness.get("report_ready", "")
    )

    if not main_date:
        main_date = now_taipei().strftime("%Y%m%d")

    if not report_ready:
        report_ready = "False"

    return {
        "main_price_date": main_date,
        "report_ready": report_ready,
        "freshness": freshness,
        "manifest": manifest,
    }


def ensure_dated_artifacts(main_date: str) -> dict[str, Path]:
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    dated_summary_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.md"
    dated_full_md = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.md"
    dated_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_summary.pdf"
    dated_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full.pdf"

    dated_summary_cn_md = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.md"
    dated_full_cn_md = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版.md"
    dated_summary_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.pdf"
    dated_full_cn_pdf = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版表格.pdf"

    safe_copy(SUMMARY_LATEST_MD, dated_summary_md)
    safe_copy(FULL_LATEST_MD, dated_full_md)
    safe_copy(SUMMARY_LATEST_PDF, dated_summary_pdf)
    safe_copy(FULL_LATEST_PDF, dated_full_pdf)

    safe_copy(SUMMARY_CN_MD, dated_summary_cn_md)
    safe_copy(FULL_CN_MD, dated_full_cn_md)
    safe_copy(SUMMARY_CN_PDF, dated_summary_cn_pdf)
    safe_copy(FULL_CN_PDF, dated_full_cn_pdf)

    return {
        "dated_summary_md": dated_summary_md,
        "dated_full_md": dated_full_md,
        "dated_summary_pdf": dated_summary_pdf,
        "dated_full_pdf": dated_full_pdf,
        "dated_summary_cn_md": dated_summary_cn_md,
        "dated_full_cn_md": dated_full_cn_md,
        "dated_summary_cn_pdf": dated_summary_cn_pdf,
        "dated_full_cn_pdf": dated_full_cn_pdf,
    }


def build_packet_text(main_date: str, report_ready: str, paths: dict[str, Path], meta: dict[str, Any]) -> str:
    summary_text = safe_read_text(SUMMARY_LATEST_MD)
    full_text = safe_read_text(FULL_LATEST_MD)
    freshness = meta.get("freshness", {})
    report_manifest = read_json(REPORT_MANIFEST_JSON)
    kline_status = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)
    curated_pdf = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf = fixed_pdf_manifest.get("full_table_pdf", {})

    history_packet_path = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    lines: list[str] = []

    lines.append("CHATGPT DAILY REPORT PACKET")
    lines.append("")
    lines.append(f"generated_at: {now_text()}")
    lines.append("repo: LeoChen0727/tdcc-weekly-report")
    lines.append(f"main_price_date: {main_date}")
    lines.append(f"report_ready: {report_ready}")
    lines.append(f"all_candidates_date: {freshness.get('all_candidates_date', '')}")
    lines.append(f"official_price_fetch_date: {freshness.get('official_price_fetch_date', '')}")
    lines.append(f"stock_monitor_date: {freshness.get('stock_monitor_date', '')}")
    lines.append(f"warrant_flow_date: {freshness.get('warrant_flow_date', '')}")
    lines.append("")
    lines.append("PACKET_PATHS")
    lines.append(f"latest_packet_path: {PACKET_LATEST.as_posix()}")
    lines.append(f"history_packet_path: {history_packet_path.as_posix()}")
    lines.append("")
    lines.append("SUMMARY_PDF_KLINE_STATUS")
    lines.append(f"summary_pdf_path: {SUMMARY_LATEST_PDF.as_posix()}")
    lines.append(f"summary_pdf_kline_policy: {kline_status.get('policy') or report_manifest.get('summary_pdf_kline_policy', 'local_price_redraw_first')}")
    lines.append(f"summary_pdf_kline_status: {kline_status.get('status') or report_manifest.get('summary_pdf_kline_status', '')}")
    lines.append(f"summary_pdf_kline_output_dir: {kline_status.get('pdf_kline_output_dir') or report_manifest.get('summary_pdf_kline_output_dir', 'output/latest/charts/pdf_kline')}")
    lines.append(f"summary_pdf_kline_total_charts: {kline_status.get('total_charts', report_manifest.get('summary_pdf_kline_total_charts', 0))}")
    lines.append(f"summary_pdf_kline_local_price_redraw_count: {kline_status.get('local_price_redraw_count', report_manifest.get('summary_pdf_kline_local_price_redraw_count', 0))}")
    lines.append(f"summary_pdf_kline_chart_path_fallback_count: {kline_status.get('chart_path_fallback_count', report_manifest.get('summary_pdf_kline_chart_path_fallback_count', 0))}")
    lines.append(f"summary_pdf_kline_missing_count: {kline_status.get('missing_count', report_manifest.get('summary_pdf_kline_missing_count', 0))}")
    lines.append(f"summary_pdf_kline_status_md_path: {PDF_KLINE_STATUS_MD.as_posix()}")
    lines.append("summary_pdf_chart_path_and_chart_url_are_fallback_only: True")
    lines.append("do_not_label_summary_pdf_as_chart_path_version_or_image_download_failed: True")
    lines.append("note: The summary PDF K-line charts are generated by the pipeline from local/repo daily price data first. Candidate chart_path/chart_url values are fallback references only.")
    lines.append("")
    lines.append("CURATED PDF REPORT")
    lines.append(f"pages_url: {curated_pdf.get('pages_url') or pages_url(Path('docs/latest/daily_market_curated_report_latest.pdf'))}")
    lines.append(f"raw_url: {curated_pdf.get('raw_url') or raw_url(CURATED_REPORT_PDF)}")
    lines.append(f"file_path: {curated_pdf.get('file_path') or CURATED_REPORT_PDF.as_posix()}")
    lines.append(f"generated_at: {fixed_pdf_manifest.get('generated_at', '')}")
    lines.append(f"status: {curated_pdf.get('status') or ('generated' if CURATED_REPORT_PDF.exists() else 'missing')}")
    lines.append("")
    lines.append("FULL TABLE PDF REPORT")
    lines.append(f"pages_url: {full_table_pdf.get('pages_url') or pages_url(Path('docs/latest/daily_market_full_table_report_latest.pdf'))}")
    lines.append(f"raw_url: {full_table_pdf.get('raw_url') or raw_url(FULL_TABLE_REPORT_PDF)}")
    lines.append(f"file_path: {full_table_pdf.get('file_path') or FULL_TABLE_REPORT_PDF.as_posix()}")
    lines.append(f"generated_at: {fixed_pdf_manifest.get('generated_at', '')}")
    lines.append(f"status: {full_table_pdf.get('status') or ('generated' if FULL_TABLE_REPORT_PDF.exists() else 'missing')}")
    lines.append("")
    lines.append("FIXED PDF VALIDATION")
    lines.append(f"status: {fixed_pdf_validation.get('status', '')}")
    lines.append(f"validation_json_path: {FIXED_PDF_VALIDATION_JSON.as_posix()}")
    lines.append(f"validation_md_path: output/latest/daily_market_report_validation_latest.md")
    lines.append("")
    lines.append("SIGNAL PERFORMANCE TRACKING")
    lines.append(f"signal_log_path: {DAILY_SIGNAL_LOG.as_posix()}")
    lines.append(f"performance_csv_path: {DAILY_SIGNAL_PERFORMANCE.as_posix()}")
    lines.append(f"summary_latest_raw_url: {raw_url(DAILY_SIGNAL_SUMMARY_MD)}")
    lines.append(f"weekly_report_pdf_pages_url: {pages_url(Path('docs/latest/daily_signal_performance_weekly_latest.pdf'))}")
    lines.append(f"monthly_report_pdf_pages_url: {pages_url(Path('docs/latest/daily_signal_performance_monthly_latest.pdf'))}")
    lines.append(f"last_updated_at: {now_text()}")
    lines.append(f"status: {'generated' if DAILY_SIGNAL_LOG.exists() and DAILY_SIGNAL_PERFORMANCE.exists() else 'missing'}")
    lines.append("")
    chip_flow_status = read_json(CHIP_FLOW_STATUS_JSON)
    lines.append("CHIP FLOW POSITIVE STREAK")
    lines.append(f"definition: main_force_net_lots - institutional_net_lots - eight_banks_net_lots > 0 for 3 consecutive trading days")
    lines.append(f"status: {chip_flow_status.get('status', 'missing')}")
    lines.append(f"reason: {chip_flow_status.get('reason', '')}")
    lines.append(f"latest_csv_raw_url: {raw_url(CHIP_FLOW_STREAK_CSV)}")
    lines.append(f"latest_md_raw_url: {raw_url(CHIP_FLOW_STREAK_MD)}")
    lines.append(f"status_json_raw_url: {raw_url(CHIP_FLOW_STATUS_JSON)}")
    lines.append(f"institutional_flow_raw_url: {raw_url(INSTITUTIONAL_FLOW_CSV)}")
    lines.append("broker_branch_data_required: True")
    lines.append("do_not_infer_if_status_not_ready: True")
    lines.append("")
    lines.append("WARRANT MARKET ANALYSIS")
    lines.append(f"market_report_md_raw_url: {raw_url(WARRANT_MARKET_MD)}")
    lines.append(f"market_report_pdf_pages_url: {pages_url(Path('docs/latest/warrant_market_report_latest.pdf'))}")
    lines.append(f"market_report_pdf_raw_url: {raw_url(WARRANT_MARKET_PDF)}")
    lines.append(f"flow_by_stock_csv_raw_url: {raw_url(WARRANT_FLOW_BY_STOCK_CSV)}")
    lines.append(f"sector_heat_csv_raw_url: {raw_url(WARRANT_SECTOR_HEAT_CSV)}")
    lines.append(f"signal_performance_md_raw_url: {raw_url(WARRANT_SIGNAL_PERFORMANCE_MD)}")
    lines.append(f"status: {'generated' if WARRANT_MARKET_MD.exists() and WARRANT_FLOW_BY_STOCK_CSV.exists() else 'missing'}")
    lines.append("note: Warrant flow is an auxiliary signal only, not a standalone buy reason.")
    lines.append("")
    lines.append("PURPOSE")
    lines.append("This packet embeds the daily market report content directly.")
    lines.append("If ChatGPT cannot read GitHub raw/latest/MD/PDF files, paste this packet into the daily report conversation.")
    lines.append("Do not recreate this report from stale older files.")
    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED SUMMARY REPORT")
    lines.append("=" * 80)
    lines.append("")

    if summary_text.strip():
        lines.append(summary_text)
    else:
        lines.append("[daily_market_summary_latest.md missing or empty]")

    lines.append("")
    lines.append("=" * 80)
    lines.append("EMBEDDED FULL REPORT")
    lines.append("=" * 80)
    lines.append("")

    if full_text.strip():
        lines.append(full_text)
    else:
        lines.append("[daily_market_full_latest.md missing or empty]")

    lines.append("")
    lines.append("=" * 80)
    lines.append("END OF PACKET")
    lines.append("=" * 80)
    lines.append("")

    return "\n".join(lines)


def write_packet_manifest(main_date: str, report_ready: str, paths: dict[str, Path]) -> None:
    history_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"
    report_manifest = read_json(REPORT_MANIFEST_JSON)
    kline_status = read_json(PDF_KLINE_STATUS_JSON).get("summary", {})
    fixed_pdf_manifest = read_json(FIXED_PDF_MANIFEST_JSON)
    fixed_pdf_validation = read_json(FIXED_PDF_VALIDATION_JSON)
    curated_pdf = fixed_pdf_manifest.get("curated_pdf", {})
    full_table_pdf = fixed_pdf_manifest.get("full_table_pdf", {})

    manifest = {
        "generated_at": now_text(),
        "main_price_date": main_date,
        "report_ready": report_ready,
        "summary_pdf_kline_policy": kline_status.get("policy") or report_manifest.get("summary_pdf_kline_policy", "local_price_redraw_first"),
        "summary_pdf_kline_status": kline_status.get("status") or report_manifest.get("summary_pdf_kline_status", ""),
        "summary_pdf_kline_total_charts": kline_status.get("total_charts", report_manifest.get("summary_pdf_kline_total_charts", 0)),
        "summary_pdf_kline_local_price_redraw_count": kline_status.get("local_price_redraw_count", report_manifest.get("summary_pdf_kline_local_price_redraw_count", 0)),
        "summary_pdf_kline_chart_path_fallback_count": kline_status.get("chart_path_fallback_count", report_manifest.get("summary_pdf_kline_chart_path_fallback_count", 0)),
        "summary_pdf_kline_missing_count": kline_status.get("missing_count", report_manifest.get("summary_pdf_kline_missing_count", 0)),
        "summary_pdf_kline_status_md_path": PDF_KLINE_STATUS_MD.as_posix(),
        "daily_market_curated_pdf_pages_url": curated_pdf.get("pages_url") or pages_url(Path("docs/latest/daily_market_curated_report_latest.pdf")),
        "daily_market_curated_pdf_raw_url": curated_pdf.get("raw_url") or raw_url(CURATED_REPORT_PDF),
        "daily_market_curated_pdf_path": curated_pdf.get("file_path") or CURATED_REPORT_PDF.as_posix(),
        "daily_market_full_table_pdf_pages_url": full_table_pdf.get("pages_url") or pages_url(Path("docs/latest/daily_market_full_table_report_latest.pdf")),
        "daily_market_full_table_pdf_raw_url": full_table_pdf.get("raw_url") or raw_url(FULL_TABLE_REPORT_PDF),
        "daily_market_full_table_pdf_path": full_table_pdf.get("file_path") or FULL_TABLE_REPORT_PDF.as_posix(),
        "fixed_pdf_validation_status": fixed_pdf_validation.get("status", ""),
        "daily_signal_log_path": DAILY_SIGNAL_LOG.as_posix(),
        "daily_signal_performance_csv_path": DAILY_SIGNAL_PERFORMANCE.as_posix(),
        "daily_signal_performance_summary_raw_url": raw_url(DAILY_SIGNAL_SUMMARY_MD),
        "daily_signal_performance_weekly_pdf_pages_url": pages_url(Path("docs/latest/daily_signal_performance_weekly_latest.pdf")),
        "daily_signal_performance_monthly_pdf_pages_url": pages_url(Path("docs/latest/daily_signal_performance_monthly_latest.pdf")),
        "daily_signal_performance_status": "generated" if DAILY_SIGNAL_LOG.exists() and DAILY_SIGNAL_PERFORMANCE.exists() else "missing",
        "latest_packet_path": PACKET_LATEST.as_posix(),
        "latest_packet_raw_url_main": raw_url(PACKET_LATEST, ref="main"),
        "legacy_latest_packet_path": PACKET_LATEST_OLD.as_posix(),
        "history_packet_path": history_packet.as_posix(),
        "history_packet_raw_url_main": raw_url(history_packet, ref="main"),
        "dated_summary_md_path": paths["dated_summary_md"].as_posix(),
        "dated_full_md_path": paths["dated_full_md"].as_posix(),
        "dated_summary_pdf_path": paths["dated_summary_pdf"].as_posix(),
        "dated_full_pdf_path": paths["dated_full_pdf"].as_posix(),
    }

    PACKET_MANIFEST.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    meta = extract_main_meta()
    main_date = meta["main_price_date"]
    report_ready = str(meta["report_ready"])

    paths = ensure_dated_artifacts(main_date)

    packet_text = build_packet_text(
        main_date=main_date,
        report_ready=report_ready,
        paths=paths,
        meta=meta,
    )

    history_packet = HISTORY_REPORT_DIR / f"{main_date}_CHATGPT_DAILY_REPORT_PACKET.txt"

    PACKET_LATEST.write_text(packet_text, encoding="utf-8")
    PACKET_LATEST_OLD.write_text(packet_text, encoding="utf-8")
    history_packet.write_text(packet_text, encoding="utf-8")

    write_packet_manifest(main_date, report_ready, paths)

    print(f"Saved: {PACKET_LATEST}")
    print(f"Saved: {PACKET_LATEST_OLD}")
    print(f"Saved: {history_packet}")
    print(f"Saved: {PACKET_MANIFEST}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
