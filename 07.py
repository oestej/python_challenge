from PIL import Image

image = Image.open('data07/oxygen.png')

lastpoint = 0
counter = 0
for index in range(0,629):
  data = image.getpixel((index,45))
  if (data[0] == data[1]) and ((data[0] != lastpoint) or counter > 6):
    lastpoint = data[0]
    counter = 0
    print(chr(data[0]),end='')
  else:
    counter += 1
print()
