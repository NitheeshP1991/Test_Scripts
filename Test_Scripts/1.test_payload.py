
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, date

tree = ET.parse('../test_payload1.xml')
root = tree.getroot()

for data in root.findall('REQUEST'):
    if data.find('TP'):
        DEPART = data.find('TP').find('DEPART')
        DEPART.text = str(date.today() + timedelta(days=2))
        RETURN = data.find('TP').find('RETURN')
        RETURN.text = str(date.today() + timedelta(days=2))

tree.write('../out_test_payload1.xml')

