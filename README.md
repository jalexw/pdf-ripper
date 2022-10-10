# BibliU PDF Ripper

Use this code to get a PDF from BibliU by automatically looping through your textbook and taking a screenshot of each page.

## Installation
### 1. Install [Python3](https://www.python.org/downloads/) 
Check if you already have it installed or if it already exists with the `python3 --version` command in your Terminal / Command Prompt)

### 2. Install the required python package [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
Install with the command `pip3 install pyautogui`. If you don't have it installed, you will get an error that looks like: `ModuleNotFoundError: No module named 'pyautogui'`.

### 3. Install the required python package [Pillow](https://pillow.readthedocs.io/en/stable/)
Install with the command `pip3 install Pillow`. If you don't have it installed, you will get an error that looks like: `ModuleNotFoundError: No module named 'PIL'`.

### 4. Install the required python package [PySimpleGUI](https://www.pysimplegui.org/en/latest/)
Install with the command `pip3 install pysimplegui`. If you get an error related to tkinter, see [this StackOverflow post](https://stackoverflow.com/questions/5459444/tkinter-python-may-not-be-configured-for-tk). Use brew to install python-tk to fix the problem on Mac, `brew install python-tk`.

### 5. Download the python code in the repository

 - #### 5a. Download as a ZIP archive by hitting the green 'Code' button at the top of this page, then hitting 'Download ZIP'. Extract the code in the ZIP archive to your Desktop.

 - #### 5b. Or, Clone this repository with git using the command: `git clone https://github.com/jalexw/bibliu-pdf-ripper.git`

## Usage / Execution
### 1. Open your textbook in the BibliU web application
- Open up BibliU on the web to the textbook you would like to rip. 

### 2. Resize your browser window to get the screenshots as big as you can
- Screenshots are only taken on your primary monitor.
- If you are using Google Chrome you can open the developer tools menu (Hit 'Command + Option + I' on Mac) to resize the textbook page better. BibliU doesn't allow you to right click such that you can open Developer Tools, however, you can do this from the menu in the top right corner of Google Chrome (or with 'Command + Option + I' on Mac).
- It is convenient to start the script from a second monitor where the terminal doesn't block the textbook. Otherwise, minimize your terminal window after starting the sciprt and selecting the screenshot area.
- Play around with zooming in/out.

### 3. Executing the automatic page scrolling and screenshotting script
- Open your terminal / command prompt to the directory this README file is in.
  - You can change your working directory with the `cd` command. e.g. `cd ~/Desktop/bibliu-pdf-ripper` if you saved the code on your Desktop.
  - Links to tutorials on how to run a Python program on [Windows](https://youtu.be/pFYcAOsNyvs) and [Mac](https://youtu.be/M323OL6K5vs).
- Run the command `python3 bibliu-pdf-ripper.py` after changing your working directory to the repository folder.

### 4. Input settings for PDF ripping
- Enter the number of pages in your textbook.
- Enter the start/finish page here if you don't want to rip the entire textbook and just a chapter.
- Enter whether coordinates of screenshot area should be doubled (see [this issue](https://github.com/python-pillow/Pillow/issues/3293) for more details). It seems like some computers need to have the coordinates doubled, while others don't. Try both (y)es and (n)o and see what works for you.
- Select the region on your screen that should be screenshot. You do this by hovering your mouse over the top left corner and the bottom right corner of the area that should be screenshot.
- Finally, hover your mouse over the page selection menu at the bottom of the page to tell the script where it should type in new page numbers to change the page.

### 5. The script takes control of your device
- The script will take control of your mouse and keyboard while it takes screenshots for the PDF! Don't touch anything while it works its magic! 
- On Mac, a pop-up should ask you to allow the script to record your screen and use accessibility services.
- Screenshots are combined into a PDF file in the `bibliu-pdf-ripper/output/` folder
- If everything worked succesfully then a new PDF file should appear in the `output` folder made from all of the screenshots!

## Contributing
Tested on Mac and Windows. Feel free to fix it for Linux and make a PR if necessary :)
