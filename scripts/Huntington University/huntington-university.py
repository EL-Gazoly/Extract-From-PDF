import re
import csv

# Open the text file
with open('./huntington-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create the first regex pattern to match most course data, including prerequisites
    pattern = re.compile(r'([A-Z]{2} \d{2,3}[A-Z]*[A-Z]?)\s+([\w\s:/?]+)\s*\(([^)]+)\)\s*([\s\S]*?)(?:Prerequisite:\s*(.*?)(?=\n[A-Z]{2} \d{2,3}[A-Z]*[A-Z]?|$))', re.DOTALL)

    # Initialize a set to store unique course codes
    unique_course_codes = set()

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content using the first pattern
    matches = pattern.findall(txt_content)
    
    # Initialize variables to keep track of prerequisites
    current_prerequisite = None
    
    for match in matches:
        code = match[0]
        
        # Check if the course code is already in the set, if so, skip this course
        if code in unique_course_codes:
            continue
        
        # Add the course code to the set
        unique_course_codes.add(code)

        # Extract and clean up the course title
        title = match[1].strip()
        title = title.replace(': ', ':').replace(':  ', ': ')
        credits_match = re.search(r'(\d+\s*to\s*\d+|\d+)\s*credit', match[2])
        if credits_match:
            credits = credits_match.group(1).replace('to', '-')  # Replace "to" with "-"
        else:
            credits = match[2]
        description = match[3].strip()
        prerequisites = match[4].strip() if match[4] else "None"

        # Check if the current course has a prerequisite
        if prerequisites != "None":
            current_prerequisite = prerequisites
        else:
            prerequisites = current_prerequisite

        # Clean up description and concatenate prerequisites
        description = description.replace('\n', ' ').strip()
        if prerequisites != "None":
            description += f'\nPrerequisite: {prerequisites}'

        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,  # Renamed "credit hours" to "credits"
            'description': description
        })

    # Special regex pattern to match courses with specific patterns
    # Special regex pattern to match courses with specific patterns
    special_pattern = re.compile(r'([A-Z]{2} \d{2,3}[A-Z]*[A-Z]?)\s+(.*?)(\d+\s+credit[s]?)\s*-([\s\S]*?)(?:Prerequisite:\s*(.*?)(?=\n[A-Z]{2} \d{2,3}[A-Z]*[A-Z]?|$)|(?=\n[A-Z]{2} \d{2,3}[A-Z]*[A-Z]?)|$)', re.DOTALL)

    
    # Find all matches in the text content using the special pattern
    special_matches = special_pattern.findall(txt_content)
    
    for special_match in special_matches:
        code = special_match[0]
        
        # Check if the course code is already in the set, if so, skip this course
        if code in unique_course_codes:
            continue
        
        # Add the course code to the set
        unique_course_codes.add(code)

        # Extract and clean up the course title
        title = special_match[1].strip()
        title = title.replace(': ', ':').replace(':  ', ': ')
        credits_match = re.search(r'(\d+\s*to\s*\d+|\d+)\s*credit', special_match[2])
        if credits_match:
            credits = credits_match.group(1).replace('to', '-')  # Replace "to" with "-"
        else:
            credits = special_match[2]
        description = special_match[3].strip()
        prerequisites = special_match[4].strip() if special_match[4] else "None"

        # Check if the current course has a prerequisite
        if prerequisites != "None":
            current_prerequisite = prerequisites
        else:
            prerequisites = current_prerequisite

        # Clean up description and concatenate prerequisites
        description = description.replace('\n', ' ').strip()
        if prerequisites != "None":
            description += f'\nPrerequisite: {prerequisites}'

        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,  # Renamed "credit hours" to "credits"
            'description': description
        })

    # Third special regex pattern to capture courses with Prerequisite issue
    third_special_pattern = re.compile(r'([A-Z]{2} \d{2,3}[A-Z]*[A-Z]?)\s+([\w\s:/?]+)\s*\(([^)]+)\)\s*([\s\S]*?)(?:Prerequisite:\s*([A-Z]{2} \d{2,3}[A-Z]*[A-Z]+)(?=\n[A-Z]{2} \d{2,3}[A-Z]*[A-Z]?|$)|(?=\n[A-Z]{2} \d{2,3}[A-Z]*[A-Z]?)|$)', re.DOTALL)
    
    # Find all matches in the text content using the third special pattern
    third_special_matches = third_special_pattern.findall(txt_content)
    
    for third_special_match in third_special_matches:
        code = third_special_match[0]
        
        # Check if the course code is already in the set, if so, skip this course
        if code in unique_course_codes:
            continue
        
        # Add the course code to the set
        unique_course_codes.add(code)

        # Extract and clean up the course title
        title = third_special_match[1].strip()
        title = title.replace(': ', ':').replace(':  ', ': ')
        credits_match = re.search(r'(\d+\s*to\s*\d+|\d+)\s*credit', third_special_match[2])
        if credits_match:
            credits = credits_match.group(1).replace('to', '-')  # Replace "to" with "-"
        else:
            credits = third_special_match[2]
        description = third_special_match[3].strip()
        prerequisites = third_special_match[4].strip() if third_special_match[4] else "None"

        # Check if the current course has a prerequisite
        if prerequisites != "None":
            current_prerequisite = prerequisites
        else:
            prerequisites = current_prerequisite

        # Clean up description and concatenate prerequisites
        description = description.replace('\n', ' ').strip()
        if prerequisites != "None":
            description += f'\nPrerequisite: {prerequisites}'

        course_data.append({
            'code': code,
            'title': title,
            'credits': credits,  # Renamed "credit hours" to "credits"
            'description': description
        })

# Write the extracted course data to a CSV file
with open('huntington-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['code', 'title', 'credits', 'description'])

    # Write header row
    csv_writer.writeheader()

    # Write course data rows
    csv_writer.writerows(course_data)

print("CSV file 'huntington-university.csv' has been created with the extracted course data, including prerequisites in the description, and improved course titles and 'credit hours' renamed to 'credits'.")
