from pdf2image import convert_from_path
import sys
from PIL import Image, ImageEnhance
from pathlib import Path
from typing import List

import os

if len(sys.argv) != 2:
    print(f"Usage: {__file__} path/to/pdf.pdf")
    exit(1)


original_pdf_filepath = Path(sys.argv[1])

output_dirpath = original_pdf_filepath.parent / f"{original_pdf_filepath.stem}_darkened"
os.makedirs(output_dirpath)

# Store Pdf with convert_from_path function
images: List[Image.Image] = convert_from_path(original_pdf_filepath)
images_darkened = []
for i, im in enumerate(images):
    enhancer = ImageEnhance.Contrast(im)
    im_output = enhancer.enhance(factor=5)
    im_output.save(output_dirpath / f"{i}.png")
    images_darkened.append(im_output)

images_darkened[0].save(output_dirpath / f"{original_pdf_filepath.stem}_darkened.pdf", save_all=True, append_images=images_darkened[1:])
print("Done")
