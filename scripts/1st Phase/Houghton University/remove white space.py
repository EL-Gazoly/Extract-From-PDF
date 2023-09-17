input_file_path = "houghton-university.txt"
output_file_path = "output.txt"

with open(input_file_path, "r", encoding="utf-8") as input_file:
    content = input_file.read()

content_without_newlines = content.replace("\n", " ")

with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(content_without_newlines)

print("New lines removed and saved to output.txt")
