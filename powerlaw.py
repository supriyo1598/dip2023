import cv2
import numpy as np

img=cv2.imread('apple.jpg',0)

cv2.imshow("Original",img)

gamma=1.5

height,width=img.shape

for i in range(height):
    for j in range(width):
        pixel_value=img[i,j]/255
        powervalue=(pixel_value**gamma)*255
        img[i,j]=np.clip(powervalue,0,255)

img=np.uint8(img)

cv2.imshow("Output",img)
cv2.waitKey(0)