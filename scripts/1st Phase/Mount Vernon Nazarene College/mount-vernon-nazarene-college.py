import re
import csv

# Open the text file
with open('./mount-vernon-nazarene-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Za-z0-9]+\s\d{4}[A-Za-z]?) - ([^\n]+)\s\(([\d\s-]+)\)(?:\s+([\s\S]*?)(?=(?:[A-Za-z0-9]+\s\d{4}[A-Za-z]?)|$))')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]
        name = match[1].strip()
        credit_hours = match[2].replace(" ", "").replace("-", " - ")
        description = match[3].strip()

        # Append the extracted data as a dictionary
        course_data.append({
            'code': code,
            'name': name,
            'credit hours': credit_hours,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('mount-vernon-nazarene-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'mount-vernon-nazarene-college.csv' has been created with the extracted course data.")
