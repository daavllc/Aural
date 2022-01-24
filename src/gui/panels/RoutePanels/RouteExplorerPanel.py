import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class RouteExplorerPanel:
    def __init__(self, manager):
        self.log = Logger("Aural.GUI.Panels.RouteExplorer", "gui.log")
        self.manager = manager

        self.Panel = "RouteExplorer"
        self.Pre = "RtEx"

        with dpg.window(tag=self.Panel, label="Route Explorer", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Route Explorer Panel")