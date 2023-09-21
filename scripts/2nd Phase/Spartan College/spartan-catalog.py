import re
import csv

# Open the text file
with open('./spartan-catalog.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\d+\w+)\s-\s(.*?)(?:\s\| (\d+)\sSemester Credit.*?\n(.*?)(?=\n\w+\d+\w+|\Z)|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, credits, description = match
        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': int(credits) if credits else None,
            'description': description.strip()
        })

# Write the extracted course data to a CSV file
with open('spartan-catalog.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'spartan-catalog' has been created with the extracted course data.")
