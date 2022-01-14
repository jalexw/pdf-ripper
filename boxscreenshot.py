# This file uses the PIL libraries to take screenshots.

from PIL import Image, ImageGrab

# Take a screenshot on the primary monitor given the coordinates of the top left and bottom right corners
def box_screenshot(topLeft: tuple, bottomRight: tuple, doubleCoords: bool):
  topLeftX, topLeftY = topLeft
  bottomRightX, bottomRightY = bottomRight

  if (topLeftX < 0 or topLeftY < 0 or bottomRightX < 0 or bottomRightY < 0):
    raise Exception("Invalid coordinates. Error.")
  if (topLeftX > bottomRightX or topLeftY > bottomRightY):
    raise Exception("Invalid coordinates. Error.")

  if doubleCoords:
    topLeftX *= 2
    topLeftY *= 2
    bottomRightX *= 2
    bottomRightY *= 2
  screenshot = ImageGrab.grab(bbox=(topLeftX, topLeftY, bottomRightX, bottomRightY))
  
  print("Page was ripped.")

  screenshot.load()
  background = Image.new("RGB", screenshot.size, (255,255,255))
  background.paste(screenshot, mask=screenshot.split()[3]) # 3 is the alpha channel
  return background
