# GUI Library
import PySimpleGUI as sg
from gui.layout import DisableAllElements

# Threading Library (for ripping thread)
import threading

# Operating System (check if directory exists)
import os

# Ripper Thread
from lib.rip_thread import rip_thread

# Error Messages
from gui.status import hideStatus, showErrorMessage

# Configuration Dataclass
from lib.config import RipConfiguration

# Show an error message and don't start ripping if there is an error with the user's input
def quit_before_rip_with_error_message(window: sg.Window, message: str, dev: bool = False):
  if dev:
    print("Error starting PDF Ripper: ", message)
  showErrorMessage(window, message)
  return

# Validate a tuple of screen coordinates (x, y)
def is_valid_coords_tuple(value, dev: bool = False):
  if (not isinstance(value, tuple) or len(value) != 2):
    if dev:
      print("Invalid coordinate tuple (not tuple): ", value)
    return False
  elif (not isinstance(value[0], float) and not isinstance(value[0], int)):
    if dev:
      print("Invalid value 1 of coordinate tuple (not float/int): ", value)
    return False
  elif (not isinstance(value[1], float) and not isinstance(value[1], int)):
    if dev:
      print("Invalid value 2 of coordinate tuple (not float/int): ", value)
    return False
  elif (value[0] < 0 or value[1] < 0):
    if dev:
      print("Invalid coordinate tuple (negative): ", value)
    return False
  return True

# Function called when the start button is pressed
# Gather all the data from the GUI and start the rip thread
def start_rip(window: sg.Window, values, dev: bool = False):
  # Disable all elements in the GUI (except exit) while ripping
  DisableAllElements(window)
  hideStatus(window)

  if dev:
    print("\tGathering Ripper Configuration from GUI data...")
    print("\t\tValues: ", values)

  try:
    start_page: int = int(values["start_page"])
  except:
    quit_before_rip_with_error_message(window, "Start page must be an integer", dev)
    return

  if start_page < 1:
    quit_before_rip_with_error_message(window, "Start page must be greater than 0", dev)
    return

  try:
    end_page: int = int(values["end_page"])
  except:
    quit_before_rip_with_error_message(window, "End page must be an integer", dev)
    return

  if end_page < start_page:
    quit_before_rip_with_error_message(
      window,
      "End page must be greater than or equal to start page",
      dev
    )
    return

  doubleCoords = values["double_coordinates"]

  if not isinstance(doubleCoords, bool):
    quit_before_rip_with_error_message(
      window,
      "Double coordinates must be a boolean",
      dev
    )
    return

  topLeftCoords = window['select_topleft'].metadata
  bottomRightCoords = window['select_bottomright'].metadata
  pageSelectionCoords = window['select_page_change_box'].metadata

  if not is_valid_coords_tuple(topLeftCoords, dev):
    quit_before_rip_with_error_message(
      window,
      "Top left of screenshot area coordinates are invalid",
      dev
    )
    return
  
  if not is_valid_coords_tuple(bottomRightCoords, dev):
    quit_before_rip_with_error_message(
      window,
      "Bottom right of screenshot area coordinates are invalid",
      dev
    )
    return

  if bottomRightCoords[0] < topLeftCoords[0] or bottomRightCoords[1] < topLeftCoords[1]:
    quit_before_rip_with_error_message(
      window,
      "Coordinates of bottom right of screenshot area must be greater than the top left",
      dev
    )
    return

  if not is_valid_coords_tuple(pageSelectionCoords, dev):
    quit_before_rip_with_error_message(
      window,
      "Page change box coordinates are invalid",
      dev
    )
    return

  outputDir: str = values["outputDir"]

  if (not os.path.isdir(outputDir)):
    quit_before_rip_with_error_message(
      window,
      "Output directory does not exist",
      dev
    )
    return

  config = RipConfiguration(
    start_page=start_page,
    end_page=end_page,
    doubleCoords=doubleCoords,
    topLeftCoords=topLeftCoords,
    bottomRightCoords=bottomRightCoords,
    pageSelectionCoords=pageSelectionCoords,
    outputDir=outputDir
  )
  if dev:
    print("\tStarting up ripper thread...")

  # Start the rip thread
  threading.Thread(
    target=rip_thread,
    args=(window, config, dev),
    daemon=True
  ).start()

  # Continue the GUI event loop
  return

