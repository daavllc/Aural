import dearpygui.dearpygui as dpg

from helpers.logger import Logger

class HelpMenu:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menus.Help", "gui.log")
        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="Example")