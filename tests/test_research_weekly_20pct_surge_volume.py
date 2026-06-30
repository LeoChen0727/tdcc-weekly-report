from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from research_weekly_20pct_surge_volume import read_price  # noqa: E402


def test_read_price_preserves_market_column(tmp_path: Path) -> None:
    price_csv = tmp_path / "2330.csv"
    price_csv.write_text(
        "\n".join(
            [
                "date,stock_id,stock_name,market,open,high,low,close,volume",
                "20260630,2330,台積電,TWSE,1000,1010,990,1005,123456",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    df = read_price(price_csv)

    assert list(df["market"]) == ["TWSE"]


def test_read_price_requires_market_column(tmp_path: Path) -> None:
    price_csv = tmp_path / "2330.csv"
    price_csv.write_text(
        "\n".join(
            [
                "date,stock_id,stock_name,open,high,low,close,volume",
                "20260630,2330,台積電,1000,1010,990,1005,123456",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    df = read_price(price_csv)

    assert df.empty
