import matplotlib.pyplot as plt
from pdf2image import convert_from_path

import os
import sys

pdf_path = sys.argv[1]
png_path = pdf_path.replace('.pdf', '.png')

# assert only one page

if not os.path.exists(png_path):
    pages = convert_from_path(pdf_path, 300)
    assert len(pages) == 1
    pages[0].save(png_path, 'PNG')