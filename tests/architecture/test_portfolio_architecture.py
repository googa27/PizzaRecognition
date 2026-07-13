from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def test_portfolio_architecture_contract() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/check_portfolio_architecture.py"],
        check=False,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_preservation_runtime_support_caveat_is_explicit() -> None:
    root = Path(__file__).resolve().parents[2]
    contract = json.loads((root / "docs" / "ARCHITECTURE.yaml").read_text(encoding="utf-8"))
    warning = contract["preservation"]["runtime_support_warning"].lower()
    for fragment in ("gpu", "cuda", "runtime", "tested"):
        assert fragment in warning

    readme = (root / "README.md").read_text(encoding="utf-8")
    assert "Hardware/runtime support caveat" in readme
    assert "GPU" in readme and "CUDA" in readme
