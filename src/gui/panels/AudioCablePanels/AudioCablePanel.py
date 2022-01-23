import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

from .AudioCableExplorerPanel import AudioCableExplorerPanel
from .AudioCableEditorPanel import AudioCableEditorPanel

class AudioCablePanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.AudioCable", "gui.log")

        self.AudioCableExplorer = AudioCableExplorerPanel()
        self.AudioCableEditor = AudioCableEditorPanel()