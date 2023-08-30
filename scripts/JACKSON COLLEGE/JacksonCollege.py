import PyPDF2
import re
import csv

# Open the PDF file
with open('./JacksonCollege.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{3,4}\s\d{3})\s(.+?)\s\((\d+)\sCR\)\s([\s\S]+?)(?=\n[A-Z]{3,4}\s\d{3}|$)')
    
    # Initialize a list to store extracted course data
    course_data = []
    
    # Iterate through each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        page_text = pdf_reader.pages[page_num].extract_text()
        matches = pattern.findall(page_text)
        
        # Append matched data to the course_data list
        course_data.extend(matches)
        
# Write the extracted course data to a CSV file
with open('JacksonCollege.csv.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header row
    csv_writer.writerow(['Course Code', 'Course Title', 'Credit Hours', 'Description'])
    
    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)
        
print("CSV file 'course_data.csv' has been created with the extracted course data.")
