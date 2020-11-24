import requests, re

# Parse out the text block
link = 'http://www.pythonchallenge.com/pc/def/ocr.html'
body = requests.get(link)

pattern = re.compile('<!--\n%((.|\n)*?)-->')
match = pattern.search(body.text)

data = match.group()
data = re.sub('<!--\n','',data)
data = re.sub('\n-->','',data)

frequency = {}
for letter in data:
  if letter in frequency:
    frequency[letter] = frequency[letter] + 1
  else:
    frequency[letter] = 1

rare = ""
for key in frequency:
  if frequency[key] == 1:
    rare += key

print(rare)