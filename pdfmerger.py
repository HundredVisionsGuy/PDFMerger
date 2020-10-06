# pdfmerger.py
from pathlib import Path
from PyPDF2 import PdfFileMerger

# Set the base path to this current directory
BASE_PATH = (
    Path.cwd()
    / "input"
)

# Add a BASE_PATH / "filename.pdf" for each page you want to merge
# Make sure you put them in the correct order
pdf_paths = [BASE_PATH / "TestDoc01.pdf",
             BASE_PATH / "TestDoc02.pdf",
             BASE_PATH / "TestDoc03.pdf"]

# If you want a different name for your final PDF
# file, be sure to change it below 
output_filename = "YourMergedDocument.pdf"

if __name__ == "__main__":
    # create a merger object
    pdf_merger = PdfFileMerger()
    
    # append files in pdf_paths
    for path in pdf_paths:
        pdf_merger.append(str(path))

    # write merged contents to file
    output_path = Path.cwd() / "output" / output_filename
    with output_path.open(mode="wb") as output_file:
        pdf_merger.write(output_file)