"""theme.import.py's fzf list marks already-installed themes with a suffix
(INSTALLED_MARKER) so "More Themes" shows what's already there. The marker
must round-trip: get_theme_preview() and fzf_menu()'s selection handling both
look the raw theme name up in the gallery JSON by exact match, so a
marker that isn't stripped back off breaks that lookup -- get_theme_preview()
in particular then hits `theme_data.get(...)` on a `None` and crashes.

This checks the --preview path (the only marker-sensitive behavior reachable
without driving an interactive fzf session) with a marker-decorated name,
which would raise AttributeError if the strip were missing or broken.
"""

from __future__ import annotations

import json
import os
import pathlib
import subprocess
import sys

REPO_ROOT = pathlib.Path(os.environ.get("REPO_ROOT", "."))
SCRIPT_PATH = REPO_ROOT / "Configs/.local/lib/hyde/theme.import.py"
INSTALLED_MARKER = "  ✓ installed"

failures = 0


def check(condition: bool, message: str) -> None:
    global failures
    if not condition:
        failures += 1
        print(f"    fail: {message}")


def run_preview(cache_home: pathlib.Path, theme_arg: str):
    env = dict(os.environ)
    env["XDG_CACHE_HOME"] = str(cache_home)
    return subprocess.run(
        [sys.executable, str(SCRIPT_PATH), "--skip-clone", "--preview", theme_arg],
        capture_output=True,
        text=True,
        env=env,
    )


def main() -> int:
    with __import__("tempfile").TemporaryDirectory() as tmp:
        tmp_path = pathlib.Path(tmp)
        # Matches theme.import.py's own CLONE_DIR: os.path.join(XDG_CACHE_HOME, "hyde/gallery-database")
        clone_dir = tmp_path / "hyde" / "gallery-database"
        clone_dir.mkdir(parents=True)
        (clone_dir / "hyde-themes.json").write_text(
            json.dumps(
                [
                    {
                        "THEME": "Vesper",
                        "LINK": "https://example.invalid/vesper",
                        "OWNER": "someone",
                        "DESCRIPTION": "test fixture",
                        "COLORSCHEME": ["#111111", "#222222"],
                    }
                ]
            )
        )

        result = run_preview(tmp_path, "Vesper" + INSTALLED_MARKER)
        check(
            "AttributeError" not in result.stderr,
            f"--preview with the installed marker crashed instead of stripping it: {result.stderr}",
        )
        check(
            result.returncode == 0,
            f"--preview with the installed marker exited {result.returncode}: {result.stderr}",
        )

        # Sanity check: an unmarked, genuinely unknown theme is the actual
        # not-found path, not a crash -- distinguishes "strip works" above
        # from "the script never crashes on anything".
        result_unknown = run_preview(tmp_path, "DoesNotExist")
        check(
            "AttributeError" not in result_unknown.stderr,
            f"an unknown theme name should print 'not found', not crash: {result_unknown.stderr}",
        )

    return failures


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
