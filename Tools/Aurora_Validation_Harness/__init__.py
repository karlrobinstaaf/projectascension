"""Validation infrastructure for Project Ascension's Aurora architecture.

The package is validator-owned infrastructure. It must remain external to
Aurora's cognitive state and must never expose world truth, validator-only
knowledge, future state, or expected results through its public Aurora adapter.
"""

from importlib.metadata import PackageNotFoundError, version
from typing import Final

PACKAGE_NAME: Final[str] = "aurora-validation-harness"

try:
    _installed_version = version(PACKAGE_NAME)
except PackageNotFoundError:
    # Supports direct execution from a source checkout before installation.
    _installed_version = "0.1.0"

__version__: Final[str] = _installed_version

__all__ = ["PACKAGE_NAME", "__version__"]
