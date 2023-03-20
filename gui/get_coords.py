# GUI Library
import PySimpleGUI as sg

# Threads
import threading

# Pause while giving the user time to select a coordinate with the mouse
from time import sleep

# Error Message if unable to get mouse coordinates
from gui.status import showErrorMessage

# Get mouse coordinates
from lib.mouseposition import get_mouse_position

# Disable all elements of the GUI
from gui.layout import DisableAllElements, EnableAllElements

# Custom GUI Window
from gui.window import window

# Ran in a seperate thread so GUI doesn't stall.
# Sends "take-mouse-coordinates" event when countdown finished
def GrabCoordinatesCountdownThread(key: str, countdown: int = 5):
  # Update button with countdown timer
  for i in range(countdown, 0, -1):
    window.write_event_value("update-button-countdown", (key, i))
    sleep(1.0)
  window.write_event_value("take-mouse-coordinates", (key))
  return

# Click-handler for coordinate selection buttons
def CoordinateSelectionButtonClickHandler(key: str, dev: bool = False):
  # Disable all elements of the GUI
  DisableAllElements(window)

  # Seconds to count down from before taking the mouse cursor position
  countdownLength: int = 5

  # Make countdown shorter in dev mode for faster testing
  if dev:
    print("\tCoordinate selection button clicked: ", key)
    countdownLength = 2
  
  # Start the countdown thread
  threading.Thread(
    target=GrabCoordinatesCountdownThread,
    args=(key, countdownLength),
    daemon=True
  ).start()
  # Return this thread to GUI event loop (GUI re-enabled after countdown)
  return

# Update button text with current countdown timer
def UpdateCountdown(key: str, seconds: int, dev: bool = False):
  if dev:
    print("\t\tUpdate button countdown event ({i})".format(i=seconds))
  window[key].update(disabled=True, text="{i}".format(i=seconds))
  return

# Activated by "take-mouse-coordinates" event sent by countdown thread
def TakeMouseCoordinates(coordinate_selection_button_key: str, dev: bool = False):
  if dev:
    print("\tTake mouse coordinates event (countdown finished)")

  # Get coordinates of mouse cursor
  try:
    coords: tuple[float, float] = get_mouse_position()

    # Update button with coordinates to show selection
    newButtonText = "({x}, {y})".format(x=coords[0], y=coords[1])
    window[coordinate_selection_button_key].update(disabled=False, text=newButtonText)
    window[coordinate_selection_button_key].metadata = coords

    if dev:
      print("\t\tCoordinates:", window[coordinate_selection_button_key].metadata)
    
    # Re-enable all elements of the GUI
    EnableAllElements(window)
    return
  except:
    showErrorMessage(
      window,
      "Unable to get mouse coordinates.\nEnsure mouse is on your primary monitor/screen.",
      dev
    )
    return