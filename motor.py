# /robotafm/motor/motor.py
# Program for calculating engine parameters.

# imports:
import cv2
import os
import numpy as np

# constants:
image_path = './data/imgs/'
image = image_path + 'motor.png'

# vars:
stator_poles = 4 # motor stator poles count
rotor_poles = 8 # motor rotor poles count
phases = 3 # motor phases count
outrunner = True # inrunner or outrunner

# create motor image 
mat = cv2.imread(image)

# Window name in which image is displayed
window_name = 'Motor'

# circle
center_coordinates = (150, 150)
radius = 100
color = (155, 155, 155) # Color in BGR
thickness = -1
output_image = cv2.circle(mat, center_coordinates, radius, color, thickness)

# line
start_point = (50, 50)
end_point = (60, 70)
color = (255, 0, 0) # Color in BGR
thickness = 25
output_image = cv2.line(output_image, start_point, end_point, color, thickness)
  
# Displaying the image
cv2.imshow(window_name, output_image)
