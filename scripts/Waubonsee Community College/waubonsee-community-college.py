import re
import csv

# Open the text file
with open('./waubonsee-community-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'(\w+\s+\d+)\s+(.+?)\n(.*?)(?=\n(\w+\s+\d+)\s+|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    
    for match in matches:
        code = match[0]
        name = match[1]
        description = match[2].strip()
        
        # Search for credit hours in the description, including variations like "1 to 3" and "0.5"
        credit_hours_match = re.search(r'(\d+(?:\s+to\s+\d+)?(?:\.\d+)?)\s+sem\s+hrs', description)
        if credit_hours_match:
            credit_hours = credit_hours_match.group(1)
        else:
            credit_hours = "N/A"
        
        course_info = {
            "code": code,
            "name": name,
            "credit hours": credit_hours,
            "description": description
        }
        course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('waubonsee-community-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credit hours', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course["code"], course["name"], course["credit hours"], course["description"]])

print("CSV file 'waubonsee-community-college.csv' has been created with the extracted course data.")
