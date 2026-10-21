from enum import StrEnum


class Scope(StrEnum):
    ADMIN = "ADMIN"
    READ = "READ"
    WRITE = "WRITE"

    def __str__(self) -> str:
        return str(self.value)
