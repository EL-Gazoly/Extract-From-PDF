import re
import csv

# Open the text file
with open('./southeastern-oklahoma.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+ \d{4})\s+(.*?)(?:\n(.*?))?(?=\n\w+ \d{4}|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, description = match
        course_data.append({
            'code': code.strip(),
            'name': title.strip(),
            'description': description.strip() if description else ''
        })

# Write the extracted course data to a CSV file
with open('southeastern-oklahoma.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['description']])

print("CSV file 'southeastern-oklahoma' has been created with the extracted course data.")
