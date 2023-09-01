import re
import csv

# Open the text file
with open('./adrian-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w{6})\.  ([^\(]+) \((\d)\)\.\s*([^\.]+)\. ')

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, credits, description = match
        course_data.append({
            'code': code.strip(),
            'name': title.strip(),
            'credit hours': int(credits),
            'description': description.strip()
        })

# Write the extracted course data to a CSV file
with open('adrian-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], course['credit hours'], course['description']])

print("CSV file 'adrian-college' has been created with the extracted course data.")
