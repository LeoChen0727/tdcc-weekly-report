from __future__ import annotations

import argparse
import builtins
import json
import runpy
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Callable, Iterator


ROOT = Path(__file__).resolve().parents[1]


@dataclass
class FileAccess:
    operation: str
    path: str
    normalized_path: str


class FileAccessTracer:
    """Trace runtime file reads/writes for a Python entrypoint.

    The tracer is intentionally standard-library only so it can run before the
    workflow installs pandas/reportlab. It records the common file APIs used in
    this repo. Heavy production scripts should be traced in diagnostics mode or
    one at a time, then compared against config/runtime_file_lineage_contract.csv.
    """

    def __init__(self, repo_root: Path = ROOT) -> None:
        self.repo_root = repo_root.resolve()
        self.events: list[FileAccess] = []
        self._patches: list[tuple[Any, str, Any]] = []

    def __enter__(self) -> FileAccessTracer:
        self._patch(builtins, "open", self._wrap_open(builtins.open, "open"))
        self._patch(Path, "open", self._wrap_path_method(Path.open, "Path.open"))
        self._patch(Path, "read_text", self._wrap_path_method(Path.read_text, "Path.read_text", forced_mode="r"))
        self._patch(Path, "read_bytes", self._wrap_path_method(Path.read_bytes, "Path.read_bytes", forced_mode="rb"))
        self._patch(Path, "write_text", self._wrap_path_method(Path.write_text, "Path.write_text", forced_mode="w"))
        self._patch(Path, "write_bytes", self._wrap_path_method(Path.write_bytes, "Path.write_bytes", forced_mode="wb"))
        return self

    def __exit__(self, exc_type: object, exc: object, tb: object) -> None:
        for obj, name, original in reversed(self._patches):
            setattr(obj, name, original)
        self._patches.clear()

    def _patch(self, obj: Any, name: str, replacement: Any) -> None:
        self._patches.append((obj, name, getattr(obj, name)))
        setattr(obj, name, replacement)

    def _record(self, operation: str, path_value: object) -> None:
        try:
            path = Path(path_value)
        except TypeError:
            return
        raw = str(path_value).replace("\\", "/")
        normalized = self._normalize(path)
        self.events.append(FileAccess(operation=operation, path=raw, normalized_path=normalized))

    def _normalize(self, path: Path) -> str:
        try:
            resolved = path.expanduser().resolve()
        except OSError:
            resolved = path.expanduser().absolute()
        try:
            return resolved.relative_to(self.repo_root).as_posix()
        except ValueError:
            return resolved.as_posix()

    @staticmethod
    def _operation_from_mode(mode: str) -> str:
        return "write" if any(token in mode for token in ("w", "a", "x", "+")) else "read"

    def _wrap_open(self, original: Callable[..., Any], api_name: str) -> Callable[..., Any]:
        def wrapper(file: object, mode: str = "r", *args: Any, **kwargs: Any) -> Any:
            self._record(f"{api_name}:{self._operation_from_mode(str(mode))}", file)
            return original(file, mode, *args, **kwargs)

        return wrapper

    def _wrap_path_method(
        self,
        original: Callable[..., Any],
        api_name: str,
        forced_mode: str | None = None,
    ) -> Callable[..., Any]:
        def wrapper(path_self: Path, *args: Any, **kwargs: Any) -> Any:
            mode = forced_mode or (str(args[0]) if args else str(kwargs.get("mode", "r")))
            self._record(f"{api_name}:{self._operation_from_mode(mode)}", path_self)
            return original(path_self, *args, **kwargs)

        return wrapper

    def iter_unique_events(self) -> Iterator[FileAccess]:
        seen: set[tuple[str, str]] = set()
        for event in self.events:
            key = (event.operation, event.normalized_path)
            if key in seen:
                continue
            seen.add(key)
            yield event

    def write_json(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(event) for event in self.iter_unique_events()]
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def trace_script(script_path: Path, argv: list[str], output_path: Path, repo_root: Path = ROOT) -> int:
    old_argv = sys.argv[:]
    sys.argv = [str(script_path), *argv]
    tracer = FileAccessTracer(repo_root=repo_root)
    try:
        with tracer:
            runpy.run_path(str(script_path), run_name="__main__")
    except SystemExit as exc:
        code = int(exc.code or 0)
    else:
        code = 0
    finally:
        sys.argv = old_argv
        tracer.write_json(output_path)
    return code


def main() -> int:
    parser = argparse.ArgumentParser(description="Trace runtime file lineage for one Python script.")
    parser.add_argument("script", type=Path)
    parser.add_argument("script_args", nargs=argparse.REMAINDER)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=ROOT / "output" / "debug" / "runtime_file_lineage_latest.json")
    args = parser.parse_args()

    script = args.script.expanduser()
    if not script.is_absolute():
        script = (args.repo_root / script).resolve()
    if not script.exists():
        print(f"ERROR: script not found: {script}")
        return 1
    return trace_script(script, list(args.script_args), args.output.expanduser(), args.repo_root.expanduser())


if __name__ == "__main__":
    raise SystemExit(main())
