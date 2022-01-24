import os
import uuid

import helpers.config as config

import settings.Serializer as Serializer
import objects.AudioCable as ac
import objects.Route as rt

class Configuration:
    def __init__(self):
        self._Generate()
        self._Initialize()

    def _GenerateAudioCables(self):
        cable = ac.AudioCable()
        self.AudioCables = dict(
            Version = config.VERSION_AUDIOCABLE,
            Default = cable.GetConfiguration()
        )

    def _GenerateRoutes(self):
        route = rt.Route()
        self.Routes = dict(
            Version = config.VERSION_ROUTE,
            Default = route.GetConfiguration()
        )

    def GetAudioCables(self) -> list[ac.AudioCable]:
        cables = []
        for key, value in self.AudioCables.items():
            if key in {"Version", "Default"}:
                continue
            cable = ac.AudioCable()
            cable.Configuration = value
            cables.append(cable)
        return cables

    def GetRoutes(self) -> list[rt.Route]:
        routes = []
        for key, value in self.Routes.items():
            if key in {"Version", "Default"}:
                continue
            route = rt.Route()
            route.Configuration = value
            routes.append(route)
        return routes

    def _Generate(self):
        self._GenerateAudioCables()
        self._GenerateRoutes()

    def _Initialize(self):
        if os.path.exists(f"{config.PATH_SETTINGS}{os.sep}audiocables.json"):
            self.ImportAudioCables()
        if os.path.exists(f"{config.PATH_SETTINGS}{os.sep}routes.json"):
            self.ImportRoutes()

    def ImportAudioCables(self): # TODO: make this not overwrite the 'default' config, as new options could be added
        self.AudioCables = self._Deserialize(f"{config.PATH_SETTINGS}{os.sep}audiocables.json")

    def ExportAudioCables(self):
        self._Serialize(f"{config.PATH_SETTINGS}{os.sep}audiocables.json", self.AudioCables)

    def ImportRoutes(self): # TODO: make this not overwrite the 'default' config, as new options could be added
        self.Routes = self._Deserialize(f"{config.PATH_SETTINGS}{os.sep}routes.json")

    def ExportRoutes(self):
        self._Serialize(f"{config.PATH_SETTINGS}{os.sep}routes.json", self.AudioCables)

    def _Deserialize(self, path: str) -> dict:
        return Serializer.Deserialize(path)

    def _Serialize(self, path: str, config: dict):
        Serializer.Serialize(path, config)