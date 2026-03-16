# MacroX — The best SNIPER DUELS macro of all time.
# Made by @Hazzereign & @yorioncheat.

# Sniper Duels' quickswitching is trash, so I made a macro
# that quickly switches your weapon in a single click.

# Press Z for quickswitching.
# Press F1 to pause or continue the Macro.
# Press F2 to switch the quickswitching mode.

# QUICKSWITCHING MODES
# First mode presses 2 --> 1 [recommended while holding sniper]
# Second mode presses 1 --> 2 [recommended while holding melee]

# This MUST be used for Sniper Duels or any sniper game, since
# it uses a well-developed system that checks if ROBLOX's down.
# ...or set the ROBLOX_Check variable to false.

# All rights reserved.
# Find me anywhere! @Hazzereign.

import keyboard
import pyautogui
import pydirectinput
pydirectinput.PAUSE = 0
import os
import time
from datetime import datetime
from colorama import Fore, Style, init
import requests
import sys

# here the MacroX initiates btw
macro = True # toggles the macro (toggle it by clicking f1)
quickswitch_mode = 1
ROBLOX_Check = True
ROBLOX_State = "not checked" # don't change this.
init()

if ROBLOX_Check:
    try:
        r = requests.get("https://www.roblox.com", timeout=10)

        if r.status_code == 200:
            print("ROBLOX is up, proceeding with normal tasks.")
            ROBLOX_State = "up"
        else:
            ROBLOX_State = "down"
            confirm = input("MacroX detected ROBLOX is down. Are you sure\nyou want to proceed? (y/n)")
            if confirm.lower() in ["y", "yes"]:
                pass
            else:
                print("See you next time.")
                sys.exit()
    except requests.exceptions.RequestException:
        ROBLOX_State = "not able to check"
        print("MacroX wasn't able to connect with roblox.com.")
        

print("MacroX can only run on Windows.")
os.system("cls")

print("=============================")
print("           MacroX            ")
print("    Made by @yorioncheat.    ")
print("   Use this on SNIPER DUELS. ")
print("=============================")

def log(level, msg):
    timestamp = datetime.now().strftime("%H:%M:%S")

    colors = {
        "INFO": Fore.CYAN,
        "ACTION": Fore.GREEN,
        "WARN": Fore.YELLOW,
        "ERROR": Fore.RED,
        "DEBUG": Fore.MAGENTA
    }

    color = colors.get(level, Fore.WHITE)

    print(f"[{timestamp}] {color}[{level}]{Style.RESET_ALL} {msg}")

log("INFO", "Loading system...")

def quickswitch():
    global macro

    if not macro:
        return

    log("INFO", "Quickswitched.")

    if quickswitch_mode == 1:
        pydirectinput.keyDown("2"); pydirectinput.keyUp("2")
        time.sleep(0.1)
        pydirectinput.keyDown("1"); pydirectinput.keyUp("1")
    else:
        pydirectinput.keyDown("1"); pydirectinput.keyUp("1")
        time.sleep(0.1)
        pydirectinput.keyDown("2"); pydirectinput.keyUp("2")

def toggle():
    global macro
    macro = not macro
    log("INFO", f"MacroX has been set to {'ON' if macro else 'OFF'}")

def switch_quickswitch_mode():
    global quickswitch_mode
    quickswitch_mode = 1 if quickswitch_mode == 2 else 2
    log("INFO", f"Set quickswitch mode to {quickswitch_mode}.")

def main():
    log("INFO", "Loading core...")

    keyboard.on_press_key("z", lambda _: quickswitch())
    keyboard.add_hotkey("f1", toggle)
    keyboard.add_hotkey("f2", switch_quickswitch_mode)

    os.system("title MacroX — Sniper Duels")
    log("INFO", "MacroX is ready to run.")

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("============ // ============")
        log("INFO", "MacroX stopped by user.")

    finally:
        log("INFO", "Thank you for using MacroX.")

if __name__ == "__main__":
    main()
