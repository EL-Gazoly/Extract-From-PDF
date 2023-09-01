import re
import csv

# Open the text file
with open('./thomas-more-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\s+[0-9-]+)\s*[-–]\s*(.*?)\s*\((.*?)\)(?:\s*\n(.*?)(?=\w+\s+[0-9-]+\s*[-–]|\Z))?', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        name = match[1]
        credit_hours = match[2].strip()
        if "variable credit" in credit_hours.lower():
            credit_hours = "Variable Credit"
        elif ',' in credit_hours:
            credit_hours = credit_hours.replace(',', ' and ')
        description = match[3].strip() if match[3] else ''
        course_data.append({
            'code': code.strip(),
            'name': name.strip(),
            'credit hours': credit_hours,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('thomas-more-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credit hours', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'thomas-more-university.csv' has been created with the extracted course data.")
