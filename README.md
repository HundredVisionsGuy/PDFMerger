# PDFMerger.py
This is a simple python project that merges multiple files in the input folder into 1 PDF document in the output folder

## Why?
My wife wanted me to take some images and merge them all into 1 PDF file. I don't have the software installed, so I looked for some free options, but they were all sketchy or clunky.

My Solution: Write a Python program to do it.

## Instructions
1. Place the PDF documents to be merged into the input folder 
2. add a path for each PDF document into the pdf_paths list using the format below:
```
pdf_paths = [BASE_PATH / "TestDoc01.pdf",
             BASE_PATH / "TestDoc02.pdf",
             BASE_PATH / "TestDoc03.pdf"] 
```
3. If you want to change the file name for the final product, change YourMergeDocument.pdf in `output_filename = "YourMergedDocument.pdf"` to the filename you prefer (make sure it ends with '.pdf')

## Future Iterations
Who knows, maybe I'll read the rest of the article and come up with some other features.

## Credits
Pretty much all credit goes to [David Amos](https://realpython.com/team/damos/)'s article on RealPython, titled [Create and Modify PDF Files in Python](https://realpython.com/creating-modifying-pdf/#concatenating-and-merging-pdfs)

All I did was set up the folder structure, change the BASE_PATH to start from the project's root folder, and create a pipenv environment.