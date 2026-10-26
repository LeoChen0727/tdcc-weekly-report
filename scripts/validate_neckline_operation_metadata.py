"""Independently check frozen neckline trade/stock metadata, without replaying trades.

This validates identity counts and mirrored metadata only. It does not validate
prices, point-in-time availability, strategy performance, or promotion readiness.
"""
from __future__ import annotations

import ast
import csv
import hashlib
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "neckline_volume_breakout_confirmation"
MODULE_ID = "neckline_strict_45_signal_90_score_v1"
DETAIL_PATH = Path(
    "output/latest/research_backtest/"
    "neckline_strict_45_signal_90_score_operation_candidate_detail_latest.csv"
)
DETAIL_CANONICAL_SHA256 = "a12aa68687221a8b756791e0dbed7a7e761c66c8a8e626728836b29e3b3d3f2f"
EXPECTED_TRADE_COUNT = 51
EXPECTED_UNIQUE_STOCK_COUNT = 50
CSV_CONSUMERS = (
    (
        Path("output/latest/approved_operation_patterns_latest.csv"),
        Path("docs/latest/approved_operation_patterns_latest.csv"),
        {"model_id": MODEL_ID, "operation_module_id": MODULE_ID},
        ("best_evidence_sample_size", "neckline_confirmation_candidate_count", "neckline_tradable_entry_count"),
        "neckline_unique_stock_count",
    ),
    (
        Path("output/latest/daily_model_parameter_recommendations_latest.csv"),
        Path("docs/latest/daily_model_parameter_recommendations_latest.csv"),
        {"model_id": MODEL_ID, "parameter_set_id": MODULE_ID, "sample_status": "approved_operation_v1"},
        ("selected_stock_days",),
        "selected_unique_stocks",
    ),
    (
        Path("output/latest/research_backtest/daily_model_research_parity_latest.csv"),
        Path("docs/latest/daily_model_research_parity_latest.csv"),
        {"model_id": MODEL_ID, "research_baseline_parameter_set_id": MODULE_ID},
        ("baseline_selected_stock_days",),
        "baseline_selected_unique_stocks",
    ),
)
MARKDOWN_PATHS = (
    Path("output/latest/research_backtest/daily_model_research_parity_latest.md"),
    Path("docs/latest/daily_model_research_parity_latest.md"),
)


def canonical_bytes(path: Path) -> bytes:
    """Use Git's LF content basis, permitting Windows checkout line endings."""
    return path.read_bytes().replace(b"\r\n", b"\n")


def read_rows(root: Path, relative: Path, required: set[str], errors: list[str]) -> list[dict[str, str]]:
    try:
        reader = csv.DictReader(io.StringIO((root / relative).read_text(encoding="utf-8-sig")), strict=True)
        fields = reader.fieldnames or []
        if len(fields) != len(set(fields)) or not required.issubset(fields):
            errors.append(f"{relative}: 欄位缺漏或重複")
            return []
        rows = list(reader)
        if any(None in row or any(value is None for value in row.values()) for row in rows):
            errors.append(f"{relative}: CSV 列寬不一致")
            return []
        return rows
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"{relative}: 無法讀取 CSV ({exc})")
        return []


def check_mirror(root: Path, left: Path, right: Path, errors: list[str]) -> None:
    try:
        if canonical_bytes(root / left) != canonical_bytes(root / right):
            errors.append(f"{left}: mirror 與 {right} 不一致")
    except OSError as exc:
        errors.append(f"{left}: 無法讀取 mirror ({exc})")


def check_producer_metadata(root: Path, trades: int, stocks: int, errors: list[str]) -> None:
    relative = Path("scripts/build_approved_operation_patterns.py")
    try:
        tree = ast.parse((root / relative).read_text(encoding="utf-8-sig"))
        nodes = [
            node.value for node in tree.body
            if isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "NECKLINE_APPROVAL_METRICS" for target in node.targets)
        ]
        if len(nodes) != 1:
            raise ValueError("NECKLINE_APPROVAL_METRICS 必須只有一個 literal 定義")
        metrics = ast.literal_eval(nodes[0])
        for field, expected in (
            ("tradable_entry_count", trades),
            ("confirmation_candidate_count", trades),
            ("unique_stock_count", stocks),
        ):
            if metrics.get(field) != str(expected):
                errors.append(f"{relative}: NECKLINE_APPROVAL_METRICS[{field}] 必須為 {expected}")
    except (OSError, UnicodeError, SyntaxError, ValueError, TypeError, AttributeError) as exc:
        errors.append(f"{relative}: 無法獨立解析頸線中繼資料 ({exc})")


def validate_metadata(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        digest = hashlib.sha256(canonical_bytes(root / DETAIL_PATH)).hexdigest()
    except OSError as exc:
        return [f"{DETAIL_PATH}: 無法讀取凍結逐筆 ({exc})"]
    if digest != DETAIL_CANONICAL_SHA256:
        return [f"{DETAIL_PATH}: 凍結 detail canonical SHA-256 不符；不得改用新逐筆自動更新核准中繼資料"]
    detail = read_rows(root, DETAIL_PATH, {"model_id", "operation_candidate_id", "stock_id", "tradability_status"}, errors)
    if not detail:
        return errors or [f"{DETAIL_PATH}: 凍結逐筆不可為空"]
    if any(
        row["model_id"] != MODEL_ID or row["operation_candidate_id"] != MODULE_ID
        or row["tradability_status"] != "tradable" or not row["stock_id"].strip()
        for row in detail
    ):
        errors.append(f"{DETAIL_PATH}: 凍結逐筆模型、可交易狀態或股票識別不符")
    trades = len(detail)
    stocks = len({row["stock_id"].strip() for row in detail})
    if (trades, stocks) != (EXPECTED_TRADE_COUNT, EXPECTED_UNIQUE_STOCK_COUNT):
        errors.append(f"{DETAIL_PATH}: 必須保留 51 筆交易／50 檔股票，實際 {trades}／{stocks}")
    if errors:
        return errors

    check_producer_metadata(root, trades, stocks, errors)
    for output, mirror, selector, trade_fields, stock_field in CSV_CONSUMERS:
        for relative in (output, mirror):
            rows = read_rows(root, relative, set(selector) | set(trade_fields) | {stock_field}, errors)
            selected = [row for row in rows if all(row.get(key) == value for key, value in selector.items())]
            if len(selected) != 1:
                errors.append(f"{relative}: 必須有且只有一列指定頸線中繼資料，實際 {len(selected)}")
                continue
            for field, expected in [(field, trades) for field in trade_fields] + [(stock_field, stocks)]:
                if selected[0][field] != str(expected):
                    errors.append(f"{relative}: {field} 必須為 {expected}，實際 {selected[0][field]!r}")
        check_mirror(root, output, mirror, errors)

    expected_headers = {"model_id", "baseline_selected_stock_days", "baseline_selected_unique_stocks"}
    for relative in MARKDOWN_PATHS:
        try:
            rows = [
                [cell.strip() for cell in line.strip().strip("|").split("|")]
                for line in (root / relative).read_text(encoding="utf-8").splitlines()
                if line.lstrip().startswith("|")
            ]
            headers = [row for row in rows if expected_headers.issubset(row)]
            if len(headers) != 1:
                raise ValueError("缺少唯一中繼資料表頭")
            header = headers[0]
            selected = [row for row in rows if row and row[0] == MODEL_ID]
            if len(selected) != 1 or len(selected[0]) != len(header):
                raise ValueError("缺少唯一頸線中繼資料列")
            row = dict(zip(header, selected[0]))
            if row["baseline_selected_stock_days"] != str(trades) or row["baseline_selected_unique_stocks"] != str(stocks):
                raise ValueError("頸線必須為 51 筆交易／50 檔股票")
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f"{relative}: Markdown 中繼資料不符 ({exc})")
    check_mirror(root, *MARKDOWN_PATHS, errors)
    return errors


def main() -> int:
    errors = validate_metadata()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("頸線操作中繼資料驗證通過：凍結 51 筆交易、50 檔股票；3 種 CSV consumer 與鏡像及 parity Markdown 一致。")
    print("此檢查僅驗證凍結中繼資料，不構成價格、PIT、報酬或模型升級證據。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
