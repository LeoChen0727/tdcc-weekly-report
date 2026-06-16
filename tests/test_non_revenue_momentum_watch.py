from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_non_revenue_momentum_watch as builder  # noqa: E402


def test_non_revenue_momentum_empty_output_keeps_csv_contract(tmp_path, monkeypatch) -> None:
    out_csv = tmp_path / "non_revenue_momentum_watch_latest.csv"
    out_md = tmp_path / "non_revenue_momentum_watch_latest.md"
    docs_dir = tmp_path / "docs" / "latest"
    docs_csv = docs_dir / out_csv.name
    docs_md = docs_dir / out_md.name

    monkeypatch.setattr(builder, "OUT_CSV", out_csv)
    monkeypatch.setattr(builder, "OUT_MD", out_md)
    monkeypatch.setattr(builder, "DOCS_LATEST_DIR", docs_dir)
    monkeypatch.setattr(builder, "DOCS_CSV", docs_csv)
    monkeypatch.setattr(builder, "DOCS_MD", docs_md)
    monkeypatch.setattr(builder, "read_main_price_date", lambda: "20260612")
    monkeypatch.setattr(builder, "now_text", lambda: "2026-06-15 12:00:00 Asia/Taipei")

    builder.write_outputs(pd.DataFrame(columns=builder.OUTPUT_COLUMNS))

    df = pd.read_csv(out_csv, dtype=str, keep_default_na=False)
    docs_df = pd.read_csv(docs_csv, dtype=str, keep_default_na=False)

    assert df.empty
    assert list(df.columns) == builder.OUTPUT_COLUMNS
    assert list(docs_df.columns) == builder.OUTPUT_COLUMNS
    assert "No rows matched the non-revenue momentum watch conditions." in out_md.read_text(encoding="utf-8")
    assert docs_md.exists()
