import re
import csv

# Open the text file
with open('./AlabamaAGriculturalMechanicalUniversity.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+\s\d+[A-Z]*\s?[A-Z]*)\s+([\w\s\-]+)\s*–\s*(\d+)\s+credit\s+hour[s]*[\s\S]*?([\s\S]+?)(?=\n[A-Z]+\s\d+|\Z)', re.IGNORECASE)
    
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_code = match[0]
        course_title = match[1]
        credit_hours = match[2]  # Only the number of credit hours
        description = match[3].strip()

        course_data.append((course_code, course_title, credit_hours, description))

# Write the extracted course data to a CSV file
with open('./AlabamaAGriculturalMechanicalUniversity.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Course Code', 'Course Title', 'Credit Hours', 'Description'])

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'AlabamaAGriculturalMechanicalUniversity.csv' has been created with the extracted course data.")
