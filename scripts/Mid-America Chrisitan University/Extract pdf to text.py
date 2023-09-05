from docx import Document

# Define the input Word document file path
input_docx_file = 'mid-america-chrisitan-university.docx'

# Define the output text file path
output_txt_file = 'mid-america-chrisitan-university.txt'

# Define the page range you want to extract (inclusive)
start_page = 131  # Replace with the starting page number
end_page = 169    # Replace with the ending page number

try:
    # Open the Word document
    doc = Document(input_docx_file)

    # Initialize an empty text string to store the extracted text
    extracted_text = ""

    # Iterate through the paragraphs in the specified page range
    for page, paragraph in enumerate(doc.paragraphs, start=1):
        if start_page <= page <= end_page:
            extracted_text += paragraph.text + "\n"

    # Write the extracted text to the output text file
    with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
        txt_file.write(extracted_text)

    print(f"Successfully converted pages {start_page}-{end_page} to '{output_txt_file}'.")

except Exception as e:
    print(f"An error occurred: {str(e)}")
