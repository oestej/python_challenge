import requests, base64

xml_test_string = f"""<?xml version='1.0' encoding='utf-8'?>
<methodCall>
<methodName>phone</methodName>
<params>
<param>
<value><string>Bert</string></value>
</param>
</params>
</methodCall>"""
headers = {'Content-Type': 'application/xml'}
print(requests.post('http://www.pythonchallenge.com/pc/phonebook.php',data=xml_test_string, headers=headers).text)