# AGENTS.md — PizzaRecognition

Purpose: Project #24 legacy preservation. This repository is classified as `Fork / Legacy ML` with `legacy` profile and Advisory enforcement. Do not make unsupported maturity, security, maintenance, or production-readiness claims.

Canonical docs:
- `README.md` root preservation notice
- `docs/ARCHITECTURE.yaml` machine-readable source of truth
- `docs/ARCHITECTURE.md` rationale and maintained-library/revival notes

Provenance and attribution:
- Origin owner: `googa27`; issue: https://github.com/googa27/arxiv-implementation-lab/issues/24
- Upstream/canonical reference: https://github.com/TamaraCucumides/PizzaRecognition.git
- Preserve history, existing public names, authorship, copyright notices, and file contents. Do not delete, rewrite, or hide inherited material in this preservation change.

Safety boundaries:
- License/provenance: No root LICENSE detected; verify upstream project, dataset, model-weight, and image licenses before reuse.
- Data posture: Legacy image/model workflow only; image data, labels, trained weights, and evaluation splits require provenance/license/privacy review.
- Private-data rule: Do not add private images, customer/store identifiers, model weights with unclear rights, or API keys.
- Security/hardware warning: Treat model files and image inputs as untrusted; do not deserialize arbitrary artifacts without sandboxing and checksum/provenance review.
- Hardware/runtime support caveat: No GPU, CUDA, cuDNN, driver, container, model-weight, or training/inference runtime support is currently certified or tested by this preservation change. Treat hardware acceleration and CPU-only fallback behavior as unknown until a revival task pins dependencies and verifies public-synthetic smoke tests on the target environment.

Exact commands:
- Setup: no supported automated setup is declared; treating runtime setup as a revival gate is required.
- Tests: no inherited runtime test suite is claimed; run the architecture checker only.
- Lint/format: no lint/format command is declared.
- Architecture: `python scripts/check_portfolio_architecture.py`

Implementation rules for future work:
- Research upstream/current maintained libraries, standards, datasets, licenses, and security posture before changing runtime code.
- Prefer maintained libraries; custom code must be limited to domain semantics, adapters, composition, or genuinely missing algorithms with oracle/reference tests.
- Avoid invasive refactors of inherited code. Record exact no-growth exceptions and compatibility risks before structural changes.
- Do not introduce generated caches, secrets, private identifiers, restricted data, or fabricated outputs.
- Keep AI-facing contracts deterministic and local. Add Hermes skills for recurring workflows only; plugin/MCP needs stable public contracts, measured multi-client need, least privilege, and separate verification.
- Human/notebook interface: Current script/demo API may be documented; typed model adapter only if independently revived.
- Core posture: No core coupling; optional generic model-output manifest only after revival.

Revival gates:
- Resolve source/upstream and root license before distributing code, images, labels, or weights.
- Define dataset card/model card with provenance, rights, split, metrics, and failure modes.
- Pin ML framework, Python, GPU/CUDA/cuDNN/driver or CPU-only runtime versions and add deterministic smoke tests using public-synthetic images.
- Review artifact loading security before accepting external weights or serialized objects.

Definition of done for preservation edits:
- README, AGENTS, `docs/ARCHITECTURE.yaml`, `docs/ARCHITECTURE.md`, and tests agree.
- `python scripts/check_portfolio_architecture.py` passes.
- Only advisory governance files are changed unless a separate reviewed revival task authorizes runtime edits.
