import re
import csv

# Open the text file
with open('cameron-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with both old and enhanced formats
    pattern = re.compile(r'(\d+(?:-\d+)?\*?\w*)\s+([^0-9]+)\s+(\d+(?:-\d+)?)\s*(?:credit\s*hours)?\s+(.*?)(?=\d+(?:-\d+)?\*?|\Z)(?:\s+Prerequisites:\s(.*?))?(?:\s+Corequisite:\s(.*?))?', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, credits, description, prerequisites, corequisite = match

        # Filter courses with course codes consisting of only one letter or one digit
        if len(code) == 1 and code.isalpha() or len(code) == 1 and code.isdigit():
            continue  # Skip this course

        # Remove extra whitespace from the description
        description = description.strip()

        # If prerequisites and corequisite are not specified, set them to "none"
        if not prerequisites:
            prerequisites = "none"
        if not corequisite:
            corequisite = "none"

        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': credits.strip(),
            'description': description + prerequisites.strip() + corequisite.strip(),
        })

# Write the extracted course data to a CSV file
with open('cameron-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'cameron-university.csv' has been created with the extracted course data.")
