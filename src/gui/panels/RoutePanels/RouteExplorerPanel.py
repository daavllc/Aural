import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class RouteExplorerPanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.RouteExplorer", "gui.log")

        self.Panel = "RouteExplorer"
        self.Pre = "REx"

        with dpg.window(tag=self.Panel, label="Route Explorer", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Route Explorer Panel")