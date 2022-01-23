import dearpygui.dearpygui as dpg

from helpers.logger import Logger

class FileMenu:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menus.File", "gui.log")
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Example")