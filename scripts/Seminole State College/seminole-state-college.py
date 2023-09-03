import re
import csv

# Open the text file
with open('./seminole-state-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+\s+\d+)(\d)\s+(\w+)\s+(.*?)(?=\w+\s+\d+|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        credit_hours = match[1]
        title = match[2]
        description = match[3].strip()
        full_code = code + credit_hours  # Combine code and credit hours
        course_data.append({'code': full_code, 'name': title, 'credits': credit_hours, 'description': description})

# Write the extracted course data to a CSV file
with open('seminole-state-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Name', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credits'], course['description']])

print("CSV file 'seminole-state-college' has been created with the extracted course data.")
