# Imports
import PySimpleGUI as sg
from mouseposition import get_mouse_position

# Settings elements for the GUI
rip_settings = sg.Frame(
  "Settings", # Frame Title
  [ # Frame content layout
    [sg.Text("Start Page:"), sg.Input(key="start_page", default_text="1")],
    [sg.Text("End Page:"), sg.Input(key="end_page", default_text="1")],
    [sg.Text("Double Coordinates?"), sg.Checkbox("", key="double_coordinates", default=True)],
  ],
  # Frame layout options
  expand_x=True,
  expand_y=True,
)

screenshot_area_selector = [
  [
    sg.Image( # Image showing which corners of the screenshot area to select
      filename="topleftbottomright.png",
      key="screenshot_area_selector_image",
    ),
    sg.Frame( # Buttons to select and display the screenshot area
      "Screenshot Area Coordinates", # Frame title
      [ # Frame content layout
        [sg.Text("Top Left Corner:"), sg.Button("Select", key="select_topleft")],
        [sg.Text("Bottom Right Corner:"), sg.Button("Select", key="select_bottomright")],
      ],
      # Frame layout options
      expand_y=True,
      expand_x=True,
      element_justification="center",
    ),
  ],
]

# Page change box coordinate selector
page_change_box_coordinate_selector = [
  [
    sg.Image( # Image showing where the page change box is
      filename="pagechangebox.png",
      key="page_change_box_coordinate_selector_image",
    ),
    sg.Frame( # Buttons to select and display the page change box
      "Page Change Box Coordinates", # Frame title)
      [ # Frame content layout
        [sg.Text("Page Change Box:"), sg.Button("Select", key="select_page_change_box")],
      ],
      # Frame layout options
      expand_y=True,
      expand_x=True,
      element_justification="center",
    ),
  ]
]

# Function that starts the PDF ripper once inputs has been validated
# Called after clicking the Start button
#def start_ripping(window):
 
# Get the coordinate of the current mouse position
def get_coords(update_button_text):
  update_button_text(5)



# Create layout of GUI
layout = [
  # GUI Header
  [sg.Text("PDF Ripper", justification="center", font=("Helvetica", 25), expand_x=True)],
  [rip_settings],
  [screenshot_area_selector],
  [page_change_box_coordinate_selector],
  [sg.Button("Start", key="start_button", button_color="Green"), sg.Exit(button_color="Red")],
]

window = sg.Window("PDF Ripper", layout, element_padding=6)

# GUI Event Loop
while True:
  event, values = window.read()
  if event == sg.WIN_CLOSED or event == 'Exit':
    break

  # Start button pressed
  if event == "start_button":
    print("Start button pressed")

  # Coordinate selection buttons pressed
  if event == "select_topleft":
    print("Select top left button pressed")

  if event == "select_bottomright":
    print("Select bottom right button pressed")

  if event == "select_page_change_box":
    print("Select page change box button pressed")

window.close()
