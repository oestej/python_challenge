from PIL import Image

#image = Image.open('data12/evil1.jpg')

#new_image = Image.new('RGB',(128,96))

#for x in range(1,640):
#  for y in range(1,480):
#    if x%5 == 0 and y%5 == 0:
#      pixel = image.getpixel((x,y))
#      new_image.putpixel((int((x/5)),int((y)/5)), pixel)

#image.close()
#new_image.show()

# Open files

out_list = list()
for i in range(0,5):
  out_list.append(open(f"data12/out{i}.png", "wb+"))

with open('data12/evil2.gfx', 'rb') as in_file:
  byte = in_file.read(1)
  i = 0
  while byte:
    out_list[i].write(byte)
    i = (i + 1) % 5
    byte = in_file.read(1)

# Close files
for f in out_list:
  f.close()

in_file.close()

#disproportionality