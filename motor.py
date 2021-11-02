# /robotafm/motor/motor.py
# Program for calculating engine parameters.

# imports:
import os
import numpy as np
from PIL import Image, ImageDraw

# constants:
image_path = './data/imgs/motor.png'

# vars:
stator_poles = 8 # motor stator poles count
rotor_poles = 8 # motor rotor poles count
phases = 3 # motor phases count
outrunner = True # inrunner or outrunner

# Draw rotor:
# create rotor image 
rotor_image = Image.open(image_path)
width, height = rotor_image.size
draw = ImageDraw.Draw(rotor_image)
xy = [(width/2-0.4*width,height/2-0.4*height),(width/2+0.4*width,height/2+0.4*height)]
start = 0 # in degrees. Angles are measured from 3 o’clock, increasing clockwise
end = 180/rotor_poles
color = ['blue','red']

for count in range(rotor_poles*2):
    draw.pieslice(xy, start, end, fill=color[count%2], outline=None, width=1)
    start = end
    end = end + 180/rotor_poles

xy = [(width/2-0.33*width, height/2-0.33*height), (width/2+0.33*width, height/2+0.33*height)]
draw.ellipse(xy, fill='white', outline=None, width=1)

images =  []

for count in range(20):
    image = rotor_image.rotate(5*count, fillcolor='white') # Counterclock-wise, white corners.
    images.append(image)

#images[0].save('./data/imgs/animation.gif',
#               save_all=True, append_images=images[1:], optimize=False, duration=100, loop=0)

# Draw stator:
stator_image = Image.open(image_path) # Clean image
draw = ImageDraw.Draw(stator_image) 

xy = [(width/2-0.1*width, height/2-0.1*height), (width/2+0.1*width, height/2+0.1*height)]
draw.ellipse(xy, fill='gray', outline=None, width=1)

coord_rect1 = [(width/2-0.02*width, height/2-0.3*height), (width/2+0.02*width, height/2)]
coord_rect2 = [(width/2-0.05*width, height/2-0.3*height), (width/2+0.05*width, height/2-0.25*height)]
for count in range(stator_poles*3): # 3 phases
    image = stator_image.rotate(360/stator_poles/3*count, 
                                       fillcolor='white') # Counterclock-wise, white corners.
    draw = ImageDraw.Draw(image) 
    draw.rectangle(coord_rect1, fill='gray', outline=None, width=1)
    draw.rectangle(coord_rect2, fill='gray', outline=None, width=1)
    for line_step in range(12):
    	draw.line((width/2-0.03*width,height/2-0.24*height+0.24*height/20*line_step, 
    		       width/2+0.03*width,height/2-0.24*height+0.24*height/20*line_step), fill="red")
    image = image.rotate(-360/stator_poles/3*count, 
                                       fillcolor='white') # Clock-wise, white corners.
    stator_image = image

# Displaying the image
rotor_image.show()
stator_image.show()
