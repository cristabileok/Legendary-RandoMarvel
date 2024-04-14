
import os
import json

schemes_file = open(os.path.join(os.path.dirname(__file__),'../lists/schemes.json'), encoding='utf-8')
schemes_data = json.load(schemes_file)

counter = 0

for element in schemes_data:
    for keyword in element["keywords"]:
        if "Scheme Transforms" in keyword:
            counter += 1
print(counter)