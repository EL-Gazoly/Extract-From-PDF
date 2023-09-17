import re
import csv

# Open the text file
with open('./thomas-more-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with descriptions, including the new format
    pattern_with_description = re.compile(r'(\w+\s+[0-9/]+[A-Z]*[/]*[0-9/]*[A-Z]*)\s*[-–]\s*(.*?)\s*\((.*?)\).*?\n(.*?)(?=\w+\s+[0-9/]+\s*[-–]|\Z)', re.DOTALL)

    # Create a regex pattern to match course data without descriptions, including the new format
    pattern_no_description = re.compile(r'(\w+\s+[0-9/]+[A-Z]*[/]*[0-9/]*[A-Z]*)\s*[-–]\s*(.*?)\s*\((.*?)\)|(\w+\s+[0-9/]+[A-Z]*[/]*[0-9/]*[A-Z]*)\s*[-–]\s*(.*?)\s*\n(.*?)\n', re.DOTALL)

    # Initialize a dictionary to store extracted course data with course codes as keys
    course_data = {}

    # Find all matches with descriptions in the text content
    matches_with_description = pattern_with_description.findall(txt_content)
    for match in matches_with_description:
        code = match[0].strip()
        name = match[1].strip()
        credits_match = re.search(r'(\d+)\s*hour', match[2], re.IGNORECASE)
        credit_hours = credits_match.group(1) if credits_match else "0"
        description = match[3].strip() if match[3] else ''

        if code in course_data:
            # If the code already exists, append the new data to the existing course
            course_data[code]['credit hours'] += f" and {credit_hours}"
            course_data[code]['description'] += f"\n{description}"
        else:
            # If the code is not in the dictionary, create a new entry
            course_data[code] = {
                'code': code,
                'name': name,
                'credit hours': credit_hours,
                'description': description
            }

    # Find all matches without descriptions in the text content
    matches_no_description = pattern_no_description.findall(txt_content)
    for match in matches_no_description:
        code = match[0] if match[0] else match[3]
        name = match[1] if match[1] else match[4]
        credits_match = re.search(r'(\d+)\s*hour', match[2] if match[2] else match[5], re.IGNORECASE)
        credit_hours = credits_match.group(1) if credits_match else "0"
        code = code.strip()

        if code in course_data:
            # If the code already exists, append the new data to the existing course
            course_data[code]['credit hours'] += f" and {credit_hours}"
        else:
            # If the code is not in the dictionary, create a new entry
            course_data[code] = {
                'code': code,
                'name': name.strip(),
                'credit hours': credit_hours,
                'description': ''
            }

# Write the extracted course data to a CSV file
with open('thomas-more-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'ttile', 'credit hours', 'description'])

    # Write course data rows
    for course in course_data.values():
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'thomas-more-university.csv' has been created with the extracted course data.")
