import re
import csv

# Open the text file
with open('kentucky-mountain-bible.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match the original course data
    pattern1 = re.compile(r'(\w{2,}\s\d{3}(?:-\d{3})?)\s(.*?)(?:\((\d+)\scredits?(?:,?\srequired for graduation)?\))?\n(.*?)(?=\n\w{2,}\s\d{3}(?:-\d{3})?|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches1 = pattern1.findall(txt_content)
    for match in matches1:
        code = match[0]
        name = match[1].strip()
        credits = match[2] if match[2] else '0'  # Replace None with '0'
        description = match[3].strip()
        course_data.append({'Code': code, 'Title': name, 'Credits': credits, 'Description': description})

    # Create a regex pattern to match the new course format, allowing '&' in the title
    pattern2 = re.compile(r'(\w{2,}\s\d{3}(?:\s?and\s?\d{3})+)\s(.*?)(?:\((\d+)\scredits?(?:,?\srequired for graduation)?\))?\n(.*?)(?=\n\w{2,}\s\d{3}(?:-\d{3})?|\Z)', re.DOTALL)

    # Find all matches in the text content
    matches2 = pattern2.findall(txt_content)
    for match in matches2:
        code = match[0]
        name = match[1].strip()
        credits = match[2] if match[2] else '0'  # Replace None with '0'
        description = match[3].strip()
        course_data.append({'Code': code, 'Title': name, 'Credits': credits, 'Description': description})

# Write the extracted course data to a CSV file
with open('kentucky-mountain-bible.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'title', 'credits', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    for course in course_data:
        # Remove any extra characters from the title
        course['Title'] = course['Title'].strip('"')
        
        # Remove any extra characters from the credits
        course['Credits'] = course['Credits'].strip('"')
        
        # Write the modified course data
        csv_writer.writerow(course)

print("CSV file 'kentucky-mountain-bible.csv' has been created with the extracted course data.")
