from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_PATHS = ROOT / "config" / "workspace_cleanup_protected_paths.csv"
REPORT_TIMEZONE = "Asia/Taipei"
MANIFEST_SCHEMA_VERSION = "1"
PLANNER_VERSION = "1"
OUTPUT_GLOBS = ("chatgpt_side_outputs*",)
SMALL_HASH_SUFFIXES = {".json", ".csv", ".md", ".txt"}
PDF_DATE_RE = re.compile(r"20\d{6}")
REPORT_KEY_DROP_TOKENS = {
    "branch",
    "clean",
    "contract",
    "current",
    "diagnostic",
    "final",
    "layout",
    "manual",
    "new",
    "official",
    "pdf",
    "postmerge",
    "preview",
    "replay",
    "repo",
    "requested",
    "rules",
    "source",
}


class PlannerError(RuntimeError):
    pass


@dataclass(frozen=True)
class ProtectedPath:
    path: str
    match_type: str
    path_required: bool
    hard_block: bool


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def run_git_status() -> str:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1"],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return result.stdout


def run_git_head() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return result.stdout.strip()


def load_protected_paths() -> list[ProtectedPath]:
    rows: list[ProtectedPath] = []
    if not PROTECTED_PATHS.exists():
        return rows
    with PROTECTED_PATHS.open("r", encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            path = str(row.get("path", "")).strip().replace("\\", "/")
            if not path:
                continue
            rows.append(
                ProtectedPath(
                    path=path,
                    match_type=str(row.get("match_type", "")).strip(),
                    path_required=str(row.get("path_required", "")).strip().lower() == "true",
                    hard_block=str(row.get("hard_block", "")).strip().lower() == "true",
                )
            )
    return rows


def matches_protected(rel_path: str, protected_rows: list[ProtectedPath]) -> tuple[bool, str]:
    normalized = rel_path.replace("\\", "/").lower().rstrip("/")
    for row in protected_rows:
        protected = row.path.lower().rstrip("/")
        if row.match_type == "exact" and normalized == protected:
            return True, row.path
        if row.match_type == "prefix" and (normalized == protected or normalized.startswith(protected.rstrip("/") + "/")):
            return True, row.path
    return False, ""


def is_reparse_point(path: Path) -> bool:
    try:
        st = os.lstat(path)
    except OSError as exc:
        raise PlannerError(f"cannot stat path: {path}: {exc}") from exc
    attrs = getattr(st, "st_file_attributes", 0)
    return path.is_symlink() or bool(attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def mtime_iso(ns: int) -> str:
    return datetime.fromtimestamp(ns / 1_000_000_000, tz=UTC).isoformat()


def hash_small_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan_tree(path: Path) -> tuple[list[dict[str, object]], list[str], list[str]]:
    details: list[dict[str, object]] = []
    permission_denied: list[str] = []
    reparse_points: list[str] = []

    def scan(current: Path) -> None:
        try:
            entries = sorted(os.scandir(current), key=lambda entry: entry.name.lower())
        except PermissionError:
            permission_denied.append(rel(current))
            return
        except OSError as exc:
            permission_denied.append(f"{rel(current)} ({exc})")
            return
        for entry in entries:
            child = Path(entry.path)
            child_rel = rel(child)
            try:
                if is_reparse_point(child):
                    reparse_points.append(child_rel)
                    details.append(
                        {
                            "relative_path": child_rel,
                            "size": 0,
                            "mtime_ns": 0,
                            "mtime_iso": "",
                            "is_dir": entry.is_dir(follow_symlinks=False),
                            "reparse_point": True,
                        }
                    )
                    continue
                st = entry.stat(follow_symlinks=False)
            except PermissionError:
                permission_denied.append(child_rel)
                continue
            except OSError as exc:
                permission_denied.append(f"{child_rel} ({exc})")
                continue
            is_dir = entry.is_dir(follow_symlinks=False)
            item: dict[str, object] = {
                "relative_path": child_rel,
                "size": 0 if is_dir else st.st_size,
                "mtime_ns": st.st_mtime_ns,
                "mtime_iso": mtime_iso(st.st_mtime_ns),
                "is_dir": is_dir,
            }
            if not is_dir and child.suffix.lower() in SMALL_HASH_SUFFIXES:
                try:
                    item["sha256"] = hash_small_file(child)
                except PermissionError:
                    permission_denied.append(child_rel)
            details.append(item)
            if is_dir:
                scan(child)

    scan(path)
    return details, permission_denied, reparse_points


def fingerprint_hash(details: list[dict[str, object]]) -> str:
    payload = json.dumps(details, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def pdf_report_key(pdf_rel_path: str) -> str:
    stem = Path(pdf_rel_path).stem
    kept: list[str] = []
    for token in stem.split("_"):
        lowered = token.lower()
        if not token:
            continue
        if PDF_DATE_RE.fullmatch(token):
            continue
        if PDF_DATE_RE.fullmatch(lowered.removeprefix("repo").removeprefix("requestedrepo")):
            continue
        if lowered.startswith("repo") and PDF_DATE_RE.fullmatch(lowered.removeprefix("repo")):
            continue
        if lowered in REPORT_KEY_DROP_TOKENS:
            continue
        kept.append(token)
    return "_".join(kept).strip("_") or stem


def pdf_source_date(pdf_rel_path: str) -> str:
    matches = PDF_DATE_RE.findall(pdf_rel_path)
    return max(matches) if matches else ""


def mark_latest_pdf_layout_baselines(rows: list[dict[str, object]], scan_summary: dict[str, object]) -> None:
    latest_by_report: dict[str, dict[str, object]] = {}
    for row in rows:
        for item in row.get("fingerprint_detail", []):
            pdf_rel_path = str(item.get("relative_path", ""))
            if not pdf_rel_path.lower().endswith(".pdf"):
                continue
            report_key = pdf_report_key(pdf_rel_path)
            if not report_key:
                continue
            candidate = {
                "report_key": report_key,
                "path": pdf_rel_path,
                "root_path": row.get("path", ""),
                "pdf_name": Path(pdf_rel_path).name,
                "source_date": pdf_source_date(pdf_rel_path),
                "mtime_ns": int(item.get("mtime_ns", 0) or 0),
            }
            current = latest_by_report.get(report_key)
            current_sort = (
                str(current.get("source_date", "")) if current else "",
                int(current.get("mtime_ns", 0) if current else 0),
                str(current.get("path", "")) if current else "",
            )
            candidate_sort = (
                str(candidate["source_date"]),
                int(candidate["mtime_ns"]),
                str(candidate["path"]),
            )
            if current is None or candidate_sort > current_sort:
                latest_by_report[report_key] = candidate

    baseline_paths = {str(item["path"]) for item in latest_by_report.values()}
    baseline_rows: dict[str, list[dict[str, object]]] = {}
    for item in latest_by_report.values():
        baseline_rows.setdefault(str(item["root_path"]), []).append(item)

    for row in rows:
        row_baselines = sorted(baseline_rows.get(str(row.get("path", "")), []), key=lambda item: str(item["report_key"]))
        row["layout_baseline_keep"] = bool(row_baselines)
        row["layout_baseline_report_keys"] = [str(item["report_key"]) for item in row_baselines]
        row["layout_baseline_pdf_names"] = [str(item["pdf_name"]) for item in row_baselines]
        row["layout_baseline_pdf_paths"] = [str(item["path"]) for item in row_baselines]
        if not row_baselines:
            continue
        if row.get("planned_action") in {"quarantine", "delete"}:
            row["planned_action"] = "keep"
            if row.get("classification") not in {"official_keep", "replay_evidence_keep", "protected_keep"}:
                row["classification"] = "comparison_evidence_keep"
        reason = str(row.get("evidence_reason", ""))
        if "layout_baseline_latest_pdf" not in reason:
            row["evidence_reason"] = f"{reason};layout_baseline_latest_pdf" if reason else "layout_baseline_latest_pdf"

    scan_summary["layout_baseline_report_count"] = len(latest_by_report)
    scan_summary["layout_baseline_pdf_count"] = len(baseline_paths)
    scan_summary["layout_baseline_roots"] = sorted(baseline_rows)


def classify_candidate(
    rel_path: str,
    details: list[dict[str, object]],
    protected_rows: list[ProtectedPath],
    descendant_permission_denied: bool,
    descendant_reparse: bool,
) -> tuple[str, str, str]:
    protected, protected_match = matches_protected(rel_path, protected_rows)
    if protected:
        return "protected_keep", "keep", f"protected_path:{protected_match}"
    if descendant_permission_denied:
        return "unknown_quarantine_candidate", "report_only", "descendant_permission_denied"
    if descendant_reparse:
        return "unknown_quarantine_candidate", "report_only", "descendant_reparse_point"

    file_count = sum(1 for item in details if not bool(item.get("is_dir")))
    dir_count = sum(1 for item in details if bool(item.get("is_dir")))
    name = Path(rel_path).name.lower()
    manifest_present = any("manifest" in Path(str(item.get("relative_path", ""))).name.lower() for item in details)
    pdf_count = sum(1 for item in details if str(item.get("relative_path", "")).lower().endswith(".pdf"))

    if file_count == 0 and dir_count == 0:
        return "stale_candidate", "delete", "empty_directory"
    if "official" in name:
        return "official_keep", "keep", "name_contains_official"
    if "replay" in name:
        return "replay_evidence_keep", "keep", "name_contains_replay"
    if "comparison" in name or "historical" in name:
        return "comparison_evidence_keep", "keep", "name_contains_comparison_or_historical"
    if "diagnostic" in name:
        return "diagnostic_candidate", "quarantine", "name_contains_diagnostic"
    if not manifest_present and pdf_count == 0:
        return "stale_candidate", "quarantine", "no_manifest_and_no_pdf"
    return "unknown_quarantine_candidate", "report_only", "insufficient_evidence"


def build_rows(protected_rows: list[ProtectedPath]) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows: list[dict[str, object]] = []
    scanned_roots: list[str] = []
    skipped_roots: list[dict[str, str]] = []
    protected_candidate_count = 0
    reparse_point_candidate_count = 0

    for pattern in OUTPUT_GLOBS:
        for candidate in sorted(ROOT.glob(pattern), key=lambda p: p.name.lower()):
            candidate_rel = rel(candidate)
            if candidate.name == "_workspace_quarantine" or candidate_rel.startswith("_workspace_quarantine/"):
                skipped_roots.append({"path": candidate_rel, "reason": "quarantine_root"})
                continue
            try:
                resolved = candidate.resolve(strict=False)
            except OSError as exc:
                skipped_roots.append({"path": candidate_rel, "reason": f"resolve_error:{exc}"})
                continue
            if ROOT.resolve(strict=False) not in (resolved, *resolved.parents):
                skipped_roots.append({"path": candidate_rel, "reason": "outside_repo"})
                continue
            if matches_protected(candidate_rel, protected_rows)[0]:
                protected_candidate_count += 1
                skipped_roots.append({"path": candidate_rel, "reason": "protected"})
                continue
            try:
                if is_reparse_point(candidate):
                    reparse_point_candidate_count += 1
                    raise PlannerError(f"candidate root is reparse point: {candidate_rel}")
            except PermissionError as exc:
                raise PlannerError(f"candidate root permission denied: {candidate_rel}: {exc}") from exc

            scanned_roots.append(candidate_rel)
            details, permission_denied, reparse_points = scan_tree(candidate)
            classification, planned_action, reason = classify_candidate(
                candidate_rel,
                details,
                protected_rows,
                descendant_permission_denied=bool(permission_denied),
                descendant_reparse=bool(reparse_points),
            )
            if planned_action in {"quarantine", "delete"} and (permission_denied or reparse_points):
                planned_action = "report_only"
            pdf_names = sorted(
                Path(str(item.get("relative_path", ""))).name
                for item in details
                if str(item.get("relative_path", "")).lower().endswith(".pdf")
            )
            total_bytes = sum(int(item.get("size", 0)) for item in details)
            newest_mtime_ns = max((int(item.get("mtime_ns", 0)) for item in details), default=0)
            file_count = sum(1 for item in details if not bool(item.get("is_dir")))
            dir_count = sum(1 for item in details if bool(item.get("is_dir")))
            rows.append(
                {
                    "path": candidate_rel,
                    "planned_action": planned_action,
                    "classification": classification,
                    "evidence_reason": reason,
                    "protected_check_result": "not_protected",
                    "path_kind": "directory" if candidate.is_dir() else "file",
                    "file_count": file_count,
                    "dir_count": dir_count,
                    "total_bytes": total_bytes,
                    "newest_mtime": mtime_iso(newest_mtime_ns) if newest_mtime_ns else "",
                    "pdf_count": len(pdf_names),
                    "pdf_names": pdf_names,
                    "manifest_present": any("manifest" in Path(str(item.get("relative_path", ""))).name.lower() for item in details),
                    "path_fingerprint_hash": fingerprint_hash(details),
                    "fingerprint_detail": details,
                    "permission_denied": permission_denied,
                    "reparse_points": reparse_points,
                    "replaced_by_path": "",
                    "replaced_by_main_price_date": "",
                    "replaced_by_source_ref": "",
                    "evidence_file": "",
                }
            )

    summary = {
        "candidate_globs": list(OUTPUT_GLOBS),
        "scanned_roots": scanned_roots,
        "skipped_roots": skipped_roots,
        "candidate_count": len(rows),
        "ignored_output_count": len(rows),
        "protected_candidate_count": protected_candidate_count,
        "reparse_point_candidate_count": reparse_point_candidate_count,
    }
    mark_latest_pdf_layout_baselines(rows, summary)
    return rows, summary


def manifest_hash(manifest: dict[str, object]) -> str:
    copy = json.loads(json.dumps(manifest, ensure_ascii=False))
    copy["manifest_hash"] = ""
    payload = json.dumps(copy, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fieldnames = [
        "path",
        "planned_action",
        "classification",
        "evidence_reason",
        "protected_check_result",
        "path_kind",
        "file_count",
        "dir_count",
        "total_bytes",
        "newest_mtime",
        "pdf_count",
        "manifest_present",
        "path_fingerprint_hash",
        "layout_baseline_keep",
        "layout_baseline_report_keys",
        "layout_baseline_pdf_names",
    ]
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def summary_markdown(manifest: dict[str, object]) -> str:
    rows = list(manifest.get("rows", []))
    counts: dict[str, int] = {}
    for row in rows:
        classification = str(row.get("classification", ""))
        counts[classification] = counts.get(classification, 0) + 1
    lines = [
        "# Workspace Cleanup Policy Summary",
        "",
        f"- report_id: `{manifest.get('report_id', '')}`",
        f"- git_head: `{manifest.get('git_head', '')}`",
        f"- generated_at_local: `{manifest.get('generated_at_local', '')}`",
        f"- candidate_count: `{len(rows)}`",
        f"- manifest_hash: `{manifest.get('manifest_hash', '')}`",
        "",
        "## Classification Counts",
        "",
    ]
    if counts:
        for key in sorted(counts):
            lines.append(f"- {key}: {counts[key]}")
    else:
        lines.append("- none: 0")
    lines.extend(
        [
            "",
            "## Layout Baseline",
            "",
            f"- report kinds: `{manifest.get('workspace_output_scan_summary', {}).get('layout_baseline_report_count', 0)}`",
            f"- baseline PDFs: `{manifest.get('workspace_output_scan_summary', {}).get('layout_baseline_pdf_count', 0)}`",
            f"- baseline roots: `{', '.join(manifest.get('workspace_output_scan_summary', {}).get('layout_baseline_roots', []))}`",
            "",
            "Full local manifests are ignored under `workspace_cleanup_reports/`.",
            "This summary is review metadata only and is not an apply manifest.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dry-run workspace cleanup planner.")
    parser.add_argument("--output-dir", default="workspace_cleanup_reports")
    parser.add_argument("--history-summary", default="")
    parser.add_argument("--overwrite-history-summary", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = (ROOT / args.output_dir).resolve(strict=False)
    latest_pointer = output_dir / "latest_manifest.json"
    error_pointer = output_dir / "latest_manifest_error.json"
    report_id = datetime.now(ZoneInfo(REPORT_TIMEZONE)).strftime("%Y%m%d_%H%M%S")
    report_dir = output_dir / report_id

    try:
        if ROOT.resolve(strict=False) not in (output_dir, *output_dir.parents):
            raise PlannerError(f"output dir must stay under repo root: {output_dir}")
        before_status = run_git_status()
        protected_rows = load_protected_paths()
        rows, scan_summary = build_rows(protected_rows)
        after_status = run_git_status()
        now_utc = datetime.now(UTC)
        now_local = now_utc.astimezone(ZoneInfo(REPORT_TIMEZONE))
        manifest: dict[str, object] = {
            "generated_at_utc": now_utc.isoformat(),
            "generated_at_local": now_local.isoformat(),
            "generated_timezone": REPORT_TIMEZONE,
            "planner_version": PLANNER_VERSION,
            "git_head": run_git_head(),
            "git_status_porcelain_before_planner": before_status,
            "git_status_porcelain_after_planner": after_status,
            "workspace_output_scan_summary": scan_summary,
            "repo_root": str(ROOT),
            "source_worktree": str(ROOT),
            "report_id": report_id,
            "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
            "manifest_hash": "",
            "history_summary_path": args.history_summary.replace("\\", "/") if args.history_summary else "",
            "rows": rows,
        }
        manifest["manifest_hash"] = manifest_hash(manifest)

        report_dir.mkdir(parents=True, exist_ok=True)
        manifest_path = report_dir / "manifest.json"
        write_json(manifest_path, manifest)
        write_csv(report_dir / "manifest.csv", rows)
        (report_dir / "summary.md").write_text(summary_markdown(manifest), encoding="utf-8")
        pointer = {
            "report_id": report_id,
            "manifest_path": manifest_path.relative_to(ROOT).as_posix(),
            "manifest_hash": manifest["manifest_hash"],
            "generated_at": manifest["generated_at_utc"],
        }
        write_json(latest_pointer, pointer)
        if error_pointer.exists():
            error_pointer.unlink()

        if args.history_summary:
            history_path = ROOT / args.history_summary
            if history_path.exists() and not args.overwrite_history_summary:
                raise PlannerError(f"history summary exists; use --overwrite-history-summary: {args.history_summary}")
            history_path.parent.mkdir(parents=True, exist_ok=True)
            history_path.write_text(summary_markdown(manifest), encoding="utf-8")
        return 0
    except PlannerError as exc:
        output_dir.mkdir(parents=True, exist_ok=True)
        if latest_pointer.exists():
            latest_pointer.unlink()
        write_json(
            error_pointer,
            {
                "report_id": report_id,
                "generated_at": datetime.now(UTC).isoformat(),
                "error": str(exc),
            },
        )
        print(f"workspace cleanup planner failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
