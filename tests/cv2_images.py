# imports:
import cv2
import os
import numpy as np

# constants:
image_path = '../data/imgs/motor.png'

# create motor image 
image = cv2.imread(image_path)

# Window name in which image is displayed
window_name = 'Image'

# Polygon corner points coordinates
pts = np.array([[25, 70], [25, 160], 
                [110, 160], [110, 70]],
               np.int32)
#1print(pts)
#pts = pts.reshape((-1, 1, 2))
#print(pts)

isClosed = True
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 20
  
# Using cv2.polylines() method
# Draw a Blue polygon with 
# thickness of 1 px
image = cv2.polylines(image, [pts], 
                      isClosed, color, thickness)

# circle
center_coordinates = (150, 150)
radius = 10
color = (155, 155, 155) # Color in BGR
thickness = -1
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# line
start_point = (50, 50)
end_point = (60, 70)
color = (255, 0, 0) # Color in BGR
thickness = 25
image = cv2.line(image, start_point, end_point, color, thickness)
  
# Displaying the image
while(1):
      
    cv2.imshow('image', image)
    if cv2.waitKey(20) & 0xFF == 27:
        break
          
cv2.destroyAllWindows()

# Animation:

#import glob
#import opencv.highgui

#highgui.cvNamedWindow('mahMovie')

# Assumes an ordered sequence of filenames (001.jpg, 002.jpg, etc)
#for filename in sorted(glob.glob('./*.jpg')):
 #   img = highgui.cvLoadImage(filename)
 #   highgui.cvShowImage('mahMovie', img)
 #   highgui.cvWaitKey(33)

#highgui.DestroyWindow('mahMovie)