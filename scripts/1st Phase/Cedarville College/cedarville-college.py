import re
import csv

# Open the text file
with open('./cedarville-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+(?:-[A-Z\d]+)?-\d{4}(?:,\s?[A-Z]+(?:-[A-Z\d]+)?-\d{4})*)\s*((?:[\w\s,–]+(?:\s[a-zA-Z\d]+\s)?)?)\s+(\d+(?:–\d+)?)\s+((?:(?![A-Z]+(?:-[A-Z\d]+)?-\d{4}|Prerequisites?:)[\s\S])+)(?:\s*Prerequisites?:\s+([\w\s–,]+))?')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for i, match in enumerate( matches):
        codes = match[0].split(', ')  # Split multiple course codes by comma and space
        name = match[1].strip() or "No Name"  # Replace an empty course name with "No Name"
        credit_hours = match[2]
        description = match[3].strip()
        prerequisite = match[4].strip() if match[4] else "NONE"

        # Add the prerequisite information to the description
        if name == "No Name":
            hours_match = re.search(r'(\d+\s+hours)', txt_content)
            if hours_match:
                hours_end = hours_match.end()
                next_line_match = re.search(r'\n(.+)', txt_content[hours_end:])
                if next_line_match:
                    name = next_line_match.group(1).strip()
                    description = description.replace(hours_match.group(1), '')
                    description = description.replace(name, '')

        if prerequisite != "NONE":
            description += f"\nPrerequisite: {prerequisite}"

        for code in codes:
            course_data.append({
                'code': code,
                'name': name,
                'credit_hours': credit_hours,
                'description': description
            })

# Write the extracted course data to a CSV file
with open('cedarville-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit_hours'], course['description']])

print("CSV file 'cedarville-college' has been created with the extracted course data.")
