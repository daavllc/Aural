from manager._controller import Controller
from manager.command import Command
from helpers.logger import Logger

from manager.AudioCable.AudioCableManager import AudioCableManager
from manager.Route.RouteManager import RouteManager

class Manager:
    """
    Provides easy access to basic functions and quality of life features
    Just like a manager, it doesn't know what it's managing, but does manages it all anyway
    """
    __instance = None

    @staticmethod
    def Get():
        if Manager.__instance is None:
            Manager()
        return Manager.__instance

    def __init__(self):
        if Manager.__instance is not None:
            raise Exception("Manager attempted to re-init")
        else:
            Manager.__instance = self
            self.Controller = Controller()
            self.log = Logger("Aural.Manager", "manager.log")

            self.AudioCableManager = AudioCableManager(self)
            self.RouteManager = RouteManager(self)

    def AudioCables(self):
        return self.AudioCableManager
    
    def Routes(self):
        return self.RouteManager

    def SaveRoutes(self):
        pass

    def SaveAudioCables(self):
        pass

    # Controller abstractions
    def Execute(self, cmd: Command) -> None:
        self.Controller.Execute(cmd)

    def Undo(self) -> bool:
        self.Controller.Undo()

    def Redo(self) -> bool:
        self.Controller.Redo()

    def ClearHistory(self) -> None:
        self.Controller.Clear()

    def GetTimeline(self) -> list:
        return self.Controller.GetTimeline()

    def PrintHistory(self) -> None:
        timeline = self.GetTimeline()
        if timeline is None:
            print("No history to show")
            return
        for item in self.GetTimeline():
            print(" --- HISTORY --- ")
            print(f"{item[1]} at {item[0]}")

