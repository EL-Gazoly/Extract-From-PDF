import re
import csv

# Open the text file
with open('./AlabamaAGriculturalMechanicalUniversity.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+\s\d+)\s+([\w\s\-]+)\s*–\s*(\d+ credit hours)[\s\S]*?([\s\S]+?)(?=\n[A-Z]+\s\d+|\Z)')
    
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_data.append(match)

# Write the extracted course data to a CSV file
with open('./AlabamaAGriculturalMechanicalUniversity.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['Course Code', 'Course Title', 'Credit Hours', 'Description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course[0], course[1], course[2], course[3].strip()])

print("CSV file 'AlabamaAGriculturalMechanicalUniversity.csv' has been created with the extracted course data.")
