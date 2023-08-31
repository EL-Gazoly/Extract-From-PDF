import re
import csv

# Open the text file
with open('./spring-arbor.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]{3,4} \d{3})\s+(.*?)\s+\(([\d\-]+)\)\s+\(([^)]+)\)\s+(.*?)(?=(?:[A-Z]{3,4} \d{3})|\Z)', re.DOTALL)
    
    # Initialize a set to store course codes
    processed_courses = set()
    
    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        course_code = match[0]
        
        # Check if the course code has already been processed
        if course_code not in processed_courses:
            processed_courses.add(course_code)
            
            course_name = match[1]
            course_credit_hours = match[2]
            course_term = match[3]
            course_description = match[4]
            
            course_info = {
                'code': course_code,
                'name': course_name,
                'credit': course_credit_hours,
                'description': course_term + ' ' + course_description.strip()
            }
            
            course_data.append(course_info)

# Write the extracted course data to a CSV file
with open('spring-arbor.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'name', 'credit', 'description'])
    csv_writer.writeheader()
    csv_writer.writerows(course_data)

print("CSV file 'spring-arbor.csv' has been created with the extracted course data.")
