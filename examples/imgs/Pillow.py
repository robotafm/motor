from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter

image = Image.open('../../data/imgs/nina.png')
#image.show()

r, g, b = image.split()
#r.show()

cropped = image.crop((80, 80, 200, 400))
#cropped.show()

#cropped.save('../../data/imgs/cropped.png')

rotated = cropped.rotate(45)
#rotated.show()

 # Создаем белый квадрат
img = Image.new('RGBA', (200, 200), 'white')    
idraw = ImageDraw.Draw(img)
idraw.rectangle((10, 10, 110, 100), fill='blue')
#img.show()

text = "Hello World!"
font = ImageFont.truetype("arial.ttf", size=18)
idraw.text((10, 10), text, font=font)
#img.show()

# BLUR, SHARPEN, DETAIL, EDGE_ENHANCE, EMBOSS, SMOOTH, etc.
blur = image.filter(ImageFilter.BLUR)
#blur.show()
sharpen = image.filter(ImageFilter.SHARPEN)
#sharpen.show()
  
  # See Modes:
  #https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes
grayscale = image.convert('L')
#grayscale.show()

resize = image.resize((30, 100), Image.ANTIALIAS)
#resize.show()

  #in scale:
width, height = image.size
new_width  = 100
new_height = int(new_width * height / width)
resize = image.resize((new_width, new_height), Image.ANTIALIAS)
#resize.show()

# Gif animation:
images = []
images.append(image)
images.append(blur)
images.append(sharpen)
images.append(grayscale.convert('RGB')) #Mode RGB only!
images[0].save('../../data/imgs/nina.gif',
               save_all=True, append_images=images[1:], optimize=False, duration=500, loop=0)
