import re
import csv

# Open the text file
with open('./mid-america-chrisitan-university.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match the course data, including course codes with multiple slashes
    pattern = re.compile(r'([\w/]+ \d{4})\s+(.*?)\s+\((\d+) cr\.\)\s+(.*?)\s+(?=[\w/]+ \d{4}|$)', re.DOTALL)

    # Initialize a list to store extracted course data
    course_data = []

    # Create a set to keep track of encountered course codes
    course_codes_set = set()

    # Find all matches for the course data
    matches = pattern.findall(txt_content)

    for match in matches:
        code = match[0]

        # Check if the code has already been encountered
        if code not in course_codes_set:
            title = match[1].strip()
            credits = match[2]
            description = match[3].strip()

            # Append the extracted data as a dictionary
            course_data.append({
                'code': code,
                'title': title,
                'credits': credits,
                'description': description
            })

            # Add the code to the set
            course_codes_set.add(code)

# Write the extracted course data to a CSV file
with open('mid-america-chrisitan-university.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'title', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow([course['code'], course['title'], course['credits'], course['description']])

print("CSV file 'mid-america-chrisitan-university.csv' has been created with the extracted course data.")
