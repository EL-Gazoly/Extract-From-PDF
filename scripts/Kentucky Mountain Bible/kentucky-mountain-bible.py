import re
import csv

# Open the text file
with open('kentucky-mountain-bible.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match the original course data
    pattern1 = re.compile(r'(\w{2,}\s\d{3}(?:-\d{3})?)\s(.*?)(?:\(([\d.]+)\scredits?(?:,?\srequired for graduation)?\))?\n(.*?)(?=\n\w{2,}\s\d{3}(?:-\d{3})?|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Initialize a set to store course codes
    course_codes = set()

    # Find all matches in the text content
    matches1 = pattern1.findall(txt_content)
    for match in matches1:
        code = match[0]
        if code not in course_codes:
            name = match[1].strip()
            credits = match[2] if match[2] else '0'  # Replace None with '0'
            description = match[3].strip()
            course_data.append({'Code': code, 'Title': name, 'Credits': credits, 'Description': description})
            course_codes.add(code)

    # Create a regex pattern to match the new course format
    pattern2 = re.compile(r'(\w{2,}\s\d{3}(?:\s?and\s?\d{3})+)\s(.*?)\((\d+)\scredits?(?:\sfor each course)?\)\n(.*?)\n', re.DOTALL)

    # Find all matches in the text content
    matches2 = pattern2.findall(txt_content)
    for match in matches2:
        code = match[0]
        if code not in course_codes:
            title_parts = match[1].strip().split('(')
            titles = [t.strip() for t in title_parts[0].split('and')]
            title = ', '.join(titles)
            credits = match[2] if match[2] else '0'
            description = match[3].strip()
            course_data.append({'Code': code, 'Title': title, 'Credits': credits, 'Description': description})
            course_codes.add(code)

    # Create a regex pattern to handle '&' in the course title
    pattern3 = re.compile(r'(\w{2,}\s\d{3}(?:-\d{3})?)\s(.*?)(?:\(([\d.]+)\scredits?(?:,?\srequired for graduation)?\))?\n(.*?)(?=\n\w{2,}\s\d{3}(?:-\d{3})?|\Z)', re.DOTALL)

    # Find all matches in the text content
    matches3 = pattern3.findall(txt_content)
    for match in matches3:
        code = match[0]
        if code not in course_codes:
            name = match[1].strip()
            credits = match[2] if match[2] else '0'
            description = match[3].strip()
            course_data.append({'Code': code, 'Title': name, 'Credits': credits, 'Description': description})
            course_codes.add(code)

# Write the extracted course data to a CSV file
with open('kentucky-mountain-bible.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['Code', 'Title', 'Credits', 'Description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'kentucky-mountain-bible.csv' has been created with the extracted course data.")
