# Possible input libs:
# 1. pyautogui - old library: accesses win32api through the built-in ctypes module (so it uses old and less compatible winAPI functions)
# 2. pydirectinput - more modern than pyautogui: library aims to replicate the functionality of the pyautogui, but by utilizing DirectInput scan codes and the more modern SendInput() win32 function
# 3. pynput - not sure: based on winapi hooks (SetWindowsHookEx, GetAsyncKeyState)
# 4. win32api (pywin32) - same as 3 before, but without extra wrappers (so more low-level, but we have more control)
# 5. ctypes - allow to call functions (like SendInput) directly from DLLs (like user32.dll).


# https://stackoverflow.com/questions/70161288/pydirectinput-pynput-pyautogui-dont-always-press-keys
# For most Games you need to past scan-codes or send inputs directly to the kernel as DirectX is a different API.
# Pyautogui won't work for some of it's input methods for DirectX games.
# FFXIV for example you can press keys from pyautogui but can't use Mouse movements from that library.
# Also some games like Maplestory for example completely ignores key strokes that's not coming from hardware API aka Kernel.
# And games with an anticheat software also block this.
# However, pydirectinput fixes this as it replaces pyautogui's win32 API method with Scan-Codes which is the same-ish as the OnScreen Keyboard.
# Just need to make sure you open the script as ADMINISTRATOR!


# Also it's better to run game in WINDOWED or WINDOWED FULLSCREEN mode


# WinAPI works this way only if game handle DirectX events (like WM_KEYDOWN, WM_KEYUP).
# Also some games didn't handle DirectX events if they are not in focus:
# hwnd = win32gui.FindWindow(None, "Roblox")
# win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL) # just to be sure that it found right window (window should be minimized)

# Send WM_KEYDOWN to specific window (BTW window probably can be minimized):
# win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_SPACE, 0)
# time.sleep(0.01)
# win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_SPACE, 0)

# Mouse:
# win32api.SetCursorPos((100, 100))
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
# time.sleep(0.001)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# REQUIREMENTS:
# pip install pydirectinput
# pip install PyAutoIt


# only for keyboard buttons:
import pydirectinput

# pydirectinput.click() sometimes skip clicks, so we will use autoit for mouse instead:
# https://www.autoitscript.com/autoit3/docs/
import autoit

import time


# pydirectinput is too slow fix: https://stackoverflow.com/questions/68388029/simulating-keypresses-using-pydirectinput-too-slow
# BTW some games ignore events if they happen at the same time, so better to add some delay between actions
defaultDelay = pydirectinput.PAUSE
fastPressDelay = 0.01


# duration in seconds
def Sleep(duration):
    time.sleep(duration)


def KeyPress(key):
    pydirectinput.press(key)


def KeyHold(key, duration):
    startTime = time.time()

    while time.time() - startTime < duration:
        pydirectinput.keyDown(key)

    pydirectinput.keyUp(key)


# 1. duration in seconds
# 2. KeyHold() only put key in a KeyDown state, but for some reason, this does not seem to cause key repeats in some cases.
# So you can use KeySeparatePresses() instead, it presses key for some duration
# 3. what is bFast:
# KeySeparatePresses('w', 2, False): wwwwwww
# KeySeparatePresses('w', 2, True): wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
def KeySeparatePresses(key, duration, bFast=False):
    if bFast:
        pydirectinput.PAUSE=fastPressDelay

    startTime = time.time()

    while time.time() - startTime < duration:
        KeyPress(key)

    if bFast:
        pydirectinput.PAUSE=defaultDelay


def MousePrintPosition():
    print(autoit.mouse_get_pos())


def MouseMove(x, y):
    autoit.mouse_move(x, y)


# 'right', 'left', 'middle'
def MouseClick(button, x=-1, y=-1):
    if x == -1 or y == -1:
        autoit.mouse_click(button)
    else:
        autoit.mouse_click(button, x, y)

