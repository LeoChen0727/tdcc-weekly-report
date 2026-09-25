from __future__ import annotations

import hashlib
from pathlib import Path
import shutil
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_revenue_unreacted_range_operation_section as builder  # noqa: E402
import validate_daily_revenue_unreacted_range_operation_section as validator  # noqa: E402


def _objective_fixture(tmp_path: Path) -> dict[str, object]:
    dates = pd.bdate_range("2026-03-02", periods=170).strftime("%Y%m%d").tolist()
    assert dates[130] == builder.FORMAL_SIGNAL_EFFECTIVE_FROM

    rising = [50.0 + (30.0 * index / 109.0) for index in range(110)]
    falling = [80.0 - (12.0 * index / 15.0) for index in range(1, 16)]
    closes = rising + falling
    assert len(closes) == 125
    closes.extend([68.0, 67.0, 66.0, 65.0, 64.0])
    closes.extend([82.0, 83.0, 84.0])
    closes.extend([84.0 + (index % 3) * 0.1 for index in range(37)])
    assert len(closes) == len(dates)
    opens = list(closes)
    opens[132] = 84.5
    price = pd.DataFrame(
        {
            "date": dates,
            "open": opens,
            "high": [round(value * 1.01, 6) for value in closes],
            "low": [round(value * 0.99, 6) for value in closes],
            "close": closes,
        }
    )
    price_dir = tmp_path / "data" / "stock_price_history"
    price_dir.mkdir(parents=True)
    price_path = price_dir / "1234.csv"
    price.to_csv(price_path, index=False, lineterminator="\n")

    monthly_path = (
        tmp_path
        / "data"
        / "monthly_revenue_history"
        / "monthly_revenue_history.csv"
    )
    monthly_path.parent.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "stock_id": "1234",
                "stock_name": "測試公司",
                "revenue_period": "202607",
                "source_table_date": dates[125],
                "latest_revenue_yoy_pct": "35.0",
                "cumulative_revenue_yoy_pct": "21.0",
                "point_in_time_status": "ready_exchange_release",
                "research_join_allowed": "True",
                "revenue_numerical_anomaly_flag": "False",
            }
        ]
    ).to_csv(monthly_path, index=False, lineterminator="\n")

    taxonomy_path = tmp_path / "config" / "stock_theme_map.csv"
    taxonomy_path.parent.mkdir(parents=True)
    pd.DataFrame(
        [
            {
                "stock_id": "1234",
                "stock_name": "測試公司",
                "theme_mainstream_label": "core_mainstream",
                "primary_theme": "測試主題",
                "industry": "測試產業",
            }
        ]
    ).to_csv(taxonomy_path, index=False, lineterminator="\n")
    return {
        "dates": dates,
        "monthly_path": monthly_path,
        "price_dir": price_dir,
        "taxonomy_paths": (taxonomy_path,),
    }


def _build(
    fixture: dict[str, object],
    *,
    report_date: str,
    history_dir: Path,
) -> pd.DataFrame:
    section, _records = builder.build_operation_section(
        monthly_revenue_path=fixture["monthly_path"],
        stock_price_history_dir=fixture["price_dir"],
        taxonomy_paths=fixture["taxonomy_paths"],
        prior_history_dir=history_dir,
        report_date=report_date,
        generated_at="2026-08-30 12:00:00 Asia/Taipei",
    )
    return section


def _write(
    section: pd.DataFrame, destination: Path
) -> dict[str, str]:
    return builder.write_artifacts(
        section,
        output_csv=destination / "latest" / "operation.csv",
        output_md=destination / "latest" / "operation.md",
        docs_latest_dir=destination / "docs",
        history_dir=destination / "history",
    )


def test_pre_effective_weekend_emits_full_model_owned_empty_state(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture,
        report_date="20260828",
        history_dir=destination / "history",
    )

    assert len(section) == 12
    assert set(section["row_type"]) == {"empty_state"}
    assert set(section["formal_signal_effective_from"]) == {"20260831"}
    assert set(section["row_metric_status"]) == {
        "not_applicable_empty_state"
    }
    assert set(section["sample_size"]) == {"53"}
    assert set(section["entry_basis_zh"]) == {
        "D+1 收盤高於訊號日收盤確認；D+2 開盤進場。"
    }
    assert set(section["stop_loss_rule_id"]) == {
        "none_no_stop_reference"
    }
    assert set(section["stop_loss_price"]) == {""}
    assert set(section["planned_holding_days"]) == {"30"}
    assert set(section["row_action_status"]) == {"empty_state"}
    assert set(section["approval_status"]) == {
        "provisional_backtest_supported_oos_unconfirmed"
    }
    outputs = _write(section, destination)

    result = validator.validate_artifact(
        Path(outputs["output_csv"]),
        source_module=ROOT
        / "scripts"
        / "build_daily_revenue_unreacted_range_operation_section.py",
        history_snapshot=Path(outputs["history_csv"]),
    )
    assert result == {
        "row_count": 12,
        "data_row_count": 0,
        "empty_row_count": 12,
        "operation_asof_date": "20260828",
    }
    assert all(
        "research" not in value.lower()
        for value in section["source_artifacts"]
    )


def test_append_only_history_tolerates_bom_and_crlf_transport_drift(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture,
        report_date="20260828",
        history_dir=destination / "history",
    )
    outputs = _write(section, destination)
    history_path = Path(outputs["history_csv"])
    canonical = history_path.read_bytes()
    transport_variant = b"\xef\xbb\xbf" + canonical.replace(b"\n", b"\r\n")
    history_path.write_bytes(transport_variant)

    result = validator.validate_artifact(
        Path(outputs["output_csv"]),
        source_module=ROOT
        / "scripts"
        / "build_daily_revenue_unreacted_range_operation_section.py",
        history_snapshot=history_path,
    )
    repeated = _write(section, destination)

    assert result["row_count"] == 12
    assert repeated["history_csv"] == str(history_path)
    assert history_path.read_bytes() == transport_variant


def test_append_only_history_rejects_semantic_filename_drift(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture,
        report_date="20260828",
        history_dir=destination / "history",
    )
    outputs = _write(section, destination)
    history_path = Path(outputs["history_csv"])
    drifted = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    drifted.at[0, "adapter_note_zh"] += "; semantic drift"
    drifted.at[0, "row_canonical_sha256"] = builder._history_row_hash(
        drifted.loc[0].to_dict()
    )
    drifted.to_csv(history_path, index=False, lineterminator="\n")

    with pytest.raises(
        validator.ValidationError,
        match="semantic content hash mismatch",
    ):
        validator.validate_artifact(
            Path(outputs["output_csv"]),
            source_module=ROOT
            / "scripts"
            / "build_daily_revenue_unreacted_range_operation_section.py",
            history_snapshot=history_path,
        )


def test_append_only_history_rejects_semantic_collision(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture,
        report_date="20260828",
        history_dir=destination / "history",
    )
    outputs = _write(section, destination)
    history_path = Path(outputs["history_csv"])
    drifted = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    drifted.at[0, "adapter_note_zh"] += "; semantic collision"
    drifted.at[0, "row_canonical_sha256"] = builder._history_row_hash(
        drifted.loc[0].to_dict()
    )
    drifted.to_csv(history_path, index=False, lineterminator="\n")

    with pytest.raises(
        builder.RevenueOperationAdapterError,
        match="append-only history collision",
    ):
        _write(section, destination)


def test_d0_d1_d2_lifecycle_requires_append_only_confirmed_proof(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    dates = fixture["dates"]
    destination = tmp_path / "artifacts"
    history_dir = destination / "history"

    d0 = _build(
        fixture, report_date=dates[130], history_dir=history_dir
    )
    pending = d0[
        (d0["row_type"] == "data")
        & (d0["pdf_section"] == "pending_confirmation")
    ]
    assert len(pending) == 1
    assert pending.iloc[0]["signal_date"] == "20260831"
    assert set(pending["row_action_status"]) == {"pending_confirmation"}

    d1 = _build(
        fixture, report_date=dates[131], history_dir=history_dir
    )
    confirmed = d1[
        (d1["row_type"] == "data")
        & (d1["pdf_section"] == "confirmed_operation")
    ]
    assert len(confirmed) == 2
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["row_action_status"]) == {
        "confirmed_buy_candidate"
    }
    assert set(confirmed["entry_date"]) == {""}
    d1_outputs = _write(d1, destination)
    published_payload = Path(d1_outputs["output_csv"]).read_bytes()
    published_snapshot = history_dir / (
        "daily_revenue_unreacted_range_operation_section_"
        f"{dates[131]}_r1_"
        f"{hashlib.sha256(published_payload).hexdigest()[:12]}.csv"
    )
    published_snapshot.write_bytes(published_payload)

    with pytest.raises(
        builder.RevenueOperationAdapterError,
        match="lacks a prior formal buy-ranked confirmed history row",
    ):
        _build(
            fixture,
            report_date=dates[132],
            history_dir=tmp_path / "no-history",
        )

    d2 = _build(
        fixture, report_date=dates[132], history_dir=history_dir
    )
    active = d2[
        (d2["row_type"] == "data")
        & (d2["pdf_section"] == "active_operation")
    ]
    assert len(active) == 2
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["row_action_status"]) == {"active_operation"}
    assert set(active["entry_date"]) == {dates[132]}
    assert set(active["entry_price"]) == {"84.5"}
    assert set(active["operation_age_days"]) == {"1"}
    assert set(active["rank_reason_zh"]) == {
        "固定 source_mid_falling v2 規則命中；provisional gross historical 僅揭露、不作排序。"
    }
    assert set(active["confirmed_history_artifact"]) == {
        Path(d1_outputs["history_csv"]).resolve().as_posix()
    }
    assert all(active["confirmed_history_row_sha256"].str.fullmatch(r"[0-9a-f]{64}"))
    d2_outputs = _write(d2, destination)
    result = validator.validate_artifact(
        Path(d2_outputs["output_csv"]),
        history_snapshot=Path(d2_outputs["history_csv"]),
    )
    assert result["data_row_count"] == 2


def test_d30_close_removes_position_from_current_sections(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    dates = fixture["dates"]
    destination = tmp_path / "artifacts"
    history_dir = destination / "history"
    d1 = _build(
        fixture, report_date=dates[131], history_dir=history_dir
    )
    _write(d1, destination)

    exited = _build(
        fixture, report_date=dates[161], history_dir=history_dir
    )
    assert len(exited) == 12
    assert set(exited["row_type"]) == {"empty_state"}


def test_objective_input_guards_reject_latest_and_financial_statements(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    forbidden = tmp_path / "output" / "latest" / "monthly.csv"
    forbidden.parent.mkdir(parents=True)
    shutil.copyfile(fixture["monthly_path"], forbidden)
    with pytest.raises(
        builder.RevenueOperationAdapterError,
        match="must not consume latest/research artifacts",
    ):
        builder.load_monthly_revenue_history(forbidden)

    monthly = pd.read_csv(fixture["monthly_path"], dtype=str)
    monthly["eps"] = "1.0"
    monthly.to_csv(fixture["monthly_path"], index=False, lineterminator="\n")
    with pytest.raises(
        builder.RevenueOperationAdapterError,
        match="forbids financial-statement fields",
    ):
        builder.load_monthly_revenue_history(fixture["monthly_path"])


def test_validator_rejects_byte_tamper_and_baseline_row_metric_misuse(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture,
        report_date="20260828",
        history_dir=destination / "history",
    )
    outputs = _write(section, destination)
    artifact = Path(outputs["output_csv"])
    tampered = pd.read_csv(artifact, dtype=str, keep_default_na=False)
    tampered.at[0, "sample_size"] = "54"
    tampered.to_csv(artifact, index=False, lineterminator="\n")
    with pytest.raises(validator.ValidationError, match="fixed field drift"):
        validator.validate_artifact(artifact)

    d0 = _build(
        fixture,
        report_date=fixture["dates"][130],
        history_dir=destination / "history",
    )
    data_index = d0.index[d0["row_type"].eq("data")][0]
    d0.at[data_index, "row_metric_status"] = "ready"
    d0.at[data_index, "row_metric_scope"] = "whole_model_baseline"
    d0.at[data_index, "row_metric_sample_size"] = "53"
    d0.at[data_index, "row_canonical_sha256"] = builder._history_row_hash(
        d0.loc[data_index].to_dict()
    )
    misuse = destination / "misuse.csv"
    d0.to_csv(misuse, index=False, lineterminator="\n")
    with pytest.raises(
        validator.ValidationError,
        match="improperly exposes baseline as row-level metric",
    ):
        validator.validate_artifact(misuse)


@pytest.mark.parametrize(
    ("stock_id", "last_date", "resume_date", "ratio", "raw_close"),
    [
        ("3593", "20251210", "20251222", 0.6, 8.10),
        ("2380", "20260616", "20260629", 0.27658171, 6.60),
    ],
)
def test_formal_price_basis_adjusts_exact_authorized_action_asof_without_raw_mutation(
    tmp_path: Path, stock_id: str, last_date: str, resume_date: str,
    ratio: float, raw_close: float,
) -> None:
    price_path = tmp_path / f"{stock_id}.csv"
    raw = pd.DataFrame({
        "date": [last_date, resume_date],
        "open": [raw_close, raw_close / ratio],
        "high": [raw_close * 1.01, raw_close / ratio * 1.01],
        "low": [raw_close * 0.99, raw_close / ratio * 0.99],
        "close": [raw_close, raw_close / ratio],
    })
    raw.to_csv(price_path, index=False, lineterminator="\n")
    original = price_path.read_bytes()

    before = builder.load_price_history(price_path, asof_date=last_date)
    assert before["date"].tolist() == [last_date]
    assert before.iloc[0]["analysis_close"] == pytest.approx(raw_close)
    adjusted = builder.load_price_history(price_path, asof_date=resume_date)
    independent = validator._independent_adjusted_prices(
        price_path, stock_id=stock_id, asof_date=resume_date,
        events=validator._read_formal_price_basis(builder.FORMAL_PRICE_BASIS_PATH),
    )
    for column in ("open", "high", "low", "close"):
        expected = [float(raw.at[0, column]) / ratio, float(raw.at[1, column])]
        assert adjusted[f"analysis_{column}"].tolist() == pytest.approx(expected)
        assert [row[column] for row in independent] == pytest.approx(expected)
    # A second load starts from raw units, not the already adjusted frame.
    pd.testing.assert_frame_equal(adjusted, builder.load_price_history(price_path))
    assert price_path.read_bytes() == original


def test_formal_price_basis_replays_source_anchor_in_approved_adjusted_units(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    prices = pd.read_csv(fixture["price_dir"] / "1234.csv")
    # Synthetic 3593 history straddles the authorized 20251222 event, without
    # inventing trading sessions inside the documented suspension window.
    prices["date"] = (
        pd.bdate_range(end="2025-12-10", periods=115).strftime("%Y%m%d").tolist()
        + pd.bdate_range(start="2025-12-22", periods=55).strftime("%Y%m%d").tolist()
    )
    columns = ["open", "high", "low", "close"]
    raw = prices.copy()
    raw.loc[:114, columns] *= 0.6
    repaired_path = fixture["price_dir"] / "3593.csv"
    unregistered_path = fixture["price_dir"] / "9999.csv"
    raw.to_csv(repaired_path, index=False, lineterminator="\n")
    raw.to_csv(unregistered_path, index=False, lineterminator="\n")
    adjusted = builder.load_price_history(repaired_path)
    unadjusted = builder.load_price_history(unregistered_path)
    repaired_features = builder._source_anchor_features(adjusted, 125)
    raw_features = builder._source_anchor_features(unadjusted, 125)
    assert builder._selected_source_mid_falling(repaired_features)
    assert not builder._selected_source_mid_falling(raw_features)
    for column in columns:
        assert adjusted[f"analysis_{column}"].tolist() == pytest.approx(prices[column].tolist())
        assert unadjusted[f"analysis_{column}"].tolist() == pytest.approx(raw[column].tolist())
    assert repaired_features["shape_return20_pct"] < -5
    assert raw_features["shape_return20_pct"] > 0


def test_formal_price_basis_pin_rejects_modified_config_in_both_implementations(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    config_path = tmp_path / builder.FORMAL_PRICE_BASIS_PATH.name
    text = builder.FORMAL_PRICE_BASIS_PATH.read_text(encoding="utf-8-sig")
    config_path.write_text(text.replace(",0.6,", ",0.7,"), encoding="utf-8")
    with pytest.raises(builder.RevenueOperationAdapterError, match="SHA-256 mismatch"):
        builder.load_price_history(
            fixture["price_dir"] / "1234.csv", price_basis_path=config_path,
        )
    with pytest.raises(validator.ValidationError, match="canonical hash drift"):
        validator._read_formal_price_basis(config_path)


@pytest.mark.parametrize("field", [
    "signal_close", "source_position_120d_pct", "source_shape_return20_pct",
    "source_shape_ema23_slope5_pct",
])
def test_independent_validator_rejects_wrong_price_units_with_valid_row_hash(
    tmp_path: Path, field: str,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    section = _build(
        fixture, report_date=fixture["dates"][130],
        history_dir=tmp_path / "history",
    )
    data_index = section.index[section["row_type"].eq("data")][0]
    section.at[data_index, field] = str(float(section.at[data_index, field]) * 0.6)
    section.at[data_index, "row_canonical_sha256"] = builder._history_row_hash(
        section.loc[data_index].to_dict()
    )
    artifact = tmp_path / "bad-price-units.csv"
    section.to_csv(artifact, index=False, lineterminator="\n")
    with pytest.raises(validator.ValidationError, match=f"adjusted price basis mismatch: {field}"):
        validator.validate_artifact(artifact)


def test_price_basis_marker_cannot_be_removed_from_current_artifact(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    section = _build(
        fixture, report_date="20260828", history_dir=tmp_path / "history",
    )
    for index in section.index:
        section.at[index, "source_artifacts"] = ";".join(
            path for path in section.at[index, "source_artifacts"].split(";")
            if Path(path).name != validator.FORMAL_PRICE_BASIS_FILENAME
        )
        section.at[index, "row_canonical_sha256"] = builder._history_row_hash(
            section.loc[index].to_dict()
        )
    artifact = tmp_path / "legacy.csv"
    section.to_csv(artifact, index=False, lineterminator="\n")
    assert validator.validate_artifact(artifact)["data_row_count"] == 0
    for index in section.index:
        section.at[index, "operation_asof_date"] = "20260925"
        section.at[index, "row_canonical_sha256"] = builder._history_row_hash(
            section.loc[index].to_dict()
        )
    section.to_csv(artifact, index=False, lineterminator="\n")
    with pytest.raises(validator.ValidationError, match="missing required formal price basis"):
        validator.validate_artifact(artifact)


def test_validator_rejects_formal_price_binding_removed_from_source_module(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source.py"
    source.write_text(
        validator.DEFAULT_SOURCE_MODULE.read_text(encoding="utf-8").replace(
            validator.FORMAL_PRICE_BASIS_CANONICAL_SHA256, "0" * 64,
        ), encoding="utf-8",
    )
    with pytest.raises(validator.ValidationError, match="hash binding drift"):
        validator._validate_source_module(source)


def test_formal_price_basis_pin_accepts_bom_crlf_transport_without_changing_units(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    price_path = fixture["price_dir"] / "1234.csv"
    expected = builder.load_price_history(price_path)
    canonical = builder.FORMAL_PRICE_BASIS_PATH.read_text(encoding="utf-8-sig")
    transported = b"\xef\xbb\xbf" + canonical.replace("\n", "\r\n").encode("utf-8")
    config_path = tmp_path / builder.FORMAL_PRICE_BASIS_PATH.name
    config_path.write_bytes(transported)

    actual = builder.load_price_history(price_path, price_basis_path=config_path)
    pd.testing.assert_frame_equal(actual, expected)
    assert validator._read_formal_price_basis(config_path) == (
        validator._read_formal_price_basis(builder.FORMAL_PRICE_BASIS_PATH)
    )
    assert config_path.read_bytes() == transported


@pytest.mark.parametrize("field", ["confirmation_close", "entry_price"])
def test_independent_validator_rejects_wrong_lifecycle_price_with_valid_row_hash(
    tmp_path: Path, field: str,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    destination = tmp_path / "artifacts"
    section = _build(
        fixture, report_date=fixture["dates"][131],
        history_dir=destination / "history",
    )
    if field == "entry_price":
        _write(section, destination)
        section = _build(
            fixture, report_date=fixture["dates"][132],
            history_dir=destination / "history",
        )
    data_index = section.index[section["row_type"].eq("data")][0]
    section.at[data_index, field] = str(float(section.at[data_index, field]) * 0.6)
    section.at[data_index, "row_canonical_sha256"] = builder._history_row_hash(
        section.loc[data_index].to_dict()
    )
    artifact = tmp_path / "bad-lifecycle-price.csv"
    section.to_csv(artifact, index=False, lineterminator="\n")
    with pytest.raises(validator.ValidationError, match=f"adjusted price basis mismatch: {field}"):
        validator.validate_artifact(artifact)


def test_independent_validator_rejects_raw_source_hash_drift(
    tmp_path: Path,
) -> None:
    fixture = _objective_fixture(tmp_path / "fixture")
    section = _build(
        fixture, report_date=fixture["dates"][130], history_dir=tmp_path / "history",
    )
    artifact = tmp_path / "original-row-hashes.csv"
    section.to_csv(artifact, index=False, lineterminator="\n")
    price_path = fixture["price_dir"] / "1234.csv"
    prices = pd.read_csv(price_path)
    prices.at[0, "close"] *= 0.6
    prices.to_csv(price_path, index=False, lineterminator="\n")
    with pytest.raises(validator.ValidationError, match="raw price source hash drift"):
        validator.validate_artifact(artifact)
