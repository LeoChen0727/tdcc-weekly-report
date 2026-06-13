from __future__ import annotations

from pathlib import Path
import shutil

try:
    from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR
except ModuleNotFoundError:
    from scripts.tracking_utils import DOCS_LATEST_DIR, LATEST_DIR


CATALYST_PAGES_ARTIFACTS = [
    "fundamental_catalyst_layer_latest.md",
    "theme_event_watch_latest.csv",
    "theme_event_watch_latest.md",
    "upcoming_catalyst_calendar_latest.csv",
    "upcoming_catalyst_calendar_latest.md",
    "upcoming_macro_event_calendar_latest.csv",
    "upcoming_macro_event_calendar_latest.md",
    "catalyst_summary_latest.csv",
    "catalyst_summary_latest.md",
    "catalyst_needs_review_latest.csv",
    "catalyst_needs_review_latest.md",
    "event_calendar_validation_latest.md",
    "event_calendar_validation_latest.json",
    "catalyst_layer_validation_latest.md",
    "catalyst_layer_validation_latest.json",
    "catalyst_data_source_status_latest.md",
    "catalyst_data_source_status_latest.json",
    "calendar_data_source_status_latest.md",
    "calendar_data_source_status_latest.json",
]


def sync_artifacts(
    latest_dir: Path = LATEST_DIR,
    docs_latest_dir: Path = DOCS_LATEST_DIR,
    artifact_names: list[str] | None = None,
) -> list[tuple[Path, Path]]:
    names = artifact_names or CATALYST_PAGES_ARTIFACTS
    docs_latest_dir.mkdir(parents=True, exist_ok=True)
    missing: list[Path] = []
    copied: list[tuple[Path, Path]] = []

    for name in names:
        src = latest_dir / name
        dst = docs_latest_dir / name
        if not src.exists():
            missing.append(src)
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append((src, dst))

    if missing:
        missing_text = ", ".join(path.as_posix() for path in missing)
        raise FileNotFoundError(f"missing catalyst Pages artifact(s): {missing_text}")

    return copied


def main() -> int:
    copied = sync_artifacts()
    for src, dst in copied:
        print(f"synced {src.as_posix()} -> {dst.as_posix()}")
    print(f"synced_catalyst_pages_artifacts={len(copied)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
