#!/usr/bin/env python

'''
usage:   cat.py <first.pdf> [<next.pdf> ...]
Creates cat.<first.pdf>
This file demonstrates two features:
1) Concatenating multiple input PDFs.
2) adding metadata to the PDF.
'''

from pdf2image import convert_from_path, convert_from_bytes
from fpdf import FPDF

images = convert_from_path('/Users/Lappy/Desktop/us_doi.pdf', output_folder='/Users/Lappy/Desktop/')