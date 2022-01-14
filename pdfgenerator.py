# This function takes a list of images and combines them into a single PDF file.
def combine_images_into_pdf(images: list, output_file_name: str):
  if (len(images) <= 1):
    raise Exception("Must have at least two images to combine. Just take a screenshot if you just want one page.")
  
  img1 = images[0]
  imgs = images[1:]

  img1.save(output_file_name, "PDF", resolution=100.0, save_all=True, append_images=imgs)

  return
