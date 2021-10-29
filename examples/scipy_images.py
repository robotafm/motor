import numpy as np
from scipy import ndimage

ndimage.imread("../data/imgs/arr.png")
#rotation angle in degree
rotated = ndimage.rotate(image, 45)
ndimage.show(rotated)