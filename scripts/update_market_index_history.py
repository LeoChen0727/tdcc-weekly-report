from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import update_market_index_history  # noqa: E402


def main() -> int:
    df = update_market_index_history(months=18)
    print(f"Saved market index history rows={len(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
