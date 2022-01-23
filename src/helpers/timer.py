import time
import asyncio

from helpers.logger import Logger

class Timer:
    __instance = None

    @staticmethod
    def Get():
        if Timer.__instance is None:
            Timer()
        return Timer.__instance

    def __init__(self):
        if Timer.__instance is not None:
            return Timer.__instance
        else:
            Timer.__instance = self
            self.log = Logger("Aural.Timer", "aural.log")
            self.Track = {}

    def GetTime(self):
        return self.StartTime

    def Add(self, name: str):
        self.Track[name] = time.perf_counter()

    def Get(self, name: str):
        return self.Track.get(name, None)

    def GetElapsed(self, name: str):
        elapsed = self.Track.get(name, None)
        if elapsed is None:
            return
        return time.perf_counter() - elapsed
