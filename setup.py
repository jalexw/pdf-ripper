# This file will get the information from the user on the area the document is located to be ripped.
# As well as the number of pages to rip.

from mouseposition import get_mouse_position
from timeutils import five_second_timer, short_pause
from config import RipConfiguration

# Have the user type in the number of pages in the document
def get_number_of_pages():
  print("How many pages are in the textbook you are trying to copy?")
  try:
    n_pages = int(input())
  except:
    raise Exception("Invalid integer entered.")

  print("What page do you want to start at? (DEFAULT=1)")
  try:
    start_page = input()
    if start_page == "":
      start_page = 1
    else:
      start_page = int(start_page)
    if start_page < 1 or start_page > n_pages:
      raise Exception("Page number out of range. Please try again.")
  except:
    raise Exception("Invalid integer entered or not within page range.")

  print("What page do you want to end on? (DEFAULT=" + str(n_pages) + ")")
  try:
    end_page = input()
    if end_page == "":
      end_page = n_pages
    else:
      end_page = int(end_page)
    if end_page < 1 or end_page > n_pages or end_page < start_page:
      raise Exception("Ending page number out of range. Please try again.")
  except:
    raise Exception("Invalid integer entered or not within page range.")
  
  return n_pages, start_page, end_page

# This function will get the coordinates of the top left and bottom right corners of the area to be screenshot.
def get_screenshot_box():
  # Get top left coordinates
  print("Position the cursor over the top left corner of the screenshot area. You have 5 seconds to do so.")
  five_second_timer()
  X1, Y1 = get_mouse_position()

  # Get bottom right coordinates
  print("Position the cursor over the bottom right corner of the screenshot area. You have 5 seconds to do so.")
  five_second_timer()
  X2, Y2 = get_mouse_position()

  # Ensure that the coordinates are in the correct order
  if X1 > X2 or Y1 > Y2:
    raise Exception("Do you have your lefts and rights or ups and down mixed up? Error.")

  return (X1, Y1), (X2, Y2)

# Get the position on the screen where the program should click to type in the page number of the next page
def get_page_selection_box_coordinates():
  print("Position the cursor over 'page input' box (i.e. where you type in the page number at the bottom). You have 5 seconds to do so.")
  five_second_timer()
  X, Y = get_mouse_position()
  return X, Y

def should_coords_be_doubled():
  print("I had to double all coordinates of the screenshot area to get correct images...")
  print("If your screenshots are not coming out right after trying one setting then try the opposite setting.")
  print("Do you want to double the coordinates? (Y/n)")
  response = input()
  return response.lower() == "y" or response.lower() == "yes"

# Uses the other setup functions to collect all the necessary information as a tuple
def setup():
  # Create a RipConfiguration object
  config = RipConfiguration()

  short_pause()

  config.n_pages, config.start_page, config.end_page = get_number_of_pages()

  short_pause()

  config.should_coords_be_doubled_bool = should_coords_be_doubled()

  short_pause()

  config.topLeftCoords, config.bottomRightCoords = get_screenshot_box()

  short_pause()

  config.page_selection_box_X, config.page_selection_box_Y = get_page_selection_box_coordinates()

  short_pause()

  return config.n_pages, (config.topLeftCoords, config.bottomRightCoords), (config.page_selection_box_X, config.page_selection_box_Y), config.should_coords_be_doubled_bool, config.start_page, config.end_page
