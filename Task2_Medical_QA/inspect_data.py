import xml.etree.ElementTree as ET

file_path = "data/MedQuAD/1_CancerGov_QA/0000001_1.xml"

tree = ET.parse(file_path)
root = tree.getroot()

print("Root tag:", root.tag)

for element in root.iter():
    if element.text and element.text.strip():
        print(element.tag, ":", element.text.strip()[:300])