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
pdf_path = 'file.pdf'
output_file = 'output.txt'

extracted_text = extract_text_from_pdf(pdf_path)

# Append the extracted text to output.txt without deleting existing content or newlines
with open(output_file, 'a', encoding='utf-8') as f:
    f.write(extracted_text)



print("Text extracted from PDF and appended to output.txt")
