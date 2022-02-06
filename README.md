# BibliU PDF Ripper

## Installation
### 1. Install [Python3](https://www.python.org/downloads/) 
Check if you already have it installed with the `python --version` command)

### 2. Install the required package [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
Use the command `pip3 install pyautogui`

### 3. Download the free source code in the repository

 - #### 3a. Download as a ZIP archive by hitting the green 'Code' button at the top of this page, then hitting 'Download ZIP'. Extract the code in the ZIP archive to your Desktop.

 - #### 3b. Or, Clone this repository with git: `git clone https://github.com/jalexw/bibliu-pdf-ripper.git`


## Usage / Execution
### 1. Open your textbook in the BibliU web application
- Open up BibliU on the web to the textbook you would like to rip. 
- If you are using Google Chrome you can open the developer tools menu (Hit 'Command + Option + I' on Mac) to resize the textbook page better. BibliU doesn't allow you to right click such that you can open Developer Tools, however, you can do this from the menu in the top right corner of Google Chrome (or with 'Command + Option + I' on Mac).
  

### 2. Resize your browser window to get the screenshots as big as you can
- Screenshots are only taken on your primary monitor.
- It is convenient to start the script from a second monitor where the terminal doesn't block the textbook. Otherwise, 
- Play around with zooming in/out

### 3. Executing the automatic page scrolling and screenshotting script
- Open your terminal / command prompt to the directory this README file is in.
  - You can change your working directory with the `cd` command. e.g. `cd ~/Desktop/bibliu-pdf-ripper` if you saved the code on your Desktop.
  - How to run a Python program on [Windows](https://youtu.be/pFYcAOsNyvs) and [Mac](https://youtu.be/M323OL6K5vs)
- Run the command `python3 bibliu-pdf-ripper.py` after changing your working directory to the repository folder.

### 4. Input settings for PDF ripping
- Enter the number of pages in your textbook.
- Enter the start/finish page here if you don't want to rip the entire textbook and just a chapter.
- Enter whether coordinates of screenshot area should be doubled (see [this issue](https://github.com/python-pillow/Pillow/issues/3293) for more details). It seems like some computers need to have the coordinates doubled, while others don't. Try both (y)es and (n)o and see what works for you.
- Select the region on your screen that should be screenshot. You do this by hovering your mouse over the top left corner and the bottom right corner of the area that should be screenshot.
- Finally, hover your mouse over the page selection menu at the bottom of the page to tell the script where it should type in new page numbers to change the page.

### 5. The script takes control of your device
- The script will take control of your mouse and keyboard while it takes screenshots for the PDF! Don't touch anything while it works its magic! 
- On Mac, a pop-up should make you allow the script to record your screen and use accessibility services.

### 6. Screenshots are combined into a PDF file in the `bibliu-pdf-ripper/output/` folder
- If everything worked succesfully then a new PDF file should appear in the `output` folder made from all of the screenshots!

## Contributing
Tested on Mac and Windows. Feel free to fix it for Linux and make a PR if necessary :)
