import requests, re

def get_nothing(nothing, digits):
  url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}"
  body = requests.get(url)
  matches = digits.search(body.text)
  if matches:
  	data = matches.group(0)
  	data = re.sub('the next nothing is ','', data)
  	print(data)
  	get_nothing(data, digits)
  else:
  	print(body.text)

digits = re.compile('the next nothing is \d+')
#get_nothing('12345', digits)
get_nothing('8022', digits)