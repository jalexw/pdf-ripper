import os

outputDir = "output/"

# This function takes a list of images and combines them into a single PDF file.
def combine_images_into_pdf(images: list, output_file_name: str):
  # Make sure the output/ directory exists
  if not os.path.exists(outputDir):
    os.mkdir(outputDir)

  # Ensure there are images to be pade into a PDF
  if (len(images) == 0):
    raise Exception("No images passed to function! Error!")

  # Create a new PDF file
  outputPath = outputDir + output_file_name
  if (len(images) == 1): # Only 1 image, don't need to combine
    images[0].save(outputPath, "PDF", resolution=100.0)
    return
  else: # There are multiple images, so append them to the PDF
    images[0].save(outputPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    return
