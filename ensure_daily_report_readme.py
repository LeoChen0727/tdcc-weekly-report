from __future__ import annotations

"""Compatibility wrapper for the daily READ_ME_FIRST publisher.

Historically this file generated its own partial READ_ME_FIRST_DAILY_REPORT.txt.
That created a second publish path with fewer keys than the real workflow output,
so callers could accidentally overwrite the complete READ_ME and trigger stale
date / missing-key failures.

Keep this filename as a safe entrypoint, but delegate to the canonical publisher.
"""

from publish_chatgpt_report_readme_and_check import main as publish_readme_main


def main() -> int:
    return publish_readme_main()


if __name__ == "__main__":
    raise SystemExit(main())
