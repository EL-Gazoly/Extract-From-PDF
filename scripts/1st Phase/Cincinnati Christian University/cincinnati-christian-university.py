import re
import csv

# Open the text file
with open('./cincinnati-christian-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+(?: [A-Z]+)?(?: \d+(?:, \d+)+| & [A-Z]+(?: [A-Z]+)? \d+(?:, \d+)+| \d+[A-Za-z])?(?: \d+(?:–\d+)?(?:/[A-Z]+(?: [A-Z]+)? \d+(?:–\d+)?)?)?)\s+([^\(\n]+)\s+\(([^)]+)\)\s+([\s\S]+?)(?=\n[A-Z]+(?: [A-Z]+)? \d+(?:–\d+)?(?:/[A-Z]+(?: [A-Z]+)? \d+(?:–\d+)?)?|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        name = match[1].strip()
        hours = match[2].strip() if match[2] else '0'  # Set to '0' if hours are not provided
        description = match[3].strip()

        # Store the extracted course data in a dictionary
        course_info = {
            'Code': code,
            'Title': name,
            'Hours': hours,
            'Description': description
        }

        # Append the course data to the list
        course_data.append(course_info)

# Check if there are any courses in the description format
# and extract them separately
additional_courses = re.findall(r'([A-Z]+(?: [A-Z]+)?(?: \d+(?:, \d+)+| \d+[A-Za-z])?(?: \d+(?:–\d+)?(?:/[A-Z]+(?: [A-Z]+)? \d+(?:–\d+)?)?)?)\s+([^\(\n]+)', txt_content)
for course in additional_courses:
    code = course[0]
    name = course[1].strip()

    # Store the extracted course data in a dictionary
    course_info = {
        'Code': code,
        'Title': name,
        'Hours': '0',  # Set to '0' for courses without specified hours
        'Description': ''
    }

    # Append the course data to the list
    course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('cincinnati-christian-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'hours', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['Code'], course['Title'], course['Hours'], course['Description']])

print("CSV file 'cincinnati-christian-university.csv' has been created with the extracted course data.")
