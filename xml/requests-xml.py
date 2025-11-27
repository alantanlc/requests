import xml.etree.ElementTree as ET
import requests
import json

# root
root = ET.Element("methodCall")

# methodName
method_name = ET.SubElement(root, "methodName")
method_name.text = "callFunc"

# params
params = ET.SubElement(root, "params")

# func param
func_param = ET.SubElement(params, "param")
func_value = ET.SubElement(func_param, "value")
func_string = ET.SubElement(func_value, "string")
func_string.text = "getData"

# json param
json_param = ET.SubElement(params, "param")
json_value = ET.SubElement(json_param, "value")
json_string = ET.SubElement(json_value, "string")
json_string.text = '{"function_name":"getData","profileName":"","paramValuesDict":{"date":"20251127"}"}'

# convert to xml string
xml_data = ET.tostring(root, encoding = "utf-8", method = "xml")
print(xml_data.decode())

# call
url = "https://example.com/get-data"
headers = {"Content-Type": "text/xml"}
response = requests.post(url, data = xml_data, headers = headers)
response_text_xml = ET.fromstring(response.text)

# csv
response_string = response_text_xml.find("string").text
headers = json.loads(response_string).get("column_names")
data = json.loads(response_string).get("data")
with open("rates.csv", "w") as f:
    f.write(f"{'|'.join(headers}\n")
    for d in data:
        f.write(f"{'|'.join([str(v) for v in d])}\n")

