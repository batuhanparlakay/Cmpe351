import json
import xml.etree.ElementTree as ET

# Reading the json file
with open('Instructors.json', 'r', ) as json_file:
    data = json.load(json_file)

print(data)
data['Instructors'][0]['instructor_class'] = 6
print(data)

with open('Instructors.json', 'w', ) as json_file:
    json_file.write(json.dumps(data))
    
xml_file = ET.parse('Lectures.xml')

data = xml_file.getroot()

print(data.find('lecture').find('lecture_id').text)
xml_file.getroot().find('lecture').find('lecture_id').text = '1234'
print(data.find('lecture').find('lecture_id').text)

xml_file.write('Lectures_new.xml')    

