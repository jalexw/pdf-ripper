# This program aims to make it easy to rip a PDF from the unbelievably
# awful bibliu.com website that makes it impossible to annotate the
# online textbooks which you have purchased. I wrote this so I could
# highlight / draw in the GoodNotes app and do business cases "within"
# the textbook.

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
output_file_name = "bibliu_sucks.pdf"
combine_images_into_pdf(screenshots, output_file_name)

print("Done! Enjoy your PDF! (Saved to " + output_file_name + ")")
