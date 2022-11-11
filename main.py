from pdf2image import convert_from_path
import sys
from PIL import Image, ImageEnhance
 
 
# Store Pdf with convert_from_path function
images = convert_from_path(sys.argv[1])

for i, im in enumerate(images):
    enhancer = ImageEnhance.Contrast(im)

    factor = 5
    im_output = enhancer.enhance(factor)
    im_output.save(f"./output/{i}.png")

