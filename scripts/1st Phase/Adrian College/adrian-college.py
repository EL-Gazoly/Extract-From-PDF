import re
import csv

# Open the text file
with open('./adrian-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with the enhanced formats
    pattern = re.compile(r'([A-Z]+\s?[A-Z]*\s?\d{3}[A-Z]*)\. ([^\(]+) \((\d-\d|\d)\)(.*?)\n(?=[A-Z]+\s?[A-Z]*\s?\d{3}[A-Z]*|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, credits, description = match

        # Remove extra whitespace from the description
        description = description.strip()

        # Split credit hours into a list if it's in the "X-X" format
        credit_hours = [int(credit.strip()) for credit in credits.split('-')]

        course_data.append({
            'code': code.strip(),
            'name': title.strip(),
            'credit hours': credit_hours,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('adrian-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'adrian-college' has been created with the extracted course data.")
