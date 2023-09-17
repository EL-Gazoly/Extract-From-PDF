import re
import csv

# Open the text file
with open('./zane-state-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+ \d{4}) - ([^\n]+?)\s*\((\d+(?:-\d+)?)\s*credit hour(?:s)?[^\n]*\s*-\s*([^\n]+?)\)\s*(.*?)(?=\w+ \d{4} -|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    
    for match in matches:
        course_code = match[0]
        course_title = match[1]
        credit_hours = match[2]
        description = match[4].strip()
        
        course_data.append([course_code, course_title, credit_hours, description])

# Write the extracted course data to a CSV file
with open('zane-state-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'zane-state-college.csv' has been created with the extracted course data.")
