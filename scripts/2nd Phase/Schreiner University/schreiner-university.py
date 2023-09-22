import re
import csv

# Open the text file
with open('./schreiner-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data (four digits followed by a period)
    pattern = re.compile(r'(\d{4})\.?\s+(.*?)\n(.*?)(?=\d{4}\.|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code, title, description = match

        # Extract the second digit of the course code as credits
        credits = int(code[1]) if len(code) > 1 and code[1].isdigit() else None

        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': credits,
            'description': description.strip()
        })

# Write the extracted course data to a CSV file
with open('schreiner-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'schreiner-university.csv' has been created with the extracted course data.")
