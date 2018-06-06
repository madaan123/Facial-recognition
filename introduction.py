import cv2
import numpy as np
import matplotlib.pyplot as plt

# Input a image as a grayscake image as it is much more simplified and easy to perform analysis
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR -> 1
# IMREAD_UNCHANGED -> -1

# Showing the image
cv2.imshow('image',img)
# Waiting for pressing 0 key as a interupt for closing the imge
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Showing the image by matplotlibrary
plt.imshow(img, cmap='gray', interpolation = 'bicubic')
# Plotting a straight line of width 5 on the image
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()

# Saving the black and white image to the working directory
cv2.imwrite('watchgray.jpg',img)