import os
import xml.etree.ElementTree as ET

RUNDECK_JOBS_PATH = os.getenv('RUNDECK_JOBS_PATH')
if RUNDECK_JOBS_PATH is None:
    raise SystemExit("""
        ERROR: Missing environment variable: RUNDECK_JOBS_PATH
        Hint:
            export RUNDECK_JOBS_PATH='/path/to/rundeck/jobs'
                     """)


file_list = os.listdir(RUNDECK_JOBS_PATH)

xml_file_list = []
for filename in file_list:
    if filename.endswith('.xml'):
        xml_file_list.append(filename)
if len(xml_file_list) == 0:
    raise SystemExit("ERROR: No XML files found")

final_set = set()

for xml_file in xml_file_list:
    with open('/'.join([RUNDECK_JOBS_PATH,xml_file]), 'r') as f:
        tree = ET.parse(f)
        root = tree.getroot()
        emails = root.findall(".//email")

        for each in emails:
            recipients = each.attrib['recipients']
            multi = recipients.split(', ')
            for each_email in multi:
                final_set.add(each_email.strip())

for email in sorted(final_set):
    print (email)
