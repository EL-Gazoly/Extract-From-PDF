import re
import csv

# Open the text file
with open('./texas-lutheran-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data in the first format
    pattern1 = re.compile(r'([A-Z]+\s\d+)\.\s(.*?)(?:\((\d+:\d+(?:\.\d+)?:\d+(?:\.\d+)?)\)|\((\w+:\d+(?:\.\d+)?:\w+(?:\.\d+)?)\)|\((\w+:\w+(?:\.\d+)?:\d+(?:\.\d+)?)\)|\((\d+:\w+(?:\.\d+)?:\w+(?:\.\d+)?)\)|(\d+:\d+:\d+(?:\.\d+)?))'
                          r'(?:\s(.*?))?'
                          r'(?=\n[A-Z]+\s\d+\.|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content using the first pattern
    matches1 = pattern1.findall(txt_content)

    for match in matches1:
        code, title, credits1, credits2, credits3, credits4, credits5, description = match
        credits = credits1 if credits1 else credits2 if credits2 else credits3 if credits3 else credits4 if credits4 else credits5
        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': credits.split(":")[0].strip() if ":" in credits else credits.strip(),
            'description': description.strip() if description else ''
        })

    # Create a regex pattern to match course data in the second format
    pattern2 = re.compile(r'([A-Z]+\s\d+(?:-\d+)*)\.\s(.*?)\s\((\d+:\d+(?:\.\d+)?:\d+(?:\.\d+)?)\)'
                          r'(?:\s(.*?))?'
                          r'(?=\n[A-Z]+\s\d+\.|$)', re.DOTALL)

    # Find all matches in the text content using the second pattern
    matches2 = pattern2.findall(txt_content)

    for match in matches2:
        code, title, credits, description = match
        course_data.append({
            'code': code.strip(),
            'title': title.strip(),
            'credits': credits.split(":")[0].strip(),
            'description': description.strip() if description else ''
        })

# Write the extracted course data to a CSV file
with open('texas-lutheran-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'texas-lutheran-university.csv' has been created with the extracted course data.")
