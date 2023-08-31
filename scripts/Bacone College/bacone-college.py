import re
import csv

# Open the text file
with open('./bacone-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\s\d+(?:-\d+)?(?:,\s*-\d+)?(?:-\d+)*)\n(.+?)\n(\d+(?:-\d+)?(?:,\s*-\d+)?(?:-\d+)*)\s*Hour[s]?\n([\s\S]+?)(?=\n\w+\s\d+|\Z)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_code = match[0]
        course_name = match[1]
        credit_hours = match[2]
        description = match[3].replace('\n', ' ')  # Remove newlines within the description
        course_data.append((course_code, course_name, credit_hours, description))

# Write the extracted course data to a CSV file
with open('bacone-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Hours', 'Description'])

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'bacone-college.csv' has been created with the extracted course data.")
