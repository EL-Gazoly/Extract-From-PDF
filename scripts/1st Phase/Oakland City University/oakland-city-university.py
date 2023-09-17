import re
import csv

# Open the text file
with open('./oakland-city-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data and extract required fields
    pattern = re.compile(r'(\w{1,4}\s\d{3})\s+([^\d]+)\s+(\d+(?:\.\d+)?(?:-\d+(?:\.\d+)?)?)\s+(.*?)\s*(?:Prerequisite: (.*?))?(?=\n\w{1,4}\s\d{3}|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        title = match[1].strip()
        credits = match[2]
        description = match[3].strip()
        prerequisite = match[4].strip() if match[4] else "None"

        # Concatenate Prerequisite with the description
        description += "\nPrerequisite: " + prerequisite if prerequisite != "None" else ""

        course_data.append({
            'code': code,
            'name': title,
            'credits': credits,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('oakland-city-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credits'], course['description']])

print("CSV file 'oakland-city-university.csv' has been created with the extracted course data.")
