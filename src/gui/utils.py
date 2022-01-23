import os
import dearpygui.dearpygui as dpg

import helpers.config as config

def SaveInit():
    dpg.save_init_file(f"{config.PATH_SETTINGS}{os.sep}dpg.ini")

def DeleteItems(name: str):
    """Due to an error in dearpygui, we need to delete item aliases after the item.
        We first get all items and aliases, then sort by length(deeper nested items first)
        Then delete the item, and make sure it's alias is deleted

    Args:
        name (str): Name to search for and delete, ex: ppX.Header
    """
    aliases = []
    for item in dpg.get_all_items():
        itemName = dpg.get_item_alias(item)
        if itemName is None or len(itemName) == 0:
            continue
        elif name in itemName:
            aliases.append( (item, itemName) )
    if len(aliases) > 0:
        aliases = sorted(aliases, key=lambda alias: len(alias[1].split('.')), reverse=True)
        for item in aliases:
            dpg.delete_item(item[0])
            try:
                dpg.remove_alias(item[1])
            except SystemError:
                pass