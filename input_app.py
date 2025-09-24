# REUQIREMENTS:
# 1. pip install keyboard

import input_lib
import keyboard # just for start/exit on key


bRunApp = True
bRunScript = False
exitAppButton = 'q' # terminate application on this key
toggleRunScriptButton = 'r' # run and stop script on this key

pathToScriptCommands = 'presets/roblox_climb_and_jump.py' # <== PASTE HERE YOUR PRESET FILE WITH COMMANDS
#pathToScriptCommands = 'presets/mouse_debug.py'
scriptCommands = ''

def HandleKeyPress(event):
    global bRunApp, bRunScript, exitAppButton, toggleRunScriptButton

    if event.name == exitAppButton:
        bRunApp = False
    elif event.name == toggleRunScriptButton:
        bRunScript = not bRunScript
    

def RunScriptOnce():
    global scriptCommands
    exec(scriptCommands) # it works like paste commands from another file to here


def main():
    global bRunApp, bRunScript, pathToScriptCommands, scriptCommands

    with open(pathToScriptCommands, 'r') as file:
        scriptCommands = file.read()

    keyboard.on_press(HandleKeyPress)

    print(f"Press '{toggleRunScriptButton}' to run/stop script and '{exitAppButton}' to exit...")

    while bRunApp:
        if bRunScript:
            RunScriptOnce()


if __name__ == "__main__":
    main()
