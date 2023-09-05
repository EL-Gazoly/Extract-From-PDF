import re
import csv

# Open the text file
with open('./the-redlands-community-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with various formats
    pattern = re.compile(r'(\w+(?:\s+|\s?-)\d+(?:-\d+)?\s*)(?:\s+(.+?))?\s+([\s\S]*?)(?=\w+(?:\s+|\s?-)\d+(?:-\d+)?\s+|$)')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    # Initialize variables to store course details
    code = ""
    title = ""
    description = ""

    for match in matches:
        match_code = match[0].strip()
        match_name = match[1].strip() if match[1] else ""
        match_description = match[2].strip()

        # Check if this part of the match is a code or a title
        if re.match(r'^\w+\s+\d+(?:-\d+)?$', match_code):
            # If it's a code, update the previous course details and reset
            if code:
                course_data.append({
                    'code': code,
                    'title': title,
                    'description': description
                })
            code = match_code
            title = match_name
            description = match_description
        else:
            # If it's not a code, append the description to the current course
            description += "\n" + match_description

    # Add the last course to the list
    if code:
        course_data.append({
            'code': code,
            'title': title,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('the-redlands-community-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'title', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'the-redlands-community-college.csv' has been created with the extracted course data.")
