import json
import os

# Define the input and output file names
script_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_directory, 'list_villains.txt')
output_file = os.path.join(script_directory, 'villains.json')

# Create an empty list to store entity data
entity_data = []

# Read the input .txt file
with open(input_file, 'r') as txt_file:
    lines = txt_file.readlines()

# Initialize variables to store entity data
current_entity = None
current_keywords = []

# Parse the lines and populate the entity_data list
for line in lines:
    line = line.strip()
    if line:
        if ':' in line:
            # Split each line into name and attributes using ':' as the delimiter
            if current_entity:
                current_entity_data = {
                    "name": current_entity.strip(),
                    "keywords": current_keywords
                }
                entity_data.append(current_entity_data)
            
            current_entity, attribute_data = line.split(':')
            current_keywords = [kw.strip() for kw in attribute_data.split(',')]
        else:
            # This line contains additional attributes
            # Modify this to fit your data structure
            pass

# Handle the last entity
if current_entity:
    current_entity_data = {
        "name": current_entity.strip(),
        "keywords": current_keywords
    }
    entity_data.append(current_entity_data)

# Write the data to a .json file
with open(output_file, 'w') as json_file:
    json.dump(entity_data, json_file, indent=4)

print(f'Data from {input_file} has been successfully converted to {output_file}.')
