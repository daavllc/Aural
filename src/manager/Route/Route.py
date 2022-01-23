import datetime as dt

from helpers.logger import Logger

from objects.Route import Route
from manager.command import Command

class Route:
    def __init__(self):
        self.log = Logger("Aural.Manager.Route", "manager.log")