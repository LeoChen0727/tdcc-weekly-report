from __future__ import annotations

import argparse
import math
import os
import re
import textwrap
import urllib.request
from io import StringIO
from datetime import datetime
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image,
    CondPageBreak,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

try:
    from scripts.resolve_daily_report_source_state import resolve_daily_report_source_state
except ImportError:  # pragma: no cover - script execution from scripts/
    from resolve_daily_report_source_state import resolve_daily_report_source_state


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_REPO = SCRIPT_DIR.parents[0]


def env_path(name: str, default: Path) -> Path:
    value = os.environ.get(name)
    if not value:
        return default
    return Path(value).expanduser().resolve()


REPO = env_path("CHATGPT_DAILY_REPO_ROOT", DEFAULT_REPO)
LATEST = REPO / "output" / "latest"
DATA = REPO / "data"
OUT = env_path("CHATGPT_DAILY_OUTPUT_DIR", REPO / "chatgpt_side_outputs")
CHARTS = OUT / "charts"
TDCC_WINDOW_DIRS = [
    LATEST / "individual_stock_reports" / "tdcc_windows",
    REPO / "docs" / "latest" / "individual_stock_reports" / "tdcc_windows",
]
REMOTE_README: dict[str, str] = {}
REMOTE_LATEST_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest"
REMOTE_DATA_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data"
VOLUME_BREAKOUT_MODEL_ID = "volume_range_breakout"
W_BOTTOM_RIGHT_SIDE_MODEL_ID = "w_bottom_right_side"
W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID = "neckline_volume_breakout_confirmation"
PRICE_PULLBACK_MODEL_ID = "price_pullback_23ema"
PDF_PRESENTATION_MODEL_ORDER_OVERRIDES = {
    VOLUME_BREAKOUT_MODEL_ID: 1.0,
    W_BOTTOM_RIGHT_SIDE_MODEL_ID: 1.1,
    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID: 1.2,
    PRICE_PULLBACK_MODEL_ID: 1.3,
}
VOLUME_OPERATION_HIGHLIGHT_LIMITS = {
    "confirmed_operation": 10,
    "active_operation": 5,
}
W_BOTTOM_OPERATION_HIGHLIGHT_LIMITS = {
    "confirmed_operation": 10,
    "active_operation": 5,
}
W_BOTTOM_OPERATION_TABLE_MODEL_IDS = {
    W_BOTTOM_RIGHT_SIDE_MODEL_ID,
    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID,
}
OPERATION_TABLE_MODEL_IDS = {
    VOLUME_BREAKOUT_MODEL_ID,
    W_BOTTOM_RIGHT_SIDE_MODEL_ID,
    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID,
    PRICE_PULLBACK_MODEL_ID,
}
W_BOTTOM_OPERATION_INPUT_KEYS = {
    W_BOTTOM_RIGHT_SIDE_MODEL_ID: "w_bottom_right_side_operation",
    W_BOTTOM_NECKLINE_BREAKOUT_MODEL_ID: "w_bottom_neckline_operation",
}
PRICE_PULLBACK_OPERATION_INPUT_KEY = "price_pullback_operation"
W_BOTTOM_OPERATION_REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "row_type",
    "display_order",
    "operation_asof_date",
    "report_line",
    "report_line_memberships",
    "operation_status",
    "row_action_status",
    "buy_rank_eligible",
}
PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS = W_BOTTOM_OPERATION_REQUIRED_COLUMNS | {
    "stock_display",
    "operation_quality_zh",
    "operation_status_zh",
    "signal_date",
    "entry_basis_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "technical_package_win_rate_zh",
    "technical_package_neutral_rate_zh",
    "technical_package_failure_rate_zh",
    "technical_package_avg_return_zh",
    "operation_age_days",
    "rank_reason_zh",
    "risk_tags_zh",
}
OPERATION_HIGHLIGHT_TABLE_CONTRACT = "confirmed_buy_then_active_only"
DAILY_HIGHLIGHT_LAYOUT_CONTRACT = "legacy_volume_first"
DAILY_HIGHLIGHT_MODEL_ORDER_POLICY = "program_side_order"
DAILY_HIGHLIGHT_DESCRIPTION_POLICY = "program_side_non_volume"
MODEL_EMPTY_STATE_TEXT = "本日無股票推薦"
OPERATION_CONFIRMED_BUY_TABLE_TITLE = "本日可買 / 已確認買入候選"
OPERATION_ACTIVE_TABLE_TITLE = "操作中"
OPERATION_ACTIVE_EMPTY_STATE_TEXT = "目前無操作中追蹤列"
MODEL_PDF_VISIBILITIES = {"pdf_core_model", "pdf_specialty_section"}
VOLUME_TRIGGER_LABELS = {
    "pullback_5ma_confirmed": "回測 5 日線後站回",
    "next_day_break_signal_high_confirmed": "隔日突破訊號高點",
    "next_day_continuation_confirmed": "隔日續強確認",
    "pullback_10ma_confirmed": "回測 10 日線後站回",
}
VOLUME_ENTRY_RULE_LABELS = {
    "confirmation_next_open": "確認後下一交易日開盤",
    "pending_confirmation": "尚未確認，不列進場價",
}
VOLUME_STOP_RULE_LABELS = {
    "signal_low_stop": "跌破停損基準",
    "signal_low_stop_after_confirmation": "尚未確認，不列停損價",
}
VOLUME_EXIT_RULE_LABELS = {
    "signal_low_stop_or_fixed_10d_close": "跌破停損基準，否則最多第 10 個交易日收盤",
}

REQUEST_DATE = ""
OUTPUT_SUFFIX = "_current_rules"

FONT_NAME = "DFKai"
FONT_BOLD = "DFKai-Bold"
FONT_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
FONT_BOLD_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
MATPLOTLIB_FONT: FontProperties | None = None
TDCC_WINDOW_CACHE: dict[str, pd.Series] = {}
SOURCE_STATE: dict[str, object] = {}

MAIN_REPORT_MAINSTREAM_LIMIT = 8
MAIN_REPORT_NON_MAINSTREAM_LIMIT = 2
PATTERN_SUBTYPE_MAIN_LIMIT = 5
PATTERN_SUBTYPE_NON_LIMIT = 2
PATTERN_SUBTYPE_OPERATION_LIMIT = 6
FRONT_MAINSTREAM_LIMIT = 8
FRONT_NON_MAINSTREAM_LIMIT = 2
FULL_REPORT_MAINSTREAM_LIMIT = 12
FULL_REPORT_NON_MAINSTREAM_LIMIT = 4
MODEL_SECTION_MIN_ROOM = 58 * mm
MODEL_SUBSECTION_MIN_ROOM = 42 * mm
CHATGPT_SIDE_KLINE_DAYS = 126


def append_page_break_once(story: list) -> None:
    if story and isinstance(story[-1], PageBreak):
        return
    story.append(PageBreak())


def highlight_specs_in_layout_order(specs: list[pd.Series]) -> list[pd.Series]:
    if DAILY_HIGHLIGHT_MODEL_ORDER_POLICY == "program_side_order":
        return list(specs)
    raise ValueError(f"unsupported daily highlight model order policy: {DAILY_HIGHLIGHT_MODEL_ORDER_POLICY}")


def should_render_highlight_model_description(model_id: str) -> bool:
    if DAILY_HIGHLIGHT_DESCRIPTION_POLICY == "program_side_non_volume":
        return model_id != VOLUME_BREAKOUT_MODEL_ID
    if DAILY_HIGHLIGHT_DESCRIPTION_POLICY == "none":
        return False
    raise ValueError(f"unsupported daily highlight description policy: {DAILY_HIGHLIGHT_DESCRIPTION_POLICY}")


def read_readme_value(key: str, default: str = "") -> str:
    if REMOTE_README.get(key):
        return REMOTE_README[key]
    path = LATEST / "READ_ME_FIRST_DAILY_REPORT.txt"
    if not path.exists():
        return default
    prefix = f"{key}="
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        if line.startswith(prefix):
            return line.split("=", 1)[1].strip()
    return default


def warrant_pdf_hidden() -> bool:
    visibility = str(SOURCE_STATE.get("warrant_pdf_visibility") or read_readme_value("warrant_pdf_visibility")).strip()
    ready = str(SOURCE_STATE.get("warrant_ready") or read_readme_value("warrant_ready")).strip().lower()
    return visibility in {"hidden_unavailable", "blocked_unavailable"} or ready == "false"


def warrant_unavailable_note() -> str:
    note = read_readme_value("warrant_source_status_note") or read_readme_value("warrant_ready_note")
    status = read_readme_value("warrant_source_status")
    visibility = read_readme_value("warrant_pdf_visibility")
    return (
        "本日權證資料未更新；正式 PDF 略過權證金流表格與權證輔助判讀，"
        "不得使用舊權證資料作為候選股加分、降級或買賣依據。"
        f" status={status or 'unknown'}, visibility={visibility or 'hidden_unavailable'}, note={note or 'unavailable'}"
    )


def fetch_text_no_cache(url: str) -> str:
    cache_buster = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
    sep = "&" if "?" in url else "?"
    request = urllib.request.Request(
        f"{url}{sep}cb={cache_buster}",
        headers={
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "chatgpt-side-daily-report-generator",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def enforce_fresh_repo_data() -> None:
    global DATA_DATE, DATA_DATE_SLASH, REQUEST_DATE, REQUEST_DATE_SLASH, REMOTE_README, SOURCE_STATE

    source_ref = os.environ.get("CHATGPT_DAILY_SOURCE_REF", "origin/main")
    source_state = resolve_daily_report_source_state(REPO, source_ref=source_ref)
    SOURCE_STATE = source_state
    remote = source_state["readme_fields"]
    remote_date = source_state["main_price_date"]

    REMOTE_README = remote
    DATA_DATE = remote_date
    DATA_DATE_SLASH = date_slash(DATA_DATE)
    REQUEST_DATE = remote_date
    REQUEST_DATE_SLASH = DATA_DATE_SLASH


def date_slash(value: str) -> str:
    try:
        dt = datetime.strptime(value, "%Y%m%d")
    except ValueError:
        return value
    return f"{dt.year}/{dt.month}/{dt.day}"


DATA_DATE = ""
DATA_DATE_SLASH = ""
REQUEST_DATE_SLASH = ""


def setup_fonts() -> None:
    global FONT_NAME, FONT_BOLD, MATPLOTLIB_FONT
    try:
        if FONT_PATH.exists():
            try:
                pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH), subfontIndex=0))
            except TypeError:
                pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT_PATH)))
            if FONT_BOLD_PATH.exists():
                try:
                    pdfmetrics.registerFont(TTFont(FONT_BOLD, str(FONT_BOLD_PATH), subfontIndex=0))
                except TypeError:
                    pdfmetrics.registerFont(TTFont(FONT_BOLD, str(FONT_BOLD_PATH)))
            else:
                FONT_BOLD = FONT_NAME
            MATPLOTLIB_FONT = FontProperties(fname=str(FONT_PATH))
            plt.rcParams["font.sans-serif"] = ["DFKai-SB", "Microsoft JhengHei", "Arial Unicode MS", "DejaVu Sans"]
            plt.rcParams["axes.unicode_minus"] = False
            return
    except Exception:
        pass

    FONT_NAME = "MSung-Light"
    FONT_BOLD = "MSung-Light"
    pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))
    MATPLOTLIB_FONT = None
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "Arial Unicode MS", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False


setup_fonts()


styles = getSampleStyleSheet()
BODY = ParagraphStyle(
    "BodyCJK",
    parent=styles["BodyText"],
    fontName=FONT_NAME,
    fontSize=12,
    leading=15,
    wordWrap="CJK",
    alignment=TA_LEFT,
)
BODY_SMALL = ParagraphStyle(
    "BodySmallCJK",
    parent=BODY,
    fontSize=12,
    leading=15,
)
BODY_TINY = ParagraphStyle(
    "BodyTinyCJK",
    parent=BODY,
    fontSize=12,
    leading=15,
)
SUMMARY_CELL = ParagraphStyle(
    "SummaryCellCJK",
    parent=BODY,
    fontName=FONT_NAME,
    fontSize=14,
    leading=15.5,
    wordWrap="CJK",
    alignment=TA_LEFT,
)
SUMMARY_HEADER = ParagraphStyle(
    "SummaryHeaderCJK",
    parent=SUMMARY_CELL,
    fontName=FONT_BOLD,
    textColor=colors.white,
    alignment=TA_CENTER,
)
TITLE = ParagraphStyle(
    "TitleCJK",
    parent=styles["Title"],
    fontName=FONT_BOLD,
    fontSize=22,
    leading=27,
    alignment=TA_CENTER,
)
H1 = ParagraphStyle(
    "H1CJK",
    parent=styles["Heading1"],
    fontName=FONT_BOLD,
    fontSize=18,
    leading=22,
    spaceBefore=7,
    spaceAfter=4,
    textColor=colors.HexColor("#c00000"),
)
H2 = ParagraphStyle(
    "H2CJK",
    parent=styles["Heading2"],
    fontName=FONT_BOLD,
    fontSize=15,
    leading=18.5,
    spaceBefore=5,
    spaceAfter=3,
    textColor=colors.HexColor("#c00000"),
)
OP_LABEL = ParagraphStyle(
    "OperationLabelCJK",
    parent=BODY_SMALL,
    fontName=FONT_BOLD,
    fontSize=12,
    leading=14.5,
    textColor=colors.HexColor("#c00000"),
    alignment=TA_CENTER,
)
OP_VALUE = ParagraphStyle(
    "OperationValueCJK",
    parent=BODY_SMALL,
    fontSize=12,
    leading=14.5,
    wordWrap="CJK",
)
CENTER = ParagraphStyle(
    "CenterCJK",
    parent=BODY,
    alignment=TA_CENTER,
)


def remote_latest_url(filename: str) -> str:
    return f"{REMOTE_LATEST_BASE}/{filename}"


def remote_data_url(filename: str) -> str:
    return f"{REMOTE_DATA_BASE}/{filename}"


def read_csv(path: Path | str, **kwargs) -> pd.DataFrame:
    kwargs.setdefault("encoding", "utf-8-sig")
    kwargs.setdefault("low_memory", False)
    if isinstance(path, str) and path.startswith(("http://", "https://")):
        text = fetch_text_no_cache(path)
        if not text.strip():
            return pd.DataFrame()
        df = pd.read_csv(StringIO(text), **kwargs)
    else:
        file_path = Path(path)
        if not file_path.exists():
            return pd.DataFrame()
        df = pd.read_csv(file_path, **kwargs)
    for col in ("stock_id", "signal_date", "date"):
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace(r"\.0$", "", regex=True)
    return df


def read_latest_csv(filename: str, **kwargs) -> pd.DataFrame:
    return read_csv(LATEST / filename, **kwargs)


MAINSTREAM_CURATED_TITLE = "\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
MAINSTREAM_FULL_TITLE = "\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
NON_MAINSTREAM_CURATED_TITLE = "\u975e\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
NON_MAINSTREAM_FULL_TITLE = "\u975e\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
MAINSTREAM_LINE_LABEL = "\u4e3b\u6d41\u80a1"
NON_MAINSTREAM_LINE_LABEL = "\u975e\u4e3b\u6d41\u80a1"


def clean(value, default: str = "") -> str:
    if value is None:
        return default
    try:
        if isinstance(value, float) and math.isnan(value):
            return default
    except TypeError:
        pass
    s = str(value).strip()
    if s.lower() in {"nan", "none", "nat", "<na>"}:
        return default
    return s


CODE_REPLACEMENTS = [
    ("TDCC=strong_accumulation", "TDCC=籌碼強累積"),
    ("TDCC=mild_accumulation", "TDCC=籌碼溫和累積"),
    ("TDCC=distribution_warning", "TDCC=籌碼派發警示"),
    ("權證=call_strong_inflow", "權證=認購強流入"),
    ("權證=call_put_bullish", "權證=認購偏多"),
    ("權證=mixed_flow", "權證=多空混合"),
    ("權證=no_signal", "權證=無明確權證訊號"),
    ("warrant=call_strong_inflow", "權證=認購強流入"),
    ("strong_accumulation", "籌碼強累積"),
    ("mild_accumulation", "籌碼溫和累積"),
    ("distribution_warning", "籌碼派發警示"),
    ("call_strong_inflow", "認購強流入"),
    ("call_put_bullish", "認購偏多"),
    ("mixed_flow", "多空混合"),
    ("no_signal", "無明確訊號"),
    ("mainstream_follow_through_stock", "主流續強股"),
    ("mainstream_leader_stock", "主流領先股"),
    ("mainstream_follow_through", "主流續強"),
    ("mainstream_overheated", "短線漲幅或量能過熱，先不追"),
    ("mainstream_leader", "主流領先"),
    ("core_mainstream_theme", "核心主流族群"),
    ("non_mainstream_theme", "非主流族群"),
    ("core_mainstream_overheated", "核心主流但短線過熱"),
    ("non_mainstream_flow_active", "非主流輪動活躍"),
    ("non_mainstream_overheated", "非主流且短線過熱"),
    ("non_mainstream_single_name", "非主流單股訊號"),
    ("non_mainstream_flow_watch", "非主流輪動觀察"),
    ("individual_quality_watch", "個股條件觀察"),
    ("theme_status_missing", "資料不足"),
    ("single_name_signal", "單一個股訊號"),
    ("emerging_theme", "早期題材"),
    ("two_line_overlap", "主流與個股交集"),
    ("individual_tdcc_latent_watch", "個股籌碼潛伏"),
    ("individual_revenue_low_response_watch", "營收低反應個股"),
    ("watch_volume_theme", "放量觀察族群"),
    ("confirmed_volume_theme", "放量確認族群"),
    ("single_stock_volume_attack", "單股放量"),
    ("overheated_volume_theme", "量能過熱，先不追"),
    ("weak_or_non_mainstream_volume_watch", "弱勢或非主流放量"),
    ("revenue_breakout_low_response", "營收爆發低反應"),
    ("revenue_breakout_low_resp", "營收爆發低反應"),
    ("revenue_pullback", "營收成長回檔"),
    ("neckline_breakout", "頸線突破"),
    ("platform_right_side", "平台右側整理"),
    ("breakout_confirmed", "突破確認"),
    ("true_breakout", "有效突破"),
    ("platform_breakout", "平台突破"),
    ("range_rebound", "區間轉強"),
    ("pullback_rebound", "回檔轉強"),
    ("neckline/platform breakout", "頸線 / 平台突破"),
    ("neckline_challenge", "挑戰頸線"),
    ("upgrade only when risk checks pass", "通過風險檢查才升級"),
    ("priority_candidate", "優先候選"),
    ("close_above_ema23", "收盤站上23EMA"),
    ("macd_hist_pos", "MACD柱狀體轉正"),
    ("MACD histogram", "MACD柱狀體"),
    ("foreign_tx_futures_net_oi", "外資台指期未平倉淨口數"),
    ("foreign_futures_net_oi", "外資全部期貨未平倉"),
    ("market_regime", "市場狀態"),
    ("risk_level", "風險層級"),
    ("source_status", "資料狀態"),
    ("strong_bull", "強勢多頭"),
    ("high_risk", "高風險"),
]


def translate_codes(value: str) -> str:
    s = clean(value)
    for old, new in CODE_REPLACEMENTS:
        s = s.replace(old, new)
    s = s.replace("先不追", "觀察")
    return s


def first_text(*values, default: str = "") -> str:
    for value in values:
        s = clean(value)
        if s:
            return s
    return default


def short(value, limit: int = 62) -> str:
    s = translate_codes(clean(value))
    s = re.sub(r"\s+", " ", s)
    if len(s) <= limit:
        return s
    return s[: max(0, limit - 1)] + "…"


def para(value, style: ParagraphStyle = BODY_SMALL) -> Paragraph:
    s = translate_codes(clean(value, "資料不足 / 僅能觀察"))
    s = s.replace("；", " / ")
    escaped = (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )
    return Paragraph(escaped, style)


def table_para(value, style: ParagraphStyle = BODY_SMALL) -> Paragraph:
    s = translate_codes(clean(value, "資料不足 / 僅能觀察"))
    s = s.replace("；", " / ")
    placeholders = {
        "<font color=\"#c00000\">": "__RED_OPEN__",
        "</font>": "__RED_CLOSE__",
        "<br/>": "__BR__",
        "<br />": "__BR__",
    }
    for tag, token in placeholders.items():
        s = s.replace(tag, token)
    escaped = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br/>")
    escaped = (
        escaped.replace("__RED_OPEN__", "<font color=\"#c00000\">")
        .replace("__RED_CLOSE__", "</font>")
        .replace("__BR__", "<br/>")
    )
    return Paragraph(escaped, style)


def escape_html(value) -> str:
    s = translate_codes(clean(value))
    s = s.replace("；", " / ")
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def rich_para(markup: str, style: ParagraphStyle = SUMMARY_CELL) -> Paragraph:
    return Paragraph(markup, style)


def red(value) -> str:
    return f'<font color="#c00000">{escape_html(value)}</font>'


def num(value, ndigits: int = 2, suffix: str = "") -> str:
    s = clean(value)
    if not s:
        return ""
    try:
        n = float(str(s).replace(",", ""))
    except ValueError:
        return s
    if math.isnan(n):
        return ""
    if ndigits == 0:
        return f"{n:,.0f}{suffix}"
    return f"{n:,.{ndigits}f}{suffix}"


def signed_num(value, ndigits: int = 2, suffix: str = "") -> str:
    n = to_float(value)
    if n is None:
        return ""
    sign = "+" if n > 0 else ""
    return f"{sign}{n:,.{ndigits}f}{suffix}"


def to_float(value) -> float | None:
    s = clean(value)
    if not s:
        return None
    try:
        n = float(s.replace(",", ""))
    except ValueError:
        return None
    if math.isnan(n):
        return None
    return n


def stock_label(row: pd.Series) -> str:
    sid = stock_id_text(row.get("stock_id"))
    name = clean(row.get("stock_name"))
    return f"{sid} {name}".strip()


def stock_id_text(value) -> str:
    return re.sub(r"\.0$", "", clean(value))


def model_score_label(row: pd.Series) -> str:
    score = num(row.get("model_score"), 1)
    rank = clean(row.get("display_rank") or row.get("model_rank"))
    if rank and score:
        return f"#{rank} / {score}"
    if rank:
        return f"#{rank}"
    return score or "模型分數不足"


def model_risk_text(row: pd.Series, limit: int = 72) -> str:
    text = first_text(
        row.get("risk_tags_zh"),
        row.get("merged_risk_penalty_tags_zh"),
        row.get("risk_penalty_tags"),
        row.get("risk_tags"),
        row.get("downgrade_flags"),
        row.get("tdcc_risk_text_zh"),
    )
    return short(text, limit) if text else "未列明重大風險"


def model_source_text(row: pd.Series, limit: int = 72) -> str:
    text = first_text(
        row.get("score_components_zh"),
        row.get("merged_score_components"),
        row.get("score_components"),
        row.get("why_selected_human_zh"),
        row.get("why_selected_zh"),
        row.get("why_selected"),
    )
    return short(text, limit) if text else "模型命中條件已成立"


def category_display(category: str) -> str:
    return {
        "營收爆發低反應股": "營收爆發股價尚未反應股",
    }.get(category, category)


PATTERN_STAGE_LABELS = {
    "已突破但未過熱": "已突破待確認",
    "接近突破型": "接近突破",
    "預備發動型": "預備發動",
    "pullback_entry_zone": "回測支撐",
    "base_building": "築底整理",
    "platform_right_side": "平台右側",
    "early_entry_watch": "預備發動",
    "pullback_right_side": "回測支撐",
    "w_bottom_right_side": "W底右側",
    "neckline_challenge": "接近突破",
    "platform_breakout": "已突破待確認",
    "neckline_breakout": "已突破待確認",
    "breakout_confirmed": "已突破待確認",
    "true_breakout": "已突破待確認",
    "pattern_watch": "型態觀察",
    "no_pattern_stage": "",
}

PATTERN_SUBTYPE_ORDER = [
    "W底右側",
    "已突破待確認",
    "接近突破",
    "平台右側",
    "回測支撐",
    "預備發動",
    "築底整理",
    "型態待確認",
]


def truthy_value(value) -> bool:
    return clean(value).lower() in {"true", "1", "yes", "y", "是"}


def pattern_stage_label(
    row: pd.Series,
    prefer_w_bottom: bool = False,
    extra: pd.Series | None = None,
) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    if prefer_w_bottom and (
        truthy_value(row.get("w_bottom_right_side_flag")) or truthy_value(extra.get("w_bottom_right_side_flag"))
    ):
        return "W底右側"
    raw = first_text(row.get("pattern_stage"), row.get("pattern_route"), row.get("breakout_type"))
    if not raw:
        return ""
    if raw in PATTERN_STAGE_LABELS:
        return PATTERN_STAGE_LABELS[raw]
    text = translate_codes(raw)
    text = text.replace("neckline / platform breakout; 通過風險檢查才升級", "頸線 / 平台突破")
    return short(text, 18)


def category_stage_label(row: pd.Series, extra: pd.Series | None = None) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    category = category_display(clean(row.get("original_category_cn") or row.get("category_cn")))
    if "型態觀察" in category:
        stage = pattern_stage_label(row, prefer_w_bottom=True, extra=extra)
        return f"型態觀察：{stage or '型態待確認'}"
    stage = pattern_stage_label(row)
    if "嚴格突破" in category:
        return "突破成立" if is_strict_breakout_row(row) else stage or "突破確認"
    if "區間內轉強" in category:
        return stage or "挑戰壓力"
    if "回檔後短線轉強" in category:
        return stage or "回測轉強"
    return stage or category


LINE_GROUP_LABELS = {
    "individual_quality_watch": "個股條件觀察",
    "mainstream_leader_stock": "主流領先股",
    "mainstream_follow_through_stock": "主流續強股",
    "two_line_overlap": "主流 + 個股交集",
    "non_mainstream_flow_watch": "非主流輪動觀察",
    "individual_tdcc_latent_watch": "個股籌碼潛伏",
    "individual_revenue_low_response_watch": "營收低反應個股",
    "emerging_theme_watch": "早期題材觀察",
    "individual_pattern_watch": "個股型態觀察",
    "risk": "暫不列前排",
}

MAINSTREAM_SOURCE = "mainstream_theme_candidate"
LATENT_SOURCE = "latent_watch_candidate"
RISK_SOURCE = "risk_downgraded_candidate"
MAINSTREAM_THEME_STATUSES = {"mainstream_leader", "mainstream_follow_through"}
EARLY_OR_SINGLE_STATUSES = {"emerging_theme", "single_name_signal", "theme_status_missing", "non_mainstream"}
RISK_THEME_STATUSES = {"mainstream_overheated", "weak_theme", "failed_volume_theme", "overheated_volume_theme"}


THEME_STATUS_LABELS = {
    "mainstream_leader": "今日資金領先",
    "mainstream_follow_through": "今日資金續強",
    "mainstream_overheated": "短線漲幅或量能過熱，先不追",
    "emerging_theme": "早期題材",
    "single_name_signal": "單一個股訊號",
    "non_mainstream": "非主流",
    "theme_status_missing": "族群狀態不足",
}


STRUCTURAL_STATUS_LABELS = {
    "core_mainstream_theme": "核心主流族群",
    "non_mainstream_theme": "非主流族群",
    "theme_status_missing": "結構狀態不足",
}


MAINSTREAM_LABELS = {
    "core_mainstream_leader": "核心主流領先",
    "core_mainstream_follow_through": "核心主流續強",
    "core_mainstream_overheated": "核心主流但短線過熱",
    "non_mainstream_flow_active": "非主流輪動活躍",
    "non_mainstream_overheated": "非主流且短線過熱",
    "non_mainstream_single_name": "非主流單股訊號",
    "theme_status_missing": "程式標籤不足",
}


VOLUME_STATUS_LABELS = {
    "confirmed_volume_theme": "放量確認族群",
    "watch_volume_theme": "放量觀察族群",
    "early_mainstream_candidate": "早期主流候選",
    "single_stock_volume_attack": "單股放量",
    "non_mainstream_volume_watch": "非主流放量觀察",
    "weak_or_non_mainstream_volume_watch": "弱勢 / 非主流放量",
    "overheated_volume_theme": "量能過熱，先不追",
    "failed_volume_theme": "放量失敗",
    "theme_status_missing": "資料不足",
    "insufficient_data": "資料不足",
}


def zh_line_group(value) -> str:
    raw = clean(value, "theme_status_missing")
    return LINE_GROUP_LABELS.get(raw, raw)


def zh_theme_status(value) -> str:
    raw = clean(value, "theme_status_missing")
    return THEME_STATUS_LABELS.get(raw, raw)


def zh_structural_status(value) -> str:
    raw = clean(value, "theme_status_missing")
    return STRUCTURAL_STATUS_LABELS.get(raw, raw)


def zh_mainstream_label(value) -> str:
    raw = clean(value, "theme_status_missing")
    return MAINSTREAM_LABELS.get(raw, raw)


def zh_theme_name(value) -> str:
    raw = clean(value, "資料不足")
    return {"other": "其他", "TWSE": "整體上市"}.get(raw, raw)


TDCC_STATUS_LABELS = {
    "strong_accumulation": "籌碼強累積",
    "mild_accumulation": "籌碼溫和累積",
    "neutral": "籌碼中性",
    "weak": "籌碼偏弱",
    "distribution_warning": "籌碼派發警示",
    "no_data": "TDCC資料不足",
    "nan": "TDCC資料不足",
}


WARRANT_SIGNAL_LABELS = {
    "call_strong_inflow": "認購強流入",
    "call_put_bullish": "認購偏多",
    "mixed_flow": "多空混合",
    "no_signal": "無明確權證訊號",
    "put_strong_inflow": "認售偏空",
    "put_bearish": "認售偏空",
    "call_overheated": "認購權證過熱，先不追",
}


MARKET_REGIME_LABELS = {
    "strong_bull": "強勢多頭",
    "bull": "多頭",
    "neutral": "中性",
    "weak": "偏弱",
    "bear": "空頭",
}


RISK_LEVEL_LABELS = {
    "high_risk": "高風險",
    "medium_risk": "中風險",
    "low_risk": "低風險",
}


SOURCE_STATUS_LABELS = {
    "ready": "資料可用",
    "ok": "資料可用",
    "missing": "資料不足",
    "partial": "部分資料",
}


def zh_tdcc(value) -> str:
    raw = clean(value, "no_data")
    if raw in TDCC_STATUS_LABELS:
        return TDCC_STATUS_LABELS[raw]
    low = raw.lower()
    if "strong" in low and "accumulation" in low:
        return "籌碼強累積"
    if "mild" in low and "accumulation" in low:
        return "籌碼溫和累積"
    if "distribution" in low:
        return "籌碼派發警示"
    return raw


def series_value(row: pd.Series, extra: pd.Series, field: str):
    for src in (row, extra):
        if isinstance(src, pd.Series):
            value = src.get(field)
            if clean(value):
                return value
    return ""


def latest_tdcc_window_row(stock_id: str) -> pd.Series:
    sid = clean(stock_id)
    if not sid:
        return pd.Series(dtype=object)
    if sid in TDCC_WINDOW_CACHE:
        return TDCC_WINDOW_CACHE[sid]
    remote_template = REMOTE_README.get("individual_stock_tdcc_raw_url_template")
    if remote_template:
        remote_url = remote_template.replace("{stock_id}", sid)
        try:
            df = read_csv(remote_url, dtype=str)
        except Exception:
            df = pd.DataFrame()
        if not df.empty:
            TDCC_WINDOW_CACHE[sid] = df.tail(1).iloc[0]
            return TDCC_WINDOW_CACHE[sid]
    for folder in TDCC_WINDOW_DIRS:
        path = folder / f"{sid}_tdcc_window_latest.csv"
        if not path.exists():
            continue
        try:
            df = pd.read_csv(path, dtype=str, encoding="utf-8-sig")
        except Exception:
            continue
        if not df.empty:
            TDCC_WINDOW_CACHE[sid] = df.tail(1).iloc[0]
            return TDCC_WINDOW_CACHE[sid]
    TDCC_WINDOW_CACHE[sid] = pd.Series(dtype=object)
    return TDCC_WINDOW_CACHE[sid]


def tdcc_brief(row: pd.Series, extra: pd.Series | None = None) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    status = zh_tdcc(series_value(row, extra, "tdcc_status"))
    note = clean(series_value(row, extra, "tdcc_accumulation_note"))
    weeks = num(series_value(row, extra, "tdcc_weeks_used"), 0)
    c400 = signed_num(series_value(row, extra, "tdcc_400_change_sum"), 2)
    c1000 = signed_num(series_value(row, extra, "tdcc_1000_change_sum"), 2)
    parts = [status]
    if note:
        parts.append(note)
    if c400 or c1000:
        if weeks:
            parts.append(
                f"近{weeks}週大戶持股比率變化："
                f"400張以上{c400 or '資料不足'}百分點 / "
                f"1000張以上{c1000 or '資料不足'}百分點"
            )
        else:
            parts.append(
                "大戶持股比率變化："
                f"400張以上{c400 or '資料不足'}百分點 / "
                f"1000張以上{c1000 or '資料不足'}百分點"
            )
    return "；".join([p for p in parts if p]) or "TDCC資料不足"


def tdcc_direction(row: pd.Series, extra: pd.Series | None = None) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    raw = clean(series_value(row, extra, "tdcc_status")).lower()
    c400 = to_float(series_value(row, extra, "tdcc_400_change_sum"))
    c1000 = to_float(series_value(row, extra, "tdcc_1000_change_sum"))
    score = (c400 or 0) + (c1000 or 0)
    if "distribution" in raw:
        label = "強負向" if score < 0 else "負向"
    elif "strong_accumulation" in raw:
        label = "強正向"
    elif "mild_accumulation" in raw:
        label = "正向"
    elif score >= 1:
        label = "正向"
    elif score <= -1:
        label = "負向"
    else:
        label = "中性"
    return f"大戶籌碼：{label}"


def tdcc_detail(row: pd.Series, extra: pd.Series | None = None) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    sid = clean(series_value(row, extra, "stock_id"))
    parts = [tdcc_brief(row, extra)]
    weeks = num(series_value(row, extra, "tdcc_weeks_used"), 0)
    up400 = num(series_value(row, extra, "tdcc_400_up_weeks"), 0)
    up1000 = num(series_value(row, extra, "tdcc_1000_up_weeks"), 0)
    if weeks and (up400 or up1000):
        parts.append(f"近{weeks}週增加週數：400張以上{up400 or '0'}週、1000張以上{up1000 or '0'}週")

    latest = latest_tdcc_window_row(sid)
    ratio_parts = []
    for level in ("400", "600", "800", "1000"):
        ratio = num(latest.get(f"over_{level}_ratio"), 2, "%")
        change = signed_num(latest.get(f"over_{level}_change_1w"), 2, "百分點")
        if ratio:
            text = f"{level}張{ratio}"
            if change:
                text += f"(週變{change})"
            ratio_parts.append(text)
    if ratio_parts:
        parts.append("最新大戶比例：" + "、".join(ratio_parts))
    return "；".join([p for p in parts if p]) or "TDCC資料不足"


def zh_warrant(value) -> str:
    raw = clean(value, "no_signal")
    if raw in WARRANT_SIGNAL_LABELS:
        return WARRANT_SIGNAL_LABELS[raw]
    low = raw.lower()
    if "call" in low and ("strong" in low or "inflow" in low):
        return "認購流入"
    if "bull" in low:
        return "權證偏多"
    if "put" in low or "bear" in low:
        return "認售偏空"
    if "mixed" in low:
        return "多空混合"
    if "no_signal" in low:
        return "無明確權證訊號"
    return raw


def zh_market_regime(value) -> str:
    raw = clean(value, "資料不足")
    return MARKET_REGIME_LABELS.get(raw, raw)


def zh_risk_level(value) -> str:
    raw = clean(value, "資料不足")
    return RISK_LEVEL_LABELS.get(raw, raw)


def zh_source_status(value) -> str:
    raw = clean(value, "資料不足")
    return SOURCE_STATUS_LABELS.get(raw, raw)


def zh_market_reason(value) -> str:
    text = clean(value, "資料不足 / 僅能觀察")
    replacements = [
        ("TWSE strong bull", "上市指數強勢多頭"),
        ("TPEx strong bull", "上櫃指數強勢多頭"),
        ("TWSE bull", "上市指數多頭"),
        ("TPEx bull", "上櫃指數多頭"),
        ("Taiwan VIX elevated", "台灣 VIX 偏高"),
        ("Taiwan VIX panic-high", "台灣 VIX 極高"),
        ("Taiwan VIX", "台灣 VIX"),
        ("TXO put/call OI hedge high", "選擇權未平倉 P/C 避險偏高"),
        ("TXO put/call", "選擇權 P/C"),
        ("Foreign TX futures heavy net short", "外資台指期淨空單偏重"),
        ("Foreign TX futures net short", "外資台指期淨空"),
        ("Foreign TX futures", "外資台指期"),
        ("Retail MTX proxy net long watch", "散戶小台代理值偏多需留意"),
        ("Retail MTX proxy", "散戶小台代理值"),
        ("net long watch", "偏多需留意"),
        ("panic-high", "極高"),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    return text.replace("; ", "；")


def two_line_row(row: pd.Series, two_map: dict[str, pd.Series]) -> pd.Series:
    sid = clean(row.get("stock_id"))
    cat = clean(row.get("original_category_cn") or row.get("category_cn"))
    two = two_map.get((sid, cat))
    if two is None:
        two = two_map.get(sid, pd.Series(dtype=object))
    return two


def line_raw(row: pd.Series, two_map: dict[str, pd.Series]) -> tuple[str, str]:
    two = two_line_row(row, two_map)
    return (
        clean(two.get("candidate_line_group"), "theme_status_missing"),
        clean(two.get("theme_final_status"), "theme_status_missing"),
    )


def line_source(row: pd.Series, two_map: dict[str, pd.Series]) -> tuple[str, str, str, bool]:
    two = two_line_row(row, two_map)
    source = clean(two.get("candidate_source_type"), "source_missing")
    line = clean(two.get("candidate_line"), "分線資料不足")
    group = clean(two.get("candidate_line_group"), "theme_status_missing")
    overlap = clean(two.get("two_line_overlap_flag")).lower() == "true"
    return source, line, group, overlap


def line_structure(row: pd.Series, two_map: dict[str, pd.Series]) -> tuple[str, str]:
    two = two_line_row(row, two_map)
    return (
        clean(two.get("theme_structural_status"), "theme_status_missing"),
        clean(two.get("theme_mainstream_label"), "theme_status_missing"),
    )


def is_core_mainstream_row(row: pd.Series, two_map: dict[str, pd.Series]) -> bool:
    structural, _ = line_structure(row, two_map)
    return structural == "core_mainstream_theme"


def is_strict_breakout_row(row: pd.Series) -> bool:
    category = category_display(clean(row.get("original_category_cn") or row.get("category_cn"))).lower()
    raw_category = clean(row.get("original_category_cn") or row.get("category_cn")).lower()
    return "嚴格突破" in category or raw_category in {"true_breakout", "breakout"}


def candidate_mainstream_bucket(row: pd.Series, two_map: dict[str, pd.Series] | None = None) -> int:
    two_map = two_map or {}
    structural, label = line_structure(row, two_map)
    source, _, group, _ = line_source(row, two_map)
    if structural == "core_mainstream_theme":
        return 0
    if group in {"mainstream_leader_stock", "mainstream_follow_through_stock", "two_line_overlap"}:
        return 0
    if structural in {"emerging_theme"} or group in {"individual_tdcc_latent_watch", "individual_quality_watch"}:
        return 1
    if structural == "non_mainstream_theme" or group == "non_mainstream_flow_watch":
        return 2
    if source == RISK_SOURCE or group == "risk":
        return 4
    return 3


def candidate_quality_points(row: pd.Series) -> float:
    score = 0.0
    tdcc = clean(row.get("tdcc_status")).lower()
    if "strong_accumulation" in tdcc:
        score += 30
    elif "mild_accumulation" in tdcc:
        score += 15
    elif "distribution" in tdcc:
        score -= 80

    overheat = clean(row.get("overheat_status")).lower()
    if overheat in {"not_overheated", "normal", "none", ""}:
        score += 15
    elif "overheated" in overheat or "priced_in" in overheat:
        score -= 18

    vol = to_float(row.get("volume_ratio"))
    if vol is not None:
        if 1.5 <= vol <= 5:
            score += min(18, (vol - 1.5) * 6 + 6)
        elif 5 < vol <= 8:
            score += 8
        elif vol > 8:
            score -= 8

    ret20 = to_float(row.get("return_20d"))
    if ret20 is not None:
        if ret20 <= 10:
            score += 12
        elif ret20 <= 20:
            score += 8
        elif ret20 <= 30:
            score += 2
        else:
            score -= 14

    distance_ma20 = to_float(row.get("distance_to_ma20_pct"))
    if distance_ma20 is not None:
        if distance_ma20 <= 8:
            score += 8
        elif distance_ma20 <= 15:
            score += 3
        else:
            score -= 8

    open_value = to_float(row.get("open"))
    close_value = to_float(row.get("close"))
    high_value = to_float(row.get("high"))
    low_value = to_float(row.get("low"))
    if open_value and close_value:
        body_pct = (close_value - open_value) / open_value * 100
        if body_pct >= 5:
            score += 12
        elif body_pct >= 2:
            score += 6
        elif body_pct < 0:
            score -= 8
    if high_value and low_value and close_value and high_value > low_value:
        close_pos = (close_value - low_value) / (high_value - low_value)
        if close_pos >= 0.8:
            score += 8
        elif close_pos <= 0.45:
            score -= 8

    theme_status = clean(row.get("theme_final_status")).lower()
    if theme_status in {"mainstream_leader", "mainstream_follow_through"}:
        score += 10
    elif theme_status == "mainstream_overheated":
        score += 2
    elif theme_status in {"single_name_signal", "emerging_theme"}:
        score -= 4

    raw_risk = clean(row.get("risk_tags") or row.get("downgrade_flags") or row.get("why_downgraded")).lower()
    if raw_risk and raw_risk not in {"nan", "none", "no_risk", "risk_none"}:
        if "false_breakout" in raw_risk or "distribution" in raw_risk:
            score -= 60
        elif "overheat" in raw_risk or "priced_in" in raw_risk:
            score -= 12
        else:
            score -= 8
    return score


def model_risk_order(row: pd.Series) -> int:
    raw = clean(
        first_text(
            row.get("risk_tags"),
            row.get("risk_penalty_tags"),
            row.get("merged_risk_penalty_tags"),
            row.get("downgrade_flags"),
            row.get("tdcc_status"),
        )
    ).lower()
    if any(token in raw for token in ["distribution", "false_breakout", "missing_data", "source_missing"]):
        return 3
    if any(token in raw for token in ["overheat", "priced_in", "stale_signal", "repeated_but_no_breakout"]):
        return 2
    if raw and raw not in {"nan", "none", "no_risk", "risk_none"}:
        return 1
    return 0


def model_sort_key(row: pd.Series, two_map: dict[str, pd.Series] | None = None) -> tuple:
    model_rank = to_float(row.get("model_rank"))
    display_rank = to_float(row.get("display_rank"))
    score = to_float(row.get("model_score"))
    quality = candidate_quality_points(row)
    return (
        model_rank if model_rank is not None else 9999,
        display_rank if display_rank is not None else 9999,
        candidate_mainstream_bucket(row, two_map),
        model_risk_order(row),
        -(score if score is not None else -9999),
        -quality,
    )


def sort_model_frame(df: pd.DataFrame, two_map: dict[str, pd.Series] | None = None) -> pd.DataFrame:
    if df.empty:
        return df
    tmp = df.copy()
    tmp["_sort_key"] = [model_sort_key(row, two_map) for _, row in tmp.iterrows()]
    return tmp.sort_values("_sort_key").drop(columns=["_sort_key"])


def build_table(
    rows: list[list],
    widths: list[float],
    font_size: float = 7.2,
    header_bg=colors.HexColor("#1f4e79"),
) -> Table:
    font_size = max(font_size, 12.0)
    style = BODY_TINY if font_size < 7.0 else BODY_SMALL
    data: list[list] = []
    for idx, row in enumerate(rows):
        row_style = ParagraphStyle(
            f"tbl_{id(rows)}_{idx}",
            parent=style,
            fontName=FONT_BOLD if idx == 0 else FONT_NAME,
            fontSize=font_size,
            leading=font_size + 1.8,
            textColor=colors.white if idx == 0 else colors.black,
            wordWrap="CJK",
            alignment=TA_CENTER if idx == 0 else TA_LEFT,
        )
        data.append([table_para(cell, row_style) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1, splitByRow=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), header_bg),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#b7b7b7")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 2.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f6f8fa")]),
            ]
        )
    )
    return table


def date_note() -> Paragraph:
    return para(
        f"主資料日期：{DATA_DATE_SLASH}；本次請求日期：{REQUEST_DATE_SLASH}。",
        BODY,
    )


def footer(label: str):
    def draw(canvas, doc):
        canvas.saveState()
        canvas.setFont(FONT_NAME, 9)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawString(14 * mm, 8 * mm, f"{label}｜主資料日期 {DATA_DATE_SLASH}")
        canvas.drawRightString(283 * mm, 8 * mm, str(canvas.getPageNumber()))
        canvas.restoreState()

    return draw


def write_pdf(path: Path, story: list, label: str) -> None:
    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=10 * mm,
        bottomMargin=13 * mm,
        title=label,
        author="Codex",
    )
    doc.build(story, onFirstPage=footer(label), onLaterPages=footer(label))


def get_stock_extra_maps(
    all_candidates: pd.DataFrame,
    two_line: pd.DataFrame,
    volume_stocks: pd.DataFrame,
) -> tuple[dict[str, pd.Series], dict[str, pd.Series], dict[str, pd.Series]]:
    all_map: dict[str, pd.Series] = {}
    if not all_candidates.empty and "stock_id" in all_candidates.columns:
        for _, row in all_candidates.iterrows():
            sid = clean(row.get("stock_id"))
            if sid and sid not in all_map:
                all_map[sid] = row

    two_map: dict[str, pd.Series] = {}
    if not two_line.empty and "stock_id" in two_line.columns:
        for _, row in two_line.iterrows():
            sid = clean(row.get("stock_id"))
            cat = clean(row.get("category_cn") or row.get("original_category_cn"))
            if sid and cat:
                two_map.setdefault((sid, cat), row)
            if sid and sid not in two_map:
                two_map[sid] = row

    vol_map: dict[str, pd.Series] = {}
    if not volume_stocks.empty and "stock_id" in volume_stocks.columns:
        for _, row in volume_stocks.iterrows():
            sid = clean(row.get("stock_id"))
            if sid and sid not in vol_map:
                vol_map[sid] = row

    return all_map, two_map, vol_map


def model_signal_tag(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> str:
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    tdcc = clean(row.get("tdcc_status")).lower()
    risk_level = model_risk_order(row)
    sid = clean(row.get("stock_id"))
    vol_row = (vol_map or {}).get(sid, pd.Series(dtype=object))
    vol_status = clean(vol_row.get("theme_volume_attack_status")).lower()
    if source == RISK_SOURCE or group == "risk":
        return "風險線"
    if "distribution_warning" in tdcc or risk_level >= 3:
        return "高風險模型列"
    if "overheated" in status or "overheated" in label or "overheated" in vol_status or risk_level == 2:
        return "模型命中 / 風險較高"
    if structural == "non_mainstream_theme" or group == "non_mainstream_flow_watch":
        return "模型命中 / 非主流"
    if status == "emerging_theme":
        return "模型命中 / 早期題材"
    return "模型命中"


def display_signal_tag(tag: str) -> str:
    return clean(tag, "模型命中")


def key_level_context(row: pd.Series, extra: pd.Series) -> tuple[str, str, float | None]:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    close_value = to_float(first_text(row.get("close"), source.get("close")))
    level_value = to_float(
        first_text(
            source.get("neckline_price"),
            source.get("platform_high"),
            source.get("previous_60d_high"),
            source.get("previous_high"),
        )
    )
    if level_value is None:
        return "", "", close_value
    level_text = num(level_value)
    if close_value is None:
        return "關鍵價", level_text, close_value
    tolerance = max(abs(close_value) * 0.003, 0.01)
    if level_value < close_value - tolerance:
        return "短線支撐", level_text, close_value
    if level_value > close_value + tolerance:
        return "短線壓力", level_text, close_value
    return "關鍵價", level_text, close_value


def selection_brief(row: pd.Series, extra: pd.Series) -> str:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    stage = translate_codes(first_text(row.get("pattern_stage"), source.get("pattern_stage"), row.get("breakout_type"), source.get("pattern_route")))
    level_label, level_text, _ = key_level_context(row, extra)
    close = num(first_text(row.get("close"), source.get("close")))
    tdcc = zh_tdcc(first_text(row.get("tdcc_status"), source.get("tdcc_status")))
    vol_ok = clean(source.get("volume_confirmed_breakout")).lower() == "true"
    if level_label == "短線支撐" and level_text:
        level_part = f"站在短線支撐 {level_text} 上方"
    elif level_label == "短線壓力" and level_text:
        level_part = f"接近短線壓力 {level_text}"
    elif level_label == "關鍵價" and level_text:
        level_part = f"貼近關鍵價 {level_text}"
    else:
        level_part = ""
    parts = [
        stage,
        f"收盤 {close}" if close else "",
        level_part,
        "成交量放大" if vol_ok else "",
        tdcc,
    ]
    return "；".join([p for p in parts if p]) or short(row.get("why_selected"), 78)


def plot_stock_chart(
    stock_id: str,
    stock_name: str,
    extra: pd.Series,
    candidate_row: pd.Series | None = None,
) -> Path | None:
    remote_template = REMOTE_README.get("individual_stock_price_raw_url_template")
    local_source = LATEST / "individual_stock_reports" / "price_windows" / f"{stock_id}_price_window_180_latest.csv"
    df = read_csv(local_source)
    if df.empty and remote_template:
        try:
            df = read_csv(remote_template.replace("{stock_id}", stock_id))
        except Exception:
            df = pd.DataFrame()
    if df.empty or "date" not in df.columns or "close" not in df.columns:
        return None
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ("open", "high", "low", "close", "volume", "ema23", "ma20", "ma60"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", ""), errors="coerce")
    df = df.dropna(subset=["date", "close"]).tail(CHATGPT_SIDE_KLINE_DAYS)
    if df.empty:
        return None

    chart_kind = "op" if isinstance(candidate_row, pd.Series) and not candidate_row.empty else "plain"
    path = CHARTS / f"{stock_id}_kline_{CHATGPT_SIDE_KLINE_DAYS}_{chart_kind}.png"
    fig, (ax, axv) = plt.subplots(
        2,
        1,
        figsize=(11.5, 4.8),
        dpi=150,
        sharex=True,
        gridspec_kw={"height_ratios": [3.2, 1]},
    )
    xs = mdates.date2num(df["date"])
    width = 0.55
    for _, r in df.iterrows():
        x = mdates.date2num(r["date"])
        o = r.get("open")
        h = r.get("high")
        l = r.get("low")
        c = r.get("close")
        if pd.isna(o) or pd.isna(h) or pd.isna(l) or pd.isna(c):
            continue
        color = "#d62728" if c >= o else "#2ca02c"
        ax.vlines(x, l, h, color=color, linewidth=0.75)
        body_low = min(o, c)
        body_high = max(o, c)
        height = max(body_high - body_low, 0.03)
        ax.add_patch(
            plt.Rectangle(
                (x - width / 2, body_low),
                width,
                height,
                facecolor=color,
                edgecolor=color,
                alpha=0.78,
            )
        )

    for col, color, label, lw in (
        ("ema23", "#1f77b4", "23EMA", 1.5),
    ):
        if col in df.columns and df[col].notna().sum() > 1:
            ax.plot(df["date"], df[col], color=color, label=label, linewidth=lw)

    source_row = candidate_row if isinstance(candidate_row, pd.Series) and not candidate_row.empty else extra
    supports, pressures, close_value = nearby_price_levels(source_row, extra)
    level_label, level_text, _ = key_level_context(source_row, extra)
    annotated_levels: set[float] = set()

    def add_price_line(value, label: str, color: str, linestyle: str = "--", linewidth: float = 1.05) -> None:
        level = to_float(value)
        if level is None:
            return
        key = round(level, 2)
        if key in annotated_levels:
            return
        annotated_levels.add(key)
        ax.axhline(level, color=color, linewidth=linewidth, linestyle=linestyle, alpha=0.88)
        ax.text(
            0.992,
            level,
            f" {label} {num(level)} ",
            transform=ax.get_yaxis_transform(),
            va="center",
            ha="right",
            fontsize=8,
            fontproperties=MATPLOTLIB_FONT,
            color=color,
            bbox=dict(facecolor="white", edgecolor=color, boxstyle="round,pad=0.18", alpha=0.88),
        )

    if level_label == "短線壓力" and level_text:
        add_price_line(level_text, "模型確認/壓力", "#c00000", "-", 1.25)
    elif level_label == "短線支撐" and level_text:
        add_price_line(level_text, "支撐/跌破退出", "#007a3d", "-", 1.25)
    elif level_label == "關鍵價" and level_text:
        add_price_line(level_text, "模型確認/關鍵價", "#c00000", "-", 1.25)

    for idx, level in enumerate(supports[:2], start=1):
        add_price_line(level, f"支撐{idx}", "#007a3d")
    for idx, level in enumerate(pressures[:2], start=1):
        add_price_line(level, f"壓力{idx}/停利觀察", "#d98200")

    if close_value is not None:
        last_date = df["date"].iloc[-1]
        ax.scatter([last_date], [close_value], color="#1f77b4", s=24, zorder=5)
        ax.annotate(
            f"收盤 {num(close_value)}",
            xy=(last_date, close_value),
            xytext=(-54, -16),
            textcoords="offset points",
            fontsize=8,
            fontproperties=MATPLOTLIB_FONT,
            color="#1f77b4",
            arrowprops=dict(arrowstyle="->", color="#1f77b4", linewidth=0.8),
            bbox=dict(facecolor="white", edgecolor="#1f77b4", boxstyle="round,pad=0.18", alpha=0.88),
        )

    volumes = df["volume"] if "volume" in df.columns else pd.Series([0] * len(df))
    colors_v = [
        "#d62728" if close >= open_ else "#2ca02c"
        for open_, close in zip(df.get("open", df["close"]), df["close"])
    ]
    axv.bar(df["date"], volumes, width=0.8, color=colors_v, alpha=0.38)
    axv.set_ylabel("量", fontproperties=MATPLOTLIB_FONT, fontsize=8)
    ax.set_title(
        f"{stock_id} {stock_name} 半年K線 / 23EMA",
        fontproperties=MATPLOTLIB_FONT,
        fontsize=11,
    )
    ax.grid(True, linewidth=0.25, alpha=0.35)
    axv.grid(True, linewidth=0.25, alpha=0.3)
    ax.legend(prop=MATPLOTLIB_FONT, fontsize=7, loc="upper left")
    ax.xaxis_date()
    axv.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=7))
    axv.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    for label in axv.get_xticklabels():
        label.set_rotation(0)
        if MATPLOTLIB_FONT:
            label.set_fontproperties(MATPLOTLIB_FONT)
    fig.tight_layout(pad=0.9)
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return path


def plot_index_chart(index_code: str, index_name: str) -> Path | None:
    path = REMOTE_README.get("market_index_ohlc_history_raw_url") or remote_data_url("market_index_ohlc_history.csv")
    df = read_csv(path)
    if df.empty or "index_code" not in df.columns:
        return None
    sub = df[df["index_code"].astype(str).str.upper() == index_code.upper()].copy()
    if sub.empty:
        return None
    sub["date"] = pd.to_datetime(sub["date"], errors="coerce")
    sub["close"] = pd.to_numeric(sub["close"].astype(str).str.replace(",", ""), errors="coerce")
    sub = sub.dropna(subset=["date", "close"]).sort_values("date").tail(130)
    if sub.empty:
        return None
    sub["ema23"] = sub["close"].ewm(span=23, adjust=False).mean()
    sub["ma20"] = sub["close"].rolling(20).mean()
    sub["ma60"] = sub["close"].rolling(60).mean()

    out = CHARTS / f"market_{index_code.lower()}_technical.png"
    fig, ax = plt.subplots(figsize=(8.8, 3.7), dpi=150)
    ax.plot(sub["date"], sub["close"], color="#111111", linewidth=1.3, label="Close")
    ax.plot(sub["date"], sub["ema23"], color="#1f77b4", linewidth=1.1, label="23EMA")
    ax.plot(sub["date"], sub["ma20"], color="#ff7f0e", linewidth=1.0, label="MA20")
    ax.plot(sub["date"], sub["ma60"], color="#6f42c1", linewidth=1.0, label="MA60")
    ax.set_title(f"{index_name} 技術結構", fontproperties=MATPLOTLIB_FONT, fontsize=11)
    ax.grid(True, linewidth=0.25, alpha=0.35)
    ax.legend(prop=MATPLOTLIB_FONT, fontsize=7, loc="upper left")
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    fig.tight_layout(pad=0.8)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def plot_vix_chart() -> Path | None:
    df = read_csv(remote_latest_url("taiwan_vix_latest.csv"))
    if df.empty:
        return None
    date_col = "date" if "date" in df.columns else df.columns[0]
    value_col = "taiwan_vix" if "taiwan_vix" in df.columns else ("close" if "close" in df.columns else df.columns[-1])
    sub = df[[date_col, value_col]].copy()
    sub[date_col] = pd.to_datetime(sub[date_col], errors="coerce")
    sub[value_col] = pd.to_numeric(sub[value_col].astype(str).str.replace(",", ""), errors="coerce")
    sub = sub.dropna().sort_values(date_col).tail(130)
    if sub.empty:
        return None
    out = CHARTS / "market_taiwan_vix.png"
    fig, ax = plt.subplots(figsize=(8.8, 3.2), dpi=150)
    ax.plot(sub[date_col], sub[value_col], color="#8c564b", linewidth=1.3)
    ax.axhline(30, color="#d62728", linestyle="--", linewidth=0.9, alpha=0.7)
    ax.set_title("Taiwan VIX", fontproperties=MATPLOTLIB_FONT, fontsize=11)
    ax.grid(True, linewidth=0.25, alpha=0.35)
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    fig.tight_layout(pad=0.8)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def plot_put_call_chart() -> Path | None:
    df = read_csv(remote_latest_url("futures_options_put_call_ratio_latest.csv"))
    if df.empty:
        return None
    date_col = "日期" if "日期" in df.columns else df.columns[0]
    oi_col = "買賣權未平倉量比率%" if "買賣權未平倉量比率%" in df.columns else None
    vol_col = "買賣權成交量比率%" if "買賣權成交量比率%" in df.columns else None
    if not oi_col and not vol_col:
        return None
    sub = df.copy()
    sub[date_col] = pd.to_datetime(sub[date_col], errors="coerce")
    for col in (oi_col, vol_col):
        if col:
            sub[col] = pd.to_numeric(sub[col].astype(str).str.replace(",", ""), errors="coerce")
    sub = sub.dropna(subset=[date_col]).sort_values(date_col).tail(90)
    if sub.empty:
        return None
    out = CHARTS / "market_put_call_ratio.png"
    fig, ax = plt.subplots(figsize=(8.8, 3.2), dpi=150)
    if oi_col:
        ax.plot(sub[date_col], sub[oi_col], color="#1f77b4", linewidth=1.2, label="OI Put/Call %")
    if vol_col:
        ax.plot(sub[date_col], sub[vol_col], color="#ff7f0e", linewidth=1.0, label="Volume Put/Call %")
    ax.set_title("TXO Put/Call Ratio", fontproperties=MATPLOTLIB_FONT, fontsize=11)
    ax.grid(True, linewidth=0.25, alpha=0.35)
    ax.legend(prop=MATPLOTLIB_FONT, fontsize=7, loc="upper left")
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(minticks=4, maxticks=7))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    fig.tight_layout(pad=0.8)
    fig.savefig(out, bbox_inches="tight")
    plt.close(fig)
    return out


def load_inputs() -> dict[str, pd.DataFrame]:
    return {
        "two_line": read_latest_csv("daily_candidate_two_line_view_latest.csv"),
        "all": read_latest_csv("all_candidates_latest.csv"),
        "model_registry": read_latest_csv("daily_report_model_registry_latest.csv"),
        "model_parameters": read_latest_csv("daily_candidate_model_parameters_latest.csv"),
        "model_signals": read_latest_csv("daily_candidate_model_signals_for_report_latest.csv"),
        "model_summary": read_latest_csv("daily_candidate_model_summary_for_report_latest.csv"),
        "model_readiness": read_latest_csv("model_operation_readiness_latest.csv"),
        "volume_operation": read_latest_csv("daily_volume_breakout_operation_section_latest.csv"),
        "w_bottom_right_side_operation": read_latest_csv("daily_w_bottom_right_side_operation_section_latest.csv"),
        "w_bottom_neckline_operation": read_latest_csv(
            "daily_neckline_volume_breakout_confirmation_operation_section_latest.csv"
        ),
        "price_pullback_operation": read_latest_csv("daily_price_pullback_23ema_operation_section_latest.csv"),
        "stock_theme_taxonomy": read_latest_csv("stock_theme_taxonomy_latest.csv"),
        "group_rotation": read_latest_csv("daily_candidate_group_rotation_latest.csv"),
        "themes": read_latest_csv("daily_theme_leadership_latest.csv"),
        "volume_layer": read_latest_csv("volume_attack_theme_layer_latest.csv"),
        "volume_stocks": read_latest_csv("volume_attack_theme_stocks_latest.csv"),
        "warrant": read_latest_csv("warrant_flow_latest.csv"),
        "warrant_stock": read_latest_csv("warrant_flow_by_stock_latest.csv"),
        "market_regime": read_latest_csv("market_regime_latest.csv"),
        "market_benchmark": read_latest_csv("market_benchmark_latest.csv"),
        "futures": read_latest_csv("futures_options_indicators_latest.csv"),
        "put_call": read_latest_csv("futures_options_put_call_ratio_latest.csv"),
        "tdcc_edge": read_latest_csv("tdcc_overheated_short_term_edge_candidates_latest.csv"),
        "weekly_surge": read_latest_csv("weekly_surge_strict_parameter_candidates_latest.csv"),
    }




def model_display(row: pd.Series) -> str:
    model = clean(row.get("model_name_zh"))
    if model:
        return model
    return category_display(clean(row.get("original_category_cn") or row.get("category_cn")))


def model_stage_label(row: pd.Series, extra: pd.Series | None = None) -> str:
    model = clean(row.get("model_name_zh"))
    if not model:
        return category_stage_label(row, extra)
    status = clean(row.get("same_model_repeat_status_zh") or row.get("display_rank_repeated_signal") or row.get("display_rank_new_signal"))
    confirm = clean(row.get("next_confirmation_zh") or row.get("next_confirmation"))
    if status and confirm:
        return f"{model}：{status} / {short(confirm, 32)}"
    if status:
        return f"{model}：{status}"
    if confirm:
        return f"{model}：{short(confirm, 36)}"
    return model


def core_model_specs(inputs: dict[str, pd.DataFrame], line: str | None = None) -> list[pd.Series]:
    registry = inputs.get("model_registry", pd.DataFrame()).copy()
    params = inputs.get("model_parameters", pd.DataFrame()).copy()
    if registry.empty:
        signals = inputs.get("model_signals", pd.DataFrame()).copy()
        if signals.empty:
            return []
        cols = ["model_id", "model_name_zh"]
        registry = signals[cols].drop_duplicates().copy()
        registry["model_registry_order"] = range(1, len(registry) + 1)
        registry["model_registry_active"] = True
        registry["report_line_applicability"] = "both"
    if "model_registry_active" in registry.columns:
        registry = registry[registry["model_registry_active"].astype(str).str.lower().isin({"true", "1", "yes", "y"})].copy()
    if line and "report_line_applicability" in registry.columns:
        registry = registry[registry["report_line_applicability"].astype(str).isin(["both", line])].copy()
    if not params.empty and {"model_id", "pdf_visibility"}.issubset(params.columns):
        registry = registry.merge(params[["model_id", "pdf_visibility"]], on="model_id", how="left")
    readiness = inputs.get("model_readiness", pd.DataFrame()).copy()
    if not readiness.empty and {"model_id", "presentation_allowed"}.issubset(readiness.columns):
        registry = registry.merge(readiness[["model_id", "presentation_allowed"]], on="model_id", how="left")
    visibility_mask = (
        registry["pdf_visibility"].astype(str).isin(MODEL_PDF_VISIBILITIES)
        if "pdf_visibility" in registry.columns
        else pd.Series(False, index=registry.index)
    )
    presentation_mask = (
        registry["presentation_allowed"].astype(str).str.lower().isin({"true", "1", "yes", "y"})
        if "presentation_allowed" in registry.columns
        else pd.Series(False, index=registry.index)
    )
    if "pdf_visibility" in registry.columns or "presentation_allowed" in registry.columns:
        registry = registry[visibility_mask | presentation_mask].copy()
    if registry.empty:
        return []
    registry["_order"] = pd.to_numeric(registry.get("model_registry_order"), errors="coerce").fillna(9999)
    registry["_pdf_order"] = registry.apply(
        lambda row: PDF_PRESENTATION_MODEL_ORDER_OVERRIDES.get(clean(row.get("model_id")), row["_order"]),
        axis=1,
    )
    registry = registry.sort_values(["_pdf_order", "_order", "model_id"])
    return [row.drop(labels=["_order", "_pdf_order"], errors="ignore") for _, row in registry.iterrows()]


def model_signal_rows(inputs: dict[str, pd.DataFrame], model_id: str, line: str | None = None) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "model_id" not in signals.columns:
        return []
    sub = signals[signals["model_id"].astype(str).eq(model_id)].copy()
    if line:
        if "report_line" in sub.columns:
            sub = sub[sub["report_line"].astype(str).eq(line)].copy()
        elif "report_bucket" in sub.columns:
            sub = sub[sub["report_bucket"].astype(str).eq(line)].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def mainstream_curated_core_model_specs(inputs: dict[str, pd.DataFrame]) -> list[pd.Series]:
    return core_model_specs(inputs, "mainstream")


def mainstream_full_core_model_specs(inputs: dict[str, pd.DataFrame]) -> list[pd.Series]:
    return core_model_specs(inputs, "mainstream")


def non_mainstream_curated_core_model_specs(inputs: dict[str, pd.DataFrame]) -> list[pd.Series]:
    return core_model_specs(inputs, "non_mainstream")


def non_mainstream_full_core_model_specs(inputs: dict[str, pd.DataFrame]) -> list[pd.Series]:
    return core_model_specs(inputs, "non_mainstream")


def mainstream_curated_model_signal_rows(inputs: dict[str, pd.DataFrame], model_id: str) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "model_id" not in signals.columns:
        return []
    sub = signals[signals["model_id"].astype(str).eq(model_id)].copy()
    if "report_line" in sub.columns:
        sub = sub[sub["report_line"].astype(str).eq("mainstream")].copy()
    elif "report_bucket" in sub.columns:
        sub = sub[sub["report_bucket"].astype(str).eq("mainstream")].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def mainstream_full_model_signal_rows(inputs: dict[str, pd.DataFrame], model_id: str) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "model_id" not in signals.columns:
        return []
    sub = signals[signals["model_id"].astype(str).eq(model_id)].copy()
    if "report_line" in sub.columns:
        sub = sub[sub["report_line"].astype(str).eq("mainstream")].copy()
    elif "report_bucket" in sub.columns:
        sub = sub[sub["report_bucket"].astype(str).eq("mainstream")].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def non_mainstream_curated_model_signal_rows(inputs: dict[str, pd.DataFrame], model_id: str) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "model_id" not in signals.columns:
        return []
    sub = signals[signals["model_id"].astype(str).eq(model_id)].copy()
    if "report_line" in sub.columns:
        sub = sub[sub["report_line"].astype(str).eq("non_mainstream")].copy()
    elif "report_bucket" in sub.columns:
        sub = sub[sub["report_bucket"].astype(str).eq("non_mainstream")].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def non_mainstream_full_model_signal_rows(inputs: dict[str, pd.DataFrame], model_id: str) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "model_id" not in signals.columns:
        return []
    sub = signals[signals["model_id"].astype(str).eq(model_id)].copy()
    if "report_line" in sub.columns:
        sub = sub[sub["report_line"].astype(str).eq("non_mainstream")].copy()
    elif "report_bucket" in sub.columns:
        sub = sub[sub["report_bucket"].astype(str).eq("non_mainstream")].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def is_true_text(value) -> bool:
    return clean(value).lower() in {"true", "1", "yes", "y"}


def volume_operation_frame(
    inputs: dict[str, pd.DataFrame],
    pdf_view: str,
    pdf_section: str,
) -> pd.DataFrame:
    frame = inputs.get("volume_operation", pd.DataFrame()).copy()
    required = {"model_id", "pdf_view", "pdf_section", "row_type", "display_order"}
    if frame.empty or not required.issubset(frame.columns):
        return pd.DataFrame()
    frame = frame[
        frame["model_id"].astype(str).eq(VOLUME_BREAKOUT_MODEL_ID)
        & frame["pdf_view"].astype(str).eq(pdf_view)
        & frame["pdf_section"].astype(str).eq(pdf_section)
    ].copy()
    if frame.empty:
        return frame
    frame["_display_order"] = pd.to_numeric(frame["display_order"], errors="coerce").fillna(9999)
    return frame.sort_values(["_display_order", "stock_id"]).drop(columns=["_display_order"], errors="ignore")


def w_bottom_operation_source_key(model_id: str) -> str:
    key = W_BOTTOM_OPERATION_INPUT_KEYS.get(model_id)
    if not key:
        raise RuntimeError(f"unsupported W-bottom operation model_id for PDF renderer: {model_id}")
    return key


def require_w_bottom_operation_readiness(inputs: dict[str, pd.DataFrame], model_id: str) -> None:
    readiness = inputs.get("model_readiness", pd.DataFrame()).copy()
    if readiness.empty or "model_id" not in readiness.columns:
        raise RuntimeError(f"W-bottom PDF operation adapter readiness missing for {model_id}")
    rows = readiness[readiness["model_id"].astype(str).eq(model_id)].copy()
    if rows.empty:
        raise RuntimeError(f"W-bottom PDF operation adapter readiness row missing for {model_id}")
    row = rows.iloc[0]
    if clean(row.get("pdf_integration_status")) != "pdf_integrated_daily_adapter":
        raise RuntimeError(
            f"W-bottom PDF operation adapter is not pdf_integrated_daily_adapter for {model_id}: "
            f"{clean(row.get('pdf_integration_status'), 'missing')}"
        )
    sections = clean(row.get("daily_adapter_sections"))
    section_tokens = {token.strip() for token in re.split(r"[|,;]", sections) if token.strip()}
    missing_sections = {"confirmed_operation", "active_operation"} - section_tokens
    if missing_sections:
        raise RuntimeError(
            f"W-bottom PDF operation adapter sections missing for {model_id}: "
            + ",".join(sorted(missing_sections))
        )


def w_bottom_operation_frame(
    inputs: dict[str, pd.DataFrame],
    model_id: str,
    pdf_view: str,
    pdf_section: str,
) -> pd.DataFrame:
    require_w_bottom_operation_readiness(inputs, model_id)
    key = w_bottom_operation_source_key(model_id)
    frame = inputs.get(key, pd.DataFrame()).copy()
    if frame.empty:
        raise RuntimeError(f"W-bottom PDF operation adapter artifact is empty or missing for {model_id}: {key}")
    missing = sorted(W_BOTTOM_OPERATION_REQUIRED_COLUMNS - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"W-bottom PDF operation adapter artifact missing required columns for {model_id}: "
            + ",".join(missing)
        )
    frame = frame[
        frame["model_id"].astype(str).eq(model_id)
        & frame["pdf_view"].astype(str).eq(pdf_view)
        & frame["pdf_section"].astype(str).eq(pdf_section)
    ].copy()
    if frame.empty:
        raise RuntimeError(f"W-bottom PDF operation adapter has no {pdf_view}/{pdf_section} rows for {model_id}")
    frame["_display_order"] = pd.to_numeric(frame["display_order"], errors="coerce").fillna(999999)
    return frame.sort_values(["_display_order", "stock_id"]).drop(columns=["_display_order"], errors="ignore")


def require_price_pullback_operation_readiness(inputs: dict[str, pd.DataFrame]) -> None:
    readiness = inputs.get("model_readiness", pd.DataFrame()).copy()
    if readiness.empty or "model_id" not in readiness.columns:
        raise RuntimeError("price_pullback_23ema PDF operation adapter readiness missing")
    rows = readiness[readiness["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)].copy()
    if rows.empty:
        raise RuntimeError("price_pullback_23ema PDF operation adapter readiness row missing")
    row = rows.iloc[0]
    if clean(row.get("pdf_integration_status")) != "pdf_integrated_daily_adapter":
        raise RuntimeError(
            "price_pullback_23ema PDF operation adapter is not pdf_integrated_daily_adapter: "
            f"{clean(row.get('pdf_integration_status'), 'missing')}"
        )
    sections = clean(row.get("daily_adapter_sections"))
    section_tokens = {token.strip() for token in re.split(r"[|,;]", sections) if token.strip()}
    missing_sections = {"confirmed_operation", "active_operation"} - section_tokens
    if missing_sections:
        raise RuntimeError(
            "price_pullback_23ema PDF operation adapter sections missing: "
            + ",".join(sorted(missing_sections))
        )


def price_pullback_operation_frame(
    inputs: dict[str, pd.DataFrame],
    pdf_view: str,
    pdf_section: str,
) -> pd.DataFrame:
    require_price_pullback_operation_readiness(inputs)
    frame = inputs.get(PRICE_PULLBACK_OPERATION_INPUT_KEY, pd.DataFrame()).copy()
    if frame.empty:
        raise RuntimeError(
            "price_pullback_23ema PDF operation adapter artifact is empty or missing: "
            f"{PRICE_PULLBACK_OPERATION_INPUT_KEY}"
        )
    missing = sorted(PRICE_PULLBACK_OPERATION_REQUIRED_COLUMNS - set(frame.columns))
    if missing:
        raise RuntimeError(
            "price_pullback_23ema PDF operation adapter artifact missing required columns: "
            + ",".join(missing)
        )
    frame = frame[
        frame["model_id"].astype(str).eq(PRICE_PULLBACK_MODEL_ID)
        & frame["pdf_view"].astype(str).eq(pdf_view)
        & frame["pdf_section"].astype(str).eq(pdf_section)
    ].copy()
    if frame.empty:
        raise RuntimeError(f"price_pullback_23ema PDF operation adapter has no {pdf_view}/{pdf_section} rows")
    frame["_display_order"] = pd.to_numeric(frame["display_order"], errors="coerce").fillna(999999)
    return frame.sort_values(["_display_order", "stock_id"]).drop(columns=["_display_order"], errors="ignore")


def report_lines_for_stock_from_frame(frame: pd.DataFrame, stock_id: str) -> set[str]:
    if frame.empty or "stock_id" not in frame.columns or not stock_id:
        return set()
    part = frame[frame["stock_id"].map(stock_id_text).eq(stock_id)].copy()
    if part.empty:
        return set()
    lines: set[str] = set()
    for col in ("report_line", "report_bucket"):
        if col in part.columns:
            lines.update(
                value
                for value in (clean(raw) for raw in part[col].tolist())
                if value in {"mainstream", "non_mainstream"}
            )
    for col in ("report_line_memberships", "taxonomy_report_line_memberships"):
        if col in part.columns:
            for raw_value in part[col].tolist():
                value = clean(raw_value)
                if not value:
                    continue
                for token in value.replace(";", "|").replace(",", "|").split("|"):
                    token = token.strip()
                    if token in {"mainstream", "non_mainstream"}:
                        lines.add(token)
    truth_cols = [
        ("mainstream_report_eligible", "mainstream"),
        ("taxonomy_mainstream_report_eligible", "mainstream"),
        ("non_mainstream_report_eligible", "non_mainstream"),
        ("taxonomy_non_mainstream_report_eligible", "non_mainstream"),
    ]
    for col, line in truth_cols:
        if col in part.columns and part[col].map(is_true_text).any():
            lines.add(line)
    return lines


def volume_operation_report_lines_for_stock(inputs: dict[str, pd.DataFrame], stock_id: str) -> set[str]:
    lines: set[str] = set()
    sources = [
        inputs.get("model_signals", pd.DataFrame()),
        inputs.get("two_line", pd.DataFrame()),
        inputs.get("all", pd.DataFrame()),
        inputs.get("stock_theme_taxonomy", pd.DataFrame()),
    ]
    for frame in sources:
        lines.update(report_lines_for_stock_from_frame(frame.copy(), stock_id))
    return lines


def filter_volume_operation_rows_for_line(
    rows: pd.DataFrame,
    inputs: dict[str, pd.DataFrame],
    line: str | None,
) -> pd.DataFrame:
    if rows.empty or not line:
        return rows
    if "report_line" in rows.columns:
        return rows[rows["report_line"].astype(str).eq(line)].copy()
    if "report_bucket" in rows.columns:
        return rows[rows["report_bucket"].astype(str).eq(line)].copy()
    row_type = rows.get("row_type", pd.Series(dtype=str)).astype(str)
    stock_ids = rows["stock_id"].map(stock_id_text)
    empty_state = row_type.eq("empty_state") & stock_ids.eq("")
    mask = empty_state | stock_ids.map(lambda value: line in volume_operation_report_lines_for_stock(inputs, value))
    return rows[mask].copy()


def w_bottom_operation_row_matches_line(row: pd.Series, line: str | None) -> bool:
    if not line:
        return True
    report_line = clean(row.get("report_line"))
    if report_line == line or report_line == "both":
        return True
    memberships = clean(row.get("report_line_memberships"))
    if memberships:
        tokens = {token.strip() for token in re.split(r"[|,;]", memberships) if token.strip()}
        return line in tokens or "both" in tokens
    return False


def filter_w_bottom_operation_rows_for_line(rows: pd.DataFrame, line: str | None) -> pd.DataFrame:
    if rows.empty or not line:
        return rows
    return rows[rows.apply(lambda row: w_bottom_operation_row_matches_line(row, line), axis=1)].copy()


def volume_operation_empty_text(rows: pd.DataFrame, fallback: str) -> str:
    if rows.empty:
        return fallback
    for col in ("adapter_note_zh", "pdf_note_zh", "operation_status_zh", "stock_display"):
        if col in rows.columns:
            text = " / ".join(clean(v) for v in rows[col].tolist() if clean(v))
            if text:
                return text
    return fallback


def limit_volume_operation_rows_for_pdf_view(
    rows: pd.DataFrame,
    pdf_view: str,
    pdf_section: str,
) -> pd.DataFrame:
    if rows.empty or pdf_view != "highlight":
        return rows
    limit = VOLUME_OPERATION_HIGHLIGHT_LIMITS.get(pdf_section)
    if limit is None:
        return rows
    if "row_type" not in rows.columns:
        return rows.head(limit).copy()
    row_type = rows["row_type"].astype(str)
    data_rows = rows[row_type.eq("data")].head(limit).copy()
    if not data_rows.empty:
        return data_rows
    return rows.copy()


def limit_w_bottom_operation_rows_for_pdf_view(
    rows: pd.DataFrame,
    pdf_view: str,
    pdf_section: str,
) -> pd.DataFrame:
    if rows.empty or pdf_view != "highlight":
        return rows
    limit = W_BOTTOM_OPERATION_HIGHLIGHT_LIMITS.get(pdf_section)
    if limit is None:
        return rows
    row_type = rows.get("row_type", pd.Series(dtype=str)).astype(str)
    data_rows = rows[row_type.eq("data")].head(limit).copy()
    if not data_rows.empty:
        return data_rows
    return rows.copy()


def volume_operation_date_label(value) -> str:
    text = clean(value)
    if not text:
        return "-"
    return date_slash(text)


def volume_operation_score_label(row: pd.Series) -> str:
    operation_score = num(row.get("operation_score"), 2)
    final_score = num(row.get("final_rank_score"), 2)
    parts = []
    if operation_score:
        parts.append(f"操作 {operation_score}")
    if final_score:
        parts.append(f"最終 {final_score}")
    return " / ".join(parts) if parts else "-"


def volume_operation_trigger_label(row: pd.Series) -> str:
    trigger_id = clean(row.get("selected_trigger_id"))
    if trigger_id:
        return VOLUME_TRIGGER_LABELS.get(trigger_id, trigger_id)
    matched = clean(row.get("matched_trigger_ids"))
    if matched:
        labels = [
            VOLUME_TRIGGER_LABELS.get(token.strip(), token.strip())
            for token in matched.replace(";", "|").replace(",", "|").split("|")
            if token.strip()
        ]
        if labels:
            return " / ".join(labels)
    return "-"


def volume_operation_entry_label(row: pd.Series, status: str) -> str:
    if status == "pending_confirmation":
        return "尚未確認，不列進場價"
    entry_date = clean(row.get("entry_date"))
    entry_price = clean(row.get("entry_price"))
    if entry_date or entry_price:
        date = date_slash(entry_date) if entry_date else "進場日未提供"
        price = entry_price if entry_price else "進場價未提供"
        return f"{date} / {price}"
    rule_id = clean(row.get("entry_rule_id"))
    basis = clean(row.get("entry_price_basis"))
    label = VOLUME_ENTRY_RULE_LABELS.get(rule_id, rule_id or basis)
    if status == "confirmed_operation" and rule_id == "confirmation_next_open":
        return f"{label}，尚未產生"
    return label or "-"


def volume_operation_stop_label(row: pd.Series, status: str) -> str:
    if status == "pending_confirmation":
        return "尚未確認，不列停損價"
    label = clean(row.get("stop_loss_label_zh"))
    price = clean(row.get("stop_loss_price"))
    if label and price:
        return f"{label} {price}"
    if label or price:
        return label or price
    rule_id = clean(row.get("stop_loss_rule_id"))
    return VOLUME_STOP_RULE_LABELS.get(rule_id, rule_id or "-")


def volume_operation_exit_label(row: pd.Series) -> str:
    rule_id = clean(row.get("exit_rule_id"))
    holding_days = clean(row.get("planned_holding_days"))
    label = VOLUME_EXIT_RULE_LABELS.get(rule_id, rule_id)
    if rule_id == "signal_low_stop_or_fixed_10d_close" and holding_days and holding_days != "10":
        return f"跌破停損基準，否則最多第 {holding_days} 個交易日收盤"
    return label or "-"


def w_bottom_operation_signal_label(row: pd.Series) -> str:
    return w_bottom_pdf_safe_text(
        first_text(
            row.get("operation_status_zh"),
            row.get("quality_status_zh"),
            row.get("entry_basis_zh"),
            row.get("row_action_status"),
            default="-",
        ),
        42,
    )


def w_bottom_operation_signal_date_label(row: pd.Series) -> str:
    return volume_operation_date_label(first_text(row.get("confirmation_date"), row.get("signal_date")))


def w_bottom_pdf_safe_text(value, limit: int) -> str:
    text = clean(value)
    if not text:
        return "-"
    text = text.replace("待確認", "確認價未定")
    return short(text, limit)


def w_bottom_operation_entry_label(row: pd.Series) -> str:
    entry_date = clean(row.get("entry_date"))
    entry_price = clean(row.get("entry_price"))
    if entry_date or entry_price:
        date = date_slash(entry_date) if entry_date else "進場日未定"
        price = entry_price if entry_price else "進場價未定"
        return f"{date} / {price}"
    return w_bottom_pdf_safe_text(
        first_text(row.get("entry_basis_zh"), row.get("entry_rule_id"), row.get("entry_price_status_zh"), default="-"),
        40,
    )


def w_bottom_operation_stop_label(row: pd.Series) -> str:
    label = first_text(row.get("stop_loss_label_zh"), row.get("stop_basis_zh"), row.get("stop_loss_rule_id"))
    price = clean(row.get("stop_loss_price"))
    if label and price:
        return w_bottom_pdf_safe_text(f"{label} {price}", 38)
    return w_bottom_pdf_safe_text(label or price or "-", 38)


def w_bottom_operation_exit_label(row: pd.Series) -> str:
    return w_bottom_pdf_safe_text(first_text(row.get("exit_rule_zh"), row.get("exit_rule_id"), default="-"), 48)


def w_bottom_operation_age_label(row: pd.Series) -> str:
    age = clean(row.get("operation_age_days"))
    planned = clean(row.get("planned_holding_days"))
    if age or planned:
        return f"{age or '-'} / {planned or '-'}"
    return "-"


def w_bottom_operation_score_label(row: pd.Series) -> str:
    parts: list[str] = []
    for label, column in (("操作", "operation_score"), ("模型", "model_score"), ("最終", "final_rank_score")):
        value = clean(row.get(column))
        if value:
            parts.append(f"{label} {value}")
    return " / ".join(parts) if parts else "-"


def w_bottom_operation_note_label(row: pd.Series) -> str:
    return w_bottom_pdf_safe_text(
        first_text(
            row.get("rank_reason_zh"),
            row.get("risk_tags_zh"),
            row.get("pdf_note_zh"),
            row.get("adapter_note_zh"),
            default="-",
        ),
        74,
    )


def build_volume_confirmed_operation_table(rows: pd.DataFrame) -> Table:
    data = [[
        "排名",
        "股票",
        "確認方式",
        "確認日",
        "買入方式",
        "停損基準",
        "出場規則",
        "操作 / 最終分數",
        "樣本數",
        "勝率",
        "中位數報酬",
        "排名原因",
    ]]
    if rows.empty:
        data.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", MODEL_EMPTY_STATE_TEXT])
    for _, row in rows.iterrows():
        data.append(
            [
                clean(row.get("display_order"), "-"),
                clean(row.get("stock_display"), "-"),
                volume_operation_trigger_label(row),
                volume_operation_date_label(first_text(row.get("confirmation_date"), row.get("selected_confirmation_date"))),
                volume_operation_entry_label(row, "confirmed_operation"),
                volume_operation_stop_label(row, "confirmed_operation"),
                volume_operation_exit_label(row),
                volume_operation_score_label(row),
                clean(row.get("sample_size"), "-"),
                clean(row.get("win_rate_zh"), "-"),
                clean(row.get("median_return_zh"), "-"),
                clean(row.get("rank_reason_zh"), "-"),
            ]
        )
    return build_table(
        data,
        [8 * mm, 18 * mm, 27 * mm, 18 * mm, 31 * mm, 28 * mm, 35 * mm, 28 * mm, 11 * mm, 14 * mm, 17 * mm, 38 * mm],
        12.0,
        header_bg=colors.HexColor("#7f6000"),
    )


def build_volume_unranked_operation_table(rows: pd.DataFrame) -> Table:
    data = [[
        "股票",
        "確認方式",
        "確認日",
        "未列排名原因",
        "樣本數",
        "勝率",
        "中位數報酬",
        "證據狀態",
    ]]
    if rows.empty:
        data.append(["-", "-", "-", "目前沒有已確認但未通過買入排名門檻的股票。", "-", "-", "-", "-"])
    for _, row in rows.iterrows():
        evidence_status = clean(row.get("evidence_match_status"), "-")
        if evidence_status == "row_level_evidence_not_buy_ranked":
            evidence_status = "歷史證據未過門檻"
        elif evidence_status == "no_matching_row_level_evidence":
            evidence_status = "沒有可匹配的歷史證據"
        data.append(
            [
                clean(row.get("stock_display"), "-"),
                volume_operation_trigger_label(row),
                volume_operation_date_label(first_text(row.get("confirmation_date"), row.get("selected_confirmation_date"))),
                clean(row.get("rank_reason_zh"), "-"),
                clean(row.get("sample_size"), "-"),
                clean(row.get("win_rate_zh"), "-"),
                clean(row.get("median_return_zh"), "-"),
                evidence_status,
            ]
        )
    return build_table(
        data,
        [28 * mm, 32 * mm, 18 * mm, 78 * mm, 14 * mm, 16 * mm, 20 * mm, 42 * mm],
        12.0,
        header_bg=colors.HexColor("#8064a2"),
    )


def build_volume_pending_operation_table(rows: pd.DataFrame) -> Table:
    data = [["股票", "等待天數", "等待分組", "待確認條件", "模型分數 / 排名原因", "進場 / 停損狀態", "狀態"]]
    if rows.empty:
        data.append(["-", "-", "-", "目前無待確認列。", "-", "不列進場價 / 不列停損價", "待確認"])
    for _, row in rows.iterrows():
        score_text = volume_operation_score_label(row)
        reason = clean(row.get("rank_reason_zh"))
        if reason:
            score_text = f"{score_text} / {reason}" if score_text != "-" else reason
        data.append(
            [
                clean(row.get("stock_display"), "-"),
                clean(row.get("pending_age_zh"), "-"),
                clean(row.get("pending_group_zh"), "-"),
                clean(row.get("pending_confirmation_zh"), "-"),
                score_text,
                f'{volume_operation_entry_label(row, "pending_confirmation")} / {volume_operation_stop_label(row, "pending_confirmation")}',
                clean(row.get("operation_status_zh"), "待確認"),
            ]
        )
    return build_table(
        data,
        [26 * mm, 20 * mm, 24 * mm, 62 * mm, 76 * mm, 40 * mm, 25 * mm],
        12.0,
        header_bg=colors.HexColor("#5f7530"),
    )


def build_volume_active_operation_table(rows: pd.DataFrame) -> Table:
    data = [["股票", "確認方式", "進場日 / 價", "停損基準", "持有天數", "出場規則", "操作 / 最終分數", "備註"]]
    if rows.empty:
        data.append(["-", "-", "-", "-", "-", "-", "-", OPERATION_ACTIVE_EMPTY_STATE_TEXT])
    for _, row in rows.iterrows():
        age = clean(row.get("operation_age_days"))
        planned = clean(row.get("planned_holding_days"))
        age_text = "-"
        if age or planned:
            age_text = f"{age or '-'} / {planned or '-'}"
        data.append(
            [
                clean(row.get("stock_display"), "目前無資料"),
                volume_operation_trigger_label(row),
                volume_operation_entry_label(row, "active_operation"),
                volume_operation_stop_label(row, "active_operation"),
                age_text,
                volume_operation_exit_label(row),
                volume_operation_score_label(row),
                first_text(row.get("rank_reason_zh"), row.get("adapter_note_zh"), row.get("pdf_note_zh"), default=OPERATION_ACTIVE_EMPTY_STATE_TEXT),
            ]
        )
    return build_table(
        data,
        [30 * mm, 28 * mm, 36 * mm, 34 * mm, 22 * mm, 46 * mm, 32 * mm, 45 * mm],
        12.0,
        header_bg=colors.HexColor("#44546a"),
    )


def build_w_bottom_confirmed_operation_table(rows: pd.DataFrame) -> Table:
    data = [[
        "排名",
        "股票",
        "確認方式",
        "確認日",
        "進場日 / 價",
        "停損基準",
        "出場規則",
        "操作 / 模型分數",
        "樣本數",
        "勝率",
        "中位數報酬",
        "備註",
    ]]
    if rows.empty:
        data.append(["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", MODEL_EMPTY_STATE_TEXT])
    for _, row in rows.iterrows():
        data.append(
            [
                clean(row.get("display_order"), "-"),
                clean(row.get("stock_display"), "-"),
                w_bottom_operation_signal_label(row),
                w_bottom_operation_signal_date_label(row),
                w_bottom_operation_entry_label(row),
                w_bottom_operation_stop_label(row),
                w_bottom_operation_exit_label(row),
                w_bottom_operation_score_label(row),
                clean(row.get("sample_size"), "-"),
                clean(row.get("win_rate_zh"), "-"),
                clean(row.get("median_return_zh"), "-"),
                w_bottom_operation_note_label(row),
            ]
        )
    return build_table(
        data,
        [8 * mm, 28 * mm, 34 * mm, 18 * mm, 35 * mm, 30 * mm, 40 * mm, 30 * mm, 13 * mm, 15 * mm, 18 * mm, 22 * mm],
        12.0,
        header_bg=colors.HexColor("#7f6000"),
    )


def build_w_bottom_active_operation_table(rows: pd.DataFrame) -> Table:
    data = [["股票", "確認方式", "進場日 / 價", "停損基準", "持有天數", "出場規則", "操作 / 模型分數", "備註"]]
    if rows.empty:
        data.append(["-", "-", "-", "-", "-", "-", "-", OPERATION_ACTIVE_EMPTY_STATE_TEXT])
    for _, row in rows.iterrows():
        data.append(
            [
                clean(row.get("stock_display"), "-"),
                w_bottom_operation_signal_label(row),
                w_bottom_operation_entry_label(row),
                w_bottom_operation_stop_label(row),
                w_bottom_operation_age_label(row),
                w_bottom_operation_exit_label(row),
                w_bottom_operation_score_label(row),
                w_bottom_operation_note_label(row),
            ]
        )
    return build_table(
        data,
        [30 * mm, 36 * mm, 36 * mm, 34 * mm, 22 * mm, 50 * mm, 32 * mm, 33 * mm],
        12.0,
        header_bg=colors.HexColor("#44546a"),
    )


def price_pullback_metrics_label(row: pd.Series) -> str:
    base = (
        f"基礎 {clean(row.get('win_rate_zh'), '-')} / "
        f"{clean(row.get('neutral_rate_zh'), '-')} / "
        f"{clean(row.get('failure_rate_zh'), '-')} / "
        f"{clean(row.get('avg_return_zh'), '-')}"
    )
    quality = clean(row.get("operation_quality"))
    if quality != "technical_strength":
        return base
    technical = (
        f"技術強勢 {clean(row.get('technical_package_win_rate_zh'), '-')} / "
        f"{clean(row.get('technical_package_neutral_rate_zh'), '-')} / "
        f"{clean(row.get('technical_package_failure_rate_zh'), '-')} / "
        f"{clean(row.get('technical_package_avg_return_zh'), '-')}"
    )
    return f"{base}; {technical}"


def price_pullback_note_label(row: pd.Series) -> str:
    reason = clean(row.get("rank_reason_zh"))
    risk = clean(row.get("risk_tags_zh"))
    if reason and risk:
        return f"{reason}；風險：{risk}"
    return reason or (f"風險：{risk}" if risk else "-")


def build_price_pullback_confirmed_operation_table(rows: pd.DataFrame) -> Table:
    data = [["股票", "操作品質", "訊號日", "買入", "賣出", "停損", "勝/和/敗/報酬", "理由 / 風險"]]
    if rows.empty:
        data.append(["-", "-", "-", MODEL_EMPTY_STATE_TEXT, "-", "-", "-", "-"])
    for _, row in rows.iterrows():
        data.append(
            [
                clean(row.get("stock_display"), "-"),
                clean(row.get("operation_quality_zh"), "-"),
                clean(row.get("signal_date"), "-"),
                clean(row.get("entry_basis_zh"), "-"),
                clean(row.get("exit_rule_zh"), "-"),
                clean(row.get("stop_basis_zh"), "-"),
                price_pullback_metrics_label(row),
                price_pullback_note_label(row),
            ]
        )
    return build_table(
        data,
        [26 * mm, 22 * mm, 18 * mm, 42 * mm, 43 * mm, 43 * mm, 33 * mm, 46 * mm],
        11.0,
        header_bg=colors.HexColor("#7f6000"),
    )


def build_price_pullback_active_operation_table(rows: pd.DataFrame) -> Table:
    data = [["股票", "操作品質", "訊號日", "買入", "出場 / 停損", "持有天數", "目前狀態", "理由 / 風險"]]
    if rows.empty:
        data.append(["-", "-", "-", "-", "-", "-", OPERATION_ACTIVE_EMPTY_STATE_TEXT, "-"])
    for _, row in rows.iterrows():
        age = clean(row.get("operation_age_days"))
        planned = clean(row.get("planned_holding_days"))
        age_text = f"{age or '-'} / {planned or '-'}" if (age or planned) else "-"
        exit_stop = f"{clean(row.get('exit_rule_zh'), '-')} / {clean(row.get('stop_basis_zh'), '-')}"
        data.append(
            [
                clean(row.get("stock_display"), "-"),
                clean(row.get("operation_quality_zh"), "-"),
                clean(row.get("signal_date"), "-"),
                clean(row.get("entry_basis_zh"), "-"),
                exit_stop,
                age_text,
                clean(row.get("operation_status_zh"), "-"),
                price_pullback_note_label(row),
            ]
        )
    return build_table(
        data,
        [26 * mm, 22 * mm, 18 * mm, 42 * mm, 62 * mm, 20 * mm, 34 * mm, 49 * mm],
        11.0,
        header_bg=colors.HexColor("#44546a"),
    )


def render_w_bottom_operation_section(
    story: list,
    inputs: dict[str, pd.DataFrame],
    model_id: str,
    pdf_view: str,
    line: str | None = None,
) -> None:
    confirmed_all = filter_w_bottom_operation_rows_for_line(
        w_bottom_operation_frame(inputs, model_id, pdf_view, "confirmed_operation"),
        line,
    )
    active_all = filter_w_bottom_operation_rows_for_line(
        w_bottom_operation_frame(inputs, model_id, pdf_view, "active_operation"),
        line,
    )
    confirmed = confirmed_all[
        confirmed_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & confirmed_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_buy_candidate")
        & confirmed_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not confirmed_all.empty else pd.DataFrame()
    confirmed = limit_w_bottom_operation_rows_for_pdf_view(confirmed, pdf_view, "confirmed_operation")
    active_rows = active_all[
        active_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & active_all.get("operation_status", pd.Series(dtype=str)).astype(str).eq("active_operation")
        & ~active_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not active_all.empty else pd.DataFrame()
    active_rows = limit_w_bottom_operation_rows_for_pdf_view(active_rows, pdf_view, "active_operation")

    story.append(Spacer(1, 6))
    story.append(Paragraph(OPERATION_CONFIRMED_BUY_TABLE_TITLE, H2))
    story.append(build_w_bottom_confirmed_operation_table(confirmed))
    story.append(Spacer(1, 5))
    story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))
    story.append(build_w_bottom_active_operation_table(active_rows))


def render_price_pullback_operation_section(
    story: list,
    inputs: dict[str, pd.DataFrame],
    pdf_view: str,
    line: str | None = None,
) -> None:
    confirmed_all = filter_w_bottom_operation_rows_for_line(
        price_pullback_operation_frame(inputs, pdf_view, "confirmed_operation"),
        line,
    )
    active_all = filter_w_bottom_operation_rows_for_line(
        price_pullback_operation_frame(inputs, pdf_view, "active_operation"),
        line,
    )
    confirmed = confirmed_all[
        confirmed_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & confirmed_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_buy_candidate")
        & confirmed_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not confirmed_all.empty else pd.DataFrame()
    active_rows = active_all[
        active_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & active_all.get("operation_status", pd.Series(dtype=str)).astype(str).eq("active_operation")
        & ~active_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not active_all.empty else pd.DataFrame()

    story.append(Spacer(1, 6))
    story.append(Paragraph(OPERATION_CONFIRMED_BUY_TABLE_TITLE, H2))
    story.append(build_price_pullback_confirmed_operation_table(confirmed))
    story.append(Spacer(1, 5))
    story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))
    story.append(build_price_pullback_active_operation_table(active_rows))


def render_volume_range_breakout_operation_section(
    story: list,
    inputs: dict[str, pd.DataFrame],
    pdf_view: str,
    line: str | None = None,
) -> None:
    confirmed_all = filter_volume_operation_rows_for_line(
        volume_operation_frame(inputs, pdf_view, "confirmed_operation"),
        inputs,
        line,
    )
    unranked_all = filter_volume_operation_rows_for_line(
        volume_operation_frame(inputs, pdf_view, "confirmed_unranked_operation"),
        inputs,
        line,
    )
    pending_all = filter_volume_operation_rows_for_line(
        volume_operation_frame(inputs, pdf_view, "pending_confirmation"),
        inputs,
        line,
    )
    active_all = filter_volume_operation_rows_for_line(
        volume_operation_frame(inputs, pdf_view, "active_operation"),
        inputs,
        line,
    )

    confirmed = confirmed_all[
        confirmed_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & confirmed_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_buy_candidate")
        & confirmed_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not confirmed_all.empty else pd.DataFrame()
    confirmed = limit_volume_operation_rows_for_pdf_view(confirmed, pdf_view, "confirmed_operation")

    unranked = unranked_all[
        unranked_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & unranked_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("confirmed_not_buy_ranked")
        & ~unranked_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not unranked_all.empty and pdf_view == "full" else pd.DataFrame()

    if pdf_view == "full":
        pending = pending_all[
            pending_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
            & pending_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("pending_confirmation")
            & ~pending_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
        ].copy() if not pending_all.empty else pd.DataFrame()
    else:
        pending = pd.DataFrame()
    active_rows = active_all[
        active_all.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
        & active_all.get("row_action_status", pd.Series(dtype=str)).astype(str).eq("active_operation")
        & ~active_all.get("buy_rank_eligible", pd.Series(dtype=str)).map(is_true_text)
    ].copy() if not active_all.empty else pd.DataFrame()
    active_rows = limit_volume_operation_rows_for_pdf_view(active_rows, pdf_view, "active_operation")

    story.append(Spacer(1, 6))
    story.append(Paragraph(OPERATION_CONFIRMED_BUY_TABLE_TITLE, H2))
    story.append(build_volume_confirmed_operation_table(confirmed))
    story.append(Spacer(1, 5))
    if pdf_view == "full":
        story.append(Paragraph("已確認但未通過買入排名門檻", H2))
        if unranked.empty:
            story.append(para(volume_operation_empty_text(unranked_all, "目前沒有已確認但未通過買入排名門檻的股票。"), BODY_SMALL))
        story.append(build_volume_unranked_operation_table(unranked))
        story.append(Spacer(1, 5))
        story.append(Paragraph("待確認", H2))
        if pending.empty:
            story.append(para(volume_operation_empty_text(pending_all, "目前無待確認列。"), BODY_SMALL))
        story.append(build_volume_pending_operation_table(pending))
        story.append(Spacer(1, 5))
    story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))
    story.append(build_volume_active_operation_table(active_rows))


def render_model_operation_section_if_applicable(
    story: list,
    inputs: dict[str, pd.DataFrame],
    model_id: str,
    pdf_view: str,
    line: str | None = None,
) -> bool:
    if model_id == VOLUME_BREAKOUT_MODEL_ID:
        render_volume_range_breakout_operation_section(story, inputs, pdf_view, line)
        return True
    if model_id in W_BOTTOM_OPERATION_TABLE_MODEL_IDS:
        render_w_bottom_operation_section(story, inputs, model_id, pdf_view, line)
        return True
    if model_id == PRICE_PULLBACK_MODEL_ID:
        render_price_pullback_operation_section(story, inputs, pdf_view, line)
        return True
    return False


def model_signal_rows_for_stock(inputs: dict[str, pd.DataFrame], stock_id: str, line: str | None = None) -> list[pd.Series]:
    signals = inputs.get("model_signals", pd.DataFrame()).copy()
    if signals.empty or "stock_id" not in signals.columns:
        return []
    sub = signals[signals["stock_id"].astype(str).str.replace(r"\.0$", "", regex=True).eq(stock_id_text(stock_id))].copy()
    if line:
        if "report_line" in sub.columns:
            sub = sub[sub["report_line"].astype(str).eq(line)].copy()
        elif "report_bucket" in sub.columns:
            sub = sub[sub["report_bucket"].astype(str).eq(line)].copy()
    if sub.empty:
        return []
    core_ids = {clean(spec.get("model_id")) for spec in core_model_specs(inputs, line)}
    if core_ids and "model_id" in sub.columns:
        sub = sub[sub["model_id"].astype(str).isin(core_ids)].copy()
    if sub.empty:
        return []
    sub["_model_rank"] = pd.to_numeric(sub.get("model_rank"), errors="coerce").fillna(9999)
    sub["_display_rank"] = pd.to_numeric(sub.get("display_rank"), errors="coerce").fillna(9999)
    sub["_model_score"] = pd.to_numeric(sub.get("model_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score"], ascending=[True, True, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score"], errors="ignore") for _, row in sub.iterrows()]


def preferred_model_label_for_stock(inputs: dict[str, pd.DataFrame], stock_id: str, line: str | None = None) -> str:
    rows = model_signal_rows_for_stock(inputs, stock_id, line)
    if not rows:
        return ""
    first = rows[0]
    name = clean(first.get("model_name_zh"))
    rank = clean(first.get("display_rank") or first.get("model_rank"))
    if rank:
        return f"{name} #{rank}"
    return name


def preferred_model_status_for_stock(inputs: dict[str, pd.DataFrame], stock_id: str, line: str | None = None) -> str:
    rows = model_signal_rows_for_stock(inputs, stock_id, line)
    if not rows:
        return "模型訊號未對應"
    first = rows[0]
    return f"{model_score_label(first)} / 風險：{model_risk_text(first, 32)}"


def build_mainstream_curated_model_table(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    limit: int = 6,
) -> list:
    title = MAINSTREAM_LINE_LABEL
    selected_rows = rows[:limit]
    story: list = []
    for label, color in [("新上榜", "#c00000"), ("重複上榜", "#1f4e79")]:
        data = [["標的", "模型狀態", "模型排名 / 分數", "族群 / 資金", "大戶籌碼", "模型依據 / 風險"]]
        matched = False
        for row in selected_rows:
            stage = display_signal_tag(model_signal_tag(row, two_map))
            row_label = listing_status_label(row, stage)
            if label == "新上榜" and row_label != "新上榜":
                continue
            if label == "重複上榜" and row_label == "新上榜":
                continue
            matched = True
            extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
            data.append(
                [
                    stock_label(row),
                    stage,
                    model_score_label(row),
                    f"{category_position_text(row, two_map)} / {zh_warrant(row.get('warrant_flow_signal'))}",
                    tdcc_direction(row, extra),
                    f"{model_source_text(row, 54)}；風險：{model_risk_text(row, 34)}",
                ]
            )
        if not matched:
            empty_text = (
                f"{MODEL_EMPTY_STATE_TEXT}；本模型今日無{label}資料。"
                if not selected_rows
                else f"本模型今日無{label}資料。"
            )
            data.append(["-", "-", title, "-", "-", empty_text])
        story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
        story.append(Paragraph(f'<font color="{color}">{label}</font>', H2))
        story.append(build_table(data, [32 * mm, 22 * mm, 30 * mm, 54 * mm, 44 * mm, 86 * mm], 12.0))
    return story




def build_mainstream_full_model_table(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    limit: int = 6,
) -> list:
    title = MAINSTREAM_LINE_LABEL
    selected_rows = rows[:limit]
    story: list = []
    for label, color in [("新上榜", "#c00000"), ("重複上榜", "#1f4e79")]:
        data = [["標的", "模型狀態", "模型排名 / 分數", "族群 / 資金", "大戶籌碼", "模型依據 / 風險"]]
        matched = False
        for row in selected_rows:
            stage = display_signal_tag(model_signal_tag(row, two_map))
            row_label = listing_status_label(row, stage)
            if label == "新上榜" and row_label != "新上榜":
                continue
            if label == "重複上榜" and row_label == "新上榜":
                continue
            matched = True
            extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
            data.append(
                [
                    stock_label(row),
                    stage,
                    model_score_label(row),
                    f"{category_position_text(row, two_map)} / {zh_warrant(row.get('warrant_flow_signal'))}",
                    tdcc_direction(row, extra),
                    f"{model_source_text(row, 54)}；風險：{model_risk_text(row, 34)}",
                ]
            )
        if not matched:
            empty_text = (
                f"{MODEL_EMPTY_STATE_TEXT}；本模型今日無{label}資料。"
                if not selected_rows
                else f"本模型今日無{label}資料。"
            )
            data.append(["-", "-", title, "-", "-", empty_text])
        story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
        story.append(Paragraph(f'<font color="{color}">{label}</font>', H2))
        story.append(build_table(data, [32 * mm, 22 * mm, 30 * mm, 54 * mm, 44 * mm, 86 * mm], 12.0))
    return story




def build_non_mainstream_curated_model_table(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    limit: int = 6,
) -> list:
    title = NON_MAINSTREAM_LINE_LABEL
    selected_rows = rows[:limit]
    story: list = []
    for label, color in [("新上榜", "#c00000"), ("重複上榜", "#1f4e79")]:
        data = [["標的", "模型狀態", "模型排名 / 分數", "族群 / 資金", "大戶籌碼", "模型依據 / 風險"]]
        matched = False
        for row in selected_rows:
            stage = display_signal_tag(model_signal_tag(row, two_map))
            row_label = listing_status_label(row, stage)
            if label == "新上榜" and row_label != "新上榜":
                continue
            if label == "重複上榜" and row_label == "新上榜":
                continue
            matched = True
            extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
            data.append(
                [
                    stock_label(row),
                    stage,
                    model_score_label(row),
                    f"{category_position_text(row, two_map)} / {zh_warrant(row.get('warrant_flow_signal'))}",
                    tdcc_direction(row, extra),
                    f"{model_source_text(row, 54)}；風險：{model_risk_text(row, 34)}",
                ]
            )
        if not matched:
            empty_text = (
                f"{MODEL_EMPTY_STATE_TEXT}；本模型今日無{label}資料。"
                if not selected_rows
                else f"本模型今日無{label}資料。"
            )
            data.append(["-", "-", title, "-", "-", empty_text])
        story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
        story.append(Paragraph(f'<font color="{color}">{label}</font>', H2))
        story.append(build_table(data, [32 * mm, 22 * mm, 30 * mm, 54 * mm, 44 * mm, 86 * mm], 12.0))
    return story




def build_non_mainstream_full_model_table(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    limit: int = 6,
) -> list:
    title = NON_MAINSTREAM_LINE_LABEL
    selected_rows = rows[:limit]
    story: list = []
    for label, color in [("新上榜", "#c00000"), ("重複上榜", "#1f4e79")]:
        data = [["標的", "模型狀態", "模型排名 / 分數", "族群 / 資金", "大戶籌碼", "模型依據 / 風險"]]
        matched = False
        for row in selected_rows:
            stage = display_signal_tag(model_signal_tag(row, two_map))
            row_label = listing_status_label(row, stage)
            if label == "新上榜" and row_label != "新上榜":
                continue
            if label == "重複上榜" and row_label == "新上榜":
                continue
            matched = True
            extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
            data.append(
                [
                    stock_label(row),
                    stage,
                    model_score_label(row),
                    f"{category_position_text(row, two_map)} / {zh_warrant(row.get('warrant_flow_signal'))}",
                    tdcc_direction(row, extra),
                    f"{model_source_text(row, 54)}；風險：{model_risk_text(row, 34)}",
                ]
            )
        if not matched:
            empty_text = (
                f"{MODEL_EMPTY_STATE_TEXT}；本模型今日無{label}資料。"
                if not selected_rows
                else f"本模型今日無{label}資料。"
            )
            data.append(["-", "-", title, "-", "-", empty_text])
        story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
        story.append(Paragraph(f'<font color="{color}">{label}</font>', H2))
        story.append(build_table(data, [32 * mm, 22 * mm, 30 * mm, 54 * mm, 44 * mm, 86 * mm], 12.0))
    return story





def mainstream_curated_recommendation_rows(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
    limit: int = 8,
) -> list[list]:
    line = "mainstream"
    line_label = MAINSTREAM_LINE_LABEL
    rows = [["分線", "模型", "標的", "模型分數 / 風險"]]
    seen: set[tuple[str, str]] = set()
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        for row in model_signal_rows(inputs, model_id, line):
            sid = clean(row.get("stock_id"))
            key = (sid, model_id)
            if not sid or key in seen:
                continue
            rows.append(
                [
                    red(line_label),
                    red(model_name),
                    red(stock_label(row)),
                    f"{escape_html(model_score_label(row))}<br/>風險：{escape_html(model_risk_text(row, 62))}",
                ]
            )
            seen.add(key)
            if len(rows) > limit:
                return rows
    return rows






def non_mainstream_curated_recommendation_rows(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
    limit: int = 8,
) -> list[list]:
    line = "non_mainstream"
    line_label = NON_MAINSTREAM_LINE_LABEL
    rows = [["分線", "模型", "標的", "模型分數 / 風險"]]
    seen: set[tuple[str, str]] = set()
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        for row in model_signal_rows(inputs, model_id, line):
            sid = clean(row.get("stock_id"))
            key = (sid, model_id)
            if not sid or key in seen:
                continue
            rows.append(
                [
                    red(line_label),
                    red(model_name),
                    red(stock_label(row)),
                    f"{escape_html(model_score_label(row))}<br/>風險：{escape_html(model_risk_text(row, 62))}",
                ]
            )
            seen.add(key)
            if len(rows) > limit:
                return rows
    return rows







def listing_status_label(row: pd.Series, stage: str) -> str:
    text_parts = [
        stage,
        row.get("listing_status_zh"),
        row.get("appearance_status_zh"),
        row.get("signal_repeat_status_zh"),
        row.get("repeat_signal_label_zh"),
        row.get("repeat_status_zh"),
        row.get("same_model_repeat_status_zh"),
        row.get("model_stage_zh"),
        row.get("signal_stage_zh"),
    ]
    text = " ".join(clean(part) for part in text_parts if clean(part))
    lower_text = text.lower()
    if "重複" in text or "repeat" in lower_text:
        return "重複上榜"
    if "新上榜" in text or "新進" in text or "new" in lower_text:
        return "新上榜"
    return "未標示"


def listing_status_sort_key(label: str) -> int:
    order = {"新上榜": 0, "重複上榜": 1}
    return order.get(label, 2)


def mainstream_curated_front_observation_rows(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
    limit: int | None = None,
) -> list[list]:
    line = "mainstream"
    line_label = MAINSTREAM_LINE_LABEL
    target_limit = limit if limit is not None else FRONT_MAINSTREAM_LIMIT
    rows = [["榜別", "模型", "股票", "模型狀態", "分數 / 風險"]]
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        model_rows = 0
        model_display_rows: list[tuple[int, int, list]] = []
        for row in model_signal_rows(inputs, model_id, line):
            sid = clean(row.get("stock_id"))
            extra = all_map.get(sid, pd.Series(dtype=object))
            stage = model_stage_label(row, extra) or display_signal_tag(model_signal_tag(row, two_map, vol_map or {}))
            reminder = (
                row.get("next_confirmation_zh")
                or row.get("why_selected_human_zh")
                or row.get("why_selected_zh")
                or row.get("why_selected")
                or observation_focus(row, extra)
            )
            listing_label = listing_status_label(row, stage)
            model_display_rows.append(
                (
                    listing_status_sort_key(listing_label),
                    model_rows,
                    [
                        listing_label,
                        red(model_name),
                        stock_label(row),
                        stage,
                        f"{escape_html(model_score_label(row))}<br/>風險：{escape_html(model_risk_text(row, 48))}<br/>{escape_html(short(reminder, 54))}",
                    ],
                )
            )
            model_rows += 1
            if model_rows >= target_limit:
                break
        for _, _, row_data in sorted(model_display_rows, key=lambda item: (item[0], item[1])):
            rows.append(row_data)
        if model_rows == 0:
            rows.append(["-", red(model_name), "-", "-", f"{escape_html(line_label)}目前無符合觀察列"])
    return rows




def non_mainstream_curated_front_observation_rows(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
    limit: int | None = None,
) -> list[list]:
    line = "non_mainstream"
    line_label = NON_MAINSTREAM_LINE_LABEL
    target_limit = limit if limit is not None else FRONT_NON_MAINSTREAM_LIMIT
    rows = [["榜別", "模型", "股票", "模型狀態", "分數 / 風險"]]
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        model_rows = 0
        model_display_rows: list[tuple[int, int, list]] = []
        for row in model_signal_rows(inputs, model_id, line):
            sid = clean(row.get("stock_id"))
            extra = all_map.get(sid, pd.Series(dtype=object))
            stage = model_stage_label(row, extra) or display_signal_tag(model_signal_tag(row, two_map, vol_map or {}))
            reminder = (
                row.get("next_confirmation_zh")
                or row.get("why_selected_human_zh")
                or row.get("why_selected_zh")
                or row.get("why_selected")
                or observation_focus(row, extra)
            )
            listing_label = listing_status_label(row, stage)
            model_display_rows.append(
                (
                    listing_status_sort_key(listing_label),
                    model_rows,
                    [
                        listing_label,
                        red(model_name),
                        stock_label(row),
                        stage,
                        f"{escape_html(model_score_label(row))}<br/>風險：{escape_html(model_risk_text(row, 48))}<br/>{escape_html(short(reminder, 54))}",
                    ],
                )
            )
            model_rows += 1
            if model_rows >= target_limit:
                break
        for _, _, row_data in sorted(model_display_rows, key=lambda item: (item[0], item[1])):
            rows.append(row_data)
        if model_rows == 0:
            rows.append(["-", red(model_name), "-", "-", f"{escape_html(line_label)}目前無符合觀察列"])
    return rows





def append_mainstream_curated_group_rotation_end_section(story: list, inputs: dict[str, pd.DataFrame], limit: int = 18) -> None:
    group_rotation = inputs.get("group_rotation", pd.DataFrame()).copy()
    if group_rotation.empty:
        return
    if "theme_resolution_status" in group_rotation.columns:
        group_rotation = group_rotation[group_rotation["theme_resolution_status"].astype(str).eq("resolved")].copy()
    if group_rotation.empty:
        return
    append_page_break_once(story)
    story.append(Paragraph("資金進入族群觀察", H1))
    story.append(
        para(
            "本表只作族群資金擴散與慢速進場觀察；需等個股模型觸發後，才可成為個股進場依據。",
            BODY_SMALL,
        )
    )
    rows = [["族群", "模型", "族群股票數", "慢速進場", "量能擴散", "15日/30日", "領先股", "判讀"]]
    for _, r in group_rotation.head(limit).iterrows():
        leaders = " / ".join(
            [clean(r.get("leader_1")), clean(r.get("leader_2")), clean(r.get("leader_3"))]
        )
        leaders = leaders.strip(" /")
        rows.append(
            [
                clean(r.get("theme_display_zh") or r.get("theme")),
                clean(r.get("rotation_model_name") or r.get("rotation_model_id")),
                num(r.get("stock_count"), 0),
                f"{num(r.get('slow_inflow_count'), 0)} / {num(r.get('slow_inflow_ratio'), 2)}",
                f"3x:{num(r.get('volume_expansion_3x_count'), 0)} / 1.5x:{num(r.get('volume_expansion_1_5x_count'), 0)}",
                f"{num(r.get('median_return_15d'), 1)}% / {num(r.get('median_return_30d'), 1)}%",
                leaders,
                short(r.get("interpretation_zh") or r.get("interpretation") or r.get("diffusion_status_zh"), 95),
            ]
        )
    story.append(build_table(rows, [26 * mm, 32 * mm, 18 * mm, 24 * mm, 34 * mm, 28 * mm, 46 * mm, 60 * mm], 11.0))












def append_mainstream_full_group_rotation_end_section(story: list, inputs: dict[str, pd.DataFrame], limit: int = 18) -> None:
    group_rotation = inputs.get("group_rotation", pd.DataFrame()).copy()
    if group_rotation.empty:
        return
    if "theme_resolution_status" in group_rotation.columns:
        group_rotation = group_rotation[group_rotation["theme_resolution_status"].astype(str).eq("resolved")].copy()
    if group_rotation.empty:
        return
    append_page_break_once(story)
    story.append(Paragraph("資金進入族群觀察", H1))
    story.append(
        para(
            "本表只作族群資金擴散與慢速進場觀察；需等個股模型觸發後，才可成為個股進場依據。",
            BODY_SMALL,
        )
    )
    rows = [["族群", "模型", "族群股票數", "慢速進場", "量能擴散", "15日/30日", "領先股", "判讀"]]
    for _, r in group_rotation.head(limit).iterrows():
        leaders = " / ".join(
            [clean(r.get("leader_1")), clean(r.get("leader_2")), clean(r.get("leader_3"))]
        )
        leaders = leaders.strip(" /")
        rows.append(
            [
                clean(r.get("theme_display_zh") or r.get("theme")),
                clean(r.get("rotation_model_name") or r.get("rotation_model_id")),
                num(r.get("stock_count"), 0),
                f"{num(r.get('slow_inflow_count'), 0)} / {num(r.get('slow_inflow_ratio'), 2)}",
                f"3x:{num(r.get('volume_expansion_3x_count'), 0)} / 1.5x:{num(r.get('volume_expansion_1_5x_count'), 0)}",
                f"{num(r.get('median_return_15d'), 1)}% / {num(r.get('median_return_30d'), 1)}%",
                leaders,
                short(r.get("interpretation_zh") or r.get("interpretation") or r.get("diffusion_status_zh"), 95),
            ]
        )
    story.append(build_table(rows, [26 * mm, 32 * mm, 18 * mm, 24 * mm, 34 * mm, 28 * mm, 46 * mm, 60 * mm], 11.0))












def append_non_mainstream_curated_group_rotation_end_section(story: list, inputs: dict[str, pd.DataFrame], limit: int = 18) -> None:
    group_rotation = inputs.get("group_rotation", pd.DataFrame()).copy()
    if group_rotation.empty:
        return
    if "theme_resolution_status" in group_rotation.columns:
        group_rotation = group_rotation[group_rotation["theme_resolution_status"].astype(str).eq("resolved")].copy()
    if group_rotation.empty:
        return
    append_page_break_once(story)
    story.append(Paragraph("資金進入族群觀察", H1))
    story.append(
        para(
            "本表只作族群資金擴散與慢速進場觀察；需等個股模型觸發後，才可成為個股進場依據。",
            BODY_SMALL,
        )
    )
    rows = [["族群", "模型", "族群股票數", "慢速進場", "量能擴散", "15日/30日", "領先股", "判讀"]]
    for _, r in group_rotation.head(limit).iterrows():
        leaders = " / ".join(
            [clean(r.get("leader_1")), clean(r.get("leader_2")), clean(r.get("leader_3"))]
        )
        leaders = leaders.strip(" /")
        rows.append(
            [
                clean(r.get("theme_display_zh") or r.get("theme")),
                clean(r.get("rotation_model_name") or r.get("rotation_model_id")),
                num(r.get("stock_count"), 0),
                f"{num(r.get('slow_inflow_count'), 0)} / {num(r.get('slow_inflow_ratio'), 2)}",
                f"3x:{num(r.get('volume_expansion_3x_count'), 0)} / 1.5x:{num(r.get('volume_expansion_1_5x_count'), 0)}",
                f"{num(r.get('median_return_15d'), 1)}% / {num(r.get('median_return_30d'), 1)}%",
                leaders,
                short(r.get("interpretation_zh") or r.get("interpretation") or r.get("diffusion_status_zh"), 95),
            ]
        )
    story.append(build_table(rows, [26 * mm, 32 * mm, 18 * mm, 24 * mm, 34 * mm, 28 * mm, 46 * mm, 60 * mm], 11.0))












def append_non_mainstream_full_group_rotation_end_section(story: list, inputs: dict[str, pd.DataFrame], limit: int = 18) -> None:
    group_rotation = inputs.get("group_rotation", pd.DataFrame()).copy()
    if group_rotation.empty:
        return
    if "theme_resolution_status" in group_rotation.columns:
        group_rotation = group_rotation[group_rotation["theme_resolution_status"].astype(str).eq("resolved")].copy()
    if group_rotation.empty:
        return
    append_page_break_once(story)
    story.append(Paragraph("資金進入族群觀察", H1))
    story.append(
        para(
            "本表只作族群資金擴散與慢速進場觀察；需等個股模型觸發後，才可成為個股進場依據。",
            BODY_SMALL,
        )
    )
    rows = [["族群", "模型", "族群股票數", "慢速進場", "量能擴散", "15日/30日", "領先股", "判讀"]]
    for _, r in group_rotation.head(limit).iterrows():
        leaders = " / ".join(
            [clean(r.get("leader_1")), clean(r.get("leader_2")), clean(r.get("leader_3"))]
        )
        leaders = leaders.strip(" /")
        rows.append(
            [
                clean(r.get("theme_display_zh") or r.get("theme")),
                clean(r.get("rotation_model_name") or r.get("rotation_model_id")),
                num(r.get("stock_count"), 0),
                f"{num(r.get('slow_inflow_count'), 0)} / {num(r.get('slow_inflow_ratio'), 2)}",
                f"3x:{num(r.get('volume_expansion_3x_count'), 0)} / 1.5x:{num(r.get('volume_expansion_1_5x_count'), 0)}",
                f"{num(r.get('median_return_15d'), 1)}% / {num(r.get('median_return_30d'), 1)}%",
                leaders,
                short(r.get("interpretation_zh") or r.get("interpretation") or r.get("diffusion_status_zh"), 95),
            ]
        )
    story.append(build_table(rows, [26 * mm, 32 * mm, 18 * mm, 24 * mm, 34 * mm, 28 * mm, 46 * mm, 60 * mm], 11.0))













def matches_line(row: pd.Series, two_map: dict[str, pd.Series], line: str) -> bool:
    return is_core_mainstream_row(row, two_map) if line == "mainstream" else not is_core_mainstream_row(row, two_map)


def filter_theme_rows_for_line(themes: pd.DataFrame, line: str) -> pd.DataFrame:
    if themes.empty:
        return themes
    if line == "mainstream":
        mask = themes.get("theme_structural_status", pd.Series(dtype=str)).astype(str).eq("core_mainstream_theme")
    else:
        mask = ~themes.get("theme_structural_status", pd.Series(dtype=str)).astype(str).eq("core_mainstream_theme")
    return themes[mask].copy()


def mainstream_curated_operation_representatives(
    ranked_rows: list[pd.Series],
    total_limit: int = 3,
) -> list[pd.Series]:
    return list(ranked_rows[:total_limit])


def non_mainstream_curated_operation_representatives(
    ranked_rows: list[pd.Series],
    total_limit: int = 1,
) -> list[pd.Series]:
    return list(ranked_rows[:total_limit])


def category_position_text(row: pd.Series, two_map: dict[str, pd.Series]) -> str:
    source, _, group, _ = line_source(row, two_map)
    structural, label = line_structure(row, two_map)
    _, status = line_raw(row, two_map)
    if is_core_mainstream_row(row, two_map):
        return "主流族群，資金線較完整。"
    if source == RISK_SOURCE or group == "risk":
        return "風險線，條件回復前只列風險摘要。"
    if structural == "non_mainstream_theme" or group == "non_mainstream_flow_watch":
        return "非主流族群，只追蹤輪動延續。"
    if source == LATENT_SOURCE:
        return "個股訊號，只看個股確認。"
    if status == "emerging_theme":
        return "早期題材，要等族群擴散。"
    if "overheated" in status or "overheated" in label:
        return "短線過熱，先等回測。"
    return "資料不足，只能觀察。"


def drawback_brief(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> str:
    explicit = first_text(row.get("why_downgraded"), row.get("risk_tags"), row.get("downgrade_flags"))
    if explicit:
        text = clean(explicit).lower()
        raw = clean(explicit)
        if "distribution" in text or "派發" in raw:
            return "籌碼派發警示"
        if "false_breakout" in text or "假突破" in raw or "漲幅過低" in raw:
            return "漲幅過低"
        if "overheat" in text or "過熱" in raw or "已反應" in raw:
            return "短線過熱或利多已反應"
        if "資料不足" in raw or "data" in text:
            return "資料不足"
        if "repeated_but_no_breakout" not in text and "反覆上榜" not in raw and "連續上榜" not in raw:
            return short(raw, 72)
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    if "overheated" in status or "overheated" in label:
        return "短線漲幅或量能過熱，先等回測或重新確認"
    if structural != "core_mainstream_theme" or group == "non_mainstream_flow_watch":
        return "非主流，族群延續性不足"
    if source == RISK_SOURCE or group == "risk":
        return "已進風險線，條件回復前只列風險摘要"
    if status not in MAINSTREAM_THEME_STATUSES:
        return "主流資金未確認"
    return "模型未列明重大風險，仍需追蹤關鍵價位"


def observation_focus(row: pd.Series, extra: pd.Series) -> str:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    level_label, level_text, close_value = key_level_context(row, extra)
    close = num(first_text(row.get("close"), source.get("close")))
    level_value = to_float(level_text)
    repeated = first_text(row.get("why_downgraded"), row.get("risk_tags"), row.get("downgrade_flags"))
    if "repeated_but_no_breakout" in clean(repeated).lower() or "反覆上榜" in clean(repeated) or "連續上榜" in clean(repeated):
        if level_label == "短線壓力" and level_text:
            return f"反覆上榜但尚未突破，等收盤放量站上 {level_text}。"
        if level_label == "短線支撐" and level_text:
            return f"已在 {level_text} 上方，但反覆上榜尚未轉強；跌回才降級，未跌回不代表買前條件未成立。"
        return "反覆上榜但尚未突破，等有效突破再看。"
    if level_label == "短線支撐" and level_text:
        return f"已收盤站上短線支撐 {level_text}；後續跌回才降級。"
    if level_label == "短線壓力" and level_text:
        return f"尚未突破短線壓力 {level_text}；等收盤放量站上。"
    if level_label == "關鍵價" and level_text:
        if close_value is not None and level_value is not None and close_value >= level_value:
            return f"已收盤站上關鍵價 {level_text}；後續跌回才降級。"
        return f"尚未站上關鍵價 {level_text}；等收盤放量站上。"
    if close:
        return f"先看收盤 {close} 附近能否守住，等待下一根確認K。"
    return "等待價格與成交量重新確認。"


def nearby_price_levels(row: pd.Series, extra: pd.Series) -> tuple[list[float], list[float], float | None]:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    close_value = to_float(first_text(row.get("close"), source.get("close")))
    if close_value is None:
        return [], [], None

    support_candidates = [
        source.get("neckline_price"),
        source.get("platform_high"),
        source.get("platform_low"),
        source.get("short_platform_low"),
        source.get("previous_20d_low"),
        source.get("ema23"),
        source.get("ma20"),
        source.get("ma60"),
    ]
    pressure_candidates = [
        source.get("neckline_price"),
        source.get("platform_high"),
        source.get("short_platform_high"),
        source.get("previous_20d_high"),
        source.get("previous_60d_high"),
        source.get("previous_high"),
        source.get("high_20"),
        source.get("high_60"),
    ]

    supports: list[float] = []
    pressures: list[float] = []
    tolerance = max(abs(close_value) * 0.003, 0.01)
    for value in support_candidates:
        level = to_float(value)
        if level is not None and level < close_value - tolerance:
            supports.append(level)
    for value in pressure_candidates:
        level = to_float(value)
        if level is not None and level > close_value + tolerance:
            pressures.append(level)

    supports = sorted(set(round(v, 2) for v in supports), reverse=True)[:2]
    pressures = sorted(set(round(v, 2) for v in pressures))[:2]
    return supports, pressures, close_value


def price_plan_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, close_value = nearby_price_levels(row, extra)
    parts = [f"收盤 {num(close_value)}" if close_value is not None else ""]
    level_label, level_text, _ = key_level_context(row, extra)
    if level_label == "關鍵價" and level_text:
        parts.append(f"關鍵價 {level_text}")
    if supports:
        parts.append("支撐 " + " / ".join(num(v) for v in supports))
    if pressures:
        parts.append("壓力 " + " / ".join(num(v) for v in pressures))
    return " / ".join([p for p in parts if p]) or "關鍵價資料不足"


def next_confirmation_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, close_value = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    level_value = to_float(level_text)
    if level_label == "短線壓力" and level_text:
        return f"收盤放量站上壓力 {level_text}，模型強度才算延續。"
    if level_label == "短線支撐" and level_text:
        return f"已站在支撐 {level_text} 上方；後續需量價維持，不追急拉。"
    if level_label == "關鍵價" and level_text:
        if close_value is not None and level_value is not None and close_value >= level_value:
            return f"已站上關鍵價 {level_text}；後續需量價維持。"
        return f"收盤站上關鍵價 {level_text}，模型強度才算延續。"
    if pressures:
        return f"收盤站上壓力 {num(pressures[0])}，模型強度才算延續。"
    if supports:
        return f"守住支撐 {num(supports[0])}，並出現轉強K線，模型強度才算延續。"
    return "等待收盤站上關鍵價，且成交量延續。"


def invalidation_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, _ = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    level_value = to_float(level_text)
    close_value = to_float(first_text(row.get("close"), extra.get("close") if isinstance(extra, pd.Series) else ""))
    if level_label == "關鍵價" and level_text:
        if close_value is not None and level_value is not None and close_value >= level_value:
            return f"跌破關鍵價 {level_text}，模型延續性失效。"
        return f"收盤未站上關鍵價 {level_text}，模型強度不足。"
    if supports:
        return f"跌破支撐 {num(supports[0])}，模型延續性失效。"
    if pressures:
        return f"只碰壓力 {num(pressures[0])} 但收盤站不上，模型強度不足。"
    return "價格未站穩關鍵價，或爆量長上影，列為風險升高。"


def tracking_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, _ = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    if level_label == "關鍵價" and level_text:
        return f"跌破關鍵價 {level_text} 視為模型失效；急拉長上影列風險升高。"
    if supports and pressures:
        return f"靠近壓力 {num(pressures[0])} 轉弱列風險升高；跌破支撐 {num(supports[0])} 視為模型失效。"
    if supports:
        return f"跌破支撐 {num(supports[0])} 視為模型失效；急拉長上影列風險升高。"
    if pressures:
        return f"靠近壓力 {num(pressures[0])} 量縮或長上影，列風險升高。"
    return "跌回確認區或量能失控，視為模型失效。"


def operation_cell_text(value, limit: int = 110) -> str:
    text = short(value, limit).replace("；", " / ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def operation_cell_markup(value, highlights: list[str] | None = None, limit: int = 110) -> str:
    text = operation_cell_text(value, limit)
    escaped = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for item in highlights or []:
        key = operation_cell_text(item, 40)
        if not key:
            continue
        safe_key = key.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        escaped = escaped.replace(safe_key, red(key), 1)
    return escaped


def model_signal_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
    extra: pd.Series,
) -> tuple[str, list[str]]:
    tag = display_signal_tag(model_signal_tag(row, two_map, vol_map or {}))
    text = f"{tag}；{model_score_label(row)}。{observation_focus(row, extra)}"
    return text, [tag, "模型"]


def operation_confirmation_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
    extra: pd.Series,
) -> tuple[str, list[str]]:
    return next_confirmation_summary(row, extra), ["確認", "模型"]


def operation_invalidation_sentence(row: pd.Series, extra: pd.Series) -> str:
    return invalidation_summary(row, extra)


def operation_tracking_sentence(row: pd.Series, extra: pd.Series) -> str:
    return tracking_summary(row, extra)


def operation_risk_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
) -> str:
    risk = drawback_brief(row, two_map, vol_map)
    if risk == "模型未列明重大風險，仍需追蹤關鍵價位":
        return risk
    return risk


def operation_tdcc_sentence(row: pd.Series, extra: pd.Series) -> str:
    direction = tdcc_direction(row, extra)
    label = direction.split("：", 1)[-1] if "：" in direction else direction
    weeks = num(series_value(row, extra, "tdcc_weeks_used"), 0)
    c400_value = to_float(series_value(row, extra, "tdcc_400_change_sum"))
    c1000_value = to_float(series_value(row, extra, "tdcc_1000_change_sum"))
    sid = clean(series_value(row, extra, "stock_id"))
    latest = latest_tdcc_window_row(sid)
    has_800 = bool(num(latest.get("over_800_ratio"), 2, "%"))
    has_1000 = bool(num(latest.get("over_1000_ratio"), 2, "%"))

    if c400_value is not None and c1000_value is not None and c400_value > 0 and c1000_value > 0:
        sync = "400張以上與1000張以上同步增加"
    elif c1000_value is not None and c1000_value > 0:
        sync = "1000張以上大戶增加"
    elif c400_value is not None and c400_value > 0:
        sync = "400張以上大戶增加，但高門檻同步性較弱"
    elif (c400_value is not None and c400_value < 0) or (c1000_value is not None and c1000_value < 0):
        sync = "大戶持股減少"
    else:
        sync = "大戶持股變化不明顯"

    parts = [f"大戶籌碼：{label}。"]
    if weeks and (c400_value is not None or c1000_value is not None):
        parts.append(f"近{weeks}週{sync}。")
    else:
        parts.append(sync + "。")
    if has_800 and has_1000:
        parts.append("800張以上與1000張以上高門檻大戶仍有支撐。")
    elif has_1000:
        parts.append("1000張以上高門檻大戶仍有支撐。")
    elif has_800:
        parts.append("800張以上大戶仍有支撐。")
    if label in {"強正向", "正向"}:
        parts.append("籌碼加分，但仍需價格站穩。")
    elif label in {"負向", "強負向"}:
        parts.append("籌碼扣分，警示解除前只列風險摘要。")
    elif label == "中性":
        parts.append("籌碼不構成主要加分。")
    else:
        parts.append("資料不足，只能回到價格與量能確認。")
    return " ".join(parts)


def build_mainstream_curated_operation_page(
    row: pd.Series,
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    story: list,
    vol_map: dict[str, pd.Series] | None = None,
) -> None:
    sid = clean(row.get("stock_id"))
    name = clean(row.get("stock_name"))
    extra = all_map.get(sid, pd.Series(dtype=object))
    chart = plot_stock_chart(sid, name, extra, row)

    signal_text, signal_marks = model_signal_sentence(row, two_map, vol_map, extra)
    confirmation_text, confirmation_marks = operation_confirmation_sentence(row, two_map, vol_map, extra)
    op_rows = [
        ["模型狀態", signal_text, signal_marks, 112],
        ["優點", selection_brief(row, extra), ["成交量放大", "籌碼", "突破"], 106],
        ["關鍵價位", price_plan_summary(row, extra), ["支撐", "壓力"], 98],
        ["下一確認", confirmation_text, confirmation_marks, 112],
        ["失效條件", operation_invalidation_sentence(row, extra), ["失效", "風險"], 100],
        ["追蹤重點", operation_tracking_sentence(row, extra), ["模型失效", "風險"], 104],
        ["主要風險", operation_risk_sentence(row, two_map, vol_map), ["風險"], 94],
        ["籌碼", operation_tdcc_sentence(row, extra), ["強正向", "強負向", "正向", "負向"], 150],
    ]
    paired_rows = []
    for idx in range(0, len(op_rows), 2):
        left_item = op_rows[idx]
        right_item = op_rows[idx + 1] if idx + 1 < len(op_rows) else ["", "", [], 80]
        paired_rows.append(
            [
                rich_para(left_item[0], OP_LABEL),
                rich_para(operation_cell_markup(left_item[1], left_item[2], left_item[3]), OP_VALUE),
                rich_para(right_item[0], OP_LABEL),
                rich_para(operation_cell_markup(right_item[1], right_item[2], right_item[3]), OP_VALUE),
            ]
        )
    op_table = Table(
        paired_rows,
        colWidths=[22 * mm, 111 * mm, 22 * mm, 111 * mm],
        splitByRow=1,
    )
    op_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d9d9d9")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#fff2f2")),
                ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#fff2f2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    if chart and chart.exists():
        img = Image(str(chart), width=266 * mm, height=111 * mm)
    else:
        img = para("K線圖：資料不足 / 僅能觀察", BODY)
    chart_table = Table([[img]], colWidths=[266 * mm])
    chart_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#cccccc")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(
        KeepTogether(
            [
                Paragraph(f"{sid} {name}｜{model_display(row)}", H2),
                op_table,
                Spacer(1, 4),
                chart_table,
            ]
        )
    )
    story.append(PageBreak())








def build_non_mainstream_curated_operation_page(
    row: pd.Series,
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    story: list,
    vol_map: dict[str, pd.Series] | None = None,
) -> None:
    sid = clean(row.get("stock_id"))
    name = clean(row.get("stock_name"))
    extra = all_map.get(sid, pd.Series(dtype=object))
    chart = plot_stock_chart(sid, name, extra, row)

    signal_text, signal_marks = model_signal_sentence(row, two_map, vol_map, extra)
    confirmation_text, confirmation_marks = operation_confirmation_sentence(row, two_map, vol_map, extra)
    op_rows = [
        ["模型狀態", signal_text, signal_marks, 112],
        ["優點", selection_brief(row, extra), ["成交量放大", "籌碼", "突破"], 106],
        ["關鍵價位", price_plan_summary(row, extra), ["支撐", "壓力"], 98],
        ["下一確認", confirmation_text, confirmation_marks, 112],
        ["失效條件", operation_invalidation_sentence(row, extra), ["失效", "風險"], 100],
        ["追蹤重點", operation_tracking_sentence(row, extra), ["模型失效", "風險"], 104],
        ["主要風險", operation_risk_sentence(row, two_map, vol_map), ["風險"], 94],
        ["籌碼", operation_tdcc_sentence(row, extra), ["強正向", "強負向", "正向", "負向"], 150],
    ]
    paired_rows = []
    for idx in range(0, len(op_rows), 2):
        left_item = op_rows[idx]
        right_item = op_rows[idx + 1] if idx + 1 < len(op_rows) else ["", "", [], 80]
        paired_rows.append(
            [
                rich_para(left_item[0], OP_LABEL),
                rich_para(operation_cell_markup(left_item[1], left_item[2], left_item[3]), OP_VALUE),
                rich_para(right_item[0], OP_LABEL),
                rich_para(operation_cell_markup(right_item[1], right_item[2], right_item[3]), OP_VALUE),
            ]
        )
    op_table = Table(
        paired_rows,
        colWidths=[22 * mm, 111 * mm, 22 * mm, 111 * mm],
        splitByRow=1,
    )
    op_table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#d9d9d9")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#fff2f2")),
                ("BACKGROUND", (2, 0), (2, -1), colors.HexColor("#fff2f2")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    if chart and chart.exists():
        img = Image(str(chart), width=266 * mm, height=111 * mm)
    else:
        img = para("K線圖：資料不足 / 僅能觀察", BODY)
    chart_table = Table([[img]], colWidths=[266 * mm])
    chart_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("BOX", (0, 0), (-1, -1), 0.25, colors.HexColor("#cccccc")),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(
        KeepTogether(
            [
                Paragraph(f"{sid} {name}｜{model_display(row)}", H2),
                op_table,
                Spacer(1, 4),
                chart_table,
            ]
        )
    )
    story.append(PageBreak())









def build_mainstream_curated_pdf(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series],
) -> Path:
    line = "mainstream"
    title = MAINSTREAM_CURATED_TITLE
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} {title}", TITLE),
        date_note(),
        Spacer(1, 4),
    ]

    operation_seen: set[str] = set()
    started_model_sections = False
    limit = MAIN_REPORT_MAINSTREAM_LIMIT
    for spec in highlight_specs_in_layout_order(mainstream_curated_core_model_specs(inputs)):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        ranked_rows = mainstream_curated_model_signal_rows(inputs, model_id)
        if started_model_sections:
            append_page_break_once(story)
        story.append(Paragraph(model_name, H1))
        started_model_sections = True
        desc = clean(spec.get("model_description_zh"))
        if desc and should_render_highlight_model_description(model_id):
            story.append(para(desc, BODY_SMALL))
        if render_model_operation_section_if_applicable(story, inputs, model_id, "highlight", line):
            continue
        story.extend(build_mainstream_curated_model_table(ranked_rows, two_map, all_map, limit=limit))
        reps = mainstream_curated_operation_representatives(ranked_rows)
        for row in reps:
            sid = clean(row.get("stock_id"))
            if sid and sid in operation_seen:
                continue
            build_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)
            if sid:
                operation_seen.add(sid)

    append_mainstream_curated_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out




def build_non_mainstream_curated_pdf(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series],
) -> Path:
    line = "non_mainstream"
    title = NON_MAINSTREAM_CURATED_TITLE
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} {title}", TITLE),
        date_note(),
        Spacer(1, 4),
    ]

    operation_seen: set[str] = set()
    started_model_sections = False
    limit = MAIN_REPORT_NON_MAINSTREAM_LIMIT
    for spec in highlight_specs_in_layout_order(non_mainstream_curated_core_model_specs(inputs)):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        ranked_rows = non_mainstream_curated_model_signal_rows(inputs, model_id)
        if started_model_sections:
            append_page_break_once(story)
        story.append(Paragraph(model_name, H1))
        started_model_sections = True
        desc = clean(spec.get("model_description_zh"))
        if desc and should_render_highlight_model_description(model_id):
            story.append(para(desc, BODY_SMALL))
        if render_model_operation_section_if_applicable(story, inputs, model_id, "highlight", line):
            continue
        story.extend(build_non_mainstream_curated_model_table(ranked_rows, two_map, all_map, limit=limit))
        reps = non_mainstream_curated_operation_representatives(ranked_rows)
        for row in reps:
            sid = clean(row.get("stock_id"))
            if sid and sid in operation_seen:
                continue
            build_non_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)
            if sid:
                operation_seen.add(sid)

    append_non_mainstream_curated_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out





def build_mainstream_full_candidate_pdf(
    inputs: dict[str, pd.DataFrame],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
) -> Path:
    line = "mainstream"
    title = MAINSTREAM_FULL_TITLE
    line_label = MAINSTREAM_LINE_LABEL
    model_signals = inputs.get("model_signals", pd.DataFrame()).copy()
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} {title}", TITLE),
        date_note(),
        Spacer(1, 4),
        Paragraph(f"{line_label}族群與候選摘要", H1),
    ]
    themes = filter_theme_rows_for_line(inputs["themes"], line)
    if not themes.empty:
        rows = [["族群", "候選數", "嚴格突破", "營收", "TDCC", "權證", "正式狀態"]]
        for _, r in themes.head(18).iterrows():
            rows.append(
                [
                    zh_theme_name(r.get("theme_name")),
                    num(r.get("candidate_count"), 0),
                    num(r.get("strict_breakout_count"), 0),
                    num(r.get("revenue_count"), 0),
                    num(r.get("tdcc_positive_count") or r.get("tdcc_strength_count"), 0),
                    num(r.get("warrant_positive_count") or r.get("warrant_strength_count"), 0),
                    f"{zh_theme_status(r.get('theme_final_status'))} / {zh_structural_status(r.get('theme_structural_status'))} / {zh_mainstream_label(r.get('theme_mainstream_label'))}",
                ]
            )
        story.append(build_table(rows, [40 * mm, 18 * mm, 22 * mm, 18 * mm, 22 * mm, 22 * mm, 126 * mm], 12.0))
    else:
        story.append(para("本分流沒有可用的族群摘要資料。", BODY))

    story.append(Paragraph(f"{line_label}TDCC 重點", H1))
    tdcc_rows = [["標的", "模型/來源", "模型分數 / 狀態", "TDCC 摘要"]]
    seen_tdcc: set[str] = set()
    for _, r in sort_model_frame(model_signals, two_map).iterrows():
        sid = clean(r.get("stock_id"))
        if not sid or sid in seen_tdcc or not matches_line(r, two_map, line):
            continue
        extra = all_map.get(sid, pd.Series(dtype=object))
        detail = tdcc_detail(r, extra)
        if "TDCC資料不足" in detail:
            continue
        tdcc_rows.append(
            [
                stock_label(r),
                preferred_model_label_for_stock(inputs, sid, line) or "模型訊號未對應",
                f"{model_score_label(r)} / {display_signal_tag(model_signal_tag(r, two_map))}",
                short(detail, 180),
            ]
        )
        seen_tdcc.add(sid)
        if len(tdcc_rows) >= 19:
            break
    story.append(build_table(tdcc_rows, [34 * mm, 42 * mm, 22 * mm, 170 * mm], 12.0) if len(tdcc_rows) > 1 else para("本分流沒有可用的 TDCC 摘要。", BODY))

    story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))
    story.append(Paragraph(f"{line_label}完整候選", H1))
    limit = FULL_REPORT_MAINSTREAM_LIMIT
    for spec in mainstream_full_core_model_specs(inputs):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        line_rows = mainstream_full_model_signal_rows(inputs, model_id)
        story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))
        story.append(Paragraph(model_name, H2))
        if render_model_operation_section_if_applicable(story, inputs, model_id, "full", line):
            continue
        story.extend(build_mainstream_full_model_table(line_rows, two_map, all_map, limit=limit))

    story.append(PageBreak())
    story.append(Paragraph(f"{line_label}雙線與輪動摘要", H1))
    two_line = inputs["two_line"]
    if not two_line.empty:
        found_any = False
        for group in [
            "mainstream_leader_stock",
            "mainstream_follow_through_stock",
            "two_line_overlap",
            "non_mainstream_flow_watch",
            "individual_tdcc_latent_watch",
            "individual_revenue_low_response_watch",
            "individual_pattern_watch",
            "risk",
        ]:
            sub = two_line[two_line["candidate_line_group"].astype(str) == group].copy()
            if not sub.empty:
                sub = sub[sub.apply(lambda r: matches_line(r, two_map, line), axis=1)].head(14)
            if sub.empty:
                continue
            found_any = True
            story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
            story.append(Paragraph(zh_line_group(group), H2))
            rows = [["標的", "模型/來源", "正式狀態", "模型分數 / 風險", "說明"]]
            for _, r in sub.iterrows():
                sid = clean(r.get("stock_id"))
                rows.append(
                    [
                        f"{sid} {clean(r.get('stock_name'))}",
                        preferred_model_label_for_stock(inputs, sid, line) or "模型訊號未對應",
                        f"{zh_theme_status(r.get('theme_final_status'))} / {zh_structural_status(r.get('theme_structural_status'))} / {zh_mainstream_label(r.get('theme_mainstream_label'))}",
                        preferred_model_status_for_stock(inputs, sid, line),
                        short(r.get("theme_leadership_note") or r.get("candidate_line") or r.get("why_selected"), 110),
                    ]
                )
            story.append(build_table(rows, [36 * mm, 44 * mm, 76 * mm, 30 * mm, 82 * mm], 12.0))
        if not found_any:
            story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))
    else:
        story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))

    append_mainstream_full_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out




def build_non_mainstream_full_candidate_pdf(
    inputs: dict[str, pd.DataFrame],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
) -> Path:
    line = "non_mainstream"
    title = NON_MAINSTREAM_FULL_TITLE
    line_label = NON_MAINSTREAM_LINE_LABEL
    model_signals = inputs.get("model_signals", pd.DataFrame()).copy()
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} {title}", TITLE),
        date_note(),
        Spacer(1, 4),
        Paragraph(f"{line_label}族群與候選摘要", H1),
    ]
    themes = filter_theme_rows_for_line(inputs["themes"], line)
    if not themes.empty:
        rows = [["族群", "候選數", "嚴格突破", "營收", "TDCC", "權證", "正式狀態"]]
        for _, r in themes.head(18).iterrows():
            rows.append(
                [
                    zh_theme_name(r.get("theme_name")),
                    num(r.get("candidate_count"), 0),
                    num(r.get("strict_breakout_count"), 0),
                    num(r.get("revenue_count"), 0),
                    num(r.get("tdcc_positive_count") or r.get("tdcc_strength_count"), 0),
                    num(r.get("warrant_positive_count") or r.get("warrant_strength_count"), 0),
                    f"{zh_theme_status(r.get('theme_final_status'))} / {zh_structural_status(r.get('theme_structural_status'))} / {zh_mainstream_label(r.get('theme_mainstream_label'))}",
                ]
            )
        story.append(build_table(rows, [40 * mm, 18 * mm, 22 * mm, 18 * mm, 22 * mm, 22 * mm, 126 * mm], 12.0))
    else:
        story.append(para("本分流沒有可用的族群摘要資料。", BODY))

    story.append(Paragraph(f"{line_label}TDCC 重點", H1))
    tdcc_rows = [["標的", "模型/來源", "模型分數 / 狀態", "TDCC 摘要"]]
    seen_tdcc: set[str] = set()
    for _, r in sort_model_frame(model_signals, two_map).iterrows():
        sid = clean(r.get("stock_id"))
        if not sid or sid in seen_tdcc or not matches_line(r, two_map, line):
            continue
        extra = all_map.get(sid, pd.Series(dtype=object))
        detail = tdcc_detail(r, extra)
        if "TDCC資料不足" in detail:
            continue
        tdcc_rows.append(
            [
                stock_label(r),
                preferred_model_label_for_stock(inputs, sid, line) or "模型訊號未對應",
                f"{model_score_label(r)} / {display_signal_tag(model_signal_tag(r, two_map))}",
                short(detail, 180),
            ]
        )
        seen_tdcc.add(sid)
        if len(tdcc_rows) >= 19:
            break
    story.append(build_table(tdcc_rows, [34 * mm, 42 * mm, 22 * mm, 170 * mm], 12.0) if len(tdcc_rows) > 1 else para("本分流沒有可用的 TDCC 摘要。", BODY))

    story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))
    story.append(Paragraph(f"{line_label}完整候選", H1))
    limit = FULL_REPORT_NON_MAINSTREAM_LIMIT
    for spec in non_mainstream_full_core_model_specs(inputs):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        line_rows = non_mainstream_full_model_signal_rows(inputs, model_id)
        story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))
        story.append(Paragraph(model_name, H2))
        if render_model_operation_section_if_applicable(story, inputs, model_id, "full", line):
            continue
        story.extend(build_non_mainstream_full_model_table(line_rows, two_map, all_map, limit=limit))

    story.append(PageBreak())
    story.append(Paragraph(f"{line_label}雙線與輪動摘要", H1))
    two_line = inputs["two_line"]
    if not two_line.empty:
        found_any = False
        for group in [
            "mainstream_leader_stock",
            "mainstream_follow_through_stock",
            "two_line_overlap",
            "non_mainstream_flow_watch",
            "individual_tdcc_latent_watch",
            "individual_revenue_low_response_watch",
            "individual_pattern_watch",
            "risk",
        ]:
            sub = two_line[two_line["candidate_line_group"].astype(str) == group].copy()
            if not sub.empty:
                sub = sub[sub.apply(lambda r: matches_line(r, two_map, line), axis=1)].head(14)
            if sub.empty:
                continue
            found_any = True
            story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))
            story.append(Paragraph(zh_line_group(group), H2))
            rows = [["標的", "模型/來源", "正式狀態", "模型分數 / 風險", "說明"]]
            for _, r in sub.iterrows():
                sid = clean(r.get("stock_id"))
                rows.append(
                    [
                        f"{sid} {clean(r.get('stock_name'))}",
                        preferred_model_label_for_stock(inputs, sid, line) or "模型訊號未對應",
                        f"{zh_theme_status(r.get('theme_final_status'))} / {zh_structural_status(r.get('theme_structural_status'))} / {zh_mainstream_label(r.get('theme_mainstream_label'))}",
                        preferred_model_status_for_stock(inputs, sid, line),
                        short(r.get("theme_leadership_note") or r.get("candidate_line") or r.get("why_selected"), 110),
                    ]
                )
            story.append(build_table(rows, [36 * mm, 44 * mm, 76 * mm, 30 * mm, 82 * mm], 12.0))
        if not found_any:
            story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))
    else:
        story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))

    append_non_mainstream_full_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out





def build_warrant_market_auxiliary_pdf(inputs: dict[str, pd.DataFrame]) -> Path:
    warrant = inputs["warrant"]
    hidden = warrant_pdf_hidden()
    if hidden:
        warrant = pd.DataFrame()
    elif not warrant.empty and "stock_id" in warrant.columns:
        warrant = warrant[warrant["stock_id"].astype(str).str.strip().str.match(r"^[0-9]{4}$", na=False)].copy()
    model_signals = inputs.get("model_signals", pd.DataFrame()).copy()
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} 權證市場輔助分析", TITLE),
        date_note(),
        para("權證只作為輔助訊號；任何偏多、偏空或權證過熱的狀態都必須回到現股價格與量能確認。", BODY),
        Spacer(1, 4),
        Paragraph("權證市場概況", H1),
    ]
    if hidden:
        story.append(para(warrant_unavailable_note(), BODY))
    if not warrant.empty:
        signal_counts = warrant.get("warrant_flow_signal", pd.Series(dtype=str)).map(zh_warrant).value_counts().head(12)
        rows = [["訊號", "檔數"]]
        for signal, count in signal_counts.items():
            rows.append([signal, str(count)])
        story.append(build_table(rows, [80 * mm, 24 * mm], 12.0))
    else:
        story.append(para("權證資料不足 / 僅能觀察。", BODY))

    story.append(Paragraph("偏多 / 觀察名單", H1))
    if not warrant.empty:
        sort_col = "call_turnover" if "call_turnover" in warrant.columns else ("warrant_flow_score" if "warrant_flow_score" in warrant.columns else warrant.columns[0])
        tmp = warrant.copy()
        if sort_col in tmp.columns:
            tmp["_sort"] = pd.to_numeric(tmp[sort_col].astype(str).str.replace(",", ""), errors="coerce")
            tmp = tmp.sort_values("_sort", ascending=False)
        rows = [["標的", "權證訊號", "Call成交", "Put成交", "警示", "說明"]]
        for _, r in tmp.head(22).iterrows():
            rows.append(
                [
                    f"{clean(r.get('stock_id'))} {clean(r.get('stock_name'))}",
                    zh_warrant(r.get("warrant_flow_signal")),
                    num(r.get("call_turnover") or r.get("call_turnover_value"), 0),
                    num(r.get("put_turnover") or r.get("put_turnover_value"), 0),
                    short(r.get("warrant_flow_warning") or r.get("warning"), 45),
                    short(r.get("interpretation") or r.get("note"), 80),
                ]
            )
        story.append(build_table(rows, [34 * mm, 42 * mm, 27 * mm, 27 * mm, 55 * mm, 83 * mm], 12.0))
    else:
        story.append(para("資料不足 / 僅能觀察。", BODY))

    story.append(PageBreak())
    story.append(Paragraph("候選股交集", H1))
    if not warrant.empty and not model_signals.empty:
        w_signal = set(
            warrant[
                warrant.get("warrant_flow_signal", pd.Series(dtype=str)).astype(str).str.contains("call|bull|inflow", case=False, na=False)
            ]["stock_id"].astype(str)
        )
        inter = sort_model_frame(model_signals[model_signals["stock_id"].astype(str).isin(w_signal)].copy()).head(28)
        rows = [["標的", "模型/來源", "模型分數 / 風險", "權證訊號", "條件式解讀"]]
        for _, r in inter.iterrows():
            sid = clean(r.get("stock_id"))
            rows.append(
                [
                    stock_label(r),
                    preferred_model_label_for_stock(inputs, sid) or "模型訊號未對應",
                    f"{model_score_label(r)} / 風險：{model_risk_text(r, 32)}",
                    zh_warrant(r.get("warrant_flow_signal")),
                    "權證偏多只能輔助；仍回到現股收盤、量能與模型風險欄位確認。",
                ]
            )
        story.append(build_table(rows, [36 * mm, 44 * mm, 30 * mm, 48 * mm, 110 * mm], 12.0))
    else:
        story.append(para("交集資料不足 / 僅能觀察。", BODY))

    story.append(Paragraph("偏空 / 反向 / 資料品質", H1))
    if not warrant.empty:
        risk_mask = (
            warrant.get("warrant_flow_warning", pd.Series(dtype=str)).astype(str).str.strip().ne("")
            | warrant.get("warrant_flow_signal", pd.Series(dtype=str)).astype(str).str.contains("put|bear|overheat", case=False, na=False)
        )
        risk = warrant[risk_mask].head(20)
        rows = [["標的", "權證訊號", "警示", "判讀"]]
        for _, r in risk.iterrows():
            rows.append(
                [
                    f"{clean(r.get('stock_id'))} {clean(r.get('stock_name'))}",
                    zh_warrant(r.get("warrant_flow_signal")),
                    short(r.get("warrant_flow_warning") or r.get("warning"), 80),
                    "只作提醒，不作單獨操作依據 / 回到現股價量與大戶資料確認。",
                ]
            )
        if len(rows) == 1:
            rows.append(["-", "-", "未見明確警示欄位", "資料不足 / 僅能觀察。"])
        story.append(build_table(rows, [34 * mm, 44 * mm, 98 * mm, 92 * mm], 12.0))
    else:
        story.append(para("資料不足 / 僅能觀察。", BODY))

    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_權證市場輔助分析{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, "權證市場輔助分析")
    return out


def build_market_risk_background_pdf(inputs: dict[str, pd.DataFrame]) -> Path:
    market = inputs["market_regime"]
    bench = inputs["market_benchmark"]
    futures = inputs["futures"]
    put_call = inputs["put_call"]
    twse_chart = plot_index_chart("TWSE", "TWSE")
    tpex_chart = plot_index_chart("TPEX", "TPEx")
    vix_chart = plot_vix_chart()
    pc_chart = plot_put_call_chart()

    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} 市場風險與大盤期權背景", TITLE),
        date_note(),
        para("本報告只分析大盤、期貨與選擇權背景，不放入個股推薦。", BODY),
        Spacer(1, 4),
        Paragraph("市場狀態", H1),
    ]
    if not market.empty:
        r = market.iloc[0]
        rows = [
            ["市場狀態", "風險層級", "TWSE 5日", "TWSE 20日", "TPEx 5日", "TPEx 20日", "風險原因"],
            [
                zh_market_regime(r.get("market_regime")),
                zh_risk_level(r.get("risk_level")),
                num(r.get("twse_return_5d"), 2, "%"),
                num(r.get("twse_return_20d"), 2, "%"),
                num(r.get("tpex_return_5d"), 2, "%"),
                num(r.get("tpex_return_20d"), 2, "%"),
                short(zh_market_reason(r.get("risk_reasons") or r.get("risk_reason")), 120),
            ],
        ]
        story.append(build_table(rows, [36 * mm, 30 * mm, 22 * mm, 22 * mm, 22 * mm, 22 * mm, 114 * mm], 12.0))
    else:
        story.append(para("市場狀態資料不足 / 僅能觀察。", BODY))

    if twse_chart or tpex_chart:
        images = []
        if twse_chart:
            images.append(Image(str(twse_chart), width=128 * mm, height=54 * mm))
        if tpex_chart:
            images.append(Image(str(tpex_chart), width=128 * mm, height=54 * mm))
        story.append(Table([images], colWidths=[132 * mm] * len(images)))
    else:
        story.append(para("TWSE / TPEx 圖表資料不足 / 僅能觀察。", BODY))

    story.append(Paragraph("TWSE / TPEx 技術表", H1))
    if not bench.empty:
        rows = [["指數", "收盤", "MA20", "MA60", "5日", "20日", "狀態"]]
        for _, r in bench.iterrows():
            rows.append(
                [
                    clean(r.get("index_code") or r.get("index_name")),
                    num(r.get("close")),
                    num(r.get("ma20")),
                    num(r.get("ma60")),
                    num(r.get("return_5d"), 2, "%"),
                    num(r.get("return_20d"), 2, "%"),
                    short(r.get("technical_state") or r.get("trend_state"), 70),
                ]
            )
        story.append(build_table(rows, [30 * mm, 28 * mm, 28 * mm, 28 * mm, 22 * mm, 22 * mm, 110 * mm], 12.0))
    else:
        story.append(para("技術表資料不足 / 僅能觀察。", BODY))

    story.append(PageBreak())
    story.append(Paragraph("期貨 / 選擇權 / 波動率", H1))
    if not futures.empty:
        r = futures.iloc[0]
        rows = [
            ["外資台指期未平倉淨口數", "選擇權未平倉P/C", "台灣VIX", "散戶小台代理值", "資料狀態", "解讀"],
            [
                num(r.get("foreign_tx_futures_net_oi"), 0),
                num(r.get("put_call_oi_ratio_pct"), 2, "%"),
                num(r.get("taiwan_vix"), 2),
                num(r.get("retail_mtx_net_oi_proxy"), 0),
                zh_source_status(r.get("source_status")),
                "台指期方向主軸使用外資台指期未平倉淨口數；外資全部期貨未平倉不作為台指期方向判斷。",
            ],
        ]
        story.append(build_table(rows, [44 * mm, 38 * mm, 28 * mm, 42 * mm, 28 * mm, 88 * mm], 12.0))
    else:
        story.append(para("期貨選擇權指標資料不足 / 僅能觀察。", BODY))

    img_row = []
    if vix_chart:
        img_row.append(Image(str(vix_chart), width=128 * mm, height=48 * mm))
    if pc_chart:
        img_row.append(Image(str(pc_chart), width=128 * mm, height=48 * mm))
    if img_row:
        story.append(Table([img_row], colWidths=[132 * mm] * len(img_row)))

    story.append(Paragraph("Put/Call 明細", H1))
    if not put_call.empty:
        latest = put_call.tail(12)
        rows = [["日期", "成交量P/C", "未平倉P/C"]]
        for _, r in latest.iterrows():
            rows.append(
                [
                    clean(r.get("日期") or r.get("date")),
                    num(r.get("買賣權成交量比率%"), 2, "%"),
                    num(r.get("買賣權未平倉量比率%"), 2, "%"),
                ]
            )
        story.append(build_table(rows, [34 * mm, 34 * mm, 34 * mm], 12.0))
    else:
        story.append(para("Put/Call 明細不足 / 僅能觀察。", BODY))

    story.append(Paragraph("大盤操作背景", H1))
    story.append(
        para(
            "市場屬強勢但高風險狀態時，候選股只能採條件式處理：突破股必須守住突破區，回檔股必須守住均線或平台，權證熱度不得取代現股確認。若 VIX 維持高檔、Put/Call 顯示避險堆疊，或 foreign_tx_futures_net_oi 持續偏空，追價風險提高。",
            BODY,
        )
    )

    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_市場風險與大盤期權背景{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, "市場風險與大盤期權背景")
    return out


def stock_pdf_line_for_path(path: Path) -> str | None:
    name = path.name
    if NON_MAINSTREAM_CURATED_TITLE in name or NON_MAINSTREAM_FULL_TITLE in name:
        return "non_mainstream"
    if MAINSTREAM_CURATED_TITLE in name or MAINSTREAM_FULL_TITLE in name:
        return "mainstream"
    return None


def required_stock_model_text_missing(inputs: dict[str, pd.DataFrame], line: str, text: str) -> list[str]:
    missing: list[str] = []
    zero_candidate_models = 0
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        if model_name and model_name not in text:
            missing.append(model_name)
        if len(model_signal_rows(inputs, model_id, line)) == 0:
            zero_candidate_models += 1
    if zero_candidate_models and text.count(MODEL_EMPTY_STATE_TEXT) < zero_candidate_models:
        missing.append(f"{MODEL_EMPTY_STATE_TEXT} x{zero_candidate_models}")
    return missing


def validate_outputs(paths: list[Path], inputs: dict[str, pd.DataFrame] | None = None) -> None:
    from pypdf import PdfReader

    forbidden = ["debug", "fallback", "ChatGPT 道歉", "流程重跑版", "版本字樣"]
    report_lines = []
    validation_errors: list[str] = []
    for path in paths:
        reader = PdfReader(str(path))
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
        missing = not text.strip()
        hits = [term for term in forbidden if term in text]
        required_missing: list[str] = []
        if "每日推薦分析" in path.name:
            required = ["模型", "族群", "風險"]
            required_missing = [term for term in required if term not in text]
        model_required_missing: list[str] = []
        if inputs is not None:
            line = stock_pdf_line_for_path(path)
            if line:
                model_required_missing = required_stock_model_text_missing(inputs, line, text)
        if missing or hits or required_missing:
            validation_errors.append(
                f"{path.name}: text_missing={missing}, forbidden_hits={hits}, required_missing={required_missing}"
            )
        if model_required_missing:
            validation_errors.append(f"{path.name}: model_required_missing={model_required_missing}")
        report_lines.append(
            {
                "file": path.name,
                "pages": len(reader.pages),
                "text_chars": len(text),
                "text_missing": missing,
                "forbidden_hits": hits,
                "required_missing": required_missing,
                "model_required_missing": model_required_missing,
            }
        )
    pd.DataFrame(report_lines).to_csv(OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_pdf_validation.csv", index=False, encoding="utf-8-sig")
    if validation_errors:
        raise RuntimeError("pdf_validation_failed: " + " | ".join(validation_errors))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Renderer for the six ChatGPT-side daily Taiwan stock PDF deliverables. "
            "Official generation must be started by scripts/run_chatgpt_daily_report_entrypoint.py."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=REPO,
        help="tdcc-weekly-report checkout to read; defaults to this script's repository.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUT,
        help="Directory for generated ChatGPT-side PDFs.",
    )
    return parser.parse_args()


def require_entrypoint_invocation() -> None:
    if os.environ.get("CHATGPT_DAILY_REPORT_ENTRYPOINT") == "1":
        return
    raise RuntimeError(
        "direct ChatGPT-side daily PDF generator invocation is blocked. "
        "Use scripts/run_chatgpt_daily_report_entrypoint.py so origin/main source-state "
        "preflight cannot be bypassed."
    )


def configure_paths(args: argparse.Namespace) -> None:
    global REPO, LATEST, DATA, OUT, CHARTS, TDCC_WINDOW_DIRS

    REPO = args.repo_root.expanduser().resolve()
    LATEST = REPO / "output" / "latest"
    DATA = REPO / "data"
    OUT = args.output_dir.expanduser().resolve()
    CHARTS = OUT / "charts"
    TDCC_WINDOW_DIRS = [
        LATEST / "individual_stock_reports" / "tdcc_windows",
        REPO / "docs" / "latest" / "individual_stock_reports" / "tdcc_windows",
    ]


def main() -> None:
    require_entrypoint_invocation()
    args = parse_args()
    configure_paths(args)
    enforce_fresh_repo_data()
    OUT.mkdir(exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)
    inputs = load_inputs()
    all_map, two_map, vol_map = get_stock_extra_maps(inputs["all"], inputs["two_line"], inputs["volume_stocks"])
    paths = [
        build_mainstream_curated_pdf(inputs, all_map, two_map, vol_map),
        build_mainstream_full_candidate_pdf(inputs, two_map, all_map),
        build_non_mainstream_curated_pdf(inputs, all_map, two_map, vol_map),
        build_non_mainstream_full_candidate_pdf(inputs, two_map, all_map),
        build_warrant_market_auxiliary_pdf(inputs),
        build_market_risk_background_pdf(inputs),
    ]
    validate_outputs(paths, inputs)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
