# GUI Library
import PySimpleGUI as sg

# Application Layout
from gui.layout import layout

# Application Title
title: str = "PDF Ripper"

window = sg.Window(title, layout, element_padding=6)
