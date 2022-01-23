import sys
import dearpygui.dearpygui as dpg

from helpers.logger import Logger

class DebugMenu:
    def __init__(self):
        self.log = Logger("Aural.GUI.Menus.Debug", "gui.log")
        with dpg.menu(label="Debug"):
            dpg.add_menu_item(label="Show dpg items", callback=self.PrintDPG)
            dpg.add_separator()
            dpg.add_menu_item(label="Reload GUI", callback=lambda: sys.exit(-3))

    def PrintDPG(self):
        for item in dpg.get_all_items():
            itemName = dpg.get_item_alias(item)
            if itemName is None or len(itemName) == 0:
                itemName = "None"
            try:
                itemType = dpg.get_item_type(item)
            except SystemError:
                itemType = "Unknown"
            print(f"{item} : {itemName} -> {itemType}")