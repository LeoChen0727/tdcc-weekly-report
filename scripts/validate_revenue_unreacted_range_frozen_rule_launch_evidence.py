from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
import hashlib
import json
from pathlib import Path
import re
from statistics import median
from typing import Iterable, Mapping

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
EVIDENCE_ID = "revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence"
EVIDENCE_VERSION = "revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830"
AUTHORIZATION_REFERENCE = "user_authorized_4A_4C_20260830"
RULE_SPEC_ID = "revenue_unreacted_range_source_mid_falling_d30_v1"
RULE_CANONICAL_SHA256 = "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
SOURCE_ARTIFACT_VERSION = "low_mid_falling_candidate_v3_20260829"
SOURCE_ARTIFACT_CANONICAL_SHA256 = "24d9900c956273ba72c5f9f2d3e2b77be3bea201c4f2996b9e4ea782d67e2b3a"
SOURCE_ROW_SET_SHA256 = "f91dd55cab602224011fc68b65dcb4e7dfb59b7720fb1cce0941941234c78c93"
SOURCE_CANONICAL_LF_SHA256 = "7dc4f1f89a16dd77d39af175de1dfd3340059a863a670c77e0276d8ec91582d7"
SOURCE_RELATIVE_PATH = Path(
    "output/history/research/"
    "revenue_unreacted_range_low_mid_falling_candidate_audit_detail_v3_20260829.csv"
)
INDEX_RELATIVE_PATH = Path("data/market_index_history.csv")
ANOMALY_REGISTRY_RELATIVE_PATH = Path(
    "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv"
)
ANOMALY_REGISTRY_CANONICAL_LF_SHA256 = (
    "d56fb059cb008b504cb6f64464277e5252566059512ba723668e3cd5f824d489"
)
ANOMALY_EVIDENCE_ROOT = "docs/evidence/revenue_unreacted_range/"
EVIDENCE_DIRECTORY = Path("config/approved_operation_evidence")
DETAIL_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_VERSION}_detail.csv"
MATRIX_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_VERSION}_matrix.csv"
MANIFEST_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_VERSION}_manifest.csv"

EXPECTED_OPERATION_COUNT = 53
EXPECTED_BUCKET_SIZES = (18, 18, 17)
LIFECYCLE_POLICY_ID = "rearm_after_realized_exit_next_trade_day"
CONFIRMATION_VARIANT_ID = "delayed_next_close_continuation_bonus"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
SAMPLE_SELECTION_POLICY = "fixed_preselected_no_reselection"
FORWARD_HOLDOUT_USE_POLICY = "post_launch_monitoring_non_hard_no_tuning"
ANOMALY_POLICY = "primary_retains_verified_real_extremes_and_repaired_source_rerun"
ANOMALY_DISPOSITION_STATUS = "verified_8_real_extreme_1_data_error_repaired_effective_blockers_0"
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
COMMISSION_RATE_EACH_SIDE = Decimal("0.001425")
SELL_TRANSACTION_TAX_RATE = Decimal("0.003")
COST_SCENARIOS = (
    ("declared_cost_slippage_0bp_each_side", Decimal("0")),
    ("declared_cost_slippage_10bp_each_side", Decimal("0.001")),
    ("declared_cost_slippage_25bp_each_side", Decimal("0.0025")),
)
FOUR_PLACES = Decimal("0.0001")
EVIDENCE_REFERENCE_RE = re.compile(
    r"^evidence_id=(?P<evidence_id>[a-z0-9][a-z0-9_.-]*);"
    r"path=(?P<path>docs/evidence/revenue_unreacted_range/[^;\r\n]+\.json);"
    r"canonical_sha256=(?P<canonical_sha256>[0-9a-f]{64})$"
)
ANOMALY_ROOT_CHECK_COLUMNS = (
    "identity_non_overlap_status",
    "formal_operation_replay_status",
    "pit_calendar_continuity_status",
    "raw_source_lineage_status",
    "units_formula_adjustment_status",
    "authoritative_event_history_status",
    "independent_source_corroboration_status",
    "reproducible_evidence_reference_status",
)


DETAIL_COLUMNS = (
    "evidence_id",
    "evidence_version",
    "model_id",
    "rule_spec_id",
    "rule_canonical_sha256",
    "source_artifact_path",
    "source_artifact_version",
    "source_operation_key",
    "source_candidate_detail_row_sha256",
    "chronological_order",
    "chronological_bucket_id",
    "stock_id",
    "stock_name",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "gross_realized_return_pct",
    "source_anomaly_candidate_flag",
    "operation_return_review_candidate_flag",
    "anomaly_policy",
    "market_source_value",
    "benchmark_index_code",
    "benchmark_entry_date",
    "benchmark_entry_open",
    "benchmark_exit_date",
    "benchmark_exit_close",
    "benchmark_return_pct",
    "excess_return_pct",
    "benchmark_exact_date_coverage",
    "entry_index_close",
    "entry_index_ma20",
    "entry_index_ma60",
    "entry_index_return_20d_pct",
    "entry_index_above_ma20",
    "entry_index_above_ma60",
    "entry_market_regime",
    "commission_rate_each_side",
    "sell_transaction_tax_rate",
    "net_return_slippage_0bp_each_side_pct",
    "net_return_slippage_10bp_each_side_pct",
    "net_return_slippage_25bp_each_side_pct",
    "financial_statement_scope",
    "forward_holdout_use_policy",
    "sample_selection_policy",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
)

MATRIX_COLUMNS = (
    "evidence_id",
    "evidence_version",
    "analysis_family",
    "group_id",
    "return_basis",
    "sample_count",
    "positive_count",
    "positive_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "min_return_pct",
    "max_return_pct",
    "comparator_sample_count",
    "comparator_avg_return_pct",
    "comparator_median_return_pct",
    "avg_difference_pct_points",
    "median_difference_pct_points",
    "group_count",
    "coverage_count",
    "coverage_total",
    "status",
    "notes",
)


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _canonical_lf_bytes(path: Path) -> bytes:
    """Normalize only transport EOL; business rows remain independently replayed."""
    try:
        payload = path.read_bytes()
        payload.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"evidence text is not UTF-8: {path}") from exc
    canonical = payload.replace(b"\r\n", b"\n")
    if b"\r" in canonical:
        raise RuntimeError(f"evidence text contains unsupported lone CR: {path}")
    return canonical


def _payload_bundle_sha256(payloads: dict[Path, bytes]) -> str:
    members = "".join(
        f"{path.as_posix()}|{len(payload)}|{_sha256_bytes(payload)}\n"
        for path, payload in sorted(payloads.items(), key=lambda item: item[0].as_posix())
    )
    return _sha256_bytes(members.encode("utf-8"))


def _is_transport_provenance_name(name: object) -> bool:
    normalized = str(name).strip().lower()
    return (
        normalized == "generated_at"
        or normalized.startswith("raw_")
        or "blob_sha256" in normalized
        or "byte_sha256" in normalized
        or "bytes_sha256" in normalized
        or "crlf" in normalized
        or "line_ending" in normalized
    )


def _without_transport_provenance(value: object) -> object:
    if isinstance(value, Mapping):
        return {
            str(key): _without_transport_provenance(item)
            for key, item in value.items()
            if not _is_transport_provenance_name(key)
            or str(key) == "raw_source_lineage"
        }
    if isinstance(value, list):
        return [_without_transport_provenance(item) for item in value]
    return value


def _anomaly_evidence_semantic_sha256(document: Mapping[str, object]) -> str:
    return _records_sha256(
        {
            "schema_version": document.get("schema_version"),
            "evidence_id": document.get("evidence_id"),
            "semantic_payload": _without_transport_provenance(
                document.get("semantic_payload")
            ),
        }
    )


def _bool(value: object, label: str) -> bool:
    text = str(value).strip().lower()
    if text in {"true", "1"}:
        return True
    if text in {"false", "0"}:
        return False
    raise RuntimeError(f"{label} is not an exact boolean: {value!r}")


def _decimal(value: object, label: str) -> Decimal:
    try:
        number = Decimal(str(value).strip())
    except (InvalidOperation, ValueError) as exc:
        raise RuntimeError(f"{label} is not a decimal: {value!r}") from exc
    if not number.is_finite():
        raise RuntimeError(f"{label} is not finite: {value!r}")
    return number


def _fmt(value: Decimal | int) -> str:
    if isinstance(value, int):
        return str(value)
    return format(value.quantize(FOUR_PLACES, rounding=ROUND_HALF_EVEN), "f")


def _records_sha256(records: object) -> str:
    return _sha256_bytes(
        json.dumps(
            records,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )


def _frame_semantic_sha256(frame: pd.DataFrame) -> str:
    rows = [
        ["" if pd.isna(value) else str(value) for value in row]
        for row in frame.itertuples(index=False, name=None)
    ]
    return _records_sha256({"columns": list(frame.columns), "rows": rows})


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _pct(exit_value: Decimal, entry_value: Decimal) -> Decimal:
    if entry_value <= 0:
        raise RuntimeError("independent replay entry value must be positive")
    return (exit_value / entry_value - Decimal("1")) * Decimal("100")


def _net(entry: Decimal, exit_value: Decimal, slip: Decimal) -> Decimal:
    buy = entry * (Decimal("1") + slip)
    sell = exit_value * (Decimal("1") - slip)
    debit = buy * (Decimal("1") + COMMISSION_RATE_EACH_SIDE)
    credit = sell * (
        Decimal("1") - COMMISSION_RATE_EACH_SIDE - SELL_TRANSACTION_TAX_RATE
    )
    return _pct(credit, debit)


def _market(value: object) -> str:
    text = str(value).strip().upper()
    if "TPEX" in text or "OTC" in text:
        return "TPEX"
    if "TWSE" in text or "LISTED" in text:
        return "TWSE"
    raise RuntimeError(f"independent market mapping rejects {value!r}")


def _regime(index_row: pd.Series) -> str:
    close = _decimal(index_row["close"], "index close")
    ma20 = _decimal(index_row["ma20"], "index ma20")
    ma60 = _decimal(index_row["ma60"], "index ma60")
    return20 = _decimal(index_row["return_20d"], "index return20")
    above20 = _bool(index_row["above_ma20"], "index above ma20")
    above60 = _bool(index_row["above_ma60"], "index above ma60")
    if close < ma60 and return20 < 0:
        return "high_risk"
    if (not above20) or return20 <= Decimal("-3"):
        return "correction"
    if above20 and above60 and return20 >= Decimal("5"):
        return "strong_bull"
    if above20 and above60:
        return "mild_bull"
    return "range_bound"


def _metric(values: Iterable[Decimal]) -> dict[str, str]:
    ordered = sorted(values)
    if not ordered:
        raise RuntimeError("independent metric input is empty")
    count = len(ordered)
    positive = sum(value > 0 for value in ordered)
    return {
        "sample_count": str(count),
        "positive_count": str(positive),
        "positive_rate_pct": _fmt(Decimal(positive) * 100 / Decimal(count)),
        "avg_return_pct": _fmt(sum(ordered, Decimal("0")) / Decimal(count)),
        "median_return_pct": _fmt(Decimal(str(median(ordered)))),
        "min_return_pct": _fmt(ordered[0]),
        "max_return_pct": _fmt(ordered[-1]),
    }


def _read_frozen_source(source_root: Path) -> pd.DataFrame:
    path = source_root / SOURCE_RELATIVE_PATH
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"frozen source is missing or unsafe: {path}")
    observed_blob = _sha256_bytes(_canonical_lf_bytes(path))
    if observed_blob != SOURCE_CANONICAL_LF_SHA256:
        raise RuntimeError(
            "frozen source canonical LF SHA drift: "
            f"{observed_blob}/{SOURCE_CANONICAL_LF_SHA256}"
        )
    source = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {
        "model_id",
        "artifact_version",
        "source_variant_id",
        "operation_key",
        "candidate_detail_row_sha256",
        "detail_artifact_canonical_sha256",
        "candidate_detail_row_set_sha256",
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "stock_id",
        "stock_name",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "entry_price",
        "exit_price",
        "realized_return_pct",
        "mid_falling_member",
        "low_falling_member",
        "primary_included",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
        "financial_statement_scope",
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise RuntimeError(f"frozen source missing columns: {missing}")
    exact = {
        "model_id": MODEL_ID,
        "artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "detail_artifact_canonical_sha256": SOURCE_ARTIFACT_CANONICAL_SHA256,
        "candidate_detail_row_set_sha256": SOURCE_ROW_SET_SHA256,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
    }
    for column, expected in exact.items():
        if set(source[column]) != {expected}:
            raise RuntimeError(f"frozen source {column} drift")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    ):
        if any(_bool(value, column) for value in source[column]):
            raise RuntimeError(f"frozen source unexpectedly grants {column}")
    return source


def _selected(source: pd.DataFrame) -> pd.DataFrame:
    selected = source.loc[
        source["lifecycle_policy_id"].eq(LIFECYCLE_POLICY_ID)
        & source["confirmation_variant_id"].eq(CONFIRMATION_VARIANT_ID)
        & source["mid_falling_member"].map(lambda value: _bool(value, "mid member"))
        & source["primary_included"].map(lambda value: _bool(value, "primary"))
    ].copy()
    selected = selected.sort_values(
        ["trigger_date", "operation_key"], kind="stable"
    ).reset_index(drop=True)
    if len(selected) != EXPECTED_OPERATION_COUNT:
        raise RuntimeError(f"selected operation count drift: {len(selected)}")
    if selected["operation_key"].duplicated().any():
        raise RuntimeError("selected operation keys are not unique")
    return selected


def _anomaly_bindings(source_root: Path, source: pd.DataFrame) -> list[dict[str, str]]:
    path = source_root / ANOMALY_REGISTRY_RELATIVE_PATH
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"anomaly registry missing or unsafe: {path}")
    observed_sha = _sha256_bytes(_canonical_lf_bytes(path))
    if observed_sha != ANOMALY_REGISTRY_CANONICAL_LF_SHA256:
        raise RuntimeError(
            "anomaly registry canonical LF SHA drift: "
            f"{observed_sha}/{ANOMALY_REGISTRY_CANONICAL_LF_SHA256}"
        )
    registry = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {
        "model_id",
        "operation_key",
        "candidate_detail_row_sha256",
        "final_disposition",
        "primary_handling",
        "promotion_gate_status",
        "repair_satisfaction_status",
        "effective_anomaly_gate_status",
        "evidence_reference",
        *ANOMALY_ROOT_CHECK_COLUMNS,
    }
    missing = sorted(required - set(registry.columns))
    if missing:
        raise RuntimeError(f"anomaly registry missing columns: {missing}")
    if len(registry) != 9 or registry["operation_key"].duplicated().any():
        raise RuntimeError("anomaly registry must contain nine unique operations")
    if set(registry["model_id"]) != {MODEL_ID}:
        raise RuntimeError("anomaly registry model identity drift")
    if any(registry[column].ne("pass").any() for column in ANOMALY_ROOT_CHECK_COLUMNS):
        raise RuntimeError("anomaly registry has an incomplete lowest-evidence check")
    if set(registry["effective_anomaly_gate_status"]) != {"satisfied"}:
        raise RuntimeError("anomaly registry effective gate is not satisfied")
    if set(registry["promotion_gate_status"]) != {
        "eligible_only_after_all_other_model_gates"
    }:
        raise RuntimeError("anomaly registry promotion gate semantics drift")
    if registry["final_disposition"].value_counts().to_dict() != {
        "verified_real_extreme": 8,
        "verified_data_error": 1,
    }:
        raise RuntimeError("anomaly disposition count drift")

    selected = _selected(source)
    selected_by_key = selected.set_index("operation_key", drop=False)
    if not set(registry["operation_key"]).issubset(set(selected_by_key.index)):
        raise RuntimeError("anomaly operation is outside the frozen selected sample")
    current_candidates = set(
        selected.loc[
            selected["source_anomaly_candidate_flag"].map(
                lambda value: _bool(value, "source anomaly flag")
            )
            | selected["operation_return_review_candidate_flag"].map(
                lambda value: _bool(value, "return review flag")
            ),
            "operation_key",
        ]
    )
    real_extremes = set(
        registry.loc[
            registry["final_disposition"].eq("verified_real_extreme"),
            "operation_key",
        ]
    )
    if current_candidates != real_extremes:
        raise RuntimeError("source anomaly flags do not match verified real extremes")

    bindings: list[dict[str, str]] = []
    for row in registry.sort_values("operation_key", kind="stable").to_dict("records"):
        source_row = selected_by_key.loc[str(row["operation_key"])]
        if str(source_row["candidate_detail_row_sha256"]) != str(
            row["candidate_detail_row_sha256"]
        ):
            raise RuntimeError("anomaly candidate row SHA drift")
        match = EVIDENCE_REFERENCE_RE.fullmatch(str(row["evidence_reference"]))
        if match is None:
            raise RuntimeError("anomaly evidence reference is malformed")
        relative_text = match.group("path")
        if not relative_text.startswith(ANOMALY_EVIDENCE_ROOT) or ".." in Path(
            relative_text
        ).parts:
            raise RuntimeError("anomaly evidence path escapes the model-owned root")
        evidence_path = source_root / Path(relative_text)
        if not evidence_path.is_file() or evidence_path.is_symlink():
            raise RuntimeError(f"anomaly evidence missing or unsafe: {evidence_path}")
        document = json.loads(evidence_path.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise RuntimeError("anomaly evidence root must be an object")
        if document.get("evidence_id") != match.group("evidence_id"):
            raise RuntimeError("anomaly evidence identity drift")
        observed_evidence_sha = _anomaly_evidence_semantic_sha256(document)
        if observed_evidence_sha != match.group("canonical_sha256"):
            raise RuntimeError("anomaly evidence canonical semantic SHA drift")
        bindings.append(
            {
                "operation_key": str(row["operation_key"]),
                "candidate_detail_row_sha256": str(
                    row["candidate_detail_row_sha256"]
                ),
                "final_disposition": str(row["final_disposition"]),
                "evidence_id": match.group("evidence_id"),
                "evidence_path": relative_text,
                "evidence_canonical_sha256": observed_evidence_sha,
            }
        )
    return bindings


def _bucket(position: int) -> str:
    if position < EXPECTED_BUCKET_SIZES[0]:
        return "chronological_third_1_early_18"
    if position < EXPECTED_BUCKET_SIZES[0] + EXPECTED_BUCKET_SIZES[1]:
        return "chronological_third_2_middle_18"
    return "chronological_third_3_late_17"


def _index_frame(source_root: Path) -> pd.DataFrame:
    frame = pd.read_csv(
        source_root / INDEX_RELATIVE_PATH,
        dtype=str,
        keep_default_na=False,
    )
    required = {
        "date",
        "index_code",
        "open",
        "close",
        "ma20",
        "ma60",
        "return_20d",
        "above_ma20",
        "above_ma60",
    }
    if missing := sorted(required - set(frame.columns)):
        raise RuntimeError(f"index source missing columns: {missing}")
    if frame.duplicated(["index_code", "date"]).any():
        raise RuntimeError("index source contains duplicate keys")
    return frame.set_index(["index_code", "date"], drop=False)


def _entry_market(
    source_root: Path,
    stock_id: str,
    entry_date: str,
    cache: dict[str, pd.DataFrame],
) -> str:
    if stock_id not in cache:
        frame = pd.read_csv(
            source_root / "data" / "stock_price_history" / f"{stock_id}.csv",
            dtype=str,
            keep_default_na=False,
        )
        if not {"date", "market"}.issubset(frame.columns):
            raise RuntimeError(f"stock {stock_id} price source lacks date/market")
        cache[stock_id] = frame
    matched = cache[stock_id].loc[cache[stock_id]["date"].eq(entry_date)]
    if len(matched) != 1:
        raise RuntimeError(
            f"stock {stock_id} exact entry market coverage drift: {entry_date}/{len(matched)}"
        )
    return str(matched.iloc[0]["market"]).strip()


def _replay_detail(
    source_root: Path,
    source: pd.DataFrame,
) -> tuple[pd.DataFrame, list[dict[str, str]], list[dict[str, str]]]:
    selected = _selected(source)
    index = _index_frame(source_root)
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, str]] = []
    benchmark_bindings: list[dict[str, str]] = []
    market_bindings: list[dict[str, str]] = []
    for offset, operation in enumerate(selected.to_dict("records")):
        stock_id = str(operation["stock_id"])
        entry_date = str(operation["entry_date"])
        exit_date = str(operation["exit_date"])
        market_source = _entry_market(source_root, stock_id, entry_date, price_cache)
        benchmark_code = _market(market_source)
        entry_key = (benchmark_code, entry_date)
        exit_key = (benchmark_code, exit_date)
        if entry_key not in index.index or exit_key not in index.index:
            raise RuntimeError(
                f"exact index coverage missing: {operation['operation_key']}/{entry_key}/{exit_key}"
            )
        entry_index = index.loc[entry_key]
        exit_index = index.loc[exit_key]
        if isinstance(entry_index, pd.DataFrame) or isinstance(exit_index, pd.DataFrame):
            raise RuntimeError("index key resolves to multiple rows")
        entry_price = _decimal(operation["entry_price"], "entry price")
        exit_price = _decimal(operation["exit_price"], "exit price")
        gross = _decimal(operation["realized_return_pct"], "source gross")
        if abs(gross - _pct(exit_price, entry_price)) > Decimal("0.0001"):
            raise RuntimeError(f"source gross replay drift: {operation['operation_key']}")
        benchmark = _pct(
            _decimal(exit_index["close"], "index exit close"),
            _decimal(entry_index["open"], "index entry open"),
        )
        nets = {
            scenario: _net(entry_price, exit_price, slip)
            for scenario, slip in COST_SCENARIOS
        }
        benchmark_bindings.append(
            {
                "source_operation_key": str(operation["operation_key"]),
                "benchmark_index_code": benchmark_code,
                "entry_date": entry_date,
                "entry_open": str(entry_index["open"]),
                "entry_close": str(entry_index["close"]),
                "entry_ma20": str(entry_index["ma20"]),
                "entry_ma60": str(entry_index["ma60"]),
                "entry_return_20d": str(entry_index["return_20d"]),
                "entry_above_ma20": str(entry_index["above_ma20"]),
                "entry_above_ma60": str(entry_index["above_ma60"]),
                "exit_date": exit_date,
                "exit_close": str(exit_index["close"]),
            }
        )
        market_bindings.append(
            {
                "source_operation_key": str(operation["operation_key"]),
                "stock_id": stock_id,
                "entry_date": entry_date,
                "market_source_value": market_source,
                "benchmark_index_code": benchmark_code,
            }
        )
        rows.append(
            {
                "evidence_id": EVIDENCE_ID,
                "evidence_version": EVIDENCE_VERSION,
                "model_id": MODEL_ID,
                "rule_spec_id": RULE_SPEC_ID,
                "rule_canonical_sha256": RULE_CANONICAL_SHA256,
                "source_artifact_path": SOURCE_RELATIVE_PATH.as_posix(),
                "source_artifact_version": SOURCE_ARTIFACT_VERSION,
                "source_operation_key": str(operation["operation_key"]),
                "source_candidate_detail_row_sha256": str(
                    operation["candidate_detail_row_sha256"]
                ),
                "chronological_order": str(offset + 1),
                "chronological_bucket_id": _bucket(offset),
                "stock_id": stock_id,
                "stock_name": str(operation["stock_name"]),
                "trigger_date": str(operation["trigger_date"]),
                "confirmation_date": str(operation["confirmation_date"]),
                "entry_date": entry_date,
                "exit_date": exit_date,
                "entry_price": str(operation["entry_price"]),
                "exit_price": str(operation["exit_price"]),
                "gross_realized_return_pct": _fmt(gross),
                "source_anomaly_candidate_flag": str(
                    _bool(operation["source_anomaly_candidate_flag"], "source anomaly")
                ),
                "operation_return_review_candidate_flag": str(
                    _bool(
                        operation["operation_return_review_candidate_flag"],
                        "operation review candidate",
                    )
                ),
                "anomaly_policy": ANOMALY_POLICY,
                "market_source_value": market_source,
                "benchmark_index_code": benchmark_code,
                "benchmark_entry_date": entry_date,
                "benchmark_entry_open": str(entry_index["open"]),
                "benchmark_exit_date": exit_date,
                "benchmark_exit_close": str(exit_index["close"]),
                "benchmark_return_pct": _fmt(benchmark),
                "excess_return_pct": _fmt(gross - benchmark),
                "benchmark_exact_date_coverage": "True",
                "entry_index_close": str(entry_index["close"]),
                "entry_index_ma20": str(entry_index["ma20"]),
                "entry_index_ma60": str(entry_index["ma60"]),
                "entry_index_return_20d_pct": str(entry_index["return_20d"]),
                "entry_index_above_ma20": str(
                    _bool(entry_index["above_ma20"], "index above ma20")
                ),
                "entry_index_above_ma60": str(
                    _bool(entry_index["above_ma60"], "index above ma60")
                ),
                "entry_market_regime": _regime(entry_index),
                "commission_rate_each_side": str(COMMISSION_RATE_EACH_SIDE),
                "sell_transaction_tax_rate": str(SELL_TRANSACTION_TAX_RATE),
                "net_return_slippage_0bp_each_side_pct": _fmt(
                    nets["declared_cost_slippage_0bp_each_side"]
                ),
                "net_return_slippage_10bp_each_side_pct": _fmt(
                    nets["declared_cost_slippage_10bp_each_side"]
                ),
                "net_return_slippage_25bp_each_side_pct": _fmt(
                    nets["declared_cost_slippage_25bp_each_side"]
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "forward_holdout_use_policy": FORWARD_HOLDOUT_USE_POLICY,
                "sample_selection_policy": SAMPLE_SELECTION_POLICY,
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            }
        )
    return (
        pd.DataFrame(rows, columns=DETAIL_COLUMNS),
        benchmark_bindings,
        market_bindings,
    )


def _matrix_row(
    family: str,
    group: str,
    basis: str,
    values: list[Decimal],
    status: str,
    notes: str,
    *,
    comparator: list[Decimal] | None = None,
    group_count: str = "",
    coverage_count: str = "",
    coverage_total: str = "",
) -> dict[str, str]:
    metrics = _metric(values)
    row = {
        "evidence_id": EVIDENCE_ID,
        "evidence_version": EVIDENCE_VERSION,
        "analysis_family": family,
        "group_id": group,
        "return_basis": basis,
        **metrics,
        "comparator_sample_count": "",
        "comparator_avg_return_pct": "",
        "comparator_median_return_pct": "",
        "avg_difference_pct_points": "",
        "median_difference_pct_points": "",
        "group_count": group_count,
        "coverage_count": coverage_count,
        "coverage_total": coverage_total,
        "status": status,
        "notes": notes,
    }
    if comparator is not None:
        other = _metric(comparator)
        row["comparator_sample_count"] = other["sample_count"]
        row["comparator_avg_return_pct"] = other["avg_return_pct"]
        row["comparator_median_return_pct"] = other["median_return_pct"]
        row["avg_difference_pct_points"] = _fmt(
            _decimal(metrics["avg_return_pct"], "matrix avg")
            - _decimal(other["avg_return_pct"], "matrix comparator avg")
        )
        row["median_difference_pct_points"] = _fmt(
            _decimal(metrics["median_return_pct"], "matrix median")
            - _decimal(other["median_return_pct"], "matrix comparator median")
        )
    return row


def _expected_matrix(detail: pd.DataFrame, source: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []

    def vals(frame: pd.DataFrame, column: str) -> list[Decimal]:
        return [_decimal(value, f"matrix {column}") for value in frame[column]]

    rows.append(
        _matrix_row(
            "overall_gross",
            "all_53",
            "gross_d2_open_to_d30_close",
            vals(detail, "gross_realized_return_pct"),
            "historical_backtest_gross_positive",
            "primary retains every verified real extreme and repaired-source rerun row",
            coverage_count=str(len(detail)),
            coverage_total=str(EXPECTED_OPERATION_COUNT),
        )
    )
    for group, part in detail.groupby("chronological_bucket_id", sort=False):
        rows.append(
            _matrix_row(
                "chronological_gross",
                str(group),
                "gross_d2_open_to_d30_close",
                vals(part, "gross_realized_return_pct"),
                "gross_positive",
                "equal-count chronological thirds assigned without outcome values",
            )
        )
    rows.append(
        _matrix_row(
            "overall_market_benchmark",
            "all_53",
            "stock_gross_minus_same_market_same_dates_index_open_to_close",
            vals(detail, "excess_return_pct"),
            "weak_positive_overall",
            "exact-date TWSE or TPEX benchmark; no as-of or nearest-date fallback",
            coverage_count=str(len(detail)),
            coverage_total=str(EXPECTED_OPERATION_COUNT),
        )
    )
    for group, part in detail.groupby("chronological_bucket_id", sort=False):
        group_values = vals(part, "excess_return_pct")
        metrics = _metric(group_values)
        status = (
            "relative_edge_positive"
            if _decimal(metrics["avg_return_pct"], "bucket avg") > 0
            and _decimal(metrics["median_return_pct"], "bucket median") > 0
            else "relative_edge_negative"
        )
        rows.append(
            _matrix_row(
                "chronological_market_benchmark",
                str(group),
                "stock_gross_minus_same_market_same_dates_index_open_to_close",
                group_values,
                status,
                "relative edge is diagnostic and does not reselect the frozen sample",
            )
        )
    for regime, part in detail.groupby("entry_market_regime", sort=True):
        for basis, column in (
            ("gross_d2_open_to_d30_close", "gross_realized_return_pct"),
            (
                "stock_gross_minus_same_market_same_dates_index_open_to_close",
                "excess_return_pct",
            ),
        ):
            group_values = vals(part, column)
            metrics = _metric(group_values)
            status = (
                "gross_observed"
                if column == "gross_realized_return_pct"
                else (
                    "relative_edge_positive"
                    if _decimal(metrics["avg_return_pct"], "regime avg") > 0
                    and _decimal(metrics["median_return_pct"], "regime median") > 0
                    else "relative_edge_negative"
                )
            )
            rows.append(
                _matrix_row(
                    "entry_market_regime",
                    str(regime),
                    basis,
                    group_values,
                    status,
                    "entry-date point-in-time index regime classification",
                )
            )
    for market, part in detail.groupby("benchmark_index_code", sort=True):
        rows.append(
            _matrix_row(
                "market_coverage",
                str(market),
                "gross_d2_open_to_d30_close",
                vals(part, "gross_realized_return_pct"),
                "observed_market_coverage",
                "market comes from the stock price row on the exact entry date",
            )
        )
    for scenario, column in (
        (
            "declared_cost_slippage_0bp_each_side",
            "net_return_slippage_0bp_each_side_pct",
        ),
        (
            "declared_cost_slippage_10bp_each_side",
            "net_return_slippage_10bp_each_side_pct",
        ),
        (
            "declared_cost_slippage_25bp_each_side",
            "net_return_slippage_25bp_each_side_pct",
        ),
    ):
        rows.append(
            _matrix_row(
                "transaction_cost",
                scenario,
                "net_d2_open_to_d30_close_after_declared_costs",
                vals(detail, column),
                "net_positive_declared_grid",
                (
                    "commission 0.1425% each side is a conservative declared assumption; "
                    "sell tax 0.3%; minimum fee and position-size impact are not modeled"
                ),
            )
        )
    base = source.loc[
        source["lifecycle_policy_id"].eq(LIFECYCLE_POLICY_ID)
        & source["confirmation_variant_id"].eq(CONFIRMATION_VARIANT_ID)
        & source["primary_included"].map(lambda value: _bool(value, "control primary"))
    ].copy()
    differences: list[Decimal] = []
    treated_total = 0
    comparator_total = 0
    group_total = 0
    for key, part in base.groupby(["trigger_date", "entry_date", "exit_date"], sort=True):
        treated = part.loc[
            part["mid_falling_member"].map(lambda value: _bool(value, "control mid"))
        ]
        comparator = part.loc[
            part["low_falling_member"].map(lambda value: _bool(value, "control low"))
        ]
        if treated.empty or comparator.empty:
            continue
        treated_values = [
            _decimal(value, "treated return") for value in treated["realized_return_pct"]
        ]
        comparator_values = [
            _decimal(value, "comparator return")
            for value in comparator["realized_return_pct"]
        ]
        treated_stats = _metric(treated_values)
        comparator_stats = _metric(comparator_values)
        differences.append(
            _decimal(treated_stats["avg_return_pct"], "treated average")
            - _decimal(comparator_stats["avg_return_pct"], "comparator average")
        )
        treated_total += len(treated_values)
        comparator_total += len(comparator_values)
        group_total += 1
        rows.append(
            _matrix_row(
                "same_date_source_low_control_sensitivity",
                "|".join(str(value) for value in key),
                "gross_mid_vs_source_low_same_trigger_entry_exit_dates",
                treated_values,
                "sensitivity_sparse_not_independent",
                "challenger variant comparison; retained extremes; not a promotion hard gate",
                comparator=comparator_values,
            )
        )
    if not differences:
        raise RuntimeError("independent same-date sensitivity has no groups")
    difference_stats = _metric(differences)
    rows.append(
        {
            "evidence_id": EVIDENCE_ID,
            "evidence_version": EVIDENCE_VERSION,
            "analysis_family": "same_date_source_low_control_sensitivity_summary",
            "group_id": "equal_weight_date_group_difference",
            "return_basis": "treated_group_avg_minus_comparator_group_avg",
            "sample_count": str(treated_total),
            "positive_count": difference_stats["positive_count"],
            "positive_rate_pct": difference_stats["positive_rate_pct"],
            "avg_return_pct": "",
            "median_return_pct": "",
            "min_return_pct": "",
            "max_return_pct": "",
            "comparator_sample_count": str(comparator_total),
            "comparator_avg_return_pct": "",
            "comparator_median_return_pct": "",
            "avg_difference_pct_points": difference_stats["avg_return_pct"],
            "median_difference_pct_points": difference_stats["median_return_pct"],
            "group_count": str(group_total),
            "coverage_count": str(treated_total),
            "coverage_total": str(EXPECTED_OPERATION_COUNT),
            "status": "sensitivity_sparse_not_independent",
            "notes": "only exact shared trigger/entry/exit date groups; no nearest-date matching",
        }
    )
    return pd.DataFrame(rows, columns=MATRIX_COLUMNS)


def _expected_manifest(
    detail: pd.DataFrame,
    matrix: pd.DataFrame,
    benchmark_bindings: list[dict[str, str]],
    market_bindings: list[dict[str, str]],
    anomaly_bindings: list[dict[str, str]],
) -> pd.DataFrame:
    detail_bytes = _csv_bytes(detail)
    matrix_bytes = _csv_bytes(matrix)
    payloads = {
        DETAIL_RELATIVE_PATH: detail_bytes,
        MATRIX_RELATIVE_PATH: matrix_bytes,
    }
    gross = matrix.loc[matrix["analysis_family"].eq("overall_gross")].iloc[0]
    excess = matrix.loc[
        matrix["analysis_family"].eq("overall_market_benchmark")
    ].iloc[0]
    stress = matrix.loc[
        matrix["analysis_family"].eq("transaction_cost")
        & matrix["group_id"].eq("declared_cost_slippage_25bp_each_side")
    ].iloc[0]
    markets = detail["benchmark_index_code"].value_counts().to_dict()
    regimes = detail["entry_market_regime"].value_counts().to_dict()
    return pd.DataFrame(
        [
            {
                "evidence_id": EVIDENCE_ID,
                "evidence_version": EVIDENCE_VERSION,
                "authorization_reference": AUTHORIZATION_REFERENCE,
                "model_id": MODEL_ID,
                "rule_spec_id": RULE_SPEC_ID,
                "rule_canonical_sha256": RULE_CANONICAL_SHA256,
                "source_artifact_path": SOURCE_RELATIVE_PATH.as_posix(),
                "source_artifact_version": SOURCE_ARTIFACT_VERSION,
                "source_canonical_lf_sha256": SOURCE_CANONICAL_LF_SHA256,
                "source_artifact_canonical_sha256": SOURCE_ARTIFACT_CANONICAL_SHA256,
                "source_candidate_row_set_sha256": SOURCE_ROW_SET_SHA256,
                "detail_path": DETAIL_RELATIVE_PATH.as_posix(),
                "detail_canonical_lf_byte_count": str(len(detail_bytes)),
                "detail_canonical_lf_sha256": _sha256_bytes(detail_bytes),
                "detail_semantic_sha256": _frame_semantic_sha256(detail),
                "matrix_path": MATRIX_RELATIVE_PATH.as_posix(),
                "matrix_canonical_lf_byte_count": str(len(matrix_bytes)),
                "matrix_canonical_lf_sha256": _sha256_bytes(matrix_bytes),
                "matrix_semantic_sha256": _frame_semantic_sha256(matrix),
                "evidence_payload_bundle_sha256": _payload_bundle_sha256(payloads),
                "benchmark_source_path": INDEX_RELATIVE_PATH.as_posix(),
                "benchmark_selected_row_set_sha256": _records_sha256(
                    benchmark_bindings
                ),
                "entry_market_mapping_row_set_sha256": _records_sha256(
                    market_bindings
                ),
                "anomaly_registry_path": ANOMALY_REGISTRY_RELATIVE_PATH.as_posix(),
                "anomaly_registry_canonical_lf_sha256": (
                    ANOMALY_REGISTRY_CANONICAL_LF_SHA256
                ),
                "anomaly_evidence_binding_set_sha256": _records_sha256(
                    anomaly_bindings
                ),
                "anomaly_operation_count": "9",
                "verified_real_extreme_count": "8",
                "verified_data_error_repaired_count": "1",
                "effective_anomaly_blocker_count": "0",
                "selected_operation_count": str(len(detail)),
                "sample_start_trigger_date": str(detail["trigger_date"].min()),
                "sample_end_trigger_date": str(detail["trigger_date"].max()),
                "chronological_bucket_sizes": "18|18|17",
                "benchmark_exact_date_coverage_count": str(
                    detail["benchmark_exact_date_coverage"].eq("True").sum()
                ),
                "twse_operation_count": str(markets.get("TWSE", 0)),
                "tpex_operation_count": str(markets.get("TPEX", 0)),
                "strong_bull_operation_count": str(regimes.get("strong_bull", 0)),
                "mild_bull_operation_count": str(regimes.get("mild_bull", 0)),
                "correction_operation_count": str(regimes.get("correction", 0)),
                "range_bound_operation_count": str(regimes.get("range_bound", 0)),
                "high_risk_operation_count": str(regimes.get("high_risk", 0)),
                "gross_win_rate_pct": str(gross["positive_rate_pct"]),
                "gross_avg_return_pct": str(gross["avg_return_pct"]),
                "gross_median_return_pct": str(gross["median_return_pct"]),
                "benchmark_outperformance_rate_pct": str(excess["positive_rate_pct"]),
                "avg_excess_return_pct": str(excess["avg_return_pct"]),
                "median_excess_return_pct": str(excess["median_return_pct"]),
                "commission_rate_each_side": str(COMMISSION_RATE_EACH_SIDE),
                "sell_transaction_tax_rate": str(SELL_TRANSACTION_TAX_RATE),
                "slippage_scenarios_each_side_bp": "0|10|25",
                "cost_stress_25bp_win_rate_pct": str(stress["positive_rate_pct"]),
                "cost_stress_25bp_avg_return_pct": str(stress["avg_return_pct"]),
                "cost_stress_25bp_median_return_pct": str(
                    stress["median_return_pct"]
                ),
                "launch_evidence_status": "provisional_backtest_supported_oos_unconfirmed",
                "gross_chronological_status": "positive_all_thirds",
                "transaction_cost_status": "robust_declared_grid",
                "relative_edge_status": "weak_and_time_unstable",
                "regime_coverage_status": "limited_no_range_or_high_risk",
                "anomaly_disposition_status": ANOMALY_DISPOSITION_STATUS,
                "sample_selection_policy": SAMPLE_SELECTION_POLICY,
                "forward_holdout_use_policy": FORWARD_HOLDOUT_USE_POLICY,
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "evidence_permission_status": "evidence_only_no_permission_grant",
                "formal_model_use_allowed": "False",
                "approved_for_daily": "False",
                "presentation_allowed": "False",
                "production_allowed": "False",
            }
        ]
    )


def validate(
    *,
    artifact_root: Path = ROOT,
    source_root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    artifact_root = Path(artifact_root).resolve()
    source_root = Path(source_root).resolve()
    try:
        source = _read_frozen_source(source_root)
        anomaly_bindings = _anomaly_bindings(source_root, source)
        expected_detail, benchmark_bindings, market_bindings = _replay_detail(
            source_root, source
        )
        expected_matrix = _expected_matrix(expected_detail, source)
        expected_manifest = _expected_manifest(
            expected_detail,
            expected_matrix,
            benchmark_bindings,
            market_bindings,
            anomaly_bindings,
        )
        for relative_path in (
            DETAIL_RELATIVE_PATH,
            MATRIX_RELATIVE_PATH,
            MANIFEST_RELATIVE_PATH,
        ):
            path = artifact_root / relative_path
            if not path.is_file() or path.is_symlink():
                errors.append(f"immutable evidence artifact missing or unsafe: {path}")
        if errors:
            return errors
        observed_detail = pd.read_csv(
            artifact_root / DETAIL_RELATIVE_PATH,
            dtype=str,
            keep_default_na=False,
        )
        observed_matrix = pd.read_csv(
            artifact_root / MATRIX_RELATIVE_PATH,
            dtype=str,
            keep_default_na=False,
        )
        observed_manifest = pd.read_csv(
            artifact_root / MANIFEST_RELATIVE_PATH,
            dtype=str,
            keep_default_na=False,
        )
        comparisons = (
            ("detail", observed_detail, expected_detail),
            ("matrix", observed_matrix, expected_matrix),
            ("manifest", observed_manifest, expected_manifest),
        )
        for label, observed, expected in comparisons:
            if list(observed.columns) != list(expected.columns):
                errors.append(f"{label} column contract drift")
                continue
            if not observed.equals(expected):
                errors.append(f"{label} independent replay mismatch")
                continue
            observed_bytes = _canonical_lf_bytes(artifact_root / {
                "detail": DETAIL_RELATIVE_PATH,
                "matrix": MATRIX_RELATIVE_PATH,
                "manifest": MANIFEST_RELATIVE_PATH,
            }[label])
            if observed_bytes != _csv_bytes(expected):
                errors.append(f"{label} byte serialization drift")
        bucket_counts = expected_detail["chronological_bucket_id"].value_counts()
        if tuple(
            int(bucket_counts.get(bucket, 0))
            for bucket in (
                "chronological_third_1_early_18",
                "chronological_third_2_middle_18",
                "chronological_third_3_late_17",
            )
        ) != EXPECTED_BUCKET_SIZES:
            errors.append("chronological equal-count bucket contract drift")
        if set(expected_detail["benchmark_exact_date_coverage"]) != {"True"}:
            errors.append("benchmark exact-date coverage is incomplete")
        if any(
            expected_detail[column].ne("False").any()
            for column in (
                "formal_model_use_allowed",
                "approved_for_daily",
                "presentation_allowed",
                "production_allowed",
            )
        ):
            errors.append("evidence component grants a formal permission")
    except (
        RuntimeError,
        ValueError,
        KeyError,
        IndexError,
        pd.errors.ParserError,
    ) as exc:
        errors.append(str(exc))
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently replay frozen revenue source_mid_falling launch evidence."
    )
    parser.add_argument("--artifact-root", type=Path, default=ROOT)
    parser.add_argument("--source-root", type=Path, default=ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(
        artifact_root=args.artifact_root,
        source_root=args.source_root,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue frozen-rule launch evidence independent validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
