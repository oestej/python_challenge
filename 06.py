import re, zipfile

def get_comment(nothing):
  file = zipfile.ZipFile('data06/channel.zip')
  res = file.getinfo(f"{nothing}.txt").comment
  res = bytes.decode(res)
  file.close
  return res

def get_nothing(nothing, digits):
  file = open(f"data06/{nothing}.txt","r")
  content = file.read()
  file.close()
  matches = digits.search(content)
  if matches:
    data = matches.group(0)
    data = re.sub('Next nothing is ','',data)
    print(f"{get_comment(nothing)}", end='')
    get_nothing(data, digits)
  else:
    print(content)

digits = re.compile('Next nothing is \d+')
get_nothing('90052', digits)

#file = zipfile.ZipFile('data06/channel.zip')
#print(file.comment)
#print(file.getinfo('46145.txt').comment)
#file.close
