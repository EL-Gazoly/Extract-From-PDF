import re
import csv

# Open the text file
with open('./huntington-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{2} \d{3})\s+([\w\s]+)\s*\(([^)]+)\)\s*([\s\S]*?)(?=(?:[A-Z]{2} \d{3}|$))')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        name = match[1]
        credits_match = re.search(r'(\d+\s*to\s*\d+|\d+)\s*credit', match[2])
        if credits_match:
            credits = credits_match.group(1).replace('to', '-')  # Replace "to" with "-"
        else:
            credits = match[2]
        description = match[3].strip()

        # Clean up description
        description = description.replace('\n', ' ').strip()

        course_data.append({
            'code': code,
            'name': name,
            'credit hours': credits,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('huntington-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'name', 'credit hours', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'huntington-university.csv' has been created with the extracted course data.")
