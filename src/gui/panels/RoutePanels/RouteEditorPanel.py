import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class RouteEditorPanel:
    def __init__(self, manager):
        self.log = Logger("Aural.GUI.Panels.RouteEditor", "gui.log")
        self.manager = manager

        self.Panel = "RouteEditor"
        self.Pre = "RtEt"

        with dpg.window(tag=self.Panel, label="Route Editor", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Route Editor Panel")