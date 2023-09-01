import re
import csv

# Open the text file
with open('./oakland-city-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data and extract credit hours as numbers
    pattern = re.compile(r'(\w+\s+\d+)\s+(.*?)\s+(\d+(?:-\d+)?)\s+(?:hour|hours)\s+(.*?)\s*(?=\w+\s+\d+|\Z)', re.DOTALL | re.IGNORECASE)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        title = match[1].strip()
        credits = match[2].strip()
        description = match[3].strip()

        course_data.append({
            'code': code,
            'name': title,
            'credit hours': credits,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('oakland-city-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credit hours', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'oakland-city-university.csv' has been created with the extracted course data.")
