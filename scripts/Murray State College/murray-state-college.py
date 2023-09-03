import re
import csv

# Open the text file
with open('./murray-state-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([a-zA-Z]+\s+\d+)\s+(.*?)(?=\s*Credit:\s+((?:\w+(?:\s+\w+)?|None))\s+semester\s+hour(?:s)?|$|\n[a-zA-Z]+\s+\d+|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code = match[0]
        title_description = match[1].strip()
        credits = match[2] if len(match) > 2 else 'N/A'

        # Split the title and description if a newline character is present, or set description to an empty string
        if '\n' in title_description:
            title, description = title_description.split('\n', 1)
        else:
            title = title_description
            description = ''

        # Convert credit hours to a numeric value or set to 'N/A'
        if credits.isdigit():
            credits = int(credits)
        else:
            credits = credits.lower()  # Convert to lowercase

        course_info = {
            'code': code,
            'name': title.strip(),
            'credit hours': credits,
            'description': description.strip()
        }

        course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('murray-state-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'murray-state-college' has been created with the extracted course data.")
