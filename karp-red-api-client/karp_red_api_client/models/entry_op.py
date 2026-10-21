from enum import StrEnum


class EntryOp(StrEnum):
    ADDED = "ADDED"
    DELETED = "DELETED"
    UPDATED = "UPDATED"

    def __str__(self) -> str:
        return str(self.value)
