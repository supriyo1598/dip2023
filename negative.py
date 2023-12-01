import cv2
import numpy as np

img=cv2.imread("apple.jpg",0)

print(img.shape)

height,width=img.shape

for i in range (height):
    for j in range(width):
        img[i,j]=255-img[i,j]

cv2.imshow("Output",img)
cv2.waitKey(0)
