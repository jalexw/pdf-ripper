# This program aims to make it easy to rip a PDF from the awful bibliu.com 
# web application that makes it impossible to annotate the online 
# textbooks which you have purchased. I wrote this program so I could
# highlight / draw in the GoodNotes app and not to redistibute the textbooks

from setup import setup
from ripper import rip
from pdfgenerator import combine_images_into_pdf

print("Welcome to the BibliU PDF Ripper! :)")

# Get configuration to rip pages with from the user
config = setup()

# A nice message to the user :D
print("Ready to start ripping? :)")

# Pass the configuration to the main ripper function
screenshots = rip(config)

# Main loop finished. Just have to make the PDF now!
print("All screenshots collected. Combining into PDF file now.")

# Generate output
output_file_name = combine_images_into_pdf(screenshots)

print("Done! Enjoy your PDF! (Saved to " + output_file_name + ")")
