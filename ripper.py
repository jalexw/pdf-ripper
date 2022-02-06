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

  # The number of pages in the textbook
  num_pages = config[0]

  # The area of the page to be ripped/screenshot
  screenshot_box_coordinates = config[1]
  topLeft, bottomRight = screenshot_box_coordinates

  # The position of the page selection box
  page_selection_box_coordinates = config[2]

  # Whether coordinates should be doubled to get the correct screenshot area
  double_coordinates = config[3]

  # Rip all pages or just a subset of them?
  start_page = config[4]
  end_page = config[5]

  # Print out the configuration
  print("Configuration:")
  print("\tPages to rip:")
  print("\t\tTotal number of pages in textbook: " + str(num_pages))
  print("\t\tPage # to start on: " + str(start_page))
  print("\t\tPage # to end on: " + str(end_page))
  print("\tScreenshot box coordinates:")
  print("\t\tTop left: " + str(topLeft))
  print("\t\tBottom right: " + str(bottomRight))
  print("\t\tPage selection box coordinates: " + str(config[2]))
  print("\tDouble Coordinates?: " + str(double_coordinates))

  sleep(2)

  # Initialize the list of screenshots
  screenshots = []

  # Loop through each page of the book taking a screenshot and adding to the list
  for i in range(start_page, end_page + 1):
    print("") # spacing

    # Write the page number to the page selection box
    print("Going to page " + str(i) + " of " + str(num_pages) + "...")
    write_page_number(page_selection_box_coordinates[0], page_selection_box_coordinates[1], str(i))
    # The page should now be at the correct page number.

    # Wait a little bit to allow the page to fully load
    sleep(modify_delay_randomly(0.5))

    # Take a screenshot of the page
    print("Ripping page " + str(i) + " of " + str(num_pages))
    screenshot = box_screenshot(topLeft, bottomRight, double_coordinates)

    # Add the screenshot to the list
    screenshots.append(screenshot)

  print("") # spacing

  return screenshots
