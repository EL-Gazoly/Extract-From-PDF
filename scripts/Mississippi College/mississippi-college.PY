import re
import csv

# Open the text file
with open('./mississippi-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+(?: \d+) [–-] [^\n]+)\n(?:Credits, (\d+) sem\. hrs?)?(.*?)(?=\n\w+(?: \d+) [–-] |$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code, credit_hours, description = match
        name = code.split(' – ' if ' – ' in code else ' - ', 1)[1].strip()
        code = code.split(' – ' if ' – ' in code else ' - ', 1)[0].strip()
        credit_hours = int(credit_hours) if credit_hours else None
        # Remove trailing whitespace and newline characters from the description
        description = description.strip()
        course_data.append({
            'code': code,
            'name': name,
            'credit hours': credit_hours,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('mississippi-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'mississippi-college' has been created with the extracted course data.")
