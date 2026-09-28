"""Value objects."""

import typing as t


class Unset:
    """Model for unset values."""

    def __bool__(self) -> t.Literal[False]:
        """Return is always false."""
        return False

    def __str__(self) -> str:
        """Return the string version of this class."""
        return "UNSET"

    def __repr__(self) -> str:
        """Return the repr version of this class."""
        return "UNSET"


UNSET: Unset = Unset()

__all__ = ["UNSET", "Unset"]
