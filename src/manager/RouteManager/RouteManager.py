import datetime as dt

from helpers.logger import Logger

from objects.Route import Route
from manager.command import Command

class RouteManager:
    def __init__(self):
        self.log = Logger("Aural.Manager.RouteManager", "manager.log")