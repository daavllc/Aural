from enum import Enum

from cui.cui import CUI
from gui.gui import GUI

import helpers.config as config

class Type(Enum):
    CUI = CUI()
    GUI = GUI()

class UI:
    def __init__(self, args):
        self.inst = args.UI

    def Start(self):
        self.inst = self.inst.value
        self.inst.Launch()