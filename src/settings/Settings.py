import os

import helpers.config as config

import settings.SettingsSerializer as Serializer

class Settings:
    def _Generate(self):
        self.Settings = dict(
            MaxHistory = 100
        )

    def Get(self):
        if os.path.exists(f"{config.PATH_SETTINGS}{os.sep}settings.json"):
            self.Deserialize()
        else:
            self._Generate()
        return self.Settings

    def Deserialize(self):
        self.Settings = Serializer.Deserialize(f"{config.PATH_SETTINGS}{os.sep}settings.json")

    def Serialize(self):
        Serializer.Serialize(f"{config.PATH_SETTINGS}{os.sep}settings.json", self.Settings)