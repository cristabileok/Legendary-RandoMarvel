import json
import os

# Define the input and output file names
script_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_directory, 'list_keywords.txt')
output_file = os.path.join(script_directory, 'keywords.json')

# Create an empty list to store keyword data
keywords_data = []

# Read the input .txt file
with open(input_file, 'r', encoding='utf-8') as txt_file:
    lines = txt_file.readlines()

# Initialize variables to store keyword data
current_name = None
current_description = []

# Parse the lines and populate the keywords_data list
for line in lines:
    line = line.strip()
    if line.startswith(">> "):
        # Start of a new keyword entry
        if current_name:
            keyword_data = {
                "name": current_name,
                "description": "\n".join(current_description)
            }
            keywords_data.append(keyword_data)
        current_name = line[3:-3].strip()
        current_description = []
    elif line == "///":
        # End of a keyword entry
        if current_name:
            keyword_data = {
                "name": current_name,
                "description": "\n".join(current_description)
            }
            keywords_data.append(keyword_data)
        current_name = None
        current_description = []
    else:
        # Part of the description
        current_description.append(line)

# Write the data to a .json file
with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(keywords_data, json_file, indent=4, ensure_ascii=False)

print(f'Data from {input_file} has been successfully converted to {output_file}.')
