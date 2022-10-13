# GUI Library
import PySimpleGUI as sg

# Settings elements for the GUI
rip_settings = sg.Frame(
  "Settings", # Frame Title
  [ # Frame content layout
    [
      sg.Text("Start Page:"),
      sg.Input(
        key="start_page",
        default_text="1",
        tooltip="What page to start ripping from",
        expand_x=True
      )
    ],
    [
      sg.Text("End Page:"),
      sg.Input(
        key="end_page",
        default_text="1",
        tooltip="What page to stop ripping at",
        expand_x=True
      )
    ],
    [
      sg.Text("Double Coordinates?"),
      sg.Checkbox(
        "",
        key="double_coordinates",
        default=True,
        tooltip="Check this if pages are not coming out correctly. My Mac needed it but not my Windows PC."
      )
    ],
    [
      sg.Text('Output Directory:'),
      sg.In(enable_events=True, key='outputDir', expand_x=True),
      sg.FolderBrowse()
    ]
  ],
  # Frame layout options
  expand_x=True,
  expand_y=True,
)

screenshot_area_selector = [
  [
    sg.Image( # Image showing which corners of the screenshot area to select
      filename="media/topleftbottomright.png",
      key="screenshot_area_selector_image",
    ),
    sg.Frame( # Buttons to select and display the screenshot area
      "Screenshot Area Coordinates", # Frame title
      [ # Frame content layout
        [
          sg.Text("Top Left Corner:"),
          sg.Button(
            "Select Coords",
            key="select_topleft",
            disabled=False,
            disabled_button_color=("white", "gray"),
            tooltip="Hover your mouse at the top left corner of the screenshot area"
          )
        ],
        [
          sg.Text("Bottom Right Corner:"),
          sg.Button(
            "Select Coords",
            key="select_bottomright",
            disabled=False,
            disabled_button_color=("white", "gray"),
            tooltip="Hover your mouse at the bottom right corner of the screenshot area"
          )
        ],
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
      filename="media/pagechangebox.png",
      key="page_change_box_coordinate_selector_image",
    ),
    sg.Frame( # Buttons to select and display the page change box
      "Page Change Box Coordinates", # Frame title)
      [ # Frame content layout
        [
          sg.Text("Page Change Box:"),
          sg.Button(
            "Select Coords",
            key="select_page_change_box",
            disabled=False,
            disabled_button_color=("white", "gray"),
            tooltip="Hover your mouse where the page change box (where to type new page numbers)"
          )
        ],
      ],
      # Frame layout options
      expand_y=True,
      expand_x=True,
      element_justification="center",
    ),
  ]
]


# Create layout of GUI
layout = [
  # Settings (page #s, double coordinates)
  [rip_settings],
  # Screenshot Area Selector
  [screenshot_area_selector],
  # Page Change Box Coordinate Selector
  [page_change_box_coordinate_selector],
  [sg.HorizontalSeparator()],
  # Error Message and Progress Bar
  [
    sg.Text(
      "",
      key="info_message",
      text_color="red",
      background_color="white",
      expand_x=True,
      visible=False,
      font=("Helvetica", 14)
    )
  ],
  [
    sg.ProgressBar(
      100,
      orientation="h",
      size=(20, 20),
      key="progress_bar",
      bar_color=("green", "white"),
      expand_x=True,
      visible=False
    )
  ],
  # Start and Exit Buttons
  [
    sg.Button(
      "Start Ripping",
      key="start_button",
      button_color="Green",
      disabled=False,
      disabled_button_color=("white", "gray"),
      expand_x=True,
    ),
    sg.Exit(button_color="Red")
  ],
]

# Disable all elements of the GUI
def DisableAllElements(window: sg.Window):
  window["start_page"].update(disabled=True)
  window["end_page"].update(disabled=True)
  window["double_coordinates"].update(disabled=True)
  window["select_topleft"].update(disabled=True)
  window["select_bottomright"].update(disabled=True)
  window["select_page_change_box"].update(disabled=True)
  window["start_button"].update(disabled=True)
  return

# Enable all elements of the GUI
def EnableAllElements(window: sg.Window):
  window["start_page"].update(disabled=False)
  window["end_page"].update(disabled=False)
  window["double_coordinates"].update(disabled=False)
  window["select_topleft"].update(disabled=False)
  window["select_bottomright"].update(disabled=False)
  window["select_page_change_box"].update(disabled=False)
  window["start_button"].update(disabled=False)
  return
