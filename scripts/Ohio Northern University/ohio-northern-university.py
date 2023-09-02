import re
import csv

# Open the text file
with open('./ohio-northern-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{2,4} \d{4}) (.+?)\n(\d+(?:\.\d+)?)(?: to (\d+(?:\.\d+)?))? (?:Credit|Credits) ([^\n]+)\n(.*?)(?=\n[A-Z]{2,4} \d{4}|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]
        name = match[1]
        min_credit_hours = float(match[2])
        max_credit_hours = float(match[3]) if match[3] else None
        credits = match[4].strip()
        description = match[5].strip()
        course_data.append({
            'code': code,
            'name': name,
            'credit hours': (min_credit_hours, max_credit_hours),
            'credits': credits,
            'description': description
        })

# Write the extracted course data to a CSV file
with open('ohio-northern-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['name'], f"{course['credit hours'][0]} to {course['credit hours'][1]}" if course['credit hours'][1] is not None else course['credit hours'][0], course['description']])

print("CSV file 'ohio-northern-university' has been created with the extracted course data.")
