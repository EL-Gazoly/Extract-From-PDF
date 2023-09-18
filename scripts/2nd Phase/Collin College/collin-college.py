import re
import csv

# Open the text file
with open('collin-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{4}\s\d{4})\s(.*?)\n(.*?)((?=\n[A-Z]{4}\s\d{4})|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, description, _ = match

        # Extract the second digit from the course code as credits
        credits = int(re.search(r'[A-Z]{4}\s\d(\d)', code).group(1))

        # Remove extra whitespace from the description
        description = description.strip()

        # Replace missing prerequisites with "none"
        if "Prerequisite:" not in description:
            prerequisites = "none"
        else:
            prerequisites = re.search(r'Prerequisite:(.*?)\n', description, re.DOTALL)
            if prerequisites:
                prerequisites = prerequisites.group(1).strip()
            else:
                prerequisites = "none"

        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': credits,
            'description': description + prerequisites
        })

# Write the extracted course data to a CSV file
with open('collin-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'collin-college' has been created with the extracted course data.")
