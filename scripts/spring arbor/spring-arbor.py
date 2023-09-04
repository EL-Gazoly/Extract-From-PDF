import re
import csv

# Open the text file
with open('./spring-arbor.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\s\d+[A-Z]*\*?|\w+\s\d{3}\*?)\s(.*?)(?:\s\((\d+)\))\s([\s\S]*?)(?=\n\w+\s\d+[A-Z]*\*?\s|\Z)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, credits, description = match
        course_data.append({
            'code': code.strip(),
            'name': title.strip(),
            'credits': int(credits),
            'description': description.strip()
        })

# Write the extracted course data to a CSV file
with open('spring-arbor.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credits'], course['description']])

print("CSV file 'spring-arbor' has been created with the extracted course data.")
