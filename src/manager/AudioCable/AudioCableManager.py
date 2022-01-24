import datetime as dt
import os

from helpers.logger import Logger
import helpers.config as config
from settings.Settings import Settings

from objects.AudioCable import AudioCable
from manager.command import Command

class AudioCableManager:
    def __init__(self, manager):
        self.log = Logger("Aural.Manager.AudioCables", "manager.log")
        self.manager = manager