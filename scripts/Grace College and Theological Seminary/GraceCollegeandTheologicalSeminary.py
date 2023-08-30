import re
import csv

# Read the text from the input file
with open('./GraceCollegeandTheologicalSeminary.pdf', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Create a regex pattern to match course data
pattern = re.compile(r'([A-Z]{3,4}\s\d{4})\s(.+?)\n([\s\S]+?)(\w+\s+hours)\.')

# Initialize a list to store extracted course data
course_data = []

# Find all matches in the input text
matches = pattern.findall(input_text)

# Append matched data to the course_data list
for match in matches:
    course_data.append([match[0], match[1], match[2].strip(), match[3]])

# Write the extracted course data to a CSV file
with open('GraceCollegeandTheologicalSeminary.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Write header row
    csv_writer.writerow(['Course Code', 'Course Title', 'Description', 'Credit Hours'])
    
    # Write course data rows
    csv_writer.writerows(course_data)
        
print("CSV file 'course_data.csv' has been created with the extracted course data.")
