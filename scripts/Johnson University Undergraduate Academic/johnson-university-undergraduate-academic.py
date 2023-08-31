import re
import csv

# Open the text file
with open('johnson-university-undergraduate-academic.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{4}\s\d{4})\s(.*?)\s\((\d+)\)\.\s((?:.|\n)*?)(?=\n[A-Z]{4}\s\d{4}|$)', re.DOTALL)
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    course_data.extend(matches)

# Write the extracted course data to a CSV file
with open('johnson-university-undergraduate-academic.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'johnson-university-undergraduate-academic.csv' has been created with the extracted course data.")
