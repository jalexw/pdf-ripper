# GUI Library
import PySimpleGUI as sg

# Re-enable input elements
from gui.layout import EnableAllElements

def hideMessage(window: sg.Window):
  window['info_message'].update(value="", visible=False)
  return

def hideProgressBar(window: sg.Window):
  window['progress_bar'].update(visible=False)
  return

def showErrorMessage(window: sg.Window, message: str, dev: bool = False):
  if dev:
    print("\tRip error event: ", message)
  hideProgressBar(window)
  window['info_message'].update(
    value=message,
    visible=True,
    text_color="red",
  )
  EnableAllElements(window)
  return

def showSuccessMessage(window: sg.Window, outputFilename: str, dev: bool = False):
  if dev:
    print("\tRip success event: ", outputFilename)
  hideProgressBar(window)
  window['info_message'].update(
    value="Rip complete! Output file:\n" + outputFilename,
    visible=True,
    text_color="green",
  )
  EnableAllElements(window)
  return

def showProgressBar(window: sg.Window, current: int, total_pages: int, dev: bool = False):
  if dev:
    print("\tGUI updating progress bar: ", current, "/", total_pages)
  hideMessage(window)
  window['progress_bar'].update(
    current_count=current,
    max=total_pages,
    visible=True
  )
  return

def hideStatus(window: sg.Window):
  hideMessage(window)
  hideProgressBar(window)
  return