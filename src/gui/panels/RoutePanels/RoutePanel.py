import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger
from manager.manager import Manager

from .RouteExplorerPanel import RouteExplorerPanel
from .RouteEditorPanel import RouteEditorPanel
from .RouteOverviewPanel import RouteOverviewPanel

class RoutePanel:
    def __init__(self):
        self.log = Logger("Aural.GUI.Panels.Route", "gui.log")
        self.manager = Manager.Get().Routes()

        self.RouteExplorer = RouteExplorerPanel(self.manager)
        self.RouteEditor = RouteEditorPanel(self.manager)
        self.RouteOverview = RouteOverviewPanel(self.manager)

    def GetPanels(self):
        panels = {}
        for panel in {self.RouteExplorer, self.RouteEditor, self.RouteOverview}:
            panels[panel.Panel] = panel.Pre
        return panels