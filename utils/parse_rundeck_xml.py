import os
import xml.etree.ElementTree as ET

#file_list = os.listdir(os.getcwd())
JOBS_PATH = '/Users/dstoner/git/Rundeck-Jobs'
file_list = os.listdir(JOBS_PATH)

xml_file_list = []
for filename in file_list:
    if filename.endswith('.xml'):
        xml_file_list.append(filename)
if len(xml_file_list) == 0:
    raise SystemExit("ERROR: No XML files found")

final_set = set()

for xml_file in xml_file_list:
    with open('/'.join([JOBS_PATH,xml_file]), 'r') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        emails = root.findall(".//email")

        for each in emails:
            recipients = each.attrib['recipients']
            multi = recipients.split(', ')
            for each_email in multi:
                final_set.add(each_email)

for email in sorted(final_set):
    print (email)
