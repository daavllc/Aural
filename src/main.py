import argparse
import os
import platform
import sys

import helpers.config as config
from helpers.logger import Logger

import interface
from settings.Settings import Settings
from settings.Configuration import Configuration

log = Logger("Aural", "aural.log")

def main():
    global log
    parser = argparse.ArgumentParser(add_help=True, description="Virtual audio cable creator, manager, and router")
    parser.add_argument("-UI", help="specify user interface to use", choices=['CUI', 'GUI'])
    args = parser.parse_args()
    print("        ___                    __")
    print("       /   | __  ___________ _/ /")
    print("      / /| |/ / / / ___/ __ `/ / ")
    print("     / ___ / /_/ / /  / /_/ / /  ")
    print("    /_/  |_\__,_/_/   \__,_/_/   ")
    print(f" Copyright ©2022 DAAV, LLC - v{config.VERSION}")
    print(f" Licensed under the MIT license. See LICENSE for details.\n")

    config.PATH_ROOT = os.path.abspath("..")
    config.PATH_SETTINGS = f"{config.PATH_ROOT}{os.sep}Settings"

    if not os.path.exists(f"{config.PATH_ROOT}{os.sep}logs"):
        os.mkdir(f"{config.PATH_ROOT}{os.sep}logs")
    if not os.path.exists(f"{config.PATH_ROOT}{os.sep}Settings"):
        os.mkdir(f"{config.PATH_ROOT}{os.sep}Settings")

    log.debug(f"{config.PATH_ROOT = }")
    log.debug(f"Launching with {platform.platform()} on {platform.machine()}")
    if sys.version is not None:
        log.debug(f"Using Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    config.SETTINGS = Settings()
    config.CONFIGURATION = Configuration()

    # Begin
    if args.UI == "CUI":
        LaunchCUI(args)
    elif args.UI == "GUI":
        LaunchGUI(args)
    else:
        LaunchMenu(args)
    Exit()

def LaunchUI(args):
    ui = interface.UI(args)
    ui.Start()

def LaunchCUI(args):
    args.UI = interface.Type.CUI
    LaunchUI(args)

def LaunchGUI(args):
    args.UI = interface.Type.GUI
    LaunchUI(args)

def LaunchMenu(args):
    print("\tNote: UI is still developmental")
    print("\tPlease specify which interface you want to use:")
    print("\t    1) CUI       2) GUI")
    UsrInput = ""
    while True:
        try:
            UsrInput = input("\tSelect an option > ")
        except KeyboardInterrupt:
            return

        UsrInput = UsrInput.lower()
        if UsrInput == "exit":
            return
        elif UsrInput == "reload":
            print("Reloading...")
            sys.exit(-1)
        elif UsrInput == "cui" or UsrInput == "1":
            LaunchCUI(args)
            break
        elif UsrInput == "gui" or UsrInput == "2":
            LaunchGUI(args)
            break
        elif 'help' in UsrInput:
            print("\tCommands:")
            print("\t  help\n\t\tshow this menu")
            print("\t  1 | cui\n\t\tlaunch cui")
            print("\t  2 | gui\n\t\tlaunch gui")
            print("\t  reload\n\t\treloads Aural")
        else:
            print(" ERR: Invalid option, type 'help' to view commands")

def Exit():
    print("Goodbye!")
    sys.exit(0)

if __name__ == '__main__':
    main()