# BibliU PDF Ripper

## Installation
- Install [Python3](https://www.python.org/downloads/) (check if you already have it installed with the `python3 --version` command)
- Install the required package [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) using the command `pip3 install pyautogui`
- Clone this repository: `git clone https://github.com/jalexw/bibliu-pdf-ripper.git` (or download as a ZIP archive by hitting the green 'Code' button at the top of this page)

## Usage / Execution
- Open up BibliU on the web to the textbook you would like to rip. Resize your browser so the entire page is visible and can be screenshot.
- Run the command `python3 bibliu-pdf-ripper.py` after changing your working directory to the repository folder.
- You will have to enter the number of pages in your textbook.
- You can enter the start/finish page here if you don't want to rip the entire textbook and just a chapter.
- Enter whether coordinates should be doubled (see [this issue](https://github.com/python-pillow/Pillow/issues/3293) for more details). It seems like you should double them on Mac but not on Windows? Probably depends on your computer? Try both and see what works for you.
- Next, select the region on your screen that should be screenshot. You do this by hovering your mouse over the top left corner and the bottom right corner of the area that should be screenshot.
- Finally, hover your mouse over the page selection menu at the bottom of the page to tell the script where it should type in new page numbers to change the page.
- The script will take control of your mouse and keyboard while it generates the PDF! Don't touch anything while it works its magic!
- If everything worked succesfully then a new PDF file should appear in the folder made from all of the screenshots!

## Tips & Tricks
- Make the textbook pages as large as you can so you get better resolution screenshots.
  - Make your web browser window as big as possible.
  - Play around with zooming in/out
  - If you are using Google Chrome you can open the developer tools menu to resize the textbook viewer better (Hit 'Command + Option + I' on Mac to open Dev. Tools).
- The app only takes screenshots on your primary monitor. If you have two screens hooked up you can use your secondary screen to start the script while the textbook is open on your primary monitor.
- If your images are coming out low quality try using a friend's computer with a higher resolution screen. I got great results on a Macbook Pro. The PDF quality depends on the screenshot quality. If you have a low resolution screen it will be difficult to get high resolution screenshots.

## Contributing
I've only tested this on Mac and Windows. However, I believe it should work on Linux as well! Feel free to make a pull request if you want to add any features or fix it for Linux :)
