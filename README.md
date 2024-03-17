 # PDF Text Extractor

This Python script extracts text from a PDF file and appends it to a specified output text file without deleting existing content or newlines. It uses the PyPDF2 library to read and parse the PDF file.

## Prerequisites

To use this script, you will need to have the following installed:

* Python 3 or later
* PyPDF2 library

## Usage

To use the script, follow these steps:

1. Install the PyPDF2 library using pip:

```
pip install PyPDF2
pip install 'PyPDF2<3.0'
```

2. Save the following code as `main.py`:

```python
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

# Example usage:
pdf_path = 'fire3.pdf'
output_file = 'output.txt'

extracted_text = extract_text_from_pdf(pdf_path)

# Append the extracted text to output.txt without deleting existing content or newlines
with open(output_file, 'a', encoding='utf-8') as f:
    f.write(extracted_text)

print("Text extracted from PDF and appended to output.txt")
```

3. Replace the `pdf_path` and `output_file` variables with the path to your PDF file and the desired output text file, respectively.

4. Run the script using the following command:

```
python main.py
```

## Explanation

The script works as follows:

1. The `extract_text_from_pdf` function opens the specified PDF file in read binary mode (`'rb'`) and creates a PyPDF2 `PdfFileReader` object.

2. The `numPages` attribute of the `PdfFileReader` object is used to determine the number of pages in the PDF file.

3. A `for` loop is used to iterate over each page in the PDF file.

4. For each page, the `extractText` method of the `Page` object is used to extract the

<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
