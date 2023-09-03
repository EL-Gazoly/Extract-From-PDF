import re
import csv

# Open the text file
with open('./the-redlands-community-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\s+\d+(?:-\d+)?\s*)(?:\s+(.+?))?\s+([\s\S]*?)((?=\w+\s+\d+(?:-\d+)?\s+)|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0].strip()
        name = match[1].strip() if match[1] else ""
        description = match[2].strip()
        credit_hours = int(re.search(r'\d$', code).group())

        course_data.append({
            'Code': code,
            'Title': name,
            'Credits': credit_hours,
            'Description': description
        })

# Write the extracted course data to a CSV file
with open('the-redlands-community-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['Code', 'Title', 'Credits', 'Description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'the-redlands-community-college.csv' has been created with the extracted course data.")
