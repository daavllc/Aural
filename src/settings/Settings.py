import os

import helpers.config as config

import settings.Serializer as Serializer

class Settings:
    def __init__(self):
        self._Generate()
        self._Initialize()

    def _Generate(self):
        self.Settings = dict(
            Version = config.VERSION_SETINGS,
            MaxHistory = 100
        )

    def _Initialize(self):
        if os.path.exists(f"{config.PATH_SETTINGS}{os.sep}settings.json"):
            self.Deserialize()
        else:
            self._Generate()

    def Deserialize(self): # TODO: make this not overwrite the 'default' settings, as new options could be added
        self.Settings = Serializer.Deserialize(f"{config.PATH_SETTINGS}{os.sep}settings.json")

    def Serialize(self):
        Serializer.Serialize(f"{config.PATH_SETTINGS}{os.sep}settings.json", self.Settings)