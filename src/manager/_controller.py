import datetime as dt
from enum import Enum

from helpers.logger import Logger

from manager.command import Command

class Controller:
    class Actions(Enum):
        EXECUTE = "Executed: "
        REDO = "Undid: "
        UNDO = "Redid: "

    def __init__(self):
        self.log = Logger("Aural.Manager.Controller", "manager.log")
        self.MaxHistory = 100

        self.History = []
        self.Position = -1

    def Execute(self, command: Command) -> None:
        command.Execute()
        self.History = self.History[:self.Position]
        self.History.append([self.Actions.EXECUTE, command, dt.datetime.now()])
        self.Position += 1

    def Undo(self) -> bool:
        if self.Position < 1:
            return False
        self.Position -= 1
        undo = self.History[self.Position]
        self.History[self.Position] = [self.Actions.UNDO, undo[1], dt.datetime.now()]
        undo[1].Undo()
        return True

    def Redo(self) -> bool:
        if self.Position == len(self.History) - 1 or self.Position == 0:
            return False
        if not self.History[self.Position + 1][0] == self.Actions.UNDO:
            return False
        self.Position += 1
        redo = self.History[self.Position]
        self.History[self.Position] = [self.Actions.REDO, redo[1], dt.datetime.now()]
        redo[1].Redo()
        return True

    def Clear(self):
        self.History.Clear()
        self.Position = -1

    def GetTimeline(self, number: int = None) -> list[dt.datetime, str]:
        size = len(self.History)
        if len(self.History) == 0 or number > size:
            return None
        timeline: list[dt.datetime, str] = []
        if number == None:
            number = size

        for command in self.History[size - number:]:
            timeline.append(command[2], f"{command[0].value}{command[1].Details()}")
        return timeline