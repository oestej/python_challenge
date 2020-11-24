from PIL import Image

image = Image.open('data11/cave.jpg')

print(image)

new_1 = Image.new('RGB', (320,240))
new_2 = Image.new('RGB', (320,240))

for x in range(1,640):
  for y in range(1,480):
    pixel = image.getpixel((x,y))
    if y%2 == 0 and x%2 == 0:
      new_1.putpixel((int(x/2),int(y/2)),pixel)
    elif y%2 == 1 and x%2 == 1:
      new_2.putpixel((int((x-1)/2), int((y-1)/2)),pixel)

#make 2 320x240 images
image.close()
new_1.save('data11/cave_n1.jpg')
new_1.close()
new_2.save('data11/cave_n2.jpg')
new_2.close()