import pickle, requests

link = 'http://www.pythonchallenge.com/pc/def/banner.p'
body = requests.get(link)

data = pickle.loads(body.content)
for row in data:
  for item in row:
    print(item[0]*item[1], end='')
  print()