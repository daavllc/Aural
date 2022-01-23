import dearpygui.dearpygui as dpg

from helpers.logger import Logger
from .FileMenu import FileMenu
from .EditMenu import EditMenu
from .ViewMenu import ViewMenu
from .HelpMenu import HelpMenu
from .DebugMenu import DebugMenu

class MenuManager:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menu", "gui.log")

        with dpg.viewport_menu_bar():
            self.File  = FileMenu()
            self.Edit  = EditMenu()
            self.View  = ViewMenu()
            self.Help  = HelpMenu()
            self.Debug = DebugMenu()