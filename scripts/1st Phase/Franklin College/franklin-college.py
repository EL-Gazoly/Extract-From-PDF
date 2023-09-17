import re
import csv

# Read the text from the input file
with open('./franklin-college.txt', 'r', encoding='utf-8') as input_file:
    input_text = input_file.read()

# Regular expression pattern
pattern = re.compile(r'(\S+\s+\d+(?:\.\d+)?[A-Z]*[A-Z\d]*)\s+(.*?)\s+(\d+(?:-\d+)?|No\scredit)\s*(.*?)\s*(?:Prereq:\s(.*?)\s+)?(?:Coreq|Co-req:\s(.*?)\s+)?(except:\s(.*?)\s+)?\s*(.*?)(?=\n\S+\s+\d+|$)', re.DOTALL)

# Find all matches in the input text
matches = pattern.findall(input_text)

# Initialize a list to store extracted course data
course_data = []

# Append matched data to the course_data list
for match in matches:
    course_code = match[0]
    course_name = match[1].strip()
    credit_hours = match[2]
    if credit_hours.lower() == "no credit":
        credit_hours = "0"
    prereq = match[4].strip() if match[4] else "None"
    coreq = match[5].strip() if match[5] else "None"
    except_info = match[7].strip() if match[7] else "None"
    description = match[8].strip()

    course_info = {
        'code': course_code,
        'title': course_name,
        'credits': credit_hours,
        'description': prereq+ '' + coreq+ ''+ except_info+ '' +description
    }

    course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('franklin-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'title', 'credits','description'])
    
    # Write header row
    csv_writer.writeheader()
    
    # Write course data rows
    csv_writer.writerows(course_data)
        
print("CSV file 'franklin-college.csv' has been created with the extracted course data.")
