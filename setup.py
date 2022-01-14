# This file will get the information from the user on the area the document is located to be ripped.
# As well as the number of pages to rip.

from mouseposition import get_mouse_position
from timeutils import five_second_timer, short_pause

# Have the user type in the number of pages in the document
def get_number_of_pages():
  print("How many pages are in the document you are trying to copy?")
  return int(input())

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
  print("For some reason on my Mac I had to double all coordinates of the screenshot area to get correct images...")
  print("If your screenshots are not coming out right after trying one setting then try the opposite setting.")
  print("Do you want to double the coordinates? (Y/n)")
  response = input()
  return response.lower() == "y" or response.lower() == "yes"

# Uses the other setup functions to collect all the necessary information as a tuple
def setup():
  short_pause()

  n_pages = get_number_of_pages()

  short_pause()

  should_coords_be_doubled_bool = should_coords_be_doubled()

  short_pause()

  topLeftCoords, bottomRightCoords = get_screenshot_box()

  short_pause()

  page_selection_box_X, page_selection_box_Y = get_page_selection_box_coordinates()

  short_pause()

  return n_pages, (topLeftCoords, bottomRightCoords), (page_selection_box_X, page_selection_box_Y), should_coords_be_doubled_bool
