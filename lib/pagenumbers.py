# This file contains helper functions for moving between textbook pages in the ripper thread

from pyautogui import moveTo, write, click, press
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
