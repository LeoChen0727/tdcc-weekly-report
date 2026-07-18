from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pandas as pd


LATEST_DIR = Path("output/latest")
THEME_LAYER_CSV = LATEST_DIR / "volume_attack_theme_layer_latest.csv"
THEME_LAYER_MD = LATEST_DIR / "volume_attack_theme_layer_latest.md"
STOCK_LAYER_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
STOCK_LAYER_MD = LATEST_DIR / "volume_attack_theme_stocks_latest.md"
VOLUME_WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
CANDIDATE_CSV = LATEST_DIR / "all_candidates_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
VALIDATION_JSON = LATEST_DIR / "volume_attack_theme_layer_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "volume_attack_theme_layer_validation_latest.md"

VALID_THEME_STATUSES = {
    "confirmed_volume_theme",
    "early_mainstream_candidate",
    "watch_volume_theme",
    "single_stock_volume_attack",
    "overheated_volume_theme",
    "failed_volume_theme",
    "weak_or_non_mainstream_volume_watch",
    "non_mainstream_volume_watch",
    "theme_status_missing",
    "insufficient_data",
}

REQUIRED_THEME_COLUMNS = [
    "theme_name",
    "theme_final_status",
    "theme_structural_status",
    "theme_mainstream_label",
    "theme_volume_attack_status",
    "volume_attack_count",
    "leader_stock_id",
    "leader_stock_name",
    "interpretation",
]

REQUIRED_STOCK_COLUMNS = [
    "signal_date",
    "stock_id",
    "stock_name",
    "theme_name",
    "theme_final_status",
    "theme_structural_status",
    "theme_mainstream_label",
    "theme_volume_attack_status",
    "volume_breakout_type",
    "volume_breakout_priority",
    "selection_status",
    "volume_breakout_score",
    "volume_breakout_rank",
    "advisory_score_source_artifact",
    "advisory_score_source_sha256",
    "volume_watch_as_of",
    "volume_watch_source_artifact",
    "volume_watch_source_sha256",
    "candidate_source_type",
    "warrant_flow_signal",
    "warrant_flow_as_of",
    "warrant_flow_source_artifact",
    "warrant_flow_source_sha256",
    "warrant_flow_official_source_artifact",
    "warrant_flow_official_source_sha256",
]


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def missing_columns(df: pd.DataFrame, required: list[str]) -> list[str]:
    return [col for col in required if col not in df.columns]


def sha256_file(path: Path) -> str:
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8-sig")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    theme = read_csv(THEME_LAYER_CSV)
    stocks = read_csv(STOCK_LAYER_CSV)

    for path in [THEME_LAYER_CSV, THEME_LAYER_MD, STOCK_LAYER_CSV, STOCK_LAYER_MD]:
        if not path.exists():
            errors.append(f"missing_file: {path.as_posix()}")

    watch_sha = sha256_file(VOLUME_WATCH_CSV)
    candidate_sha = sha256_file(CANDIDATE_CSV)
    official_sha = sha256_file(WARRANT_FLOW_CSV)
    for source_name, source_sha in (
        ("volume watch", watch_sha),
        ("all_candidates", candidate_sha),
        ("official warrant", official_sha),
    ):
        if len(source_sha) != 64:
            errors.append(f"{source_name} source SHA-256 is unavailable")
    required_markdown_tokens = (
        f"source_watch: `{VOLUME_WATCH_CSV.as_posix()}`",
        f"source_watch_sha256: `{watch_sha}`",
        f"warrant_projection_source: `{CANDIDATE_CSV.as_posix()}`",
        f"warrant_projection_source_sha256: `{candidate_sha}`",
        f"warrant_official_parity_source: `{WARRANT_FLOW_CSV.as_posix()}`",
        f"warrant_official_parity_source_sha256: `{official_sha}`",
    )
    for path in (THEME_LAYER_MD, STOCK_LAYER_MD):
        if not path.is_file():
            continue
        markdown = path.read_text(encoding="utf-8")
        for token in required_markdown_tokens:
            if token not in markdown:
                errors.append(f"{path.as_posix()} missing source lineage token: {token}")

    if not theme.empty:
        miss = missing_columns(theme, REQUIRED_THEME_COLUMNS)
        if miss:
            errors.append(f"theme_layer missing columns: {miss}")
        if "theme_volume_attack_status" in theme.columns:
            invalid = sorted(set(theme["theme_volume_attack_status"].astype(str)) - VALID_THEME_STATUSES)
            if invalid:
                errors.append(f"theme_layer invalid theme_volume_attack_status: {invalid}")
    else:
        warnings.append("theme_layer_empty")

    if not stocks.empty:
        miss = missing_columns(stocks, REQUIRED_STOCK_COLUMNS)
        if miss:
            errors.append(f"stock_layer missing columns: {miss}")
        for col in ["theme_final_status", "theme_volume_attack_status"]:
            if col in stocks.columns and (stocks[col].astype(str).str.strip() == "").any():
                errors.append(f"stock_layer has blank {col}")
        allowed_warrant_columns = {
            "warrant_flow_signal",
            "warrant_flow_as_of",
            "warrant_flow_source_artifact",
            "warrant_flow_source_sha256",
            "warrant_flow_official_source_artifact",
            "warrant_flow_official_source_sha256",
        }
        leaked_sensitive_columns = {
            column
            for column in stocks.columns
            if (
                column.startswith("warrant_")
                and column not in allowed_warrant_columns
            )
            or column
            in {
                "score",
                "rank",
                "advisory_volume_breakout_score",
                "advisory_volume_breakout_rank",
                "call_warrant_count",
                "put_warrant_count",
            }
        }
        if leaked_sensitive_columns:
            errors.append(
                "stock_layer contains unregistered raw source fields: "
                + ",".join(sorted(leaked_sensitive_columns))
            )
        if not miss:
            expected_constants = {
                "volume_watch_source_artifact": VOLUME_WATCH_CSV.as_posix(),
                "volume_watch_source_sha256": watch_sha,
                "warrant_flow_source_artifact": CANDIDATE_CSV.as_posix(),
                "warrant_flow_source_sha256": candidate_sha,
                "warrant_flow_official_source_artifact": WARRANT_FLOW_CSV.as_posix(),
                "warrant_flow_official_source_sha256": official_sha,
            }
            for column, expected in expected_constants.items():
                actual = set(stocks[column].astype(str))
                if actual != {expected}:
                    errors.append(
                        f"stock_layer {column} must equal canonical source value: "
                        f"expected={expected!r} actual={sorted(actual)}"
                    )
            if (stocks["warrant_flow_as_of"].astype(str).str.strip() == "").any():
                errors.append("stock_layer has blank warrant_flow_as_of")
            if (stocks["volume_watch_as_of"].astype(str).str.strip() == "").any():
                errors.append("stock_layer has blank volume_watch_as_of")

            watch = read_csv(VOLUME_WATCH_CSV)
            watch_required = {
                "signal_date",
                "stock_id",
                "advisory_volume_breakout_score",
                "advisory_volume_breakout_rank",
                "advisory_score_as_of",
                "advisory_score_source_artifact",
                "advisory_score_source_sha256",
            }
            if watch.empty:
                errors.append("volume watch is empty while theme stock rows exist")
            elif not watch_required <= set(watch.columns):
                errors.append(
                    "volume watch advisory score/rank lineage columns missing: "
                    + ",".join(sorted(watch_required - set(watch.columns)))
                )
            else:
                forbidden_watch_columns = {
                    "volume_breakout_score",
                    "volume_breakout_rank",
                }.intersection(watch.columns)
                if forbidden_watch_columns:
                    errors.append(
                        "volume watch has forbidden legacy score/rank columns: "
                        + ",".join(sorted(forbidden_watch_columns))
                    )
                watch_keys = watch[["signal_date", "stock_id"]].astype(str).agg("|".join, axis=1)
                stock_keys = stocks[["signal_date", "stock_id"]].astype(str).agg("|".join, axis=1)
                if watch_keys.duplicated().any():
                    errors.append("volume watch score/rank lineage grain is not unique")
                if stock_keys.duplicated().any():
                    errors.append("theme stock score/rank lineage grain is not unique")
                watch_by_key = {
                    key: row
                    for key, (_, row) in zip(watch_keys.tolist(), watch.iterrows())
                }
                stocks_by_key = {
                    key: row
                    for key, (_, row) in zip(stock_keys.tolist(), stocks.iterrows())
                }
                if set(watch_by_key) != set(stocks_by_key):
                    errors.append("theme advisory watch score/rank membership mismatch")
                for key in sorted(set(watch_by_key) & set(stocks_by_key)):
                    source_row = watch_by_key[key]
                    mirror_row = stocks_by_key[key]
                    for source_column, mirror_column in (
                        ("advisory_volume_breakout_score", "volume_breakout_score"),
                        ("advisory_volume_breakout_rank", "volume_breakout_rank"),
                        (
                            "advisory_score_source_artifact",
                            "advisory_score_source_artifact",
                        ),
                        (
                            "advisory_score_source_sha256",
                            "advisory_score_source_sha256",
                        ),
                    ):
                        if str(source_row.get(source_column, "")) != str(
                            mirror_row.get(mirror_column, "")
                        ):
                            errors.append(
                                "theme advisory watch score/rank parity mismatch: "
                                f"key={key} source_column={source_column} "
                                f"mirror_column={mirror_column}"
                            )
                    signal_date = str(source_row.get("signal_date", ""))
                    advisory_score_as_of = str(
                        source_row.get("advisory_score_as_of", "")
                    )
                    if not advisory_score_as_of or advisory_score_as_of != signal_date:
                        errors.append(
                            "volume watch advisory score as_of mismatch: "
                            f"key={key}"
                        )
                    if str(mirror_row.get("volume_watch_as_of", "")) != advisory_score_as_of:
                        errors.append(
                            "theme advisory watch as_of mismatch: "
                            f"key={key}"
                        )

            candidates = read_csv(CANDIDATE_CSV)
            official = read_csv(WARRANT_FLOW_CSV)
            candidate_signals: dict[str, set[str]] = {}
            if not candidates.empty and {"stock_id", "warrant_flow_signal"} <= set(candidates.columns):
                for stock_id, part in candidates.groupby("stock_id", dropna=False):
                    candidate_signals[str(stock_id)] = set(
                        part["warrant_flow_signal"].astype(str)
                    )
            official_signals: dict[str, set[str]] = {}
            if not official.empty and {"stock_id", "warrant_flow_signal"} <= set(official.columns):
                for stock_id, part in official.groupby("stock_id", dropna=False):
                    official_signals[str(stock_id)] = set(
                        part["warrant_flow_signal"].astype(str)
                    )
            for _, row in stocks.iterrows():
                stock_id = str(row["stock_id"])
                published = str(row["warrant_flow_signal"])
                expected_set = candidate_signals.get(stock_id, {""})
                if len(expected_set) != 1 or published not in expected_set:
                    errors.append(
                        "stock_layer warrant projection differs from all_candidates: "
                        f"stock_id={stock_id} published={published!r} "
                        f"candidate={sorted(expected_set)}"
                    )
                official_set = official_signals.get(stock_id, {""})
                if (
                    len(official_set) != 1 or published not in official_set
                ):
                    errors.append(
                        "stock_layer warrant projection differs from official warrant: "
                        f"stock_id={stock_id} published={published!r} "
                        f"official={sorted(official_set)}"
                    )
    else:
        warnings.append("stock_layer_empty")

    result = {
        "status": "pass" if not errors else "fail",
        "errors": errors,
        "warnings": warnings,
        "theme_rows": int(len(theme)),
        "stock_rows": int(len(stocks)),
    }

    VALIDATION_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    VALIDATION_MD.write_text(
        "\n".join(
            [
                "# Volume Attack Theme Layer Validation",
                "",
                f"- status: `{result['status']}`",
                f"- theme_rows: `{result['theme_rows']}`",
                f"- stock_rows: `{result['stock_rows']}`",
                f"- errors: `{'; '.join(errors) if errors else 'none'}`",
                f"- warnings: `{'; '.join(warnings) if warnings else 'none'}`",
                "",
            ]
        ),
        encoding="utf-8",
    )

    if errors:
        raise SystemExit(1)
    print(f"volume_attack_theme_layer validation pass: theme_rows={len(theme)} stock_rows={len(stocks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
