from __future__ import annotations

import hashlib
import io
import json
import os
import re
import subprocess
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
ROOT = Path(__file__).resolve().parents[1]
LIVE_SOURCE_REVISION = "working_tree"

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


def canonical_text_sha256(payload: bytes) -> str:
    text = payload.decode("utf-8-sig")
    canonical_text = text.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(canonical_text.encode("utf-8")).hexdigest()


def resolve_pinned_canonical_source_revision(
    root: Path,
    artifact_path: str,
    declared_sha256: str,
    *,
    trusted_ref: str = "HEAD",
    allow_live: bool = True,
) -> tuple[bytes, str]:
    """Resolve a pinned source from the live payload or immutable HEAD history."""

    relative = Path(artifact_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise RuntimeError(f"pinned source artifact path is unsafe: {artifact_path}")
    if re.fullmatch(r"[0-9a-f]{64}", declared_sha256) is None:
        raise RuntimeError(
            f"pinned source SHA-256 is malformed: artifact={artifact_path} "
            f"sha256={declared_sha256!r}"
        )
    current_path = root / relative
    current_payload: bytes | None = None
    current_sha = "<missing>"
    if current_path.is_file():
        try:
            current_payload = current_path.read_bytes()
            current_sha = canonical_text_sha256(current_payload)
        except (OSError, UnicodeError):
            current_payload = None
    if allow_live and current_payload is not None and current_sha == declared_sha256:
        head_payload = subprocess.run(
            ["git", "show", f"HEAD:{relative.as_posix()}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        current_is_committed_at_head = False
        if head_payload.returncode == 0:
            try:
                current_is_committed_at_head = (
                    canonical_text_sha256(head_payload.stdout) == current_sha
                )
            except UnicodeError:
                current_is_committed_at_head = False
        if not current_is_committed_at_head:
            return current_payload, LIVE_SOURCE_REVISION

    history = subprocess.run(
        [
            "git",
            "log",
            "--format=%H",
            trusted_ref,
            "--",
            relative.as_posix(),
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if history.returncode != 0:
        detail = history.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            "pinned source revision history is unavailable: "
            f"artifact={artifact_path} trusted_ref={trusted_ref} "
            f"detail={detail or '<none>'}"
        )
    commits = [
        value.strip()
        for value in history.stdout.decode("utf-8", errors="replace").splitlines()
        if value.strip()
    ]
    for commit_sha in commits:
        revision = subprocess.run(
            ["git", "show", f"{commit_sha}:{relative.as_posix()}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if revision.returncode != 0:
            continue
        try:
            revision_sha = canonical_text_sha256(revision.stdout)
        except UnicodeError:
            continue
        if revision_sha == declared_sha256:
            return revision.stdout, commit_sha
    raise RuntimeError(
        "pinned source revision is not reconstructable: "
        f"artifact={artifact_path} expected_sha256={declared_sha256} "
        f"current_sha256={current_sha} trusted_ref={trusted_ref} "
        f"searched_commits={len(commits)}"
    )


def committed_artifact_revision(
    root: Path,
    artifact_path: str,
    payload: bytes,
    *,
    trusted_ref: str,
) -> str | None:
    relative = Path(artifact_path)
    committed = subprocess.run(
        ["git", "show", f"HEAD:{relative.as_posix()}"],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if committed.returncode != 0:
        return None
    try:
        if canonical_text_sha256(committed.stdout) != canonical_text_sha256(payload):
            return None
    except UnicodeError:
        return None
    revision = subprocess.run(
        [
            "git",
            "log",
            "-1",
            "--format=%H",
            "HEAD",
            "--",
            relative.as_posix(),
        ],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        text=True,
    )
    commit_sha = revision.stdout.strip() if revision.returncode == 0 else ""
    if not commit_sha:
        raise RuntimeError(
            "committed theme artifact revision cannot be identified: "
            f"artifact={artifact_path}"
        )
    trusted = subprocess.run(
        ["git", "merge-base", "--is-ancestor", commit_sha, trusted_ref],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if trusted.returncode != 0:
        raise RuntimeError(
            "committed theme artifact revision is outside trusted ref ancestry: "
            f"artifact={artifact_path} revision={commit_sha} "
            f"trusted_ref={trusted_ref}"
        )
    return commit_sha


def source_precedes_consumer(
    root: Path,
    source_revision: str,
    consumer_revision: str,
) -> bool:
    completed = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_revision, consumer_revision],
        cwd=root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return completed.returncode == 0


def read_csv_payload(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(
        io.StringIO(payload.decode("utf-8-sig")),
        dtype=str,
        keep_default_na=False,
    )


def warrant_projection_parity_errors(
    stock_id: str,
    published: str,
    candidate_signals: dict[str, set[str]],
    official_signals: dict[str, set[str]],
) -> list[str]:
    errors: list[str] = []
    expected_set = candidate_signals.get(stock_id, {""})
    if len(expected_set) != 1 or published not in expected_set:
        errors.append(
            "stock_layer warrant projection differs from all_candidates: "
            f"stock_id={stock_id} published={published!r} "
            f"candidate={sorted(expected_set)}"
        )
    if stock_id in candidate_signals:
        official_set = official_signals.get(stock_id, {""})
        if len(official_set) != 1 or published not in official_set:
            errors.append(
                "stock_layer warrant projection differs from official warrant: "
                f"stock_id={stock_id} published={published!r} "
                f"official={sorted(official_set)}"
            )
    return errors


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
    trusted_ref = os.environ.get("BASE_SHA", "").strip() or "HEAD"
    declared_official_sha = official_sha
    resolved_official = read_csv(WARRANT_FLOW_CSV)
    stock_revision: str | None = None
    stock_revision_invalid = False
    if not stocks.empty and STOCK_LAYER_CSV.is_file():
        try:
            stock_revision = committed_artifact_revision(
                ROOT,
                STOCK_LAYER_CSV.as_posix(),
                STOCK_LAYER_CSV.read_bytes(),
                trusted_ref=trusted_ref,
            )
        except (OSError, RuntimeError, UnicodeError) as exc:
            errors.append(f"stock_layer committed revision cannot be validated: {exc}")
            stock_revision_invalid = True
    if not stocks.empty and "warrant_flow_official_source_sha256" in stocks.columns:
        declared_artifacts = {
            str(value).strip()
            for value in stocks.get(
                "warrant_flow_official_source_artifact", pd.Series(dtype=str)
            )
        }
        declared_shas = {
            str(value).strip()
            for value in stocks["warrant_flow_official_source_sha256"]
        }
        expected_artifact = WARRANT_FLOW_CSV.as_posix()
        if declared_artifacts != {expected_artifact}:
            errors.append(
                "stock_layer official warrant source artifact is not singular canonical: "
                f"expected={expected_artifact!r} actual={sorted(declared_artifacts)}"
            )
        if len(declared_shas) != 1:
            errors.append(
                "stock_layer official warrant source revision is not singular: "
                f"actual={sorted(declared_shas)}"
            )
        elif declared_artifacts == {expected_artifact} and not stock_revision_invalid:
            declared_official_sha = next(iter(declared_shas))
            try:
                payload, official_revision = resolve_pinned_canonical_source_revision(
                    ROOT,
                    expected_artifact,
                    declared_official_sha,
                    trusted_ref=trusted_ref,
                    allow_live=stock_revision is None,
                )
                if stock_revision is None and official_revision != LIVE_SOURCE_REVISION:
                    errors.append(
                        "live stock_layer cannot consume a historical official warrant "
                        f"revision: source_revision={official_revision}"
                    )
                elif stock_revision is not None and (
                    official_revision == LIVE_SOURCE_REVISION
                    or not source_precedes_consumer(
                        ROOT,
                        official_revision,
                        stock_revision,
                    )
                ):
                    errors.append(
                        "official warrant revision is not available before stock_layer: "
                        f"source_revision={official_revision} "
                        f"stock_revision={stock_revision}"
                    )
                resolved_official = read_csv_payload(payload)
                missing_official_columns = sorted(
                    {"stock_id", "warrant_flow_signal"}
                    - set(resolved_official.columns)
                )
                if missing_official_columns:
                    errors.append(
                        "resolved official warrant source is missing columns: "
                        + ",".join(missing_official_columns)
                    )
                    resolved_official = pd.DataFrame()
                if resolved_official.empty:
                    errors.append(
                        "resolved official warrant source is empty; as-of cannot be verified"
                    )
                if not {"date", "signal_date"}.intersection(
                    resolved_official.columns
                ):
                    errors.append(
                        "resolved official warrant source has no as-of column"
                    )
                    resolved_official = pd.DataFrame()
            except (RuntimeError, UnicodeError, pd.errors.ParserError) as exc:
                errors.append(
                    "stock_layer official warrant source revision cannot be validated: "
                    f"{exc}"
                )
                resolved_official = pd.DataFrame()
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
        f"warrant_official_parity_source_sha256: `{declared_official_sha}`",
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
            official = resolved_official
            candidate_signals: dict[str, set[str]] = {}
            if not candidates.empty and {"stock_id", "warrant_flow_signal"} <= set(candidates.columns):
                for stock_id, part in candidates.groupby("stock_id", dropna=False):
                    candidate_signals[str(stock_id)] = set(
                        part["warrant_flow_signal"].astype(str)
                    )
            official_signals: dict[str, set[str]] = {}
            if not official.empty and {"stock_id", "warrant_flow_signal"} <= set(official.columns):
                duplicate_official_ids = sorted(
                    {
                        str(stock_id)
                        for stock_id, count in official["stock_id"]
                        .astype(str)
                        .value_counts(dropna=False)
                        .items()
                        if count > 1
                    }
                )
                if duplicate_official_ids:
                    errors.append(
                        "resolved official warrant source has duplicate stock_id rows: "
                        + ",".join(duplicate_official_ids)
                    )
                for stock_id, part in official.groupby("stock_id", dropna=False):
                    official_signals[str(stock_id)] = set(
                        part["warrant_flow_signal"].astype(str)
                    )
            official_dates = {
                str(row.get("date", "") or row.get("signal_date", "")).strip()
                for _, row in official.iterrows()
                if str(row.get("date", "") or row.get("signal_date", "")).strip()
            }
            if not official.empty:
                rows_without_as_of = [
                    str(row_number)
                    for row_number, (_, row) in enumerate(
                        official.iterrows(), start=2
                    )
                    if not str(
                        row.get("date", "") or row.get("signal_date", "")
                    ).strip()
                ]
                if rows_without_as_of:
                    errors.append(
                        "resolved official warrant source rows have no as-of: "
                        + ",".join(rows_without_as_of)
                    )
            if len(official_dates) > 1:
                errors.append(
                    "resolved official warrant source has multiple as-of dates: "
                    + ",".join(sorted(official_dates))
                )
            for source_date in sorted(official_dates):
                if re.fullmatch(r"[0-9]{8}", source_date) is None:
                    errors.append(
                        "resolved official warrant source has invalid as-of: "
                        f"{source_date!r}"
                    )
            for _, row in stocks.iterrows():
                stock_id = str(row["stock_id"])
                published = str(row["warrant_flow_signal"])
                errors.extend(
                    warrant_projection_parity_errors(
                        stock_id,
                        published,
                        candidate_signals,
                        official_signals,
                    )
                )
                if len(official_dates) == 1:
                    expected_as_of = next(iter(official_dates))
                    actual_as_of = str(row.get("warrant_flow_as_of", "")).strip()
                    if actual_as_of != expected_as_of:
                        errors.append(
                            "stock_layer warrant_flow_as_of differs from pinned official "
                            f"revision: stock_id={stock_id} expected={expected_as_of!r} "
                            f"actual={actual_as_of!r}"
                        )
                signal_date = str(row.get("signal_date", "")).strip()
                actual_as_of = str(row.get("warrant_flow_as_of", "")).strip()
                if (
                    actual_as_of
                    and signal_date
                    and re.fullmatch(r"[0-9]{8}", actual_as_of)
                    and re.fullmatch(r"[0-9]{8}", signal_date)
                    and actual_as_of > signal_date
                ):
                    errors.append(
                        "stock_layer warrant_flow_as_of is later than signal_date: "
                        f"stock_id={stock_id} signal_date={signal_date} "
                        f"warrant_flow_as_of={actual_as_of}"
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
