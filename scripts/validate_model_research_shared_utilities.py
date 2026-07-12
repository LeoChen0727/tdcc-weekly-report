from __future__ import annotations

import argparse

from model_research_shared_utility import validate_shared_utilities


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate_shared_utilities(base_ref=args.base_ref or None)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("model research shared utility validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
