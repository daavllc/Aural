import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class RouteOverviewPanel:
    def __init__(self, manager):
        self.log = Logger("Aural.GUI.Panels.RouteOverview", "gui.log")
        self.manager = manager

        self.Panel = "RouteOverview"
        self.Pre = "RtOv"

        with dpg.window(tag=self.Panel, label="Route Overview", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Route Overview Panel")