import io

import pdftotext
import ocrmypdf
import re

import os.path

class PDFSearch:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_name_clean = self.file_name[:-4]

        # Set the default output directory to be wherever the file is located
        self.file_directory = self.file_path[:-len(self.file_name)]

    # You can OCR a document but not have it load to be analyzed.
    # There an optional parameter to load it after you perform
    # the OCR process.

    def re_ocr(self, **kwargs):
        output_file_suffix = "_ocr.pdf"
        output_file_name = self.file_name_clean + output_file_suffix
        output_file_path = os.path.join(self.file_directory, output_file_name)

        ocrmypdf.api.run(input_file=self.file_path, output_file=output_file_path, force_ocr=True, deskew=True)

    def dump(self, **kwargs):
        output_file_suffix = "_txt_output.txt"
        output_file_name = self.file_name_clean + output_file_suffix
        output_file_path = os.path.join(self.file_directory, output_file_name)

        # Load your PDF
        with open(self.file_path, "rb") as f:
            pdf = pdftotext.PDF(f)

        # How many pages?
        #pdf_length = (len(pdf))

        # Iterate over all the pages
        text = []
        for page in pdf:
            text.append(page)
        text = ''.join(text)

        # Write the text file
        txt_file = open(output_file_path, "w")
        txt_file.write(text)
        txt_file.close()

        print("%s generated in %s" % (output_file_name, self.file_directory)) 


    def pdf_to_dictionary(self):

        return 0