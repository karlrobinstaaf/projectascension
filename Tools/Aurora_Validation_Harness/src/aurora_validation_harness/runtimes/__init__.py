"""Aurora runtime adapters for governed validation execution.

Modules in this package implement the minimum executable runtime boundary and
consume only the least-privilege reset and step requests supplied by the
harness. The package intentionally performs no eager adapter imports, so CLI
preflight completes before a selected runtime factory is resolved.
"""

from __future__ import annotations

__all__: tuple[str, ...] = ()
