import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

from .RouteExplorerPanel import RouteExplorerPanel
from .RouteEditorPanel import RouteEditorPanel

class RoutePanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.Route", "gui.log")

        self.AudioCableExplorer = RouteExplorerPanel()
        self.AudioCableEditor = RouteEditorPanel()