# BibliU PDF Ripper

## Installation
- Install [Python3](https://www.python.org/downloads/) (check if you already have it installed with the `python3 --version` command)
- Install the required package [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) using the command `pip3 install pyautogui`
- Clone this repository: `git clone https://github.com/jalexw/bibliu_sucks.git` (or download as a ZIP archive)

## Usage / Execution
- Open up BibliU on the web to the textbook you would like to rip. Resize your browser so the entire page is visible and can be screenshot.
- Run the command `python3 bibliu_sucks.py` after changing your working directory to the repository folder.
- You will have to enter the number of pages in your textbook and whether coordinates should be doubled (see [this issue](https://github.com/python-pillow/Pillow/issues/3293) for more details). 
- Next, select the region on your screen that should be screenshot. You do this by hovering your mouse over the top left corner and the bottom right corner of the area that should be screenshot.
- Finally, hover your mouse over the page selection menu at the bottom of the page to tell the script where it should type in new page numbers to change the page.
- The script will take control of your mouse and keyboard while it generates the PDF! Don't touch anything while it works its magic!
- If everything worked succesfully then a new PDF file should appear in the folder made from all of the screenshots!

## Contributing
I've only tested this on Mac although I believe it should work on Windows and Linux as well! Feel free to make a pull request if you want to add any features or fix it for Windows / Linux :)