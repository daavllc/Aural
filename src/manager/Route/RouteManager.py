import datetime as dt
import os

from helpers.logger import Logger
import helpers.config as config
from settings.Settings import Settings

import objects.Route as rt
import manager.Route.commands as Commands

class RouteManager:
    def __init__(self, manager):
        self.log = Logger("Aural.Manager.Routes", "manager.log")
        self.manager = manager

        self.Routes = []
        self.__Initialize()
        self.Selected: int = None
        self.Live: rt.Route = None
        self.Saved: bool = True

    def Create(self) -> None:
        self.manager.Execute(Commands.CreateRoute(self, len(self.Routes) - 1))
        self.Select(len(self.Routes) - 1)

    def Select(self, index: int) -> bool:
        if index < 0 and index >= len(self.Routes):
            return False
        self.manager.Execute(Commands.SelectRoute(self))
        return True

    def Deselect(self) -> None:
        self._Select(None)

    def HasSelected(self) -> bool:
        if self.Selected is None:
            return False
        return True

    def _Select(self, index) -> None:
        if index == None:
            self.Selected = None
            self.Live = None
            self.Saved = True
            return
        self.Live = self.Routes[index]
        self.Selected = index

    def __Initialize(self):
        self.Routes = config.CONFIGURATION.GetRoutes()
        self.log.debug(f"Initialized {len(self.Routes)} routes")