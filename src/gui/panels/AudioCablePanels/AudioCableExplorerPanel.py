import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class AudioCableExplorerPanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.AudioCableExplorer", "gui.log")

        self.Panel = "AudioCableExplorer"
        self.Pre = "ACEx"

        with dpg.window(tag=self.Panel, label="Audio Cable Explorer", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Audio Cable Explorer Panel")