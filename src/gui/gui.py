import os
import sys
import dearpygui.dearpygui as dpg

import helpers.config as config
from helpers.logger import Logger
from manager.manager import Manager

from gui.menu.MenuManager import MenuManager
from gui.panels.PanelManager import PanelManager

class GUI:
    def Launch(self):
        print("Launching GUI...")
        self._Start()

    def _Start(self):
        app = Application()
        app.Run()

class Application:
    def __init__(self):
        self.Width = 1280
        self.Height = 720

        self.log = Logger("Aural.GUI", "gui.log")

    def Run(self):
        self.Setup()
        self.Runtime()
        self.Shutdown()

    def SaveInit(self):
        dpg.save_init_file(f"{config.PATH_SETTINGS}{os.sep}dpg.ini")
        self.log.debug("Saved window configuration")

    def Reload(self):
        self.log.debug("Reloading...")
        sys.exit(-1)

    def ReloadGUI(self):
        self.log.debug("Reloading GUI...")
        sys.exit(-3)

    def Refresh(self):
        self.log.debug("Refreshing GUI...")
        self.Panels.Refresh()

    def Undo(self):
        self.manager.Undo()
        self.Refresh()

    def Redo(self):
        self.manager.Redo()
        self.Refresh()

    def Save(self):
        self.manager.Save()
        self.log.info("Saved!")
        self.Panels.Refresh()

    def Setup(self):
        self.log.debug("Setting up context...")
        dpg.create_context()
        dpg.configure_app(docking=True, docking_space=True)
        dpg.configure_app(init_file=f"{config.PATH_SETTINGS}{os.sep}dpg.ini", load_init_file=True)
        dpg.create_viewport(title=f"Aural {config.VERSION}", width=self.Width, height=self.Height, vsync=True, clear_color=[1, 0, 1, 1.0])
        dpg.setup_dearpygui()

    def Runtime(self):
        self.log.debug("Starting Runloop...")
        self.Menus = MenuManager()
        self.Panels = PanelManager()
        #self.Panels.Refresh()

        dpg.show_viewport()
        dpg.start_dearpygui()

    def Shutdown(self):
        self.log.debug("Shutting down...")
        dpg.destroy_context()