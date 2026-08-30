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
EVIDENCE_PREFIX = EVIDENCE_VERSION
DETAIL_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_PREFIX}_detail.csv"
MATRIX_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_PREFIX}_matrix.csv"
MANIFEST_RELATIVE_PATH = EVIDENCE_DIRECTORY / f"{EVIDENCE_PREFIX}_manifest.csv"

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


def _canonical_lf_bytes(path: Path) -> bytes:
    """Return portable UTF-8 bytes without treating checkout EOL as evidence."""
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
        f"{path.as_posix()}|{len(payload)}|{hashlib.sha256(payload).hexdigest()}\n"
        for path, payload in sorted(payloads.items(), key=lambda item: item[0].as_posix())
    )
    return hashlib.sha256(members.encode("utf-8")).hexdigest()


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


def _bool(value: object, *, label: str) -> bool:
    text = str(value).strip().lower()
    if text in {"true", "1"}:
        return True
    if text in {"false", "0"}:
        return False
    raise RuntimeError(f"{label} is not an exact boolean: {value!r}")


def _decimal(value: object, *, label: str) -> Decimal:
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
    payload = json.dumps(
        records,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _frame_semantic_sha256(frame: pd.DataFrame) -> str:
    rows = [
        ["" if pd.isna(value) else str(value) for value in row]
        for row in frame.itertuples(index=False, name=None)
    ]
    return _records_sha256({"columns": list(frame.columns), "rows": rows})


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(index=False, lineterminator="\n").encode("utf-8")


def _market_code(value: object) -> str:
    text = str(value).strip().upper()
    if "TPEX" in text or "OTC" in text:
        return "TPEX"
    if "TWSE" in text or "LISTED" in text:
        return "TWSE"
    raise RuntimeError(f"unsupported entry-date market mapping: {value!r}")


def _entry_regime(row: pd.Series) -> str:
    close = _decimal(row["close"], label="entry index close")
    ma20 = _decimal(row["ma20"], label="entry index ma20")
    ma60 = _decimal(row["ma60"], label="entry index ma60")
    return20 = _decimal(row["return_20d"], label="entry index return_20d")
    above20 = _bool(row["above_ma20"], label="entry index above_ma20")
    above60 = _bool(row["above_ma60"], label="entry index above_ma60")
    if close < ma60 and return20 < 0:
        return "high_risk"
    if (not above20) or return20 <= Decimal("-3"):
        return "correction"
    if above20 and above60 and return20 >= Decimal("5"):
        return "strong_bull"
    if above20 and above60:
        return "mild_bull"
    return "range_bound"


def _pct_return(exit_value: Decimal, entry_value: Decimal) -> Decimal:
    if entry_value <= 0:
        raise RuntimeError("entry value must be positive")
    return (exit_value / entry_value - Decimal("1")) * Decimal("100")


def _net_return(
    entry_price: Decimal,
    exit_price: Decimal,
    slippage_each_side: Decimal,
) -> Decimal:
    buy_execution = entry_price * (Decimal("1") + slippage_each_side)
    sell_execution = exit_price * (Decimal("1") - slippage_each_side)
    entry_cash = buy_execution * (Decimal("1") + COMMISSION_RATE_EACH_SIDE)
    exit_cash = sell_execution * (
        Decimal("1") - COMMISSION_RATE_EACH_SIDE - SELL_TRANSACTION_TAX_RATE
    )
    return _pct_return(exit_cash, entry_cash)


def _metric(values: Iterable[Decimal]) -> dict[str, str]:
    ordered = sorted(values)
    if not ordered:
        raise RuntimeError("metric input is empty")
    count = len(ordered)
    positive = sum(value > 0 for value in ordered)
    average = sum(ordered, Decimal("0")) / Decimal(count)
    middle = Decimal(str(median(ordered)))
    return {
        "sample_count": str(count),
        "positive_count": str(positive),
        "positive_rate_pct": _fmt(Decimal(positive) * Decimal("100") / Decimal(count)),
        "avg_return_pct": _fmt(average),
        "median_return_pct": _fmt(middle),
        "min_return_pct": _fmt(ordered[0]),
        "max_return_pct": _fmt(ordered[-1]),
    }


def _read_source(root: Path) -> pd.DataFrame:
    path = root / SOURCE_RELATIVE_PATH
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"frozen v3 source is missing or unsafe: {path}")
    observed_sha = hashlib.sha256(_canonical_lf_bytes(path)).hexdigest()
    if observed_sha != SOURCE_CANONICAL_LF_SHA256:
        raise RuntimeError(
            "frozen v3 source canonical LF SHA drift: "
            f"{observed_sha}/{SOURCE_CANONICAL_LF_SHA256}"
        )
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
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
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"frozen v3 source is missing columns: {missing}")
    exact_single = {
        "model_id": MODEL_ID,
        "artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "detail_artifact_canonical_sha256": SOURCE_ARTIFACT_CANONICAL_SHA256,
        "candidate_detail_row_set_sha256": SOURCE_ROW_SET_SHA256,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
    }
    for column, expected in exact_single.items():
        observed = set(frame[column].astype(str))
        if observed != {expected}:
            raise RuntimeError(f"frozen v3 source {column} drift: {sorted(observed)}")
    for permission in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
    ):
        if any(_bool(value, label=permission) for value in frame[permission]):
            raise RuntimeError(f"frozen v3 source unexpectedly grants {permission}")
    if frame["candidate_detail_row_sha256"].duplicated().any():
        raise RuntimeError("frozen v3 source candidate row SHA is not unique")
    return frame


def _selected_source(frame: pd.DataFrame) -> pd.DataFrame:
    selected = frame.loc[
        frame["lifecycle_policy_id"].eq(LIFECYCLE_POLICY_ID)
        & frame["confirmation_variant_id"].eq(CONFIRMATION_VARIANT_ID)
        & frame["mid_falling_member"].map(
            lambda value: _bool(value, label="mid_falling_member")
        )
        & frame["primary_included"].map(
            lambda value: _bool(value, label="primary_included")
        )
    ].copy()
    selected = selected.sort_values(
        ["trigger_date", "operation_key"], kind="stable"
    ).reset_index(drop=True)
    if len(selected) != EXPECTED_OPERATION_COUNT:
        raise RuntimeError(
            f"frozen selected operation count drift: {len(selected)}/{EXPECTED_OPERATION_COUNT}"
        )
    if selected["operation_key"].duplicated().any():
        raise RuntimeError("frozen selected operation_key is not unique")
    if not all(
        _bool(value, label="primary_included")
        for value in selected["primary_included"]
    ):
        raise RuntimeError("frozen selected evidence contains non-primary rows")
    return selected


def _anomaly_bindings(root: Path, source: pd.DataFrame) -> list[dict[str, str]]:
    path = root / ANOMALY_REGISTRY_RELATIVE_PATH
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"anomaly disposition registry is missing or unsafe: {path}")
    observed_sha = hashlib.sha256(_canonical_lf_bytes(path)).hexdigest()
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
    dispositions = registry["final_disposition"].value_counts().to_dict()
    if dispositions != {"verified_real_extreme": 8, "verified_data_error": 1}:
        raise RuntimeError(f"anomaly disposition count drift: {dispositions}")

    selected = _selected_source(source)
    selected_by_key = selected.set_index("operation_key", drop=False)
    if not set(registry["operation_key"]).issubset(set(selected_by_key.index)):
        raise RuntimeError("anomaly registry contains an operation outside the frozen sample")
    current_candidates = set(
        selected.loc[
            selected["source_anomaly_candidate_flag"].map(
                lambda value: _bool(value, label="source_anomaly_candidate_flag")
            )
            | selected["operation_return_review_candidate_flag"].map(
                lambda value: _bool(
                    value, label="operation_return_review_candidate_flag"
                )
            ),
            "operation_key",
        ]
    )
    verified_real_keys = set(
        registry.loc[
            registry["final_disposition"].eq("verified_real_extreme"),
            "operation_key",
        ]
    )
    if current_candidates != verified_real_keys:
        raise RuntimeError("frozen source anomaly flags do not match verified real extremes")

    bindings: list[dict[str, str]] = []
    for row in registry.sort_values("operation_key", kind="stable").to_dict("records"):
        source_row = selected_by_key.loc[str(row["operation_key"])]
        if str(source_row["candidate_detail_row_sha256"]) != str(
            row["candidate_detail_row_sha256"]
        ):
            raise RuntimeError("anomaly registry candidate row SHA drift")
        match = EVIDENCE_REFERENCE_RE.fullmatch(str(row["evidence_reference"]))
        if match is None:
            raise RuntimeError("anomaly registry has a malformed evidence reference")
        relative_text = match.group("path")
        if not relative_text.startswith(ANOMALY_EVIDENCE_ROOT) or ".." in Path(
            relative_text
        ).parts:
            raise RuntimeError("anomaly evidence reference escapes its model-owned root")
        evidence_path = root / Path(relative_text)
        if not evidence_path.is_file() or evidence_path.is_symlink():
            raise RuntimeError(f"anomaly evidence is missing or unsafe: {evidence_path}")
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


def _load_index(root: Path) -> pd.DataFrame:
    path = root / INDEX_RELATIVE_PATH
    frame = pd.read_csv(path, dtype=str, keep_default_na=False)
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
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"market index history is missing columns: {missing}")
    if frame.duplicated(["index_code", "date"]).any():
        raise RuntimeError("market index history has duplicate index/date rows")
    return frame.set_index(["index_code", "date"], drop=False)


def _price_market(
    root: Path,
    stock_id: str,
    entry_date: str,
    cache: dict[str, pd.DataFrame],
) -> str:
    if stock_id not in cache:
        path = root / "data" / "stock_price_history" / f"{stock_id}.csv"
        frame = pd.read_csv(path, dtype=str, keep_default_na=False)
        required = {"date", "market"}
        missing = sorted(required - set(frame.columns))
        if missing:
            raise RuntimeError(f"stock {stock_id} price history missing columns: {missing}")
        cache[stock_id] = frame
    rows = cache[stock_id].loc[cache[stock_id]["date"].eq(entry_date)]
    if len(rows) != 1:
        raise RuntimeError(
            f"stock {stock_id} entry-date market row count drift: {entry_date}/{len(rows)}"
        )
    return str(rows.iloc[0]["market"]).strip()


def _bucket_id(index: int) -> str:
    first, second, _third = EXPECTED_BUCKET_SIZES
    if index < first:
        return "chronological_third_1_early_18"
    if index < first + second:
        return "chronological_third_2_middle_18"
    return "chronological_third_3_late_17"


def build_detail(
    root: Path = ROOT,
) -> tuple[pd.DataFrame, pd.DataFrame, list[dict[str, str]], list[dict[str, str]]]:
    source = _read_source(root)
    selected = _selected_source(source)
    index = _load_index(root)
    price_cache: dict[str, pd.DataFrame] = {}
    detail_rows: list[dict[str, str]] = []
    benchmark_bindings: list[dict[str, str]] = []
    market_bindings: list[dict[str, str]] = []

    for order, operation in enumerate(selected.to_dict("records"), start=1):
        stock_id = str(operation["stock_id"])
        entry_date = str(operation["entry_date"])
        exit_date = str(operation["exit_date"])
        market_source = _price_market(root, stock_id, entry_date, price_cache)
        index_code = _market_code(market_source)
        entry_key = (index_code, entry_date)
        exit_key = (index_code, exit_date)
        if entry_key not in index.index or exit_key not in index.index:
            raise RuntimeError(
                "exact benchmark coverage is missing: "
                f"{operation['operation_key']}/{entry_key}/{exit_key}"
            )
        entry_index = index.loc[entry_key]
        exit_index = index.loc[exit_key]
        if isinstance(entry_index, pd.DataFrame) or isinstance(exit_index, pd.DataFrame):
            raise RuntimeError("exact benchmark key unexpectedly resolves to multiple rows")

        entry_price = _decimal(operation["entry_price"], label="entry_price")
        exit_price = _decimal(operation["exit_price"], label="exit_price")
        source_gross = _decimal(
            operation["realized_return_pct"], label="source realized_return_pct"
        )
        replayed_gross = _pct_return(exit_price, entry_price)
        if abs(source_gross - replayed_gross) > Decimal("0.0001"):
            raise RuntimeError(
                "source gross return replay drift: "
                f"{operation['operation_key']}/{source_gross}/{replayed_gross}"
            )
        benchmark_entry_open = _decimal(
            entry_index["open"], label="benchmark entry open"
        )
        benchmark_exit_close = _decimal(
            exit_index["close"], label="benchmark exit close"
        )
        benchmark_return = _pct_return(benchmark_exit_close, benchmark_entry_open)
        excess_return = source_gross - benchmark_return
        regime = _entry_regime(entry_index)
        net_values = {
            scenario_id: _net_return(entry_price, exit_price, slippage)
            for scenario_id, slippage in COST_SCENARIOS
        }
        benchmark_binding = {
            "source_operation_key": str(operation["operation_key"]),
            "benchmark_index_code": index_code,
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
        market_binding = {
            "source_operation_key": str(operation["operation_key"]),
            "stock_id": stock_id,
            "entry_date": entry_date,
            "market_source_value": market_source,
            "benchmark_index_code": index_code,
        }
        benchmark_bindings.append(benchmark_binding)
        market_bindings.append(market_binding)
        detail_rows.append(
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
                "chronological_order": str(order),
                "chronological_bucket_id": _bucket_id(order - 1),
                "stock_id": stock_id,
                "stock_name": str(operation["stock_name"]),
                "trigger_date": str(operation["trigger_date"]),
                "confirmation_date": str(operation["confirmation_date"]),
                "entry_date": entry_date,
                "exit_date": exit_date,
                "entry_price": str(operation["entry_price"]),
                "exit_price": str(operation["exit_price"]),
                "gross_realized_return_pct": _fmt(source_gross),
                "source_anomaly_candidate_flag": str(
                    _bool(
                        operation["source_anomaly_candidate_flag"],
                        label="source_anomaly_candidate_flag",
                    )
                ),
                "operation_return_review_candidate_flag": str(
                    _bool(
                        operation["operation_return_review_candidate_flag"],
                        label="operation_return_review_candidate_flag",
                    )
                ),
                "anomaly_policy": ANOMALY_POLICY,
                "market_source_value": market_source,
                "benchmark_index_code": index_code,
                "benchmark_entry_date": entry_date,
                "benchmark_entry_open": str(entry_index["open"]),
                "benchmark_exit_date": exit_date,
                "benchmark_exit_close": str(exit_index["close"]),
                "benchmark_return_pct": _fmt(benchmark_return),
                "excess_return_pct": _fmt(excess_return),
                "benchmark_exact_date_coverage": "True",
                "entry_index_close": str(entry_index["close"]),
                "entry_index_ma20": str(entry_index["ma20"]),
                "entry_index_ma60": str(entry_index["ma60"]),
                "entry_index_return_20d_pct": str(entry_index["return_20d"]),
                "entry_index_above_ma20": str(
                    _bool(entry_index["above_ma20"], label="entry index above_ma20")
                ),
                "entry_index_above_ma60": str(
                    _bool(entry_index["above_ma60"], label="entry index above_ma60")
                ),
                "entry_market_regime": regime,
                "commission_rate_each_side": str(COMMISSION_RATE_EACH_SIDE),
                "sell_transaction_tax_rate": str(SELL_TRANSACTION_TAX_RATE),
                "net_return_slippage_0bp_each_side_pct": _fmt(
                    net_values["declared_cost_slippage_0bp_each_side"]
                ),
                "net_return_slippage_10bp_each_side_pct": _fmt(
                    net_values["declared_cost_slippage_10bp_each_side"]
                ),
                "net_return_slippage_25bp_each_side_pct": _fmt(
                    net_values["declared_cost_slippage_25bp_each_side"]
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

    detail = pd.DataFrame(detail_rows, columns=DETAIL_COLUMNS)
    return detail, source, benchmark_bindings, market_bindings


def _matrix_row(
    *,
    analysis_family: str,
    group_id: str,
    return_basis: str,
    values: Iterable[Decimal],
    status: str,
    notes: str,
    comparator_values: Iterable[Decimal] | None = None,
    group_count: str = "",
    coverage_count: str = "",
    coverage_total: str = "",
) -> dict[str, str]:
    metrics = _metric(values)
    row = {
        "evidence_id": EVIDENCE_ID,
        "evidence_version": EVIDENCE_VERSION,
        "analysis_family": analysis_family,
        "group_id": group_id,
        "return_basis": return_basis,
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
    if comparator_values is not None:
        comparator = _metric(comparator_values)
        row["comparator_sample_count"] = comparator["sample_count"]
        row["comparator_avg_return_pct"] = comparator["avg_return_pct"]
        row["comparator_median_return_pct"] = comparator["median_return_pct"]
        row["avg_difference_pct_points"] = _fmt(
            _decimal(metrics["avg_return_pct"], label="metric average")
            - _decimal(comparator["avg_return_pct"], label="comparator average")
        )
        row["median_difference_pct_points"] = _fmt(
            _decimal(metrics["median_return_pct"], label="metric median")
            - _decimal(comparator["median_return_pct"], label="comparator median")
        )
    return row


def build_matrix(detail: pd.DataFrame, source: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, str]] = []

    def values(frame: pd.DataFrame, column: str) -> list[Decimal]:
        return [
            _decimal(value, label=f"matrix {column}") for value in frame[column]
        ]

    rows.append(
        _matrix_row(
            analysis_family="overall_gross",
            group_id="all_53",
            return_basis="gross_d2_open_to_d30_close",
            values=values(detail, "gross_realized_return_pct"),
            status="historical_backtest_gross_positive",
            notes="primary retains every verified real extreme and repaired-source rerun row",
            coverage_count=str(len(detail)),
            coverage_total=str(EXPECTED_OPERATION_COUNT),
        )
    )
    for bucket_id, part in detail.groupby("chronological_bucket_id", sort=False):
        rows.append(
            _matrix_row(
                analysis_family="chronological_gross",
                group_id=str(bucket_id),
                return_basis="gross_d2_open_to_d30_close",
                values=values(part, "gross_realized_return_pct"),
                status="gross_positive",
                notes="equal-count chronological thirds assigned without outcome values",
            )
        )

    rows.append(
        _matrix_row(
            analysis_family="overall_market_benchmark",
            group_id="all_53",
            return_basis="stock_gross_minus_same_market_same_dates_index_open_to_close",
            values=values(detail, "excess_return_pct"),
            status="weak_positive_overall",
            notes="exact-date TWSE or TPEX benchmark; no as-of or nearest-date fallback",
            coverage_count=str(len(detail)),
            coverage_total=str(EXPECTED_OPERATION_COUNT),
        )
    )
    for bucket_id, part in detail.groupby("chronological_bucket_id", sort=False):
        excess_values = values(part, "excess_return_pct")
        metric = _metric(excess_values)
        status = (
            "relative_edge_positive"
            if _decimal(metric["avg_return_pct"], label="bucket excess average") > 0
            and _decimal(metric["median_return_pct"], label="bucket excess median") > 0
            else "relative_edge_negative"
        )
        rows.append(
            _matrix_row(
                analysis_family="chronological_market_benchmark",
                group_id=str(bucket_id),
                return_basis="stock_gross_minus_same_market_same_dates_index_open_to_close",
                values=excess_values,
                status=status,
                notes="relative edge is diagnostic and does not reselect the frozen sample",
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
            regime_values = values(part, column)
            metric = _metric(regime_values)
            status = (
                "gross_observed"
                if column == "gross_realized_return_pct"
                else (
                    "relative_edge_positive"
                    if _decimal(metric["avg_return_pct"], label="regime excess average") > 0
                    and _decimal(metric["median_return_pct"], label="regime excess median") > 0
                    else "relative_edge_negative"
                )
            )
            rows.append(
                _matrix_row(
                    analysis_family="entry_market_regime",
                    group_id=str(regime),
                    return_basis=basis,
                    values=regime_values,
                    status=status,
                    notes="entry-date point-in-time index regime classification",
                )
            )

    for market, part in detail.groupby("benchmark_index_code", sort=True):
        rows.append(
            _matrix_row(
                analysis_family="market_coverage",
                group_id=str(market),
                return_basis="gross_d2_open_to_d30_close",
                values=values(part, "gross_realized_return_pct"),
                status="observed_market_coverage",
                notes="market comes from the stock price row on the exact entry date",
            )
        )

    cost_columns = (
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
    )
    for scenario_id, column in cost_columns:
        rows.append(
            _matrix_row(
                analysis_family="transaction_cost",
                group_id=scenario_id,
                return_basis="net_d2_open_to_d30_close_after_declared_costs",
                values=values(detail, column),
                status="net_positive_declared_grid",
                notes=(
                    "commission 0.1425% each side is a conservative declared assumption; "
                    "sell tax 0.3%; minimum fee and position-size impact are not modeled"
                ),
            )
        )

    base = source.loc[
        source["lifecycle_policy_id"].eq(LIFECYCLE_POLICY_ID)
        & source["confirmation_variant_id"].eq(CONFIRMATION_VARIANT_ID)
        & source["primary_included"].map(
            lambda value: _bool(value, label="primary_included control")
        )
    ].copy()
    date_differences: list[Decimal] = []
    treated_total = 0
    comparator_total = 0
    same_date_groups = 0
    for key, part in base.groupby(["trigger_date", "entry_date", "exit_date"], sort=True):
        treated = part.loc[
            part["mid_falling_member"].map(
                lambda value: _bool(value, label="mid_falling_member control")
            )
        ]
        comparator = part.loc[
            part["low_falling_member"].map(
                lambda value: _bool(value, label="low_falling_member control")
            )
        ]
        if treated.empty or comparator.empty:
            continue
        treated_values = [
            _decimal(value, label="same-date treated return")
            for value in treated["realized_return_pct"]
        ]
        comparator_values = [
            _decimal(value, label="same-date comparator return")
            for value in comparator["realized_return_pct"]
        ]
        treated_metric = _metric(treated_values)
        comparator_metric = _metric(comparator_values)
        difference = _decimal(
            treated_metric["avg_return_pct"], label="same-date treated average"
        ) - _decimal(
            comparator_metric["avg_return_pct"], label="same-date comparator average"
        )
        date_differences.append(difference)
        treated_total += len(treated_values)
        comparator_total += len(comparator_values)
        same_date_groups += 1
        rows.append(
            _matrix_row(
                analysis_family="same_date_source_low_control_sensitivity",
                group_id="|".join(str(value) for value in key),
                return_basis="gross_mid_vs_source_low_same_trigger_entry_exit_dates",
                values=treated_values,
                comparator_values=comparator_values,
                status="sensitivity_sparse_not_independent",
                notes="challenger variant comparison; retained extremes; not a promotion hard gate",
            )
        )
    if same_date_groups == 0:
        raise RuntimeError("same-date source-low sensitivity has no overlapping date groups")
    date_metric = _metric(date_differences)
    summary_row = {
        "evidence_id": EVIDENCE_ID,
        "evidence_version": EVIDENCE_VERSION,
        "analysis_family": "same_date_source_low_control_sensitivity_summary",
        "group_id": "equal_weight_date_group_difference",
        "return_basis": "treated_group_avg_minus_comparator_group_avg",
        "sample_count": str(treated_total),
        "positive_count": date_metric["positive_count"],
        "positive_rate_pct": date_metric["positive_rate_pct"],
        "avg_return_pct": "",
        "median_return_pct": "",
        "min_return_pct": "",
        "max_return_pct": "",
        "comparator_sample_count": str(comparator_total),
        "comparator_avg_return_pct": "",
        "comparator_median_return_pct": "",
        "avg_difference_pct_points": date_metric["avg_return_pct"],
        "median_difference_pct_points": date_metric["median_return_pct"],
        "group_count": str(same_date_groups),
        "coverage_count": str(treated_total),
        "coverage_total": str(EXPECTED_OPERATION_COUNT),
        "status": "sensitivity_sparse_not_independent",
        "notes": "only exact shared trigger/entry/exit date groups; no nearest-date matching",
    }
    rows.append(summary_row)
    return pd.DataFrame(rows, columns=MATRIX_COLUMNS)


def build_artifacts(root: Path = ROOT) -> dict[Path, bytes]:
    detail, source, benchmark_bindings, market_bindings = build_detail(root)
    anomaly_bindings = _anomaly_bindings(root, source)
    matrix = build_matrix(detail, source)
    detail_bytes = _csv_bytes(detail)
    matrix_bytes = _csv_bytes(matrix)
    payloads = {
        DETAIL_RELATIVE_PATH: detail_bytes,
        MATRIX_RELATIVE_PATH: matrix_bytes,
    }

    gross = matrix.loc[
        matrix["analysis_family"].eq("overall_gross")
    ].iloc[0]
    excess = matrix.loc[
        matrix["analysis_family"].eq("overall_market_benchmark")
    ].iloc[0]
    cost_stress = matrix.loc[
        matrix["analysis_family"].eq("transaction_cost")
        & matrix["group_id"].eq("declared_cost_slippage_25bp_each_side")
    ].iloc[0]
    regime_counts = detail["entry_market_regime"].value_counts().to_dict()
    market_counts = detail["benchmark_index_code"].value_counts().to_dict()
    manifest = pd.DataFrame(
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
                "detail_canonical_lf_sha256": hashlib.sha256(detail_bytes).hexdigest(),
                "detail_semantic_sha256": _frame_semantic_sha256(detail),
                "matrix_path": MATRIX_RELATIVE_PATH.as_posix(),
                "matrix_canonical_lf_byte_count": str(len(matrix_bytes)),
                "matrix_canonical_lf_sha256": hashlib.sha256(matrix_bytes).hexdigest(),
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
                "twse_operation_count": str(market_counts.get("TWSE", 0)),
                "tpex_operation_count": str(market_counts.get("TPEX", 0)),
                "strong_bull_operation_count": str(regime_counts.get("strong_bull", 0)),
                "mild_bull_operation_count": str(regime_counts.get("mild_bull", 0)),
                "correction_operation_count": str(regime_counts.get("correction", 0)),
                "range_bound_operation_count": str(regime_counts.get("range_bound", 0)),
                "high_risk_operation_count": str(regime_counts.get("high_risk", 0)),
                "gross_win_rate_pct": str(gross["positive_rate_pct"]),
                "gross_avg_return_pct": str(gross["avg_return_pct"]),
                "gross_median_return_pct": str(gross["median_return_pct"]),
                "benchmark_outperformance_rate_pct": str(excess["positive_rate_pct"]),
                "avg_excess_return_pct": str(excess["avg_return_pct"]),
                "median_excess_return_pct": str(excess["median_return_pct"]),
                "commission_rate_each_side": str(COMMISSION_RATE_EACH_SIDE),
                "sell_transaction_tax_rate": str(SELL_TRANSACTION_TAX_RATE),
                "slippage_scenarios_each_side_bp": "0|10|25",
                "cost_stress_25bp_win_rate_pct": str(cost_stress["positive_rate_pct"]),
                "cost_stress_25bp_avg_return_pct": str(cost_stress["avg_return_pct"]),
                "cost_stress_25bp_median_return_pct": str(
                    cost_stress["median_return_pct"]
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
    manifest_bytes = _csv_bytes(manifest)
    return {
        DETAIL_RELATIVE_PATH: detail_bytes,
        MATRIX_RELATIVE_PATH: matrix_bytes,
        MANIFEST_RELATIVE_PATH: manifest_bytes,
    }


def write_artifacts(root: Path = ROOT) -> None:
    artifacts = build_artifacts(root)
    for relative_path, payload in artifacts.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            if path.is_symlink() or _canonical_lf_bytes(path) != payload:
                raise RuntimeError(f"immutable evidence artifact drift: {path}")
            continue
        path.write_bytes(payload)


def check_artifacts(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative_path, expected in build_artifacts(root).items():
        path = root / relative_path
        if not path.is_file() or path.is_symlink():
            errors.append(f"evidence artifact is missing or unsafe: {path}")
        elif _canonical_lf_bytes(path) != expected:
            errors.append(f"evidence artifact does not match frozen replay: {path}")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build immutable frozen-rule launch evidence for revenue source_mid_falling."
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    if args.check:
        errors = check_artifacts(root)
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("revenue frozen-rule launch evidence producer replay passed")
        return 0
    write_artifacts(root)
    print("revenue frozen-rule launch evidence artifacts written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
