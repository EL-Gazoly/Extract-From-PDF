import re
import csv

# Read the text from the input file
with open('./franklin-college.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Regular expression pattern
pattern = re.compile(r'([A-Z\/\s\d]+?[A-Z\/]{3,}\s?\d{3,}[A-Z]*)(?:\s(.+?))?\n(\d+)\s*credit\s?hours?\s+([\s\S]+?)(?=\n[A-Z]{3,4}\s\d{3,4}|$)', re.IGNORECASE)
# Find all matches in the input text
matches = pattern.findall(input_text)

# Initialize a list to store extracted course data
course_data = []

# Append matched data to the course_data list
for match in matches:
    course_code = match[0]
    course_name = match[1].strip()
    credit_hours = match[2].strip()  # Only the number of credit hours
    description = match[3].strip()
    course_data.append([course_code, course_name, credit_hours, description])

# Write the extracted course data to a CSV file
with open('franklin-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header row
    csv_writer.writerow(['Code', 'Name', 'Credit', 'Description'])
    
    # Write course data rows
    csv_writer.writerows(course_data)
        
print("CSV file 'franklin-college.csv' has been created with the extracted course data.")