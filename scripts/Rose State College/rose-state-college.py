import re
import csv

# Open the text file
with open('./rose-state-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+(?:\s[A-Z]+)?\s\d{4}-?\d*)\s+(.+?)\s\((\d+|Variable)(?:-\d+-\d+)?\)\s*([\s\S]*?)(?:\nPrerequisite:\s(.*?))?\s*(?=\n[A-Z]+(?:\s[A-Z]+)?\s\d{4}|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_code = match[0]
        course_name = match[1]
        credit_hours = match[2]  # Store it as a string
        description = match[3].strip()
        prerequisite = match[4].strip() if match[4] else 'None'

        # Extract the last digit if it's a numeric value
        if credit_hours.isdigit():
            credit_hours = int(credit_hours)
        # Keep "Variable" as is
        else:
            credit_hours = "Variable"

        course_info = {
            'Code': course_code,
            'Title': course_name,
            'Credits': credit_hours,
            'Description': description + '' + prerequisite
        }

        course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('rose-state-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['Code', 'Title', 'Credits', 'Description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'rose-state-college.csv' has been created with the extracted course data.")
