import re
import csv

# Open the text file
with open('./grace-college-and-theological-seminary.txt', 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()

    # Create a regex pattern to match course data
    pattern = re.compile(r'([A-Z]+(?:[-\s/]\d{4}|\d{4}(?:–\d{4})?|(?:[A-Z/]+\s\d{4}-[A-Z/]+\s\d{4})))\s(.+?)\n([\s\S]+?)(?=\n[A-Z]+(?:[-\s/]\d{4}|\d{4}(?:–\d{4})?|(?:[A-Z/]+\s\d{4}-[A-Z/]+\s\d{4}))|$)', re.IGNORECASE)

    # Initialize a list to store extracted course data
    course_data = []

    # Find all matches in the text content
    matches = pattern.findall(txt_content)
    for match in matches:
        code, title, description = match

        # Use a regex to find the word before "hour" or "hours" in the description
        credit_match = re.search(r'(\w+)\s*(?:hour|hours)', description, re.IGNORECASE)
        credits = credit_match.group(1) if credit_match else "0"

        # Append the extracted data to the course_data list
        course_data.append([code, title, credits, description])

# Write the extracted course data to a CSV file
with open('grace-college-and-theological-seminary.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(['code', 'name', 'credits', 'description'])

    # Write course data rows
    for course in course_data:
        csv_writer.writerow(course)

print("CSV file 'grace-college-and-theological-seminary.csv' has been created with the extracted course data.")
