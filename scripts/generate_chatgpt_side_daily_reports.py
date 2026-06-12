from __future__ import annotations

import argparse
import math
import os
import re
import textwrap
import urllib.error
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
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


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
    LATEST / "individual_stock_tdcc_windows",
    REPO / "docs" / "latest" / "individual_stock_tdcc_windows",
]
REMOTE_README: dict[str, str] = {}
REMOTE_LATEST_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest"
REMOTE_DATA_BASE = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/data"

REQUEST_DATE = datetime.now().strftime("%Y%m%d")
OUTPUT_SUFFIX = "_current_rules"

REMOTE_README_URLS = [
    "https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT.txt",
    "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
]

FONT_NAME = "DFKai"
FONT_BOLD = "DFKai-Bold"
FONT_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
FONT_BOLD_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
MATPLOTLIB_FONT: FontProperties | None = None
TDCC_WINDOW_CACHE: dict[str, pd.Series] = {}

MAIN_REPORT_MAINSTREAM_LIMIT = 8
MAIN_REPORT_NON_MAINSTREAM_LIMIT = 2
PATTERN_SUBTYPE_MAIN_LIMIT = 5
PATTERN_SUBTYPE_NON_LIMIT = 2
PATTERN_SUBTYPE_OPERATION_LIMIT = 6
FRONT_MAINSTREAM_LIMIT = 8
FRONT_NON_MAINSTREAM_LIMIT = 2
FULL_REPORT_MAINSTREAM_LIMIT = 12
FULL_REPORT_NON_MAINSTREAM_LIMIT = 4


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


def parse_key_value_text(text: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


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


def fetch_remote_readme_values(request_date: str) -> tuple[dict[str, str], str]:
    urls = [
        f"https://LeoChen0727.github.io/tdcc-weekly-report/latest/READ_ME_FIRST_DAILY_REPORT_{request_date}.txt",
        f"https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/output/latest/READ_ME_FIRST_DAILY_REPORT_{request_date}.txt",
        *REMOTE_README_URLS,
    ]
    errors: list[str] = []
    for url in urls:
        try:
            text = fetch_text_no_cache(url)
            values = parse_key_value_text(text)
            if values.get("main_price_date") and values.get("commit_sha"):
                return values, url
            errors.append(f"{url}: content_not_expanded")
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            errors.append(f"{url}: raw_fetch_failed: {exc}")
    detail = " | ".join(errors[-4:])
    raise RuntimeError(f"remote_readme_fetch_failed: {detail}")


def local_readme_values() -> dict[str, str]:
    path = LATEST / "READ_ME_FIRST_DAILY_REPORT.txt"
    if not path.exists():
        raise RuntimeError(f"local_readme_missing: {path}")
    return parse_key_value_text(path.read_text(encoding="utf-8", errors="replace"))


def enforce_fresh_repo_data() -> None:
    global DATA_DATE, DATA_DATE_SLASH, REQUEST_DATE, REQUEST_DATE_SLASH, REMOTE_README

    remote, remote_url = fetch_remote_readme_values(REQUEST_DATE)
    remote_date = remote.get("main_price_date", "")
    report_ready = remote.get("report_ready", "")
    if not remote_date:
        raise RuntimeError(f"remote_readme_missing_main_price_date: source={remote_url}")
    if clean(report_ready).lower() != "true":
        raise RuntimeError(
            "remote_report_not_ready: "
            f"main_price_date={remote_date}, report_ready={report_ready}, source={remote_url}"
        )

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


DATA_DATE = read_readme_value("main_price_date", REQUEST_DATE)
DATA_DATE_SLASH = date_slash(DATA_DATE)
REQUEST_DATE_SLASH = date_slash(REQUEST_DATE)


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
    fontSize=15,
    leading=19,
    spaceBefore=7,
    spaceAfter=4,
)
H2 = ParagraphStyle(
    "H2CJK",
    parent=styles["Heading2"],
    fontName=FONT_BOLD,
    fontSize=13,
    leading=16.5,
    spaceBefore=5,
    spaceAfter=3,
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


MAINSTREAM_CURATED_TITLE = "\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
MAINSTREAM_FULL_TITLE = "\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
NON_MAINSTREAM_CURATED_TITLE = "\u975e\u4e3b\u6d41\u80a1\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
NON_MAINSTREAM_FULL_TITLE = "\u975e\u4e3b\u6d41\u80a1\u5b8c\u6574\u5019\u9078\u6e05\u55ae"
LINE_TITLE_MAP = {
    "mainstream": (MAINSTREAM_CURATED_TITLE, MAINSTREAM_FULL_TITLE, "\u4e3b\u6d41\u80a1"),
    "non_mainstream": (NON_MAINSTREAM_CURATED_TITLE, NON_MAINSTREAM_FULL_TITLE, "\u975e\u4e3b\u6d41\u80a1"),
}


def line_titles(line: str) -> tuple[str, str, str]:
    return LINE_TITLE_MAP[line]


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


def has_text(value) -> bool:
    s = clean(value)
    return bool(s) and s.lower() not in {"false", "0", "[]", "{}", "no", "none"}


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


def score_key(value) -> str:
    n = to_float(value)
    if n is None:
        return ""
    return f"{n:.4f}"


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


def priority_label(row: pd.Series) -> str:
    label = clean(row.get("decision_priority_label"))
    priority = clean(row.get("decision_priority"))
    if label in {"最優先追蹤", "可等確認"}:
        return "等確認"
    if label == "僅觀察":
        return "僅觀察"
    if "暫避" in label or "降級" in label or "暫不列" in label:
        return "不列入"
    return {
        "A_priority_watch": "等確認",
        "B_confirm_needed": "等確認",
        "C_watch_only": "僅觀察",
        "D_risk_downgrade": "不列入",
    }.get(priority, priority)


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


def zh_volume_status(value) -> str:
    raw = clean(value, "volume_status_missing")
    return VOLUME_STATUS_LABELS.get(raw, raw)


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


def tdcc_latest_levels(row: pd.Series, extra: pd.Series | None = None) -> str:
    extra = extra if isinstance(extra, pd.Series) else pd.Series(dtype=object)
    sid = clean(series_value(row, extra, "stock_id"))
    latest = latest_tdcc_window_row(sid)
    parts = []
    for level in ("400", "600", "800", "1000"):
        ratio = num(latest.get(f"over_{level}_ratio"), 2, "%")
        change = signed_num(latest.get(f"over_{level}_change_1w"), 2)
        if ratio:
            parts.append(f"{level}張 {ratio} / {change or '0'}")
    return "；".join(parts) or "級距資料不足"


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


def zh_priority_short(value) -> str:
    raw = clean(value)
    return {
        "A_priority_watch": "最優先",
        "B_confirm_needed": "等確認",
        "C_watch_only": "僅觀察",
        "D_risk_downgrade": "暫不列",
    }.get(raw, raw)


def zh_research_note(row: pd.Series) -> str:
    priority = clean(row.get("research_priority"))
    caveat = clean(row.get("research_caveat"))
    pieces = []
    if priority:
        pieces.append(
            {
                "A_strict_research_watch": "嚴格研究觀察名單",
            }.get(priority, "研究觀察名單")
        )
    if "research_only" in caveat:
        pieces.append("僅供研究，不直接改變核心權重")
    if "entry_basis_D+1_open" in caveat:
        pieces.append("進場基準需看次日開盤後確認")
    if "target_next_open_to_high_10pct" in caveat:
        pieces.append("觀察次日開盤至高點的短線彈性")
    if "strict_no_latest_theme_label" in caveat:
        pieces.append("未納入最新族群標籤")
    return "；".join(pieces) or "資料不足 / 僅能觀察"


def line_group_action(group, status) -> str:
    group_raw = clean(group)
    status_raw = clean(status)
    if group_raw == "mainstream_leader_stock":
        return "主線核心。只挑 A 級與價量續強者，失去族群領先或爆量長上影就先降低部位。"
    if group_raw == "mainstream_follow_through_stock":
        return "主線續強。可列優先追蹤，但需等待突破、回測或量能延續，不追高。"
    if group_raw == "two_line_overlap":
        return "族群與個股條件重疊。優先檢查下一確認條件，成立才可升級。"
    if group_raw == "non_mainstream_flow_watch":
        return "非主流輪動。條件乾淨時可列短線考慮，但不能補位成主流資金線。"
    if group_raw == "individual_tdcc_latent_watch":
        return "非主流個股線。只看個股確認，不當成族群主線，不用族群熱度追價。"
    if group_raw == "individual_revenue_low_response_watch":
        return "營收低反應線。等價格與量能開始反應，EPS / 毛利未確認前不升級。"
    if group_raw == "emerging_theme_watch":
        return "早期題材。樣本少，只能觀察族群是否擴散，不直接列核心。"
    if group_raw == "risk" or "overheated" in status_raw:
        return "暫不列前排。先等突破、量能或籌碼重新確認；沒確認就不買。"
    return "資料不足 / 僅能觀察；不得用原始代碼自行升級。"


def volume_action(theme_status, volume_status, structural_status=None, mainstream_label=None) -> str:
    theme = clean(theme_status)
    status = clean(volume_status)
    structural = clean(structural_status)
    label = clean(mainstream_label)
    if structural == "non_mainstream_theme":
        return "非主流族群放量。可列短線輪動考慮，不能放進主流資金線。"
    if "overheated" in label or status in {"overheated_volume_theme", "failed_volume_theme"}:
        return "量能過熱或突破失敗。先不追，等重新站穩後再看。"
    if status == "confirmed_volume_theme":
        return "族群放量已確認。只從主流或雙線交集名單挑選，仍需個股價量確認，不追單日急拉。"
    if status == "watch_volume_theme":
        return "族群有放量跡象但廣度仍不足。等待第二批個股跟進或回測不破後再升級。"
    if status == "early_mainstream_candidate":
        return "早期主流候選。先看族群擴散，不直接當核心推薦。"
    if status == "single_stock_volume_attack":
        return "偏單股訊號。不能代表族群主線，只回到該股下一確認條件。"
    if status in {"overheated_volume_theme", "failed_volume_theme", "weak_or_non_mainstream_volume_watch"}:
        return "放量品質不夠好。先不追，等重新確認。"
    if "overheated" in theme:
        return "短線漲幅或量能過熱。放量訊號只能提醒先不追，不能當買進理由。"
    return "資料不足 / 僅能觀察；不得只因放量就升級。"


def two_line_row(row: pd.Series, two_map: dict[str, pd.Series]) -> pd.Series:
    sid = clean(row.get("stock_id"))
    cat = clean(row.get("original_category_cn") or row.get("category_cn"))
    score = score_key(row.get("decision_score"))
    two = two_map.get((sid, cat, score)) if score else None
    if two is None:
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


def line_bucket(row: pd.Series, two_map: dict[str, pd.Series]) -> str:
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    if (
        structural == "core_mainstream_theme"
        and status in MAINSTREAM_THEME_STATUSES
        and source != RISK_SOURCE
        and group != "risk"
        and "overheated" not in label
    ):
        return "主流資金線"
    if source == RISK_SOURCE or status in RISK_THEME_STATUSES or group == "risk" or "overheated" in label:
        return "先不追 / 等確認"
    if structural == "non_mainstream_theme" or source == "individual_quality_candidate" or group == "non_mainstream_flow_watch":
        return "非主流輪動觀察"
    if status == "emerging_theme":
        return "早期題材觀察"
    if status == "single_name_signal":
        return "個股訊號觀察"
    if source == LATENT_SOURCE:
        return "個股潛伏觀察"
    return "分線資料不足"


def is_mainstream_row(row: pd.Series, two_map: dict[str, pd.Series]) -> bool:
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    return (
        structural == "core_mainstream_theme"
        and status in MAINSTREAM_THEME_STATUSES
        and source != RISK_SOURCE
        and group != "risk"
        and "overheated" not in label
    )


def is_core_mainstream_row(row: pd.Series, two_map: dict[str, pd.Series]) -> bool:
    structural, _ = line_structure(row, two_map)
    return structural == "core_mainstream_theme"


def is_strict_breakout_row(row: pd.Series) -> bool:
    category = category_display(clean(row.get("original_category_cn") or row.get("category_cn"))).lower()
    raw_category = clean(row.get("original_category_cn") or row.get("category_cn")).lower()
    return "嚴格突破" in category or raw_category in {"true_breakout", "breakout"}


def has_individual_overheat(row: pd.Series) -> bool:
    overheat = clean(row.get("overheat_status")).lower()
    if overheat and overheat not in {"not_overheated", "normal", "none", "nan"} and "overheated" in overheat:
        return True
    text = clean(row.get("downgrade_flags") or row.get("why_downgraded") or row.get("risk_tags")).lower()
    return any(
        token in text
        for token in (
            "overheat",
            "過熱",
            "已反應",
            "priced_in",
            "return_20d_gt_30",
            "distance_ma20_gt_20",
            "short_term_volume_overheat",
            "catalyst_overheated",
        )
    )


def split_mainstream_rows(rows: list[pd.Series], two_map: dict[str, pd.Series]) -> tuple[list[pd.Series], list[pd.Series]]:
    main = [row for row in rows if is_core_mainstream_row(row, two_map)]
    non = [row for row in rows if not is_core_mainstream_row(row, two_map)]
    return main, non


def split_by_official_line(rows: list[pd.Series], two_map: dict[str, pd.Series]) -> tuple[list[pd.Series], list[pd.Series], list[pd.Series]]:
    main: list[pd.Series] = []
    latent: list[pd.Series] = []
    risk: list[pd.Series] = []
    for row in rows:
        source, _, group, _ = line_source(row, two_map)
        _, status = line_raw(row, two_map)
        _, label = line_structure(row, two_map)
        if is_mainstream_row(row, two_map):
            main.append(row)
        elif source == RISK_SOURCE or status in RISK_THEME_STATUSES or group == "risk" or "overheated" in label:
            risk.append(row)
        else:
            latent.append(row)
    return main, latent, risk


def representative_names(df: pd.DataFrame, group: str, status: str, limit: int = 4) -> str:
    if df.empty:
        return "資料不足"
    sub = df[
        (df.get("candidate_line_group", pd.Series(dtype=str)).astype(str) == clean(group))
        & (df.get("theme_final_status", pd.Series(dtype=str)).astype(str) == clean(status))
    ].copy()
    if sub.empty:
        return "資料不足"
    if "decision_score" in sub.columns:
        sub["_score"] = pd.to_numeric(sub["decision_score"], errors="coerce")
        sub = sub.sort_values("_score", ascending=False)
    names = [f"{clean(r.get('stock_id'))} {clean(r.get('stock_name'))}".strip() for _, r in sub.head(limit).iterrows()]
    return "、".join([n for n in names if n]) or "資料不足"


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


def priority_sort_key(row: pd.Series, two_map: dict[str, pd.Series] | None = None) -> tuple:
    p = {
        "A_priority_watch": 0,
        "B_confirm_needed": 1,
        "C_watch_only": 2,
        "D_risk_downgrade": 3,
    }.get(clean(row.get("decision_priority")), 9)
    rank = to_float(row.get("decision_rank_in_category"))
    score = to_float(row.get("decision_score"))
    overall = to_float(row.get("decision_rank_overall_for_display"))
    quality = candidate_quality_points(row)
    return (
        p,
        candidate_mainstream_bucket(row, two_map),
        -quality,
        rank if rank is not None else 9999,
        -(score if score is not None else -9999),
        overall if overall is not None else 9999,
    )


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


def sort_df(df: pd.DataFrame, two_map: dict[str, pd.Series] | None = None) -> pd.DataFrame:
    if df.empty:
        return df
    tmp = df.copy()
    tmp["_sort_key"] = [priority_sort_key(row, two_map) for _, row in tmp.iterrows()]
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


def build_summary_table(rows: list[list], widths: list[float]) -> Table:
    data: list[list] = []
    for idx, row in enumerate(rows):
        if idx == 0:
            data.append([rich_para(escape_html(cell), SUMMARY_HEADER) for cell in row])
        else:
            data.append([rich_para(cell, SUMMARY_CELL) for cell in row])
    table = Table(data, colWidths=widths, repeatRows=1, splitByRow=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#b7b7b7")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
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
            score = score_key(row.get("decision_score"))
            if sid and cat and score:
                two_map.setdefault((sid, cat, score), row)
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


def front_eligible(row: pd.Series, two_map: dict[str, pd.Series], vol_map: dict[str, pd.Series]) -> bool:
    if clean(row.get("decision_priority")) != "A_priority_watch":
        return False
    source, _, group, _ = line_source(row, two_map)
    _, theme_status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    if source == RISK_SOURCE or group == "risk":
        return False
    if structural != "core_mainstream_theme":
        return False
    clean_strict_breakout = (
        is_strict_breakout_row(row)
        and theme_status == "mainstream_overheated"
        and not has_individual_overheat(row)
    )
    if theme_status not in MAINSTREAM_THEME_STATUSES and not clean_strict_breakout:
        return False
    if ("overheated" in theme_status.lower() or "overheated" in label.lower()) and not clean_strict_breakout:
        return False
    if has_text(row.get("why_downgraded")):
        return False
    for field in ("downgrade_flags", "risk_tags"):
        text = clean(row.get(field)).lower()
        if text and text not in {"no_risk", "risk_none", "none", "nan"}:
            return False
    if clean(row.get("must_not_overstate")).lower() == "true":
        return False
    if "distribution_warning" in clean(row.get("tdcc_status")).lower():
        return False
    overheat = clean(row.get("overheat_status")).lower()
    if overheat and overheat not in {"not_overheated", "normal", "none"} and "overheated" in overheat:
        return False
    sid = clean(row.get("stock_id"))
    vol_status = clean(vol_map.get(sid, pd.Series(dtype=object)).get("theme_volume_attack_status")).lower()
    if vol_status in {"overheated_volume_theme", "failed_volume_theme", "weak_or_non_mainstream_volume_watch"}:
        return False
    return True


def has_hard_exclusion(row: pd.Series, vol_map: dict[str, pd.Series] | None = None) -> bool:
    priority = clean(row.get("decision_priority"))
    if priority == "D_risk_downgrade":
        return True
    if clean(row.get("must_not_overstate")).lower() == "true":
        return True
    tdcc = clean(row.get("tdcc_status")).lower()
    if "distribution_warning" in tdcc:
        return True
    raw = clean(row.get("why_downgraded") or row.get("risk_tags") or row.get("downgrade_flags")).lower()
    hard_tokens = [
        "false_breakout",
        "tdcc_distribution",
        "distribution_warning",
        "data_insufficient",
        "missing_data",
        "source_missing",
        "stale_signal",
        "repeated_but_no_breakout",
    ]
    if any(token in raw for token in hard_tokens):
        return True
    sid = clean(row.get("stock_id"))
    vol_row = (vol_map or {}).get(sid, pd.Series(dtype=object))
    vol_status = clean(vol_row.get("theme_volume_attack_status")).lower()
    if vol_status in {"failed_volume_theme", "weak_or_non_mainstream_volume_watch"}:
        return True
    return False


def category_signal_buy_candidate(row: pd.Series, vol_map: dict[str, pd.Series] | None = None) -> bool:
    return clean(row.get("decision_priority")) == "A_priority_watch" and not has_hard_exclusion(row, vol_map)


def clean_risk_gate(row: pd.Series, vol_map: dict[str, pd.Series] | None = None) -> bool:
    if has_text(row.get("why_downgraded")):
        return False
    for field in ("downgrade_flags", "risk_tags"):
        text = clean(row.get(field)).lower()
        if text and text not in {"no_risk", "risk_none", "none", "nan"}:
            return False
    if clean(row.get("must_not_overstate")).lower() == "true":
        return False
    if "distribution_warning" in clean(row.get("tdcc_status")).lower():
        return False
    overheat = clean(row.get("overheat_status")).lower()
    if overheat and overheat not in {"not_overheated", "normal", "none"} and "overheated" in overheat:
        return False
    sid = clean(row.get("stock_id"))
    vol_row = (vol_map or {}).get(sid, pd.Series(dtype=object))
    vol_status = clean(vol_row.get("theme_volume_attack_status")).lower()
    if vol_status in {"overheated_volume_theme", "failed_volume_theme", "weak_or_non_mainstream_volume_watch"}:
        return False
    return True


def non_mainstream_trade_eligible(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> bool:
    if clean(row.get("decision_priority")) != "A_priority_watch":
        return False
    source, _, group, _ = line_source(row, two_map)
    _, theme_status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    if structural != "non_mainstream_theme":
        return False
    if source == RISK_SOURCE or group == "risk":
        return False
    if theme_status not in MAINSTREAM_THEME_STATUSES and theme_status != "emerging_theme":
        return False
    if "overheated" in theme_status.lower() or "overheated" in label.lower():
        return False
    return clean_risk_gate(row, vol_map)


def line_status(row: pd.Series, two_map: dict[str, pd.Series]) -> tuple[str, str]:
    group, theme_status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    status_text = f"{zh_theme_status(theme_status)} / {zh_structural_status(structural)} / {zh_mainstream_label(label)}"
    return zh_line_group(group), status_text


def decision_action_tag(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> str:
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    _, label = line_structure(row, two_map)
    priority = clean(row.get("decision_priority"))
    down = clean(row.get("downgrade_flags") or row.get("why_downgraded") or row.get("risk_tags")).lower()
    must_not = clean(row.get("must_not_overstate")).lower() == "true"
    tdcc = clean(row.get("tdcc_status")).lower()
    if "distribution_warning" in tdcc:
        return "先不碰"
    if category_signal_buy_candidate(row, vol_map or {}):
        return "嚴格可買" if is_strict_breakout_row(row) else "條件可買"
    if "repeated_but_no_breakout" in down or "stale_signal" in down:
        return "等突破"
    if source == RISK_SOURCE or group == "risk":
        return "暫不列"
    if front_eligible(row, two_map, vol_map or {}):
        return "嚴格可買"
    if "overheated" in status or "overheated" in label:
        return "先不追"
    if non_mainstream_trade_eligible(row, two_map, vol_map or {}):
        return "非主流短線考慮"
    if priority == "A_priority_watch" and not must_not:
        if is_core_mainstream_row(row, two_map):
            return "等確認"
        return "非主流觀察"
    if priority == "B_confirm_needed":
        return "等確認"
    if priority == "C_watch_only":
        return "僅觀察"
    if priority == "D_risk_downgrade":
        return "暫不列"
    return "等確認"


def display_action_tag(action: str) -> str:
    mapping = {
        "嚴格可買": "推薦可買",
        "條件可買": "可買候選",
        "非主流短線考慮": "短線觀察",
        "非主流觀察": "觀察",
        "僅觀察": "觀察",
        "暫不列": "排除買進",
        "先不追": "觀察",
        "先不碰": "不碰",
    }
    return mapping.get(clean(action), clean(action))


def excluded_from_recommendation_flow(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> bool:
    tag = decision_action_tag(row, two_map, vol_map or {})
    if tag in {"暫不列", "先不碰"}:
        return True
    if clean(row.get("decision_priority")) == "D_risk_downgrade":
        return True
    source, _, group, _ = line_source(row, two_map)
    return source == RISK_SOURCE or group == "risk"


def visible_recommendation_rows(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> list[pd.Series]:
    return [row for row in rows if not excluded_from_recommendation_flow(row, two_map, vol_map)]


def avoid_reason(row: pd.Series, two_map: dict[str, pd.Series]) -> str:
    explicit = first_text(row.get("why_downgraded"), row.get("risk_tags"), row.get("downgrade_flags"))
    if explicit:
        return short(explicit, 95)

    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    _, label = line_structure(row, two_map)
    action = decision_action_tag(row, two_map)
    priority = clean(row.get("decision_priority"))
    tdcc = clean(row.get("tdcc_status")).lower()

    if "distribution_warning" in tdcc:
        return "籌碼出現派發警示，先排除買進名單"
    if action == "等突破":
        return "反覆出現訊號但尚未有效突破"
    if action == "先不追":
        return "短線漲幅過大或量能過熱，容易追在短線高點"
    if source == RISK_SOURCE or group == "risk" or priority == "D_risk_downgrade":
        return "程式端列為暫不列前排，條件未回復前不列買進候選"
    if "overheated" in status or "overheated" in label:
        return "族群短線漲幅或量能過熱，先等回測或重新站穩"
    return ""


def avoid_action(row: pd.Series, two_map: dict[str, pd.Series]) -> str:
    action = decision_action_tag(row, two_map)
    if action == "先不碰":
        return "不買；籌碼派發警示解除前不列候選。"
    if action == "先不追":
        return "不追價；等回測後重新站穩，或量能續強但不失控再看。"
    if action == "等突破":
        return "等有效突破或收盤站穩壓力區，再回候選名單。"
    if action == "暫不列":
        return "不買；價格、量能或籌碼重新確認前不列前排。"
    return "先等價格、量能或籌碼重新確認。"


def technical_state(row: pd.Series, extra: pd.Series) -> str:
    close = num(row.get("close"))
    vol = num(row.get("volume_ratio"), 2)
    r5 = num(row.get("return_5d"), 2, "%")
    r20 = num(row.get("return_20d"), 2, "%")
    ema23 = num(extra.get("ema23"))
    ma20 = num(extra.get("ma20"))
    ma60 = num(extra.get("ma60"))
    high = num(extra.get("previous_60d_high") or extra.get("previous_high"))
    parts = [
        f"收盤 {close}" if close else "",
        f"成交量約 {vol} 倍" if vol else "",
        f"5日 {r5}" if r5 else "",
        f"20日 {r20}" if r20 else "",
        f"23EMA {ema23}" if ema23 else "",
        f"MA20 {ma20}" if ma20 else "",
        f"MA60 {ma60}" if ma60 else "",
        f"前高/60日高 {high}" if high else "",
    ]
    return "；".join([p for p in parts if p]) or "資料不足 / 僅能觀察"


def technical_state_brief(row: pd.Series, extra: pd.Series) -> str:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    stage = translate_codes(first_text(row.get("pattern_stage"), source.get("pattern_stage"), row.get("breakout_type"), source.get("pattern_route")))
    level_label, level_text, _ = key_level_context(row, extra)
    r5 = num(first_text(row.get("return_5d"), source.get("return_5d_pct")), 2, "%")
    r20 = num(first_text(row.get("return_20d"), source.get("return_20d_pct")), 2, "%")
    broke = clean(source.get("neckline_breakout_flag")).lower() == "true" or clean(source.get("platform_breakout_flag")).lower() == "true"
    vol_ok = clean(source.get("volume_confirmed_breakout")).lower() == "true"
    false_risk = clean(source.get("false_breakout_risk")).lower() == "true"
    parts = [
        stage or "",
        "已突破" if broke else "挑戰壓力",
        f"{level_label} {level_text}" if level_label and level_text else "",
        f"5日 {r5}" if r5 else "",
        f"20日 {r20}" if r20 else "",
        "成交量放大" if vol_ok else "",
        "假突破風險" if false_risk else "",
    ]
    return "；".join([p for p in parts if p]) or "資料不足 / 僅能觀察"


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


def operation_rules(row: pd.Series) -> tuple[str, str, str, str]:
    category = category_display(clean(row.get("original_category_cn") or row.get("category_cn")))
    next_confirm = clean(row.get("next_confirmation"), "後續追蹤價量是否延續。")
    if "不跌回平台" in next_confirm or "不跌回" in next_confirm:
        next_confirm = "這是買進後防守條件，不是今天買前等待條件。"
    if "嚴格突破" in category:
        buy = "今日收盤已站上突破區或前高上方，且量能高於近期均量時，可列入條件式買點；不需等隔日才判斷今天是否成立。"
        take = "若急拉遠離短期成本區、爆量不漲或長上影，先分批降低；靠近上一段壓力且量能鈍化時不加碼。"
        no_buy = "收盤沒有站上突破區、爆量長上影或量能失控時不買；買進後跌回突破區才退出或降部位。"
    elif "區間內轉強" in category:
        buy = "收盤有效站上區間上緣或前高壓力，且成交量同步放大時，可列入條件式買點。"
        take = "接近前高壓力但無法放量突破時先不追；若突破後兩日內失守壓力區，視為失敗。"
        no_buy = "只碰壓力不過、爆量收黑、或收盤跌回區間內時不買。"
    elif "營收爆發" in category:
        buy = "營收題材只能作背景；必須價格守住程式端確認區且量能放大，確認市場開始反應後才買。"
        take = "若營收利多後股價一次性急漲、隔日無續量，採短線分批落袋或降為觀察。"
        no_buy = "若已反應過度、EPS/毛利仍未確認、或TDCC轉弱，不買。"
    elif "營收成長" in category:
        buy = "只在回檔守住平台低點或程式端支撐區後出現轉強K線，並且量能回升時列入。"
        take = "反彈靠近前高但量能不足時先降低部位；跌回支撐區下方時退出。"
        no_buy = "跌破程式端支撐區後沒有快速站回、或營收利多已被價格反應完，不買。"
    elif "短線轉強" in category:
        buy = "今日若已收盤站回攻擊K關鍵區且成交量回升，可列入短線條件式買點；隔日跌破攻擊K低點才視為失敗。"
        take = "5至10日內若急拉、爆量不漲或長上影，先分批落袋。"
        no_buy = "收盤未站回攻擊K關鍵區、回落攻擊K低點或量能斷裂時不買。"
    else:
        buy = "型態必須完成頸線/平台確認，並且收盤守住程式端確認區；未確認前僅能觀察。"
        take = "靠近型態量測壓力或前高但量能跟不上時降低曝險。"
        no_buy = "型態未完成、假突破、跌破平台低點或程式端確認區時不買。"
    exit_rule = f"退出條件：買進後若收盤跌回突破/支撐區，或出現爆量長上影、量能失控，視為失敗。{next_confirm}"
    return buy, take, exit_rule, no_buy


def plot_stock_chart(
    stock_id: str,
    stock_name: str,
    extra: pd.Series,
    candidate_row: pd.Series | None = None,
) -> Path | None:
    remote_template = REMOTE_README.get("individual_stock_price_raw_url_template")
    source: Path | str
    source = remote_template.replace("{stock_id}", stock_id) if remote_template else (
        LATEST / "individual_stock_price_windows" / f"{stock_id}_price_window_180_latest.csv"
    )
    df = read_csv(source)
    if df.empty or "date" not in df.columns or "close" not in df.columns:
        return None
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for col in ("open", "high", "low", "close", "volume", "ema23", "ma20", "ma60"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", ""), errors="coerce")
    df = df.dropna(subset=["date", "close"]).tail(180)
    if df.empty:
        return None

    chart_kind = "op" if isinstance(candidate_row, pd.Series) and not candidate_row.empty else "plain"
    path = CHARTS / f"{stock_id}_kline_180_{chart_kind}.png"
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
        add_price_line(level_text, "買進確認/壓力", "#c00000", "-", 1.25)
    elif level_label == "短線支撐" and level_text:
        add_price_line(level_text, "支撐/跌破退出", "#007a3d", "-", 1.25)
    elif level_label == "關鍵價" and level_text:
        add_price_line(level_text, "買進確認/關鍵價", "#c00000", "-", 1.25)

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
    ax.set_title(f"{stock_id} {stock_name} 180日K線 / 23EMA", fontproperties=MATPLOTLIB_FONT, fontsize=11)
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
        "decision": read_csv(remote_latest_url("daily_candidate_decision_latest.csv")),
        "two_line": read_csv(remote_latest_url("daily_candidate_two_line_view_latest.csv")),
        "all": read_csv(remote_latest_url("all_candidates_latest.csv")),
        "model_registry": read_csv(remote_latest_url("daily_report_model_registry_latest.csv")),
        "model_parameters": read_csv(remote_latest_url("daily_candidate_model_parameters_latest.csv")),
        "model_signals": read_csv(remote_latest_url("daily_candidate_model_signals_for_report_latest.csv")),
        "model_summary": read_csv(remote_latest_url("daily_candidate_model_summary_for_report_latest.csv")),
        "group_rotation": read_csv(remote_latest_url("daily_candidate_group_rotation_latest.csv")),
        "themes": read_csv(remote_latest_url("daily_theme_leadership_latest.csv")),
        "volume_layer": read_csv(remote_latest_url("volume_attack_theme_layer_latest.csv")),
        "volume_stocks": read_csv(remote_latest_url("volume_attack_theme_stocks_latest.csv")),
        "warrant": read_csv(remote_latest_url("warrant_flow_latest.csv")),
        "warrant_stock": read_csv(remote_latest_url("warrant_flow_by_stock_latest.csv")),
        "market_regime": read_csv(remote_latest_url("market_regime_latest.csv")),
        "market_benchmark": read_csv(remote_latest_url("market_benchmark_latest.csv")),
        "futures": read_csv(remote_latest_url("futures_options_indicators_latest.csv")),
        "put_call": read_csv(remote_latest_url("futures_options_put_call_ratio_latest.csv")),
        "tdcc_edge": read_csv(remote_latest_url("tdcc_overheated_short_term_edge_candidates_latest.csv")),
        "weekly_surge": read_csv(remote_latest_url("weekly_surge_strict_parameter_candidates_latest.csv")),
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
        registry = registry[
            registry["pdf_visibility"].astype(str).isin(["pdf_core_model", "pdf_specialty_section"])
        ].copy()
    if registry.empty:
        return []
    registry["_order"] = pd.to_numeric(registry.get("model_registry_order"), errors="coerce").fillna(9999)
    registry = registry.sort_values(["_order", "model_id"])
    return [row.drop(labels=["_order"], errors="ignore") for _, row in registry.iterrows()]


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
    sub["_decision_score"] = pd.to_numeric(sub.get("decision_score"), errors="coerce").fillna(-9999)
    sub = sub.sort_values(["_model_rank", "_display_rank", "_model_score", "_decision_score"], ascending=[True, True, False, False])
    return [row.drop(labels=["_model_rank", "_display_rank", "_model_score", "_decision_score"], errors="ignore") for _, row in sub.iterrows()]


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


def model_split_table(
    rows: list[pd.Series],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    title: str,
    limit: int = 6,
) -> Table:
    data = [["標的", "層級", "模型排名 / 分數", "族群 / 資金", "大戶籌碼", "觀察重點"]]
    if not rows:
        data.append(["-", "-", title, "-", "-", "本模型今日無符合條件資料。"])
    for row in rows[:limit]:
        extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
        rank = clean(row.get("display_rank") or row.get("model_rank"))
        score = num(row.get("model_score"), 1)
        data.append(
            [
                stock_label(row),
                priority_label(row),
                f"#{rank} / {score}" if rank else score,
                f"{category_position_text(row, two_map)} / {zh_warrant(row.get('warrant_flow_signal'))}",
                tdcc_direction(row, extra),
                short(row.get("operation_reminder_zh") or row.get("why_selected_human_zh") or row.get("why_selected_zh") or row.get("why_selected") or observation_focus(row, extra), 82),
            ]
        )
    return build_table(data, [32 * mm, 22 * mm, 30 * mm, 54 * mm, 44 * mm, 86 * mm], 12.0)


def model_recommendation_rows_for_line(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    line: str,
    vol_map: dict[str, pd.Series] | None = None,
    limit: int = 8,
) -> list[list]:
    rows = [["??", "??", "??", "??"]]
    seen: set[tuple[str, str]] = set()
    _, _, line_label = line_titles(line)
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        for row in model_signal_rows(inputs, model_id, line):
            if decision_action_tag(row, two_map, vol_map or {}) not in {"??", "?????"}:
                continue
            sid = clean(row.get("stock_id"))
            key = (sid, model_id)
            if not sid or key in seen:
                continue
            extra = all_map.get(sid, pd.Series(dtype=object))
            verdict = "??" if line == "mainstream" else "????"
            rows.append(
                [
                    red(verdict),
                    red(line_label),
                    red(stock_label(row)),
                    f"{escape_html(model_name)} / {escape_html(model_stage_label(row, extra))}",
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


def model_front_observation_rows_for_line(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    line: str,
    vol_map: dict[str, pd.Series] | None = None,
    limit: int | None = None,
) -> list[list]:
    _, _, line_label = line_titles(line)
    target_limit = limit if limit is not None else (
        FRONT_MAINSTREAM_LIMIT if line == "mainstream" else FRONT_NON_MAINSTREAM_LIMIT
    )
    rows = [["榜別", "模型", "股票", "狀態", "操作提醒"]]
    strict_ids = strict_buy_stock_ids(inputs["decision"], two_map, vol_map)
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        model_rows = 0
        model_display_rows: list[tuple[int, int, list]] = []
        for row in model_signal_rows(inputs, model_id, line):
            sid = clean(row.get("stock_id"))
            if sid in strict_ids:
                continue
            tag = decision_action_tag(row, two_map, vol_map or {})
            if tag == "買進 / 加碼":
                continue
            extra = all_map.get(sid, pd.Series(dtype=object))
            stage = model_stage_label(row, extra) or "觀察"
            action = display_action_tag(tag) or "觀察"
            reminder = (
                row.get("operation_reminder_zh")
                or row.get("next_confirmation_zh")
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
                        f"{escape_html(action)}<br/>{escape_html(short(reminder, 72))}",
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


def append_group_rotation_end_section(story: list, inputs: dict[str, pd.DataFrame], limit: int = 18) -> None:
    group_rotation = inputs.get("group_rotation", pd.DataFrame()).copy()
    if group_rotation.empty:
        return
    if "theme_resolution_status" in group_rotation.columns:
        group_rotation = group_rotation[group_rotation["theme_resolution_status"].astype(str).eq("resolved")].copy()
    if group_rotation.empty:
        return
    story.append(PageBreak())
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










def operation_overview_rows(
    decision: pd.DataFrame,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> list[list]:
    display_limit = 4
    buckets = {
        "嚴格可買": [],
        "非主流短線 / 等確認": [],
        "先不追 / 已有持股降部位": [],
    }
    seen: set[str] = set()
    for _, row in sort_df(decision).iterrows():
        sid = clean(row.get("stock_id"))
        if not sid or sid in seen:
            continue
        tag = decision_action_tag(row, two_map, vol_map or {})
        cat = category_display(clean(row.get("original_category_cn") or row.get("category_cn")))
        side = "主流" if is_core_mainstream_row(row, two_map) else "非主流"
        rank = num(row.get("decision_rank_in_category"), 0)
        text = f"{stock_label(row)}｜{cat}｜{side}｜原#{rank}｜{tag}"
        if tag == "嚴格可買":
            buckets["嚴格可買"].append(text)
        elif tag in {"非主流短線考慮", "非主流觀察", "等確認", "等突破", "僅觀察"}:
            buckets["非主流短線 / 等確認"].append(text)
        else:
            buckets["先不追 / 已有持股降部位"].append(text)
        seen.add(sid)
        if all(len(v) >= display_limit for v in buckets.values()):
            break

    if not buckets["嚴格可買"]:
        buckets["嚴格可買"].append("今日無嚴格可買")
    rows = [["嚴格可買", "非主流短線 / 等確認", "先不追 / 已有持股降部位"]]
    max_len = max([len(v) for v in buckets.values()] + [1])
    for idx in range(min(max_len, display_limit)):
        rows.append(
            [
                buckets["嚴格可買"][idx] if idx < len(buckets["嚴格可買"]) else "",
                buckets["非主流短線 / 等確認"][idx] if idx < len(buckets["非主流短線 / 等確認"]) else "",
                buckets["先不追 / 已有持股降部位"][idx] if idx < len(buckets["先不追 / 已有持股降部位"]) else "",
            ]
        )
    return rows




def strict_buy_stock_ids(
    decision: pd.DataFrame,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> set[str]:
    ids: set[str] = set()
    for _, row in sort_df(decision).iterrows():
        sid = clean(row.get("stock_id"))
        if sid and decision_action_tag(row, two_map, vol_map or {}) in {"嚴格可買", "條件可買"}:
            ids.add(sid)
    return ids




def matches_line(row: pd.Series, two_map: dict[str, pd.Series], line: str) -> bool:
    return is_core_mainstream_row(row, two_map) if line == "mainstream" else not is_core_mainstream_row(row, two_map)


def recommendation_rows_for_line(
    decision: pd.DataFrame,
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    line: str,
    vol_map: dict[str, pd.Series] | None = None,
    limit: int = 8,
) -> list[list]:
    # Deprecated compatibility wrapper: do not fall back to legacy six-category rows.
    # The report entry point uses model_recommendation_rows_for_line(inputs, ...).
    rows = [["??", "??", "??", "??"]]
    return rows






def filter_theme_rows_for_line(themes: pd.DataFrame, line: str) -> pd.DataFrame:
    if themes.empty:
        return themes
    if line == "mainstream":
        mask = themes.get("theme_structural_status", pd.Series(dtype=str)).astype(str).eq("core_mainstream_theme")
    else:
        mask = ~themes.get("theme_structural_status", pd.Series(dtype=str)).astype(str).eq("core_mainstream_theme")
    return themes[mask].copy()


def valid_volume_themes(volume_layer: pd.DataFrame) -> pd.DataFrame:
    if volume_layer.empty:
        return volume_layer
    df = volume_layer[
        ~volume_layer.get("theme_name", pd.Series(dtype=str)).astype(str).str.lower().isin({"", "other", "nan"})
    ].copy()
    df = df[df.get("theme_volume_attack_status", pd.Series(dtype=str)).astype(str) != "theme_status_missing"].copy()
    if "volume_attack_count" in df.columns:
        df["_attack_count"] = pd.to_numeric(df["volume_attack_count"], errors="coerce").fillna(0)
        df = df[df["_attack_count"] > 0].copy()
    else:
        df["_attack_count"] = 0
    for col in ("theme_breadth_score", "theme_strength_score", "theme_risk_score", "median_volume_ratio"):
        df[f"_{col}"] = pd.to_numeric(df.get(col, pd.Series(dtype=float)), errors="coerce").fillna(0)
    df["_overheated"] = (
        df.get("theme_volume_attack_status", pd.Series(dtype=str)).astype(str).str.contains("overheated", case=False, na=False)
        | df.get("theme_mainstream_label", pd.Series(dtype=str)).astype(str).str.contains("overheated", case=False, na=False)
        | df.get("theme_final_status", pd.Series(dtype=str)).astype(str).str.contains("overheated", case=False, na=False)
    ).astype(int)
    df["_above2_count"] = pd.to_numeric(df.get("volume_ratio_above_2_0_count", pd.Series(dtype=float)), errors="coerce").fillna(0)
    df["_leader_confirmed"] = df.get("leader_confirmed", pd.Series(dtype=str)).astype(str).str.lower().isin({"true", "1", "yes"})
    collective_status = df.get("theme_volume_attack_status", pd.Series(dtype=str)).astype(str).isin(
        {"confirmed_volume_theme", "watch_volume_theme"}
    )
    mainstream_structure = df.get("theme_structural_status", pd.Series(dtype=str)).astype(str).eq("core_mainstream_theme")
    breadth_ok = (
        (df["_attack_count"] >= 3)
        & (df["_above2_count"] >= 2)
        & (df["_median_volume_ratio"] >= 1.8)
        & (collective_status | mainstream_structure)
    )
    df = df[(df["_overheated"] == 0) & breadth_ok].copy()
    return df.sort_values(
        ["_theme_breadth_score", "_above2_count", "_attack_count", "_median_volume_ratio", "_theme_strength_score"],
        ascending=[False, False, False, False, False],
    )


def volume_theme_stock_rows(volume_stocks: pd.DataFrame, theme_name: str, limit: int = 3) -> list[pd.Series]:
    if volume_stocks.empty or "theme_name" not in volume_stocks.columns:
        return []
    sub = volume_stocks[volume_stocks["theme_name"].astype(str) == clean(theme_name)].copy()
    if sub.empty:
        return []
    sub["_rank"] = pd.to_numeric(sub.get("volume_breakout_rank", pd.Series(dtype=float)), errors="coerce").fillna(9999)
    sub["_score"] = pd.to_numeric(sub.get("volume_breakout_score", pd.Series(dtype=float)), errors="coerce").fillna(0)
    sub["_ratio"] = pd.to_numeric(sub.get("volume_ratio", pd.Series(dtype=float)), errors="coerce").fillna(0)
    sub = sub.sort_values(["_rank", "_score", "_ratio"], ascending=[True, False, False])
    return [row for _, row in sub.head(limit).iterrows()]


def volume_leader_name(rows: list[pd.Series], idx: int) -> str:
    if idx >= len(rows):
        return "-"
    return stock_label(rows[idx])


def volume_theme_next_flow_note(row: pd.Series) -> str:
    status = clean(row.get("theme_volume_attack_status"))
    label = clean(row.get("theme_mainstream_label"))
    attack_count = to_float(row.get("volume_attack_count")) or 0
    if "overheated" in status or "overheated" in label:
        return "已出量但短線過熱，偏已反應；等回測或第二波擴散。"
    if status == "single_stock_volume_attack" or attack_count <= 1:
        return "目前偏單一個股；看老二、老三是否補量。"
    if status == "non_mainstream_volume_watch":
        return "非主流輪動出量；可用來預判資金是否擴散。"
    if status == "watch_volume_theme":
        return "族群剛開始出量；等第二批個股跟上。"
    if status == "confirmed_volume_theme":
        return "族群出量已確認；優先看龍頭回測不破。"
    return "有出量證據；用來追蹤下一波資金，不直接當買進理由。"


def build_volume_theme_section(
    story: list,
    volume_layer: pd.DataFrame,
    volume_stocks: pd.DataFrame,
    chart_limit: int = 12,
) -> None:
    themes = valid_volume_themes(volume_layer)
    if themes.empty:
        story.append(Paragraph("族群集體出量", H1))
        story.append(
            para(
                "今日無合格族群。集體出量必須是多檔同步、2倍以上量能有擴散，且不是短線過熱或單股輪動；未達條件不列龍頭表，也不畫龍頭 K 線。",
                BODY,
            )
        )
        return
    story.append(Paragraph("族群集體出量（預判下一波資金）", H1))
    story.append(
        para(
            "用途：只列多檔同步、2倍以上量能有擴散，且不是短線過熱或單股輪動的族群。這裡是資金流向預判，不是直接買進名單。",
            BODY_SMALL,
        )
    )
    rows = [["族群", "出量強度", "龍頭", "老二", "老三", "判讀"]]
    leaders_for_charts: list[tuple[str, pd.Series]] = []
    for _, r in themes.iterrows():
        theme = zh_theme_name(r.get("theme_name"))
        stock_rows = volume_theme_stock_rows(volume_stocks, clean(r.get("theme_name")), limit=3)
        if stock_rows:
            leaders_for_charts.append((theme, stock_rows[0]))
        strength = (
            f"{num(r.get('volume_attack_count'), 0)}檔出量；"
            f"中位成交量約 {num(r.get('median_volume_ratio'), 2)}倍；"
            f"2倍以上 {num(r.get('volume_ratio_above_2_0_count'), 0)}檔"
        )
        rows.append(
            [
                theme,
                strength,
                volume_leader_name(stock_rows, 0),
                volume_leader_name(stock_rows, 1),
                volume_leader_name(stock_rows, 2),
                volume_theme_next_flow_note(r),
            ]
        )
    story.append(build_table(rows, [28 * mm, 47 * mm, 34 * mm, 34 * mm, 34 * mm, 91 * mm], 12.0))

    chart_items: list[list] = []
    for theme, row in leaders_for_charts[:chart_limit]:
        sid = stock_id_text(row.get("stock_id"))
        name = clean(row.get("stock_name"))
        chart = plot_stock_chart(sid, name, row)
        if chart:
            img = Image(str(chart), width=252 * mm, height=105 * mm)
            img.hAlign = "CENTER"
            chart_items.append(
                [
                    Paragraph(f"{escape_html(theme)} 龍頭：{escape_html(sid)} {escape_html(name)}", H2),
                    img,
                ]
            )
    if chart_items:
        story.append(Spacer(1, 7))
        story.append(Paragraph("出量族群龍頭 K 線", H2))
        for item in chart_items:
            story.append(KeepTogether(item))







def operation_representatives(
    main_rows: list[pd.Series],
    non_rows: list[pd.Series],
    total_limit: int = 3,
    non_limit: int = 1,
) -> list[pd.Series]:
    reps = list(main_rows[:total_limit])
    remaining = total_limit - len(reps)
    if remaining > 0 and non_rows:
        reps.extend(non_rows[: min(non_limit, remaining)])
    return reps[:total_limit]




def category_position_text(row: pd.Series, two_map: dict[str, pd.Series]) -> str:
    source, _, group, _ = line_source(row, two_map)
    structural, label = line_structure(row, two_map)
    _, status = line_raw(row, two_map)
    if is_core_mainstream_row(row, two_map):
        return "主流族群，資金線較完整。"
    if source == RISK_SOURCE or group == "risk":
        return "風險線，條件回復前不列買進。"
    if structural == "non_mainstream_theme" or group == "non_mainstream_flow_watch":
        return "非主流族群，只追蹤輪動延續。"
    if source == LATENT_SOURCE:
        return "個股訊號，只看個股確認。"
    if status == "emerging_theme":
        return "早期題材，要等族群擴散。"
    if "overheated" in status or "overheated" in label:
        return "短線過熱，先等回測。"
    return "資料不足，只能觀察。"


def pattern_subtype_label(row: pd.Series, extra: pd.Series | None = None) -> str:
    return pattern_stage_label(row, prefer_w_bottom=True, extra=extra) or "型態待確認"


def pattern_subtype_order_key(label: str) -> int:
    try:
        return PATTERN_SUBTYPE_ORDER.index(label)
    except ValueError:
        return len(PATTERN_SUBTYPE_ORDER)


def pattern_subtype_lines(
    rows: list[pd.Series],
    limit: int,
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
) -> list[str]:
    lines: list[str] = []
    for row in rows[:limit]:
        sid = clean(row.get("stock_id"))
        action_row = row
        extra = all_map.get(sid, pd.Series(dtype=object))
        if isinstance(extra, pd.Series) and not extra.empty:
            if decision_action_tag(extra, two_map, vol_map or {}) == "嚴格可買":
                action_row = extra
        action = display_action_tag(decision_action_tag(action_row, two_map, vol_map or {}))
        lines.append(f"{escape_html(stock_label(row))}｜{escape_html(action)}")
    return lines


def pattern_subtype_overview_table(
    ranked_rows: list[pd.Series],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None = None,
    main_limit: int = PATTERN_SUBTYPE_MAIN_LIMIT,
    non_limit: int = PATTERN_SUBTYPE_NON_LIMIT,
) -> Table:
    grouped: dict[str, list[pd.Series]] = {}
    for row in ranked_rows:
        extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
        grouped.setdefault(pattern_subtype_label(row, extra), []).append(row)
    labels = sorted(grouped, key=pattern_subtype_order_key)
    data = [["型態分型", f"主流前{main_limit}", f"非主流前{non_limit}", "看法"]]
    for label in labels:
        main_rows, non_rows = split_mainstream_rows(grouped[label], two_map)
        main_lines = pattern_subtype_lines(main_rows, main_limit, all_map, two_map, vol_map)
        non_lines = pattern_subtype_lines(non_rows, non_limit, all_map, two_map, vol_map)
        if not main_lines and not non_lines:
            continue
        if label == "W底右側":
            note = "優先觀察底部右側是否延續，不能只因回升就追價。"
        elif label == "已突破待確認":
            note = "已突破但仍看是否守住關鍵價，跌回就降級。"
        elif label == "接近突破":
            note = "接近壓力，等放量突破才升級。"
        elif label == "平台右側":
            note = "平台整理偏右側，等站上平台壓力。"
        elif label == "回測支撐":
            note = "看回測是否守住支撐，失守不買。"
        elif label == "預備發動":
            note = "早期轉強，先看量價是否延續。"
        elif label == "築底整理":
            note = "仍在整理，不急著買。"
        else:
            note = "型態資料不足，只能觀察。"
        data.append(
            [
                red(label),
                "<br/>".join(main_lines) if main_lines else "無主流候選",
                "<br/>".join(non_lines) if non_lines else "無非主流候選",
                note,
            ]
        )
    if len(data) == 1:
        data.append(["型態待確認", "無主流候選", "無非主流候選", "資料不足，只能觀察。"])
    return build_table(data, [34 * mm, 82 * mm, 58 * mm, 94 * mm], 12.0)


def pattern_subtype_representatives(
    ranked_rows: list[pd.Series],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    total_limit: int = PATTERN_SUBTYPE_OPERATION_LIMIT,
) -> list[pd.Series]:
    grouped: dict[str, list[pd.Series]] = {}
    for row in ranked_rows:
        extra = all_map.get(clean(row.get("stock_id")), pd.Series(dtype=object))
        grouped.setdefault(pattern_subtype_label(row, extra), []).append(row)
    reps: list[pd.Series] = []
    seen: set[str] = set()
    for label in sorted(grouped, key=pattern_subtype_order_key):
        main_rows, non_rows = split_mainstream_rows(grouped[label], two_map)
        candidates = main_rows or non_rows
        if not candidates:
            continue
        row = candidates[0]
        sid = clean(row.get("stock_id"))
        if sid and sid not in seen:
            reps.append(row)
            seen.add(sid)
        if len(reps) >= total_limit:
            break
    return reps


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
        if "false_breakout" in text or "假突破" in raw:
            return "假突破風險"
        if "overheat" in text or "過熱" in raw or "已反應" in raw:
            return "短線過熱或利多已反應"
        if "資料不足" in raw or "data" in text:
            return "資料不足"
        if "repeated_but_no_breakout" not in text and "反覆上榜" not in raw and "連續上榜" not in raw:
            return short(raw, 72)
    action = decision_action_tag(row, two_map, vol_map or {})
    source, _, group, _ = line_source(row, two_map)
    _, status = line_raw(row, two_map)
    structural, label = line_structure(row, two_map)
    if "overheated" in status or "overheated" in label:
        return "短線漲幅或量能過熱，先等回測或重新確認"
    if action in {"嚴格可買", "條件可買"}:
        cautions: list[str] = []
        if not is_core_mainstream_row(row, two_map):
            cautions.append("非核心主流，只能短線處理")
        overheat = clean(row.get("overheat_status")).lower()
        if "priced_in" in overheat or "overheated" in overheat:
            cautions.append("短線已有反應，避免追價")
        vol = to_float(row.get("volume_ratio"))
        if vol is not None and vol > 5:
            cautions.append("量能偏急，注意長上影")
        ret20 = to_float(row.get("return_20d"))
        if ret20 is not None and ret20 > 20:
            cautions.append("短線漲幅偏高")
        return " / ".join(cautions) if cautions else "不利因素不明顯，重點是照價位控風險"
    if action == "非主流短線考慮":
        return "非核心主流，失去量能就退出"
    if structural != "core_mainstream_theme" or group == "non_mainstream_flow_watch":
        return "非主流，族群延續性不足"
    if source == RISK_SOURCE or group == "risk":
        return "已進風險線，條件回復前不列買進名單"
    if status not in MAINSTREAM_THEME_STATUSES:
        return "主流資金未確認"
    if action in {"等確認", "等突破"}:
        return "無明確風險，買點未確認"
    return "無明確風險"


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


def quality_reason(row: pd.Series, extra: pd.Series | None = None) -> str:
    source = extra if isinstance(extra, pd.Series) and not extra.empty else row
    parts: list[str] = []
    tdcc = tdcc_direction(row, source).replace("大戶籌碼：", "大戶")
    if tdcc:
        parts.append(tdcc)
    ret20 = to_float(first_text(row.get("return_20d"), source.get("return_20d_pct")))
    if ret20 is not None:
        if ret20 <= 10:
            parts.append("位階較低")
        elif ret20 <= 20:
            parts.append("位階尚可")
        elif ret20 <= 30:
            parts.append("短線漲幅偏高")
        else:
            parts.append("短線漲幅過大")
    vol = to_float(first_text(row.get("volume_ratio"), source.get("volume_ratio")))
    if vol is not None:
        if 1.5 <= vol <= 5:
            parts.append("量能放大")
        elif vol > 5:
            parts.append("量大偏急")
        elif vol > 0:
            parts.append("量能不足")
    overheat = clean(first_text(row.get("overheat_status"), source.get("overheat_status"))).lower()
    if overheat in {"not_overheated", "normal", "none", ""}:
        parts.append("未過熱")
    elif "priced_in" in overheat:
        parts.append("已反應風險")
    elif "overheated" in overheat:
        parts.append("過熱風險")
    return " / ".join(parts[:4]) or "依程式端品質排序"


def buy_condition_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, close_value = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    level_value = to_float(level_text)
    if level_label == "短線壓力" and level_text:
        return f"收盤放量站上壓力 {level_text}，才由觀察轉買點。"
    if level_label == "短線支撐" and level_text:
        return f"已站在支撐 {level_text} 上方；若屬推薦可買，只在靠近支撐或量價維持時執行，不追急拉。"
    if level_label == "關鍵價" and level_text:
        if close_value is not None and level_value is not None and close_value >= level_value:
            return f"已站上關鍵價 {level_text}；若屬推薦可買，只在量價維持時執行，不追急拉。"
        return f"收盤站上關鍵價 {level_text}，才可評估。"
    if pressures:
        return f"收盤站上壓力 {num(pressures[0])}，才可評估。"
    if supports:
        return f"守住支撐 {num(supports[0])}，並出現轉強K線，才可評估。"
    return "等收盤站上關鍵價，且成交量延續，才可評估。"


def no_buy_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, _ = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    level_value = to_float(level_text)
    close_value = to_float(first_text(row.get("close"), extra.get("close") if isinstance(extra, pd.Series) else ""))
    if level_label == "關鍵價" and level_text:
        if close_value is not None and level_value is not None and close_value >= level_value:
            return f"買進後跌破關鍵價 {level_text}，不買或退出。"
        return f"收盤未站上關鍵價 {level_text}，不買。"
    if supports:
        return f"買進後跌破支撐 {num(supports[0])}，不買或退出。"
    if pressures:
        return f"只碰壓力 {num(pressures[0])} 但收盤站不上，不買。"
    return "價格未站穩關鍵價，或爆量長上影，不買。"


def exit_summary(row: pd.Series, extra: pd.Series) -> str:
    supports, pressures, _ = nearby_price_levels(row, extra)
    level_label, level_text, _ = key_level_context(row, extra)
    if level_label == "關鍵價" and level_text:
        return f"跌破關鍵價 {level_text} 退出。急拉長上影先降部位。"
    if supports and pressures:
        return f"靠近壓力 {num(pressures[0])} 轉弱先降部位。跌破支撐 {num(supports[0])} 退出。"
    if supports:
        return f"跌破支撐 {num(supports[0])} 退出。急拉長上影先降部位。"
    if pressures:
        return f"靠近壓力 {num(pressures[0])} 量縮或長上影，先降部位。"
    return "跌回確認區或量能失控，退出。"


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


def operation_decision_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
    extra: pd.Series,
) -> tuple[str, list[str]]:
    action = display_action_tag(decision_action_tag(row, two_map, vol_map or {}))
    if action in {"推薦可買", "可買候選"}:
        return f"{action}，但只在買進條件成立時執行。", [action]
    if action in {"等確認", "等突破", "短線觀察", "觀察"}:
        return f"{action}，目前不是正式買點。{observation_focus(row, extra)}", [action, "目前不是正式買點"]
    if action in {"不列入", "不碰"}:
        return f"{action}，目前不買。{drawback_brief(row, two_map, vol_map)}", [action, "目前不買"]
    return f"{action or '觀察'}，目前不買。{observation_focus(row, extra)}", [action or "觀察", "目前不買"]


def operation_buy_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
    extra: pd.Series,
) -> tuple[str, list[str]]:
    action = display_action_tag(decision_action_tag(row, two_map, vol_map or {}))
    condition = buy_condition_summary(row, extra)
    condition = condition.replace("才由觀察轉買點", "才重新評估買點")
    condition = condition.replace("才可評估", "才重新評估買點")
    if action in {"推薦可買", "可買候選"}:
        return condition, ["買點"]
    return f"目前不買。{condition}", ["目前不買"]


def operation_no_buy_sentence(row: pd.Series, extra: pd.Series) -> str:
    return no_buy_summary(row, extra)


def operation_exit_sentence(row: pd.Series, extra: pd.Series) -> str:
    return f"若已持有，{exit_summary(row, extra)}"


def operation_risk_sentence(
    row: pd.Series,
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series] | None,
) -> str:
    risk = drawback_brief(row, two_map, vol_map)
    if risk in {"無明確風險", "無明確風險，買點未確認"}:
        return "不利因素不明顯，重點是照價位控風險。"
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
        parts.append("籌碼扣分，警示解除前不列買點。")
    elif label == "中性":
        parts.append("籌碼不構成主要加分。")
    else:
        parts.append("資料不足，只能回到價格與量能確認。")
    return " ".join(parts)


def operation_conclusion(row: pd.Series, two_map: dict[str, pd.Series], vol_map: dict[str, pd.Series] | None, extra: pd.Series) -> str:
    action = display_action_tag(decision_action_tag(row, two_map, vol_map or {}))
    if action in {"推薦可買", "可買候選"}:
        return f"條件式買進。{buy_condition_summary(row, extra)}"
    return f"{action}，目前不買。{observation_focus(row, extra)}"


def build_operation_page(
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
    story.append(Paragraph(f"{sid} {name}｜{model_display(row)}", H2))

    decision_text, decision_marks = operation_decision_sentence(row, two_map, vol_map, extra)
    buy_text, buy_marks = operation_buy_sentence(row, two_map, vol_map, extra)
    op_rows = [
        ["操作結論", decision_text, decision_marks, 112],
        ["優點", selection_brief(row, extra), ["成交量放大", "籌碼", "突破"], 106],
        ["關鍵價位", price_plan_summary(row, extra), ["支撐", "壓力"], 98],
        ["買進條件", buy_text, buy_marks, 112],
        ["不買條件", operation_no_buy_sentence(row, extra), ["不買"], 100],
        ["停利退出", operation_exit_sentence(row, extra), ["降部位", "退出"], 104],
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
    story.append(op_table)
    story.append(Spacer(1, 4))
    story.append(chart_table)
    story.append(PageBreak())






def build_curated_pdf_for_line(
    inputs: dict[str, pd.DataFrame],
    all_map: dict[str, pd.Series],
    two_map: dict[str, pd.Series],
    vol_map: dict[str, pd.Series],
    line: str,
) -> Path:
    decision = inputs["decision"]
    title, _, line_label = line_titles(line)
    rec_rows = model_recommendation_rows_for_line(inputs, all_map, two_map, line, vol_map)
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} {title}", TITLE),
        date_note(),
        Spacer(1, 4),
        Paragraph(f"{line_label}推薦結論", H1),
    ]
    if len(rec_rows) > 1:
        story.extend(
            [
                para("以下僅使用 repo structured data 既有欄位與排序結果，不在 PDF 端新增買進或排除規則。", BODY_SMALL),
                build_table(rec_rows, [28 * mm, 24 * mm, 54 * mm, 162 * mm], 12.0),
            ]
        )
    else:
        story.append(para("本日無符合條件的推薦結論。", BODY))
    story.append(PageBreak())
    story.extend(
        [
            Paragraph(f"{line_label}觀察清單", H1),
            para("以下依 program-side 新版候選模型列示；同一檔股票可在多個模型重複出現。舊六分類只作來源背景，不作本頁主分類。", BODY_SMALL),
            build_table(
                model_front_observation_rows_for_line(inputs, all_map, two_map, line, vol_map),
                [24 * mm, 36 * mm, 34 * mm, 112 * mm, 62 * mm],
                12.0,
            ),
        ]
    )

    operation_seen: set[str] = set()
    buyable_ids = strict_buy_stock_ids(decision, two_map, vol_map)
    limit = MAIN_REPORT_MAINSTREAM_LIMIT if line == "mainstream" else MAIN_REPORT_NON_MAINSTREAM_LIMIT
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        ranked_rows = model_signal_rows(inputs, model_id, line)
        ranked_rows = [
            row
            for row in ranked_rows
            if not (
                clean(row.get("stock_id")) in buyable_ids
                and decision_action_tag(row, two_map, vol_map or {}) not in {"嚴格可買", "條件可買"}
            )
        ]
        if not ranked_rows:
            continue
        story.append(PageBreak())
        story.append(Paragraph(model_name, H1))
        desc = clean(spec.get("model_description_zh"))
        if desc:
            story.append(para(desc, BODY_SMALL))
        story.append(model_split_table(ranked_rows, two_map, all_map, line_label, limit=limit))
        reps = operation_representatives(
            ranked_rows if line == "mainstream" else [],
            ranked_rows if line != "mainstream" else [],
        )
        for row in reps:
            sid = clean(row.get("stock_id"))
            if sid and sid in operation_seen:
                continue
            build_operation_page(row, all_map, two_map, story, vol_map)
            if sid:
                operation_seen.add(sid)

    append_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out


def build_full_candidate_pdf_for_line(
    inputs: dict[str, pd.DataFrame],
    two_map: dict[str, pd.Series],
    all_map: dict[str, pd.Series],
    line: str,
) -> Path:
    decision = inputs["decision"]
    _, title, line_label = line_titles(line)
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
    tdcc_rows = [["標的", "模型/來源", "操作標記", "TDCC 摘要"]]
    seen_tdcc: set[str] = set()
    for _, r in sort_df(decision).iterrows():
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
                display_action_tag(decision_action_tag(r, two_map)),
                short(detail, 180),
            ]
        )
        seen_tdcc.add(sid)
        if len(tdcc_rows) >= 19:
            break
    story.append(build_table(tdcc_rows, [34 * mm, 42 * mm, 22 * mm, 170 * mm], 12.0) if len(tdcc_rows) > 1 else para("本分流沒有可用的 TDCC 摘要。", BODY))

    story.append(Paragraph(f"{line_label}完整候選", H1))
    limit = FULL_REPORT_MAINSTREAM_LIMIT if line == "mainstream" else FULL_REPORT_NON_MAINSTREAM_LIMIT
    for spec in core_model_specs(inputs, line):
        model_id = clean(spec.get("model_id"))
        model_name = clean(spec.get("model_name_zh"), model_id)
        line_rows = model_signal_rows(inputs, model_id, line)
        story.append(Paragraph(model_name, H2))
        if not line_rows:
            story.append(para("無符合條件資料。", BODY))
            continue
        story.append(model_split_table(line_rows, two_map, all_map, line_label, limit=limit))

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
            story.append(Paragraph(zh_line_group(group), H2))
            rows = [["標的", "模型/來源", "正式狀態", "優先序", "說明"]]
            for _, r in sub.iterrows():
                sid = clean(r.get("stock_id"))
                rows.append(
                    [
                        f"{sid} {clean(r.get('stock_name'))}",
                        preferred_model_label_for_stock(inputs, sid, line) or "模型訊號未對應",
                        f"{zh_theme_status(r.get('theme_final_status'))} / {zh_structural_status(r.get('theme_structural_status'))} / {zh_mainstream_label(r.get('theme_mainstream_label'))}",
                        zh_priority_short(r.get("decision_priority")),
                        short(r.get("theme_leadership_note") or r.get("candidate_line") or r.get("why_selected"), 110),
                    ]
                )
            story.append(build_table(rows, [36 * mm, 44 * mm, 76 * mm, 30 * mm, 82 * mm], 12.0))
        if not found_any:
            story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))
    else:
        story.append(para("本分流沒有可用的雙線與輪動摘要。", BODY))

    append_group_rotation_end_section(story, inputs)
    out = OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_{title}{OUTPUT_SUFFIX}.pdf"
    write_pdf(out, story, title)
    return out


def build_warrant_pdf(inputs: dict[str, pd.DataFrame]) -> Path:
    warrant = inputs["warrant"]
    decision = inputs["decision"]
    story: list = [
        Paragraph(f"{DATA_DATE_SLASH} 權證市場輔助分析", TITLE),
        date_note(),
        para("權證只作為輔助訊號；任何偏多、偏空或權證過熱的狀態都必須回到現股價格與量能確認。", BODY),
        Spacer(1, 4),
        Paragraph("權證市場概況", H1),
    ]
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
    if not warrant.empty and not decision.empty:
        w_signal = set(
            warrant[
                warrant.get("warrant_flow_signal", pd.Series(dtype=str)).astype(str).str.contains("call|bull|inflow", case=False, na=False)
            ]["stock_id"].astype(str)
        )
        inter = sort_df(decision[decision["stock_id"].astype(str).isin(w_signal)].copy()).head(28)
        rows = [["標的", "模型/來源", "層級", "權證訊號", "條件式解讀"]]
        for _, r in inter.iterrows():
            sid = clean(r.get("stock_id"))
            rows.append(
                [
                    stock_label(r),
                    preferred_model_label_for_stock(inputs, sid) or "模型訊號未對應",
                    priority_label(r),
                    zh_warrant(r.get("warrant_flow_signal")),
                    "權證偏多只能輔助；必須現股收盤守穩關鍵價位且量能延續，否則不買。",
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
                    "只作提醒，不作單獨賣出或買進理由 / 回到現股價量與大戶資料確認。",
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


def build_market_pdf(inputs: dict[str, pd.DataFrame]) -> Path:
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


def validate_outputs(paths: list[Path]) -> None:
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
            required = ["結論", "族群", "可買"]
            required_missing = [term for term in required if term not in text]
        if missing or hits or required_missing:
            validation_errors.append(
                f"{path.name}: text_missing={missing}, forbidden_hits={hits}, required_missing={required_missing}"
            )
        report_lines.append(
            {
                "file": path.name,
                "pages": len(reader.pages),
                "text_chars": len(text),
                "text_missing": missing,
                "forbidden_hits": hits,
                "required_missing": required_missing,
            }
        )
    pd.DataFrame(report_lines).to_csv(OUT / f"{REQUEST_DATE}_requested_repo{DATA_DATE}_pdf_validation.csv", index=False, encoding="utf-8-sig")
    if validation_errors:
        raise RuntimeError("pdf_validation_failed: " + " | ".join(validation_errors))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the six ChatGPT-side daily Taiwan stock PDF deliverables."
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
    parser.add_argument(
        "--request-date",
        default=REQUEST_DATE,
        help="Requested calendar date in YYYYMMDD. Freshness is still determined by repo README.",
    )
    return parser.parse_args()


def configure_paths(args: argparse.Namespace) -> None:
    global REPO, LATEST, DATA, OUT, CHARTS, TDCC_WINDOW_DIRS, REQUEST_DATE

    REPO = args.repo_root.expanduser().resolve()
    LATEST = REPO / "output" / "latest"
    DATA = REPO / "data"
    OUT = args.output_dir.expanduser().resolve()
    CHARTS = OUT / "charts"
    TDCC_WINDOW_DIRS = [
        LATEST / "individual_stock_tdcc_windows",
        REPO / "docs" / "latest" / "individual_stock_tdcc_windows",
    ]
    REQUEST_DATE = str(args.request_date)


def main() -> None:
    args = parse_args()
    configure_paths(args)
    enforce_fresh_repo_data()
    OUT.mkdir(exist_ok=True)
    CHARTS.mkdir(parents=True, exist_ok=True)
    inputs = load_inputs()
    all_map, two_map, vol_map = get_stock_extra_maps(inputs["all"], inputs["two_line"], inputs["volume_stocks"])
    paths = [
        build_curated_pdf_for_line(inputs, all_map, two_map, vol_map, "mainstream"),
        build_full_candidate_pdf_for_line(inputs, two_map, all_map, "mainstream"),
        build_curated_pdf_for_line(inputs, all_map, two_map, vol_map, "non_mainstream"),
        build_full_candidate_pdf_for_line(inputs, two_map, all_map, "non_mainstream"),
        build_warrant_pdf(inputs),
        build_market_pdf(inputs),
    ]
    validate_outputs(paths)
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
