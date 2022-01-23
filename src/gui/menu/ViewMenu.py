import dearpygui.dearpygui as dpg

from helpers.logger import Logger

class ViewMenu:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menus.View", "gui.log")
        with dpg.menu(label="View"):
            dpg.add_menu_item(label="Example")