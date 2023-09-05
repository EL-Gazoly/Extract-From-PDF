import re
import csv

# Open the text file
with open('./connors-state-college.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Initialize a list to store extracted course data
    course_data = []

    # Define the first pattern to extract courses with hyphen in the code
    pattern1 = r'(\w+\s+\d+\s?(?:-|\w+\s\d+\s)?[\w\s]+)\s*([\d.-]+)\s*(?:Credits?|Credi)\s*([\s\S]*?)(?=\w+\s+\d+\s?(?:-|\w+\s\d+\s)?[\w\s]+|$)'

    # Find all matches in the text content for the first pattern
    matches1 = re.findall(pattern1, txt_content)

    for match in matches1:
        code_and_title = match[0]
        credits = match[1].strip() if match[1] else "N/A"
        description = match[2].strip()

        # Split code_and_title into code and title
        code_match = re.match(r'(\w+\s+\d+\s?(?:-|\w+\s\d+\s)?)([\w\s]+)', code_and_title)
        if code_match:
            code = code_match.group(1).strip()
            title = code_match.group(2).strip()
        else:
            code = "N/A"
            title = "N/A"

        # Append course data as a dictionary
        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,
            'description': description
        })

    # Define the second pattern to extract the special course format
    pattern2 = r'(\w+\s+\d+)\s?–\s([\w\s]+)\s*([\d.-]+)\s*(?:Credits?|Credi)\s*([\s\S]*?)(?=\w+\s+\d+\s?(?:-|\w+\s\d+\s)?[\w\s]+|$)'

    # Find all matches in the text content for the second pattern
    matches2 = re.findall(pattern2, txt_content)

    for match in matches2:
        code = match[0].strip()
        title = match[1].strip()
        credits = match[2].strip() if match[2] else "N/A"
        description = match[3].strip()

        # Append course data as a dictionary
        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,
            'description': description
        })

    # Define the third pattern to extract the new course format
    pattern3 = r'(\w+\s+\d+(?:/\w+\s+\d+)?)(?:-)?\s*(.+)\s+(\d+)\s*(?:Credits?|Credi)\s*([\s\S]*?)(?=\w+\s+\d+\s?(?:-|\w+\s\d+\s)?[\w\s]+|$)'

    # Find all matches in the text content for the third pattern
    matches3 = re.findall(pattern3, txt_content)

    for match in matches3:
        code = match[0].strip()
        title = match[1].strip()
        credits = match[2].strip() if match[2] else "N/A"
        description = match[3].strip()

        # Append course data as a dictionary
        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,
            'description': description
        })

# Remove duplicates based on code and title
unique_course_data = []
course_codes = set()

for course in course_data:
    course_key = (course['code'], course['title'])
    if course_key not in course_codes:
        unique_course_data.append(course)
        course_codes.add(course_key)

# Write the extracted unique course data to a CSV file
with open('connors-state-college.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in unique_course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'connors-state-college.csv' has been created with the extracted course data (duplicates removed).")
