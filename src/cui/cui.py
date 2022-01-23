
from helpers.logger import Logger

class CUI:
    def Launch(self):
        print("Launching CUI...")
        self._Start()

    def _Start(self):
        app = Application()
        app.Run()

class Application:
    def __init__(self):
        self.Width = 1280
        self.Height = 720

        self.log = Logger("Aural.CUI", "cui.log")

    def Run(self):
        print("The CUI is not currently implemented")
        input("Press enter to exit")