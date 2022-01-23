import dearpygui.dearpygui as dpg

from helpers.logger import Logger

from gui.utils import SaveInit

class EditMenu:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menus.Edit", "gui.log")
        with dpg.menu(label="Edit"):
            dpg.add_menu_item(label="Save Window Configuration", callback=SaveInit)
            self.log.debug("Saved window configuration")