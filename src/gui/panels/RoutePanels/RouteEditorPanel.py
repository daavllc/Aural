import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class RouteEditorPanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.RouteEditor", "gui.log")

        self.Panel = "RouteEditor"
        self.Pre = "REt"

        with dpg.window(tag=self.Panel, label="Route Editor", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Route Editor Panel")