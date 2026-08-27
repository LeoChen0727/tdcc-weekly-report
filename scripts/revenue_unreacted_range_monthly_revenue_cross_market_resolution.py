from __future__ import annotations

import hashlib
import json
import os
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re
import stat
import subprocess

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION = "canonical_json_v1"
RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)

KEY_COLUMNS = ("stock_id", "revenue_period")
SOURCE_IDENTITY_COLUMNS = (
    "market",
    "source_market_name",
    "source_table_date",
    "source_kind",
    "source_url",
    "source_file",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
BUSINESS_PAYLOAD_COLUMNS = (
    "stock_id",
    "stock_name",
    "industry",
    "revenue_period",
    "revenue_period_roc",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "formal_use_blocker",
    "coverage_note",
)
RAW_ROW_CANONICAL_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
RAW_ROW_NUMERIC_COLUMNS = (
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
)
RAW_ROW_BOOLEAN_COLUMNS = (
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
)
RESOLUTION_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "revenue_period",
    "earlier_market",
    "earlier_source_market_name",
    "earlier_source_table_date",
    "earlier_source_kind",
    "earlier_source_url",
    "earlier_source_file",
    "earlier_raw_row_canonical_sha256",
    "later_market",
    "later_source_market_name",
    "later_source_table_date",
    "later_source_kind",
    "later_source_url",
    "later_source_file",
    "later_raw_row_canonical_sha256",
    "official_market_transition_date",
    "canonical_source_table_date",
    "canonical_row_canonical_sha256",
    "resolution_status",
    "canonicalization_policy",
    "evidence_url",
    "formal_model_use_allowed",
    "notes",
)
CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "revenue_period",
    "earlier_market",
    "earlier_source_market_name",
    "earlier_source_table_date",
    "earlier_source_kind",
    "earlier_source_url",
    "earlier_source_file",
    "earlier_raw_row_canonical_sha256",
    "later_market",
    "later_source_market_name",
    "later_source_table_date",
    "later_source_kind",
    "later_source_url",
    "later_source_file",
    "later_raw_row_canonical_sha256",
    "official_market_transition_date",
    "canonical_source_table_date",
    "canonical_row_canonical_sha256",
    "resolution_status",
    "canonicalization_policy",
    "evidence_url",
    "formal_model_use_allowed",
)
CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS = (
    "model_id",
    "stock_id",
    "revenue_period",
    "resolution_id",
)
CANONICAL_MONTHLY_REVENUE_HISTORY_BINDING_COLUMNS = (
    "stock_id",
    "revenue_period",
    "source_row_canonical_sha256",
    "cross_market_resolution_id",
    "canonical_source_table_date",
)
CANONICAL_MONTHLY_REVENUE_HISTORY_SORT_KEYS = (
    "stock_id",
    "revenue_period",
)


def _normalize_stock_id(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text else ""


def _digits(value: object, length: int) -> str:
    text = _payload_value(value)
    exact = re.fullmatch(rf"\d{{{length}}}", text)
    if exact:
        return text
    numeric_export = re.fullmatch(rf"(\d{{{length}}})\.0+", text)
    if numeric_export:
        return numeric_export.group(1)
    raise RuntimeError(
        "monthly revenue date/period identity must be exact digits or an "
        f"equivalent numeric export: value={text!r}; digits={length}"
    )


def _payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    return text


def _canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _canonical_numeric_value(value: object) -> str:
    text = _payload_value(value)
    if not text:
        return ""
    try:
        number = Decimal(text)
    except InvalidOperation as exc:
        raise RuntimeError(f"monthly revenue canonical numeric value is invalid: {text}") from exc
    if not number.is_finite():
        raise RuntimeError(f"monthly revenue canonical numeric value is non-finite: {text}")
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    if "." in rendered:
        rendered = rendered.rstrip("0").rstrip(".")
    return rendered


def _canonical_raw_row_value(column: str, value: object) -> str:
    if column == "stock_id":
        return _normalize_stock_id(value)
    if column == "revenue_period":
        return _digits(value, 6)
    if column == "source_table_date":
        return _digits(value, 8)
    if column == "market":
        return _payload_value(value).lower()
    if column == "source_market_name":
        return _payload_value(value).upper()
    if column in RAW_ROW_NUMERIC_COLUMNS:
        return _canonical_numeric_value(value)
    if column in RAW_ROW_BOOLEAN_COLUMNS:
        text = _payload_value(value).lower()
        if text not in {"true", "false"}:
            raise RuntimeError(
                f"monthly revenue canonical boolean value is invalid: {column}={text}"
            )
        return text
    return _payload_value(value)


def canonical_monthly_revenue_raw_row_sha256(row: object) -> str:
    """Hash one normalized raw row's exact source identity and business payload."""
    if isinstance(row, pd.Series):
        missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(row.index))
        getter = row.__getitem__
    elif isinstance(row, dict):
        missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(row))
        getter = row.__getitem__
    else:
        available = set(getattr(row, "_fields", ()))
        missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - available)
        getter = lambda column: getattr(row, column)
    if missing:
        raise RuntimeError(
            f"monthly revenue raw-row canonical hash is missing columns: {missing}"
        )
    values = [
        _canonical_raw_row_value(column, getter(column))
        for column in RAW_ROW_CANONICAL_COLUMNS
    ]
    return _canonical_json_sha256(
        [
            MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION,
            list(RAW_ROW_CANONICAL_COLUMNS),
            values,
        ]
    )


def _normalize_registry_semantics(registry: pd.DataFrame) -> pd.DataFrame:
    required = set(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS)
    missing = sorted(required - set(registry.columns))
    if missing:
        raise RuntimeError(
            f"monthly revenue cross-market registry canonical hash is missing columns: {missing}"
        )
    normalized = registry.loc[
        :, list(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS)
    ].copy()
    for column in normalized.columns:
        normalized[column] = normalized[column].map(_payload_value)
    normalized["stock_id"] = normalized["stock_id"].map(_normalize_stock_id)
    normalized["revenue_period"] = normalized["revenue_period"].map(
        lambda value: _digits(value, 6)
    )
    for column in (
        "earlier_source_table_date",
        "later_source_table_date",
        "official_market_transition_date",
        "canonical_source_table_date",
    ):
        normalized[column] = normalized[column].map(lambda value: _digits(value, 8))
    for column in ("earlier_market", "later_market"):
        normalized[column] = normalized[column].str.lower()
    for column in ("earlier_source_market_name", "later_source_market_name"):
        normalized[column] = normalized[column].str.upper()
    normalized["formal_model_use_allowed"] = normalized[
        "formal_model_use_allowed"
    ].str.lower()
    return normalized.sort_values(
        list(CROSS_MARKET_RESOLUTION_REGISTRY_SORT_KEYS), kind="mergesort"
    ).reset_index(drop=True)


def cross_market_resolution_registry_canonical_sha256(
    registry: pd.DataFrame,
) -> str:
    """Hash fixed semantics including row bindings; free-form notes are excluded."""
    normalized = _normalize_registry_semantics(registry)
    rows = normalized.loc[
        :, list(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS)
    ].values.tolist()
    return _canonical_json_sha256(
        [
            MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION,
            list(CROSS_MARKET_RESOLUTION_REGISTRY_CANONICAL_COLUMNS),
            rows,
        ]
    )


def _lexical_git_worktree_root(path: Path) -> Path | None:
    lexical = Path(os.path.abspath(path))
    for candidate in (lexical.parent, *lexical.parent.parents):
        if os.path.lexists(candidate / ".git"):
            return candidate
    return None


def _path_has_reparse_identity(path: Path) -> bool:
    metadata = os.lstat(path)
    if stat.S_ISLNK(metadata.st_mode):
        return True
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    return bool(getattr(metadata, "st_file_attributes", 0) & reparse_flag)


def _clean_tracked_git_blob_sha256(path: Path) -> str | None:
    lexical_source = Path(os.path.abspath(path))
    lexical_repo_root = _lexical_git_worktree_root(lexical_source)
    if lexical_repo_root is None:
        return None
    try:
        relative_path = lexical_source.relative_to(lexical_repo_root)
    except ValueError as exc:
        raise RuntimeError(
            "monthly revenue history lexical path is outside its Git worktree: "
            f"{lexical_source}"
        ) from exc
    cursor = lexical_repo_root
    for component in relative_path.parts:
        cursor = cursor / component
        try:
            has_reparse_identity = _path_has_reparse_identity(cursor)
        except OSError as exc:
            raise RuntimeError(
                "monthly revenue history lexical path cannot be inspected: "
                f"{cursor}"
            ) from exc
        if has_reparse_identity:
            raise RuntimeError(
                "monthly revenue history path must not traverse a symbolic link or "
                f"reparse point: {cursor}"
            )
    resolved = lexical_source.resolve(strict=True)
    resolved_repo_root = lexical_repo_root.resolve(strict=True)
    try:
        resolved.relative_to(resolved_repo_root)
    except ValueError as exc:
        raise RuntimeError(
            "monthly revenue history resolved path escapes its Git worktree: "
            f"{lexical_source}"
        ) from exc
    try:
        repo_result = subprocess.run(
            ["git", "-C", str(lexical_repo_root), "rev-parse", "--show-toplevel"],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
        )
    except FileNotFoundError:
        raise RuntimeError("Git is unavailable for tracked monthly revenue history")
    if repo_result.returncode != 0:
        raise RuntimeError(
            "monthly revenue history Git worktree cannot be resolved: "
            f"{lexical_repo_root}; exit_code={repo_result.returncode}"
        )
    repo_root = Path(repo_result.stdout.strip()).resolve(strict=True)
    if not os.path.samefile(repo_root, resolved_repo_root):
        raise RuntimeError(
            "monthly revenue history lexical and Git worktree roots differ: "
            f"lexical={lexical_repo_root}; git={repo_root}"
        )
    repo_relative = relative_path.as_posix()
    tracked_result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "ls-files",
            "--stage",
            "--error-unmatch",
            "--",
            repo_relative,
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
    )
    if tracked_result.returncode != 0:
        raise RuntimeError(
            "monthly revenue history path is untracked in Git repository: "
            f"{repo_relative}"
        )
    index_rows = [line for line in tracked_result.stdout.splitlines() if line.strip()]
    if len(index_rows) != 1:
        raise RuntimeError(
            "monthly revenue history Git index must contain exactly one stage-0 entry: "
            f"{repo_relative}"
        )
    index_metadata = index_rows[0].split("\t", 1)[0].split()
    if (
        len(index_metadata) != 3
        or index_metadata[0] != "100644"
        or index_metadata[2] != "0"
        or not re.fullmatch(r"[0-9a-f]{40,64}", index_metadata[1])
        or set(index_metadata[1]) == {"0"}
    ):
        raise RuntimeError(
            "monthly revenue history Git index entry must be a resolved stage-0 "
            "100644 file: "
            f"{repo_relative}"
        )
    index_oid = index_metadata[1]
    head_result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "--no-replace-objects",
            "rev-parse",
            "--verify",
            f"HEAD:{repo_relative}",
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
    )
    if head_result.returncode != 0:
        raise RuntimeError(
            "monthly revenue history HEAD blob cannot be resolved: "
            f"{repo_relative}; exit_code={head_result.returncode}"
        )
    head_oid = head_result.stdout.strip().lower()
    if head_oid != index_oid:
        raise RuntimeError(
            "monthly revenue history Git index differs from HEAD: "
            f"{repo_relative}"
        )
    working_result = subprocess.run(
        [
            "git",
            "-C",
            str(repo_root),
            "hash-object",
            f"--path={repo_relative}",
            str(resolved),
        ],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="utf-8",
    )
    if working_result.returncode != 0:
        raise RuntimeError(
            "monthly revenue history working-tree blob cannot be resolved: "
            f"{repo_relative}; exit_code={working_result.returncode}"
        )
    working_oid = working_result.stdout.strip().lower()
    if working_oid != index_oid:
        raise RuntimeError(
            "monthly revenue history working tree differs from Git index: "
            f"{repo_relative}"
        )
    try:
        process = subprocess.Popen(
            [
                "git",
                "-C",
                str(repo_root),
                "--no-replace-objects",
                "cat-file",
                "blob",
                index_oid,
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("Git became unavailable while reading monthly revenue blob") from exc
    digest = hashlib.sha256()
    if process.stdout is None or process.stderr is None:
        process.kill()
        raise RuntimeError("monthly revenue history Git blob pipes are unavailable")
    for chunk in iter(lambda: process.stdout.read(1024 * 1024), b""):
        digest.update(chunk)
    error_text = process.stderr.read().decode("utf-8", errors="replace").strip()
    returncode = process.wait()
    if returncode != 0:
        raise RuntimeError(
            "monthly revenue history Git blob cannot be read: "
            f"{repo_relative}; exit_code={returncode}; stderr={error_text}"
        )
    return digest.hexdigest()


def monthly_revenue_history_blob_sha256(path: Path) -> str:
    tracked_git_sha = _clean_tracked_git_blob_sha256(path)
    if tracked_git_sha is not None:
        return tracked_git_sha
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_monthly_revenue_history_table_sha256(frame: pd.DataFrame) -> str:
    missing = sorted(
        set(CANONICAL_MONTHLY_REVENUE_HISTORY_BINDING_COLUMNS) - set(frame.columns)
    )
    if missing:
        raise RuntimeError(
            f"canonical monthly revenue history binding is missing columns: {missing}"
        )
    canonical = frame.loc[
        :, list(CANONICAL_MONTHLY_REVENUE_HISTORY_BINDING_COLUMNS)
    ].copy()
    for column in canonical.columns:
        canonical[column] = canonical[column].map(_payload_value)
    canonical["stock_id"] = canonical["stock_id"].map(_normalize_stock_id)
    canonical["revenue_period"] = canonical["revenue_period"].map(
        lambda value: _digits(value, 6)
    )
    canonical["canonical_source_table_date"] = canonical[
        "canonical_source_table_date"
    ].map(lambda value: _digits(value, 8))
    canonical["source_row_canonical_sha256"] = canonical[
        "source_row_canonical_sha256"
    ].str.lower()
    if canonical.duplicated(list(CANONICAL_MONTHLY_REVENUE_HISTORY_SORT_KEYS)).any():
        raise RuntimeError("canonical monthly revenue history binding repeats a stock-period")
    canonical = canonical.sort_values(
        list(CANONICAL_MONTHLY_REVENUE_HISTORY_SORT_KEYS), kind="mergesort"
    ).reset_index(drop=True)
    rows = canonical.values.tolist()
    return _canonical_json_sha256(
        [
            MONTHLY_REVENUE_LINEAGE_CANONICAL_JSON_VERSION,
            list(CANONICAL_MONTHLY_REVENUE_HISTORY_BINDING_COLUMNS),
            rows,
        ]
    )


def load_cross_market_resolutions(path: Path = RESOLUTION_CSV) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing monthly revenue cross-market resolution registry: {path}")
    registry = pd.read_csv(path, dtype=str, keep_default_na=False)
    if tuple(registry.columns) != RESOLUTION_COLUMNS:
        raise RuntimeError(
            "monthly revenue cross-market resolution registry schema mismatch: "
            f"expected={list(RESOLUTION_COLUMNS)}; actual={list(registry.columns)}"
        )
    if registry.empty:
        raise RuntimeError("monthly revenue cross-market resolution registry is empty")

    registry = registry.copy()
    registry["stock_id"] = registry["stock_id"].map(_normalize_stock_id)
    registry["revenue_period"] = registry["revenue_period"].map(lambda value: _digits(value, 6))
    for column in (
        "earlier_source_table_date",
        "later_source_table_date",
        "official_market_transition_date",
        "canonical_source_table_date",
    ):
        registry[column] = registry[column].map(lambda value: _digits(value, 8))
    for column in ("earlier_market", "later_market"):
        registry[column] = registry[column].astype(str).str.strip().str.lower()
    for column in ("earlier_source_market_name", "later_source_market_name"):
        registry[column] = registry[column].astype(str).str.strip().str.upper()
    for column in (
        "earlier_source_kind",
        "earlier_source_url",
        "earlier_source_file",
        "later_source_kind",
        "later_source_url",
        "later_source_file",
    ):
        registry[column] = registry[column].astype(str).str.strip()
    for column in (
        "earlier_raw_row_canonical_sha256",
        "later_raw_row_canonical_sha256",
        "canonical_row_canonical_sha256",
    ):
        registry[column] = registry[column].astype(str).str.strip().str.lower()

    if registry[list(KEY_COLUMNS)].eq("").any(axis=None):
        raise RuntimeError("monthly revenue cross-market resolution registry has blank keys")
    if registry["resolution_id"].astype(str).str.strip().eq("").any():
        raise RuntimeError("monthly revenue cross-market resolution registry has blank resolution IDs")
    if registry["resolution_id"].duplicated().any():
        raise RuntimeError("monthly revenue cross-market resolution registry repeats a resolution ID")
    registered_identity_columns = [
        column
        for prefix in ("earlier", "later")
        for column in (
            f"{prefix}_market",
            f"{prefix}_source_market_name",
            f"{prefix}_source_table_date",
            f"{prefix}_source_kind",
            f"{prefix}_source_url",
            f"{prefix}_source_file",
        )
    ]
    if registry[registered_identity_columns].eq("").any(axis=None):
        raise RuntimeError(
            "monthly revenue cross-market resolution registry has blank source identities"
        )
    for column in (
        "earlier_raw_row_canonical_sha256",
        "later_raw_row_canonical_sha256",
        "canonical_row_canonical_sha256",
    ):
        if not registry[column].map(lambda value: bool(SHA256_PATTERN.fullmatch(value))).all():
            raise RuntimeError(
                f"monthly revenue cross-market resolution registry has invalid {column}"
            )
    if registry.duplicated(list(KEY_COLUMNS)).any():
        raise RuntimeError("monthly revenue cross-market resolution registry repeats a stock-period key")
    if not registry["model_id"].eq(MODEL_ID).all():
        raise RuntimeError("monthly revenue cross-market resolution registry has a foreign model owner")
    if not registry["resolution_status"].eq(
        "registered_equal_payload_cross_market_mirror"
    ).all():
        raise RuntimeError("monthly revenue cross-market resolution registry has an invalid status")
    if not registry["canonicalization_policy"].eq(
        "earliest_official_source_table_date"
    ).all():
        raise RuntimeError("monthly revenue cross-market resolution registry has an invalid policy")
    if registry["formal_model_use_allowed"].astype(str).str.lower().ne("false").any():
        raise RuntimeError("monthly revenue cross-market resolutions must remain research-only")
    if not registry["evidence_url"].astype(str).str.startswith("https://").all():
        raise RuntimeError("monthly revenue cross-market resolution evidence must use HTTPS")

    for row in registry.itertuples(index=False):
        if row.earlier_market == row.later_market:
            raise RuntimeError(f"registered resolution repeats a market: {row.stock_id}/{row.revenue_period}")
        if row.earlier_source_market_name == row.later_source_market_name:
            raise RuntimeError(
                f"registered resolution repeats a source market: {row.stock_id}/{row.revenue_period}"
            )
        if not row.earlier_source_url.startswith("https://") or not row.later_source_url.startswith(
            "https://"
        ):
            raise RuntimeError(
                f"registered resolution source URLs must use HTTPS: "
                f"{row.stock_id}/{row.revenue_period}"
            )
        if not row.earlier_source_file.startswith(
            "data/monthly_revenue_history/raw/"
        ) or not row.later_source_file.startswith("data/monthly_revenue_history/raw/"):
            raise RuntimeError(
                f"registered resolution source files must be canonical repo-relative raw paths: "
                f"{row.stock_id}/{row.revenue_period}"
            )
        if not (
            row.earlier_source_table_date
            < row.official_market_transition_date
            <= row.later_source_table_date
        ):
            raise RuntimeError(
                f"registered resolution has invalid transition chronology: "
                f"{row.stock_id}/{row.revenue_period}"
            )
        if row.canonical_source_table_date != min(
            row.earlier_source_table_date, row.later_source_table_date
        ):
            raise RuntimeError(
                f"registered resolution does not canonicalize to the earliest source date: "
                f"{row.stock_id}/{row.revenue_period}"
            )
        canonical_binding = (
            row.earlier_raw_row_canonical_sha256
            if row.canonical_source_table_date == row.earlier_source_table_date
            else row.later_raw_row_canonical_sha256
        )
        if row.canonical_row_canonical_sha256 != canonical_binding:
            raise RuntimeError(
                f"registered resolution canonical row hash does not match its selected raw side: "
                f"{row.stock_id}/{row.revenue_period}"
            )
    return registry


def resolve_monthly_revenue_cross_market_mirrors(
    frame: pd.DataFrame,
    resolution_path: Path = RESOLUTION_CSV,
    *,
    observation_cutoff_date: str | None = None,
) -> pd.DataFrame:
    required = set(KEY_COLUMNS + SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS)
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"monthly revenue cross-market resolver is missing columns: {missing}")

    cutoff = None
    if observation_cutoff_date is not None:
        cutoff = str(observation_cutoff_date).strip()
        if len(cutoff) != 8 or not cutoff.isdigit():
            raise RuntimeError(
                "monthly revenue observation cutoff must be exactly YYYYMMDD"
            )

    # Load the registry even when the input appears unique. A registered mirror is
    # evidence about a required raw pair, so a missing earlier or later row must
    # never silently turn into an apparently unique history row. For a historical
    # observation projection, a resolution becomes applicable only after both raw
    # sides were available by the cutoff; a future mirror must not rewrite the
    # earlier as-of view.
    registry = load_cross_market_resolutions(resolution_path)
    if cutoff is not None:
        registry = registry.loc[
            registry["earlier_source_table_date"].le(cutoff)
            & registry["later_source_table_date"].le(cutoff)
        ].copy()
    registrations = {
        (str(row.stock_id), str(row.revenue_period)): row
        for row in registry.itertuples(index=False)
    }

    resolved = frame.copy()
    resolved["stock_id"] = resolved["stock_id"].map(_normalize_stock_id)
    resolved["revenue_period"] = resolved["revenue_period"].map(lambda value: _digits(value, 6))
    resolved["source_table_date"] = resolved["source_table_date"].map(
        lambda value: _digits(value, 8)
    )
    if cutoff is not None:
        resolved = resolved.loc[resolved["source_table_date"].le(cutoff)].copy()
    resolved["market"] = resolved["market"].astype(str).str.strip().str.lower()
    resolved["source_market_name"] = (
        resolved["source_market_name"].astype(str).str.strip().str.upper()
    )
    for column in ("source_kind", "source_url", "source_file"):
        resolved[column] = resolved[column].astype(str).str.strip()
    if resolved[list(KEY_COLUMNS + SOURCE_IDENTITY_COLUMNS)].eq("").any(axis=None):
        raise RuntimeError("monthly revenue history has blank duplicate-resolution identity fields")
    resolved["cross_market_resolution_id"] = ""
    if resolved.empty:
        resolved["source_row_canonical_sha256"] = pd.Series(dtype=str)
    else:
        resolved["source_row_canonical_sha256"] = resolved.apply(
            canonical_monthly_revenue_raw_row_sha256, axis=1
        )
    resolved["canonical_source_table_date"] = resolved["source_table_date"]

    duplicate_mask = resolved.duplicated(list(KEY_COLUMNS), keep=False)
    duplicate_keys = {
        (str(row.stock_id), str(row.revenue_period))
        for row in resolved.loc[duplicate_mask, list(KEY_COLUMNS)]
        .drop_duplicates()
        .itertuples(index=False)
    }
    unregistered_keys = sorted(duplicate_keys - set(registrations))
    if unregistered_keys:
        raise RuntimeError(
            f"unregistered monthly revenue duplicate stock-period: {unregistered_keys[0][0]}/"
            f"{unregistered_keys[0][1]}"
        )

    drop_indices: list[object] = []
    for normalized_key, registration in registrations.items():
        group = resolved.loc[
            resolved["stock_id"].eq(normalized_key[0])
            & resolved["revenue_period"].eq(normalized_key[1])
        ]
        key_text = f"{normalized_key[0]}/{normalized_key[1]}"
        if len(group) != 2:
            raise RuntimeError(
                f"registered monthly revenue mirror must contain its complete exact two-row raw pair: "
                f"{key_text}; actual_rows={len(group)}"
            )
        if group["market"].nunique(dropna=False) != len(group):
            raise RuntimeError(f"same-market monthly revenue duplicate is forbidden: {key_text}")
        if group["source_market_name"].nunique(dropna=False) != len(group):
            raise RuntimeError(f"same source-market monthly revenue duplicate is forbidden: {key_text}")

        expected_identities = {
            (
                registration.earlier_market,
                registration.earlier_source_market_name,
                registration.earlier_source_table_date,
                registration.earlier_source_kind,
                registration.earlier_source_url,
                registration.earlier_source_file,
            ),
            (
                registration.later_market,
                registration.later_source_market_name,
                registration.later_source_table_date,
                registration.later_source_kind,
                registration.later_source_url,
                registration.later_source_file,
            ),
        }
        actual_identities = {
            tuple(str(getattr(row, column)) for column in SOURCE_IDENTITY_COLUMNS)
            for row in group.itertuples(index=False)
        }
        if actual_identities != expected_identities:
            raise RuntimeError(
                f"registered monthly revenue mirror source identities mismatch: {key_text}; "
                f"expected={sorted(expected_identities)}; actual={sorted(actual_identities)}"
            )

        conflicts = [
            column
            for column in BUSINESS_PAYLOAD_COLUMNS
            if group[column].map(_payload_value).nunique(dropna=False) != 1
        ]
        if conflicts:
            raise RuntimeError(
                f"registered monthly revenue cross-market payload conflict: {key_text}; "
                f"columns={conflicts}"
            )

        earlier_identity = (
            registration.earlier_market,
            registration.earlier_source_market_name,
            registration.earlier_source_table_date,
            registration.earlier_source_kind,
            registration.earlier_source_url,
            registration.earlier_source_file,
        )
        later_identity = (
            registration.later_market,
            registration.later_source_market_name,
            registration.later_source_table_date,
            registration.later_source_kind,
            registration.later_source_url,
            registration.later_source_file,
        )
        actual_hashes = {
            tuple(str(getattr(row, column)) for column in SOURCE_IDENTITY_COLUMNS): str(
                row.source_row_canonical_sha256
            )
            for row in group.itertuples(index=False)
        }
        for side, identity, expected_hash in (
            (
                "earlier",
                earlier_identity,
                registration.earlier_raw_row_canonical_sha256,
            ),
            (
                "later",
                later_identity,
                registration.later_raw_row_canonical_sha256,
            ),
        ):
            actual_hash = actual_hashes.get(identity, "")
            if actual_hash != expected_hash:
                raise RuntimeError(
                    f"registered monthly revenue {side} raw-row canonical hash mismatch: "
                    f"{key_text}; actual={actual_hash}; expected={expected_hash}"
                )

        canonical_identity = earlier_identity
        canonical_mask = pd.Series(True, index=group.index)
        for column, expected in zip(SOURCE_IDENTITY_COLUMNS, canonical_identity):
            canonical_mask &= group[column].eq(expected)
        canonical = group.loc[canonical_mask]
        if len(canonical) != 1:
            raise RuntimeError(
                f"registered monthly revenue mirror has no unique canonical earliest row: {key_text}"
            )
        if str(canonical.iloc[0]["source_table_date"]) != registration.canonical_source_table_date:
            raise RuntimeError(
                f"registered monthly revenue mirror canonical identity/date mismatch: {key_text}"
            )
        canonical_hash = str(canonical.iloc[0]["source_row_canonical_sha256"])
        if canonical_hash != registration.canonical_row_canonical_sha256:
            raise RuntimeError(
                f"registered monthly revenue canonical raw-row hash mismatch: {key_text}; "
                f"actual={canonical_hash}; expected={registration.canonical_row_canonical_sha256}"
            )
        resolved.loc[canonical.index, "cross_market_resolution_id"] = (
            registration.resolution_id
        )
        resolved.loc[canonical.index, "canonical_source_table_date"] = (
            registration.canonical_source_table_date
        )
        drop_indices.extend(index for index in group.index if index != canonical.index[0])

    output = resolved.drop(index=drop_indices).reset_index(drop=True)
    if output.duplicated(list(KEY_COLUMNS)).any():
        raise RuntimeError("monthly revenue cross-market resolution left duplicate stock-period rows")
    return output


def load_canonical_monthly_revenue_history(
    history_path: Path,
    resolution_path: Path = RESOLUTION_CSV,
    *,
    observation_cutoff_date: str | None = None,
) -> pd.DataFrame:
    """Return the model-owned monthly history view after fail-closed mirror resolution."""
    if not history_path.is_file():
        raise RuntimeError(f"missing monthly revenue history: {history_path}")
    history = pd.read_csv(
        history_path,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    return resolve_monthly_revenue_cross_market_mirrors(
        history,
        resolution_path,
        observation_cutoff_date=observation_cutoff_date,
    )
