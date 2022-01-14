# This file contains the actual logic for getting the screenshots from BibliU and returning a list of images.

from pyautogui import moveTo, write, click, press
from boxscreenshot import box_screenshot
from random import random
from time import sleep

# This function modifies a given duration slightly to make this harder to detect
def modify_delay_randomly(duration: float):
  modifier = (random() - 0.5) * 0.15
  random_delay = duration + modifier
  return random_delay

# This function will move the mouse to the specified coordinates with a small random "human-ish" delay
def moveMouseTo(x: int, y: int, duration: float = 0.5):
  # Generate a random number within 10% of the duration specified
  if (duration > 0):
    moveTo(x, y, modify_delay_randomly(duration))
  else:
    moveTo(x, y)
  return

# Writes the page number to the page number box
def write_page_number(x: int, y: int, pageNumber: str):
  if (not pageNumber.isdigit()):
    raise Exception("Page number passed invalid: " + pageNumber)
  
  # Move the mouse to the box
  moveMouseTo(x, y)
  # Click to select the box
  click()

  # Ensure there is no text in the box
  # Hit right arrow to get to the right side of box
  for i in range(0, 5):
    press('right')
  # Hit backspace to clear the box
  for i in range(0, 5):
    press('backspace')
  press('right')
  press('backspace')
  
  # Write the page number with random delays to make it look like the user is typing
  write(pageNumber, interval=modify_delay_randomly(0.1))

  sleep(modify_delay_randomly(0.1))

  # Press enter to go to the next page
  press('enter')
  return

# This function generates a list of screenshots by looping through each page of the book and taking a screenshot.
def rip(config):
  # Break up the configuration passed to the function

  # The number of pages to be ripped
  num_pages = config[0]

  # The area of the page to be ripped/screenshot
  screenshot_box_coordinates = config[1]
  topLeft, bottomRight = screenshot_box_coordinates

  # The position of the page selection box
  page_selection_box_coordinates = config[2]

  # Print out the configuration
  print("Configuration:")
  print("  Number of pages: " + str(num_pages))
  print("  Screenshot box coordinates:")
  print("    Top left: " + str(topLeft))
  print("    Bottom right: " + str(bottomRight))
  print("  Page selection box coordinates: " + str(config[2]))
  print("  Double Coordinates?: " + str(config[3]))

  # Initialize the list of screenshots
  screenshots = []

  # Loop through each page of the book taking a screenshot and adding to the list
  for i in range(1, num_pages + 1):
    print("") # spacing

    # Write the page number to the page selection box
    print("Going to page " + str(i) + " of " + str(num_pages))
    write_page_number(page_selection_box_coordinates[0], page_selection_box_coordinates[1], str(i))
    
    # The page should now be at the correct page number.

    # Take a screenshot of the page
    print("Ripping page " + str(i) + " of " + str(num_pages))
    screenshot = box_screenshot(topLeft, bottomRight, config[3])

    # Add the screenshot to the list
    screenshots.append(screenshot)

  print("") # spacing

  return screenshots
