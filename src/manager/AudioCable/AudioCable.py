import datetime as dt

from helpers.logger import Logger

from objects.AudioCable import AudioCable
from manager.command import Command

class AudioCable:
    def __init__(self):
        self.log = Logger("Aural.Manager.AudioCable", "manager.log")