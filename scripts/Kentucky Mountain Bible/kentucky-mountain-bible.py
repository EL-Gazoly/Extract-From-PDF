import re
import csv

# Open the text file
with open('kentucky-mountain-bible.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w{2,}\s\d{3}(?:-\d{3})?)\s(.*?)(?:\(([\d.]+)\scredits? (?:for each )?course\))?\n(.*?)(?=\n\w{2,}\s\d{3}(?:-\d{3})?|\Z|\n\(\d+ credit, required for graduation\))', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        name = match[1].strip()
        credits = match[2] if match[2] else '0'  # Replace None with '0'
        description = match[3].strip()
        course_data.append({'Code': code, 'Title': name, 'Credits': credits, 'Description': description})

# Write the extracted course data to a CSV file
with open('kentucky-mountain-bible.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['Code', 'Title', 'Credits', 'Description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'kentucky-mountain-bible.csv' has been created with the extracted course data.")
