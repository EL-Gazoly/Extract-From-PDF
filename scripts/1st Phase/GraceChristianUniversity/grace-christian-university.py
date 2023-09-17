import re
import csv

# Open the text file
with open('./grace-christian-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z/ ]+\d{3}[A-Z0-9 ]*?)\s–\s([^–]+)\s+Credit Hours:\s(\d+(?:-\d+)?)\s+([\s\S]+?)(?=\n[A-Z/]+\s\d{3}[A-Z+]*?\s–|$)')
    
    # Initialize a list to store extracted course data as dictionaries
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_dict = {
            'code': match[0].strip(),
            'name': match[1].strip(),
            'credits': match[2].strip(),
            'description': match[3].strip()
        }
        course_data.append(course_dict)

# Write the extracted course data to a CSV file
with open('grace-christian-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credits'], course['description']])
