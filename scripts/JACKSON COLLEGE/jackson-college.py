import re
import csv

# Open the text file
with open('./jackson-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{3,4}\s\d{3})\s(.+?)\s\((\d+-?\d?)\s?CR\)\s([\s\S]+?)(?=\n[A-Z]{3,4}\s\d{3}|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    course_data.extend(matches)

# Write the extracted course data to a CSV file
with open('jackson-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'jackson-college.csv' has been created with the extracted course data.")
