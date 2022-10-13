import time

# This function takes a list of images and combines them into a single PDF file.
def combine_images_into_pdf(images: list, outputDir: str):
  # Ensure there are images to be made into a PDF
  if (len(images) == 0):
    raise Exception("No images passed to function! Error!")

  # Come up with a unique file name for the PDF from the time
  filename: str = "rip-{t}.pdf".format(t=time.strftime("%Y-%m-%d-%H-%M-%S"))
  # Get the path to write the PDF file to
  if (outputDir[-1] == "/"):
    outputPath = outputDir + filename
  else:
    outputPath = outputDir + "/" + filename

  # If only 1 image, don't need to combine, just convert to PDF
  if (len(images) == 1):
    images[0].save(outputPath, "PDF", resolution=100.0)
    return outputPath

  # There are multiple images, so append them to the PDF
  else: 
    images[0].save(outputPath, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
    return outputPath
