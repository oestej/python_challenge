looknsay = [1, 11, 21, 1211, 111221]

def get_next(val):
  result = ''
  string = str(val)
  current_num = 0
  count = 0
  for number in string:
    if number == current_num:
      count +=1
    elif current_num != 0:
      result = f"{result}{count}{current_num}"
      current_num = number
      count = 1
    else:
      current_num = number
      count = 1      
  result = f"{result}{count}{current_num}"
  return result

for i in range(4, 30):
  looknsay.append(get_next(looknsay[i]))

print(len(looknsay[30]))