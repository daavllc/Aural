import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger

from gui.panels.AudioCablePanels.AudioCablePanel import AudioCablePanel
from gui.panels.RoutePanels.RoutePanel import RoutePanel

class PanelManager:
    def __init__(self):
        self.log = Logger("Aural.GUI.PanelManager", "gui.log")

        self.Panel = "PanelManager"
        self.Pre = "PM"

        self.AudioCablePanel = AudioCablePanel()
        self.RoutePanel = RoutePanel()

        with dpg.window(tag=self.Panel, label="Panel Manager", no_close=True):
            with dpg.group(parent=self.Panel, tag=f"{self.Pre}.Group", horizontal=True):
                dpg.add_button(tag=f"{self.Pre}.Group.ShowRoutes", label="Show Routes", callback=lambda: self.Select(True))
                dpg.add_button(tag=f"{self.Pre}.Group.ShowAudioCables", label="Show Audio Cables", callback=lambda: self.Select(False))
                dpg.add_button(tag=f"{self.Pre}.Group.ShowBoth", label="Show Both", callback=lambda: self.Select(True, True))

    def Select(self, Routes: bool, AudioCable: bool = None):
        if AudioCable is None:
            AudioCable = not Routes
        for panelName in self.RoutePanel.GetPanels().keys():
            dpg.configure_item(panelName, show=Routes)
        for panelName in self.AudioCablePanel.GetPanels().keys():
            dpg.configure_item(panelName, show=AudioCable)