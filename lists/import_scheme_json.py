import json
import os

# Define the input and output file names
script_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_directory, 'list_schemes.txt')
output_file = os.path.join(script_directory, 'schemes.json')

# Create an empty list to store scheme data
scheme_data = []

# Read the input .txt file, divide in schemes
with open(input_file, 'r', encoding='utf-8') as txt_file:
    txt_content = txt_file.read()
    schemes_list = txt_content.split("///\n\n>> ")

# Initialize variables to store scheme data
current_scheme = None
current_keywords = []
current_description = {}
current_description_element_title = []
current_description_element_content = []

# Parse the schemes and populate the scheme_data list
for scheme in schemes_list:
    scheme = scheme.strip()
    if scheme:
        if ':::' in scheme:
            # Split each scheme into name and attributes using ':::' as the delimiter
            if current_scheme:
                current_scheme_data = {
                    "name": current_scheme.strip(),
                    "keywords": current_keywords,
                    "description": dict(zip(current_description_element_title, current_description_element_content))
                }
                scheme_data.append(current_scheme_data)
            
            scheme_title, attribute_data = scheme.split(':::')
            if "[-]" in scheme_title:
                current_scheme, current_keywords_text = scheme_title.split("[-]")
                if current_keywords_text:
                    current_keywords = current_keywords_text.split(" , ")
            
            else:
                current_scheme = scheme_title.strip()
                current_keywords = []

            current_description_list = [description.strip() for description in attribute_data.split('---')]
            if current_description_list:
                current_description_element_title = []
                current_description_element_content = []
                for element in current_description_list:
                    if "--" in element:
                        title, content = element.split("\n--\n")
                        current_description_element_title.append(title)
                        current_description_element_content.append(content)
                    #current_description_element_title, current_description_element_content = current_description_list.split("--")
                    

        else:
            # This line contains additional attributes
            # Modify this to fit your data structure
            pass

# Handle the last entity
if current_scheme:
    current_scheme_data = {
        "name": current_scheme.strip(),
        "keywords": current_keywords,
        "description": dict(zip(current_description_element_title, current_description_element_content))
    }
    scheme_data.append(current_scheme_data)

# Write the data to a .json file
with open(output_file, 'w') as json_file:
    json.dump(scheme_data, json_file, indent=4)

print(f'Data from {input_file} has been successfully converted to {output_file}.')
