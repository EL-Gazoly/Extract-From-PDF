import re
import csv

# Open the text file
with open('./blackburn-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\d+)\.\s+(.*?)\s+\(([\d.-]+(?:\s*(?:or|\-)\s*[\d.-]+)?)\s+(?:hour|hours)[^)]*\)\s*(?:\n(.*?)\s*)?(?:\nPrerequisites:\s*(.*?))?(?=\n\d+\.|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]
        name = match[1].strip()
        credit_hours = match[2]
        description = match[3].strip() if match[3] else ""
        prerequisites = match[4] if match[4] else "NONE"

        course_info = {
            'code': code,
            'name': name,
            'credit hours': credit_hours,
            'description': description + '' + prerequisites
        }

        course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('blackburn-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'blackburn-college.csv' has been created with the extracted course data.")
