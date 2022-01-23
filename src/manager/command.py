from typing import Protocol

class Command(Protocol):
    def Details(self) -> str:
        ...

    def Execute(self) -> None:
        ...

    def Undo(self) -> None:
        ...

    def Redo(self) -> None:
        ...
