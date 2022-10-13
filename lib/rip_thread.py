# GUI Library
import PySimpleGUI as sg

# Configuration Dataclass
from lib.config import RipConfiguration

# Ripper Helper Functions
from lib.pagenumbers import write_page_number
from lib.screenshot import box_screenshot

# Generates the PDF from the screenshots
from lib.pdfgenerator import combine_images_into_pdf

# Update the progress bar on the GUI after each screenshot
def sendUpdateToGUI(window: sg.Window, screenshot_index: int, total_pages: int, dev: bool = False):
  if dev:
    print("\tSending progress update to GUI from Ripped thread... ({numerator}/{denominator})".format(
      numerator=screenshot_index,
      denominator=total_pages
    ))
  window.write_event_value("rip-status-update", (screenshot_index, total_pages))
  return

# Replace the progress bar with an error message if ripping fails
def sendErrorToGUI(window: sg.Window, error: str):
  window.write_event_value("rip-error", error)
  return

def rip_thread(window: sg.Window, config: RipConfiguration, dev: bool = False):
  # Start ripping
  if dev:
    print("Ripper Thread started: ", config)

  # Initialize the list of screenshots
  screenshots = []

  # Total number of pages to be screenshot (end_page - start_page + 1)
  total_pages = config.end_page - config.start_page + 1

  # Loop through each page of the book taking a screenshot and adding to the list
  for i in range(config.start_page, config.end_page + 1):
    screenshot_index = i - config.start_page

    # Update the progress bar on the GUI
    sendUpdateToGUI(window, screenshot_index, total_pages, dev)

    if dev:
      print("")
      print(
        "\tGoing to page {currentPage}... ({numerator}/{denominator})".format(
          currentPage=i,
          numerator=screenshot_index + 1,
          denominator=total_pages
        )
      )

    write_page_number(config.pageSelectionCoords[0], config.pageSelectionCoords[1], str(i))

    # Take a screenshot of the page
    if dev:
      print(
        "\tRipping page {currentPage}... ({numerator}/{denominator})".format(
          currentPage=i,
          numerator=screenshot_index + 1,
          denominator=total_pages
        )
      )
    screenshot = box_screenshot(
      config.topLeftCoords,
      config.bottomRightCoords,
      config.doubleCoords
    )

    # Add the screenshot to the list
    screenshots.append(screenshot)

    if dev:
      print("\tPage {currentPage} ripped successfully!".format(currentPage=i))
  
  # Make sure progress bar is full
  sendUpdateToGUI(window, total_pages, total_pages, dev)

  if dev:
    print("\n\tFinished taking screenshots of all {total} pages.\n".format(total=total_pages))

  # Create a PDF from the screenshots
  output_filename = combine_images_into_pdf(screenshots, config.outputDir)

  # Send a success message to the GUI with the output filename
  window.write_event_value("rip-success", output_filename)
  return
  