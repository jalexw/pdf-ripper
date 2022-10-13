# GUI Library
import PySimpleGUI as sg

# Get mouse coordinates for screenshot area/page change box
from gui.get_coords import CoordinateSelectionButtonClickHandler, TakeMouseCoordinates, UpdateCountdown

# Custom GUI Window
from gui.window import window

# Start the PDF ripper
from gui.start_rip import start_rip

# Status Messages / Error Messages
from gui.status import showErrorMessage, showProgressBar, showSuccessMessage

# Call function to open the GUI and create the event loop
def run(dev: bool = False):
  if dev:
    print("Opening PDF Ripper GUI... (Development Mode)")

  # GUI Event Loop
  while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
      if dev:
        print("Exiting PDF Ripper...")
      break

    # Start button pressed
    if event == "start_button":
      start_rip(window, values, dev)

    # Coordinate selection button pressed
    if event == "select_topleft":
      CoordinateSelectionButtonClickHandler("select_topleft", dev)
    # Coordinate selection buttons pressed
    if event == "select_bottomright":
      CoordinateSelectionButtonClickHandler("select_bottomright", dev)
    # Coordinate selection buttons pressed
    if event == "select_page_change_box":
      CoordinateSelectionButtonClickHandler("select_page_change_box", dev)

    # Update countdown on selected coordinate selection button
    if event == "update-button-countdown":
      UpdateCountdown(values["update-button-countdown"][0], values["update-button-countdown"][1])

    # Get the coordinates of the cursor once the countdown has finished
    if event == "take-mouse-coordinates":
      TakeMouseCoordinates(values["take-mouse-coordinates"], dev)

    # Update the Error Message or Progress Bar based on Ripper status
    if event == "rip-status-update":
      showProgressBar(window, values["rip-status-update"][0], values["rip-status-update"][1], dev)
    # Show errors from the rip thread
    if event == "rip-error":
      showErrorMessage(window, values["rip-error"], dev)
    # Rip thread has finished ripping -> show output file location
    if event == "rip-success":
      showSuccessMessage(window, values["rip-success"], dev)

  # Close the GUI window
  window.close()
