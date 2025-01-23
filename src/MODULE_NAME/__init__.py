"""PROJECT_DESC"""

from typing import Any

__all__ = []


def export(defn: Any) -> None:  # noqa: ANN401
    """Module-level export decorator."""
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)  # noqa: PYI056
    return defn


__copyright__ = "Copyright (c) 2024 Ryan Kozak"
from MODULE_NAME._version import __version__
