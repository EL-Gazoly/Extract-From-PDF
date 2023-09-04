import re
import csv

# Open the text file
with open('./lincoln-christian-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data with multi-line descriptions
    pattern = re.compile(r'([A-Z]+\s\d+(?:-\d+)?)\s([A-Z][^\.]+)\.\s*([\s\S]*?)\((\d+-?\d*)\s*(?:-\d+)?\)')
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)

    for match in matches:
        course_code = match[0]
        course_name = match[1].strip()
        course_description = match[2].strip()
        credit_hours = match[3]

        # Append the extracted data as a dictionary
        course_data.append({
            'Code': course_code,
            'Title': course_name,
            'Credits': credit_hours,
            'Description': course_description
        })

# Write the extracted course data to a CSV file
with open('lincoln-christian-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Code', 'Title', 'Credits', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['Code'], course['Title'], course['Credits'], course['Description']])

print("CSV file 'lincoln-christian-university.csv' has been created with the extracted course data.")
