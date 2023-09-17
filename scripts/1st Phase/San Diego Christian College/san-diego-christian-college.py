import re
import csv

# Open the text file
with open('./san-diego-christian-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+(?:\s[A-Z]+)?\s\d+(?:[A-Z])?(?:/\w)?)(?:\s*\.{2,}\s*)([^\(]+)\s+\((\d+)\)\s*([\s\S]+?(?=(?:[A-Z]+\s\d+(?:[A-Z])?(?:/\w)?)|\Z))')
    
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0].strip()
        name = match[1].strip()
        credit_hours = match[2].strip()
        description = match[3].strip()

        course_info = {
            'code': code,
            'name': name,
            'credit hours': credit_hours,
            'description': description
        }

        course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('san-diego-christian-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'san-diego-christian-college.csv' has been created with the extracted course data.")
