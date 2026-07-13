## Project #24 Preservation notice

Status: Fork / Legacy ML (`legacy` profile, Advisory enforcement). This repository is preserved for historical/reference value and is not presented as maintained, production-ready, secure, or suitable for new operational use.

Supersession: prefer the canonical upstream or maintained libraries for new work. Canonical/provenance note: upstream ML project fork; preserve upstream compatibility and attribution. Upstream: https://github.com/TamaraCucumides/PizzaRecognition.git

License/provenance: No root LICENSE detected; verify upstream project, dataset, model-weight, and image licenses before reuse.

Security/private-data warning: Treat model files and image inputs as untrusted; do not deserialize arbitrary artifacts without sandboxing and checksum/provenance review. Do not add private images, customer/store identifiers, model weights with unclear rights, or API keys.

Hardware/runtime support caveat: No GPU, CUDA, cuDNN, driver, container, model-weight, or training/inference runtime support is currently certified or tested by this preservation change. Treat any hardware acceleration path as unknown until a revival task pins dependencies and verifies deterministic public-synthetic smoke tests on the target CPU/GPU environment.

Revival gates:
- Resolve source/upstream and root license before distributing code, images, labels, or weights.
- Define dataset card/model card with provenance, rights, split, metrics, and failure modes.
- Pin ML framework, Python, GPU/CUDA/cuDNN/driver or CPU-only runtime versions and add deterministic smoke tests using public-synthetic images.
- Review artifact loading security before accepting external weights or serialized objects.

See `AGENTS.md` and `docs/ARCHITECTURE.yaml` for the advisory preservation contract.

---

# PizzaRecognition
Proyecto de Taller de Ingeniería Matemática para Arara
