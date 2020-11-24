riddle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = ""

for letter in riddle:
  if ord(letter) >= 96 and ord(letter) <=122:
    num = ord(letter)+2
    num = (num - 96) % 26 + 96
  else:
    num = ord(letter)
  result += chr(num)

print(result)
