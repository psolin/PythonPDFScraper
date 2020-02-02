PythonPDFScraper
===================

## Description
A local webserver giving you the ability to upload PDF files. Take the PDF and OCR it and/or dump the text.

## Installation
First, download the repository.

On a Mac, install XCode:

```xcode-select --install```

Then, install ocrmypdf:
https://github.com/jbarlow83/OCRmyPDF

Lastly, install the requirements:

```sudo pip3 install -r requirements.txt```     

## To Run
```source virtual/bin/activate```

```python3 app.py runserver```

A new web page should open up in your default web browser.

## Issues
The progress bar for OCRing documents is only visible in the Terminal for now. So, be patient while it works!

## Thanks To
jbarlow83 for pikepdf and ocrmypdf
https://github.com/blueimp/jQuery-File-Upload