import os
import time

# This function takes a list of images and combines them into a single PDF file.
def combine_images_into_pdf(images: list, outputDir: str = "output/", filename: str = "pdf_" + time.strftime("%Y-%m-%d-%H-%M-%S") + ".pdf"):
  # Make sure the output/ directory exists
  if not os.path.exists(outputDir):
    print("Making output directory...")
    os.mkdir(outputDir)
  else:
    print("Output directory already exists.")

  # Ensure there are images to be pade into a PDF
  if (len(images) == 0):
    raise Exception("No images passed to function! Error!")

  # Come up with a unique file name for the PDF from the time
  output_file_name = outputDir + filename
  # Create a new PDF file
  outputPath = output_file_name
  if (len(images) == 1): # Only 1 image, don't need to combine
    images[0].save(outputPath, "PDF", resolution=100.0)
    return output_file_name
  else: # There are multiple images, so append them to the PDF
    images[0].save(outputPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    return output_file_name
