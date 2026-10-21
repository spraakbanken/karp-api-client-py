from enum import StrEnum


class HighlightParam(StrEnum):
    FALSE = "false"
    NEW = "new"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
