# Architecture — PizzaRecognition

## Project #24 preservation profile

Source of truth: `docs/ARCHITECTURE.yaml`. Tracking issue: https://github.com/googa27/arxiv-implementation-lab/issues/24. Profile: `legacy`; enforcement: Advisory.

This repository is preserved as `Fork / Legacy ML`. The governance files are intentionally advisory and additive: they document provenance, risks, and revival gates without refactoring inherited code or claiming active maintenance.

## Archival, supersession, and provenance

- Archival notice: historical/reference preservation only; not production-ready, maintained, secure, or operationally validated.
- Supersession notice: prefer upstream or maintained libraries for new work.
- Canonical/provenance: upstream ML project fork; preserve upstream compatibility and attribution
- Upstream: https://github.com/TamaraCucumides/PizzaRecognition.git
- License/provenance warning: No root LICENSE detected; verify upstream project, dataset, model-weight, and image licenses before reuse.
- Security/private-data warning: Treat model files and image inputs as untrusted; do not deserialize arbitrary artifacts without sandboxing and checksum/provenance review. Do not add private images, customer/store identifiers, model weights with unclear rights, or API keys.
- Hardware/runtime support caveat: No GPU, CUDA, cuDNN, driver, container, model-weight, or training/inference runtime support is currently certified or tested by this preservation change. Hardware acceleration and CPU-only fallback behavior remain unknown until a revival task pins dependencies and verifies deterministic public-synthetic smoke tests on the target environment.

## Research-backed defaults

| Decision | Evidence | Repository application |
|---|---|---|
| Agent context | Hermes context files; AGENTS.md convention | Root `AGENTS.md`; progressive detail in this architecture document. |
| AI tool escalation | MCP tools specification | Stable local contracts first; no repo-specific plugin/MCP during preservation. |
| Python source layout | PyPA src-layout guidance | No forced migration for legacy/fork/hardware preservation. |
| Test layout | pytest good practices | Unit/integration/e2e/architecture directories exist; empty suites declare activation triggers. |
| Module budget | Pylint too-many-lines rationale plus AI review locality | 500-line default is a no-growth ratchet where runtime source roots are activated. |
| Evolution | Evolutionary architecture | Revival requires executable fitness functions and explicit exceptions. |
| Data layers | Medallion architecture | Applied only if revived with real data; current posture is advisory. |
| Python protocols | Python data model; NumPy dispatch | Dunders are not decoration; API/protocol redesign waits for revival. |

## Maintained-library decision table

| Capability | Selected route | Alternatives | Boundary / custom-code rule |
|---|---|---|---|
| object detection/classification | Detectron2, Ultralytics/YOLO, PyTorch/torchvision after version/license review | Bespoke detector stack | Wrap maintained model runners behind a small adapter and public manifest. |
| image processing/evaluation | OpenCV, Pillow, scikit-learn metrics | Ad hoc parsers/metrics | Record dataset split/provenance before evaluation claims. |
| architecture bootstrap | Python standard-library json over JSON-subset YAML | Hand-written YAML parser | Dependency-free advisory gate only. |

## Data, security, and privacy posture

Legacy image/model workflow only; image data, labels, trained weights, and evaluation splits require provenance/license/privacy review.

Do not add private images, customer/store identifiers, model weights with unclear rights, or API keys.

Treat model files and image inputs as untrusted; do not deserialize arbitrary artifacts without sandboxing and checksum/provenance review.

No GPU, CUDA, cuDNN, driver, container, model-weight, or training/inference runtime support is currently certified or tested by this preservation change. Do not claim CPU/GPU compatibility until runtime versions are pinned and smoke-tested with public-synthetic images.

## AI and human interface

- AI interface: Minimal AGENTS with upstream/revival guidance; no MCP/plugin.
- Human/notebook interface: Current script/demo API may be documented; typed model adapter only if independently revived.
- Core posture: No core coupling; optional generic model-output manifest only after revival.

## Revival gates

- Resolve source/upstream and root license before distributing code, images, labels, or weights.
- Define dataset card/model card with provenance, rights, split, metrics, and failure modes.
- Pin ML framework, Python, GPU/CUDA/cuDNN/driver or CPU-only runtime versions and add deterministic smoke tests using public-synthetic images.
- Review artifact loading security before accepting external weights or serialized objects.

## Research anchors

- https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files
- https://agents.md/
- https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
- https://docs.pytest.org/en/stable/explanation/goodpractices.html
- https://docs.python.org/3/reference/datamodel.html
- https://numpy.org/doc/stable/user/basics.dispatch.html
- https://evolutionaryarchitecture.com/precis.html
- https://learn.microsoft.com/en-us/azure/databricks/lakehouse/medallion
