from __future__ import annotations

import json
import subprocess
import sys
from copy import deepcopy
from importlib import util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CHECKER = ROOT / "scripts" / "check_portfolio_architecture.py"


def load_checker_module():
    spec = util.spec_from_file_location("portfolio_architecture_checker", CHECKER)
    assert spec is not None and spec.loader is not None
    module = util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_portfolio_architecture_contract() -> None:
    result = subprocess.run(
        [sys.executable, str(CHECKER)],
        check=False,
        text=True,
        capture_output=True,
        cwd=Path(__file__).resolve().parent,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_malformed_limits_report_contract_errors_without_traceback(tmp_path: Path) -> None:
    checker = load_checker_module()
    contract = json.loads((ROOT / "docs" / "ARCHITECTURE.yaml").read_text(encoding="utf-8"))

    malformed = deepcopy(contract)
    malformed["source_layout"]["python_rules_applicable"] = True
    malformed["source_layout"]["python_source_roots"] = ["."]
    malformed["limits"] = {
        "max_immediate_runtime_entries": "10",
        "max_python_module_lines": None,
    }

    errors = checker.validate_contract(malformed)

    assert "limits.max_immediate_runtime_entries must be integer 10" in errors
    assert "limits.max_python_module_lines must be integer 500" in errors

    malformed_contract = tmp_path / "ARCHITECTURE.yaml"
    malformed_contract.write_text(json.dumps(malformed), encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            (
                "import importlib.util, pathlib, sys; "
                "spec = importlib.util.spec_from_file_location('checker', sys.argv[1]); "
                "module = importlib.util.module_from_spec(spec); "
                "spec.loader.exec_module(module); "
                "module.CONTRACT = pathlib.Path(sys.argv[2]); "
                "raise SystemExit(module.main())"
            ),
            str(CHECKER),
            str(malformed_contract),
        ],
        check=False,
        text=True,
        capture_output=True,
    )
    output = result.stdout + result.stderr

    assert result.returncode == 1
    assert "portfolio architecture check failed:" in output
    assert "limits.max_immediate_runtime_entries must be integer 10" in output
    assert "limits.max_python_module_lines must be integer 500" in output
    assert "Traceback" not in output


def test_exceptions_must_name_enforced_checker_rules() -> None:
    checker = load_checker_module()
    contract = json.loads((ROOT / "docs" / "ARCHITECTURE.yaml").read_text(encoding="utf-8"))
    stale_exception = {
        "rule": "blocking_ci",
        "path": ".github/workflows/portfolio-architecture.yml",
        "reason": "stale rule name probe",
        "owner": "googa27 Portfolio Project #24",
        "risk": "dead exception cannot activate",
        "accepted_ceiling": 0,
        "refactoring_trigger": "Use an enforced checker rule before registering an exception.",
    }

    invalid = deepcopy(contract)
    invalid["exceptions"] = [stale_exception]

    errors = checker.validate_contract(invalid)

    assert any("exceptions[0].rule must be one of enforced checker rules" in error for error in errors)


def test_preservation_runtime_support_caveat_is_explicit() -> None:
    contract = json.loads((ROOT / "docs" / "ARCHITECTURE.yaml").read_text(encoding="utf-8"))
    warning = contract["preservation"]["runtime_support_warning"].lower()
    for fragment in ("gpu", "cuda", "runtime", "tested"):
        assert fragment in warning

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Hardware/runtime support caveat" in readme
    assert "GPU" in readme and "CUDA" in readme
