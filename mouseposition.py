# This file uses the pyautogui library to get the screen size and where the cursor is located

from pyautogui import position, size

# Get the length and width of the primary monitor
def get_screen_size():
  return size()

# Get the location of the cursor on the primary monitor
def get_mouse_position():
  currentMouseX, currentMouseY = position()
  if (currentMouseX < 0 or currentMouseY < 0):
    raise Exception("Mouse is not on the screen. Error.")
  screenX, screenY = get_screen_size()
  if (currentMouseX > screenX or currentMouseY > screenY):
    raise Exception("Mouse is not on the screen. Error.")
  return currentMouseX, currentMouseY
