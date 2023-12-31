import re
import csv

# Open the text file
with open('./crowder-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+ \d+)\s+\S+\s+(.*?)\s+\((.*?)\)\s+(\d+(?:\.\d+)?)\s+(?:Credit|Credits)\s+([\s\S]*?)(?=\n[A-Z]+\s+\d+|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]
        name = match[1]
        credit_hours = match[3]
        description = match[4].strip()

        # If "(Prerequisite:" is not found in the description, append it to the description
        if "(Prerequisite:" not in description:
            description += " (Prerequisite: None)"

        course_data.append({
            'code': code,
            'name': name,
            'credit hours': credit_hours,
            'description': description,
        })

# Write the extracted course data to a CSV file
with open('crowder-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Name', 'Credit Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'crowder-college.csv' has been created with the extracted course data.")
