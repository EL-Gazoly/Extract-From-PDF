import re
import csv

# Open the text file
with open('./clarks-summit-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+\d+[A-Z]*\s*[-–]?\s*\d+[A-Z]*\s*)\n(.+?)\n(\d+(?:\s+credits?\/\w+)?)\s+(.+?)(?=\n[A-Z]+\d+[A-Z]*|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0].strip()
        # Extract only what comes before the em dash "—"
        name = match[1].strip().split("—")[0].strip()
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
with open('clarks-summit-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'name', 'credit hours', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'clarks-summit-university.csv' has been created with the extracted course data.")
