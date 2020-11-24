import requests, re

# Parse out the text block
link = 'http://www.pythonchallenge.com/pc/def/equality.html'
body = requests.get(link)

pattern = re.compile('[\na-z][A-Z]{3}[a-z][A-Z]{3}[a-z\n]')
match = pattern.findall(body.text)

result = ""
for data in match:
  result += data[4]

print(result)