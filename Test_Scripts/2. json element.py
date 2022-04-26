import json


def modifystore(data):
    doc = open("../test_payload.json", "w")
    doc.write(data)
    doc.close()


file = open("../test_payload.json", "r")
data = json.loads(file.read())
file.close()

for key in data.keys():
    if key == 'outParams':
        data.pop(key)
    if key == 'inParams':
        for value in list(data['inParams']):
            if value == 'appdate':
                data[key].pop(value)

new = json.dumps(data)
modifystore(new)
print(data)
