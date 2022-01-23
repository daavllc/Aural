import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

class AudioCableEditorPanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.AudioCableEditor", "gui.log")

        self.Panel = "AudioCableEditor"
        self.Pre = "ACEt"

        with dpg.window(tag=self.Panel, label="Audio Cable Editor", no_close=True):
            dpg.add_text(tag=f"{self.Pre}.Text", default_value="Audio Cable Editor Panel")