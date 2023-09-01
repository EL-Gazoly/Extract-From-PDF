import re
import csv

# Open the text file
with open('./the-kings-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z0-9, ]+)\s+LEC:\s+([^(\n]+)\s+\(([^)]+)\)\s+([\s\S]*?)(?=\n[A-Z0-9, ]+\s+LEC:|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]
        name = match[1]
        credits = match[2]
        description = match[3].strip()
        
        # Append course data to the list
        course_data.append({
            'Code': code,
            'Title': name,
            'Credits': credits,
            'Description': description
        })

# Write the extracted course data to a CSV file
with open('the-kings-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['Code'], course['Title'], course['Credits'], course['Description']])

print("CSV file 'the-kings-college.csv' has been created with the extracted course data.")
