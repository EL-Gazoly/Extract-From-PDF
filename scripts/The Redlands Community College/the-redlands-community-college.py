import re
import csv

# Open the text file
with open('./the-redlands-community-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with various formats
    pattern = re.compile(r'(\w+(?:\s+|\s?-)\d+(?:-\d+)?\s*)(.*?)(?=\n\w+(?:\s+|\s?-)\d+(?:-\d+)?\s+|\Z)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    for match in pattern.finditer(txt_content):
        match_code = match.group(1).strip()
        match_description = match.group(2).strip()

        # Split the description into lines
        description_lines = match_description.split('\n')

        # The first line is the title
        title = description_lines[0]

        # The rest is the description
        description = '\n'.join(description_lines[1:])

        # Extract course credits from the course code (last digit(s))
        credits_match = re.search(r'(\d+(?:-\d+)?)$', match_code)
        course_credits = credits_match.group(1)[-1] if credits_match else ""

        course_data.append({
            'code': match_code,
            'title': title,
            'credits': course_credits,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('the-redlands-community-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'title', 'credits', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'the-redlands-community-college.csv' has been created with the extracted course data.")
