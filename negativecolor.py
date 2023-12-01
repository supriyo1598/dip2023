import cv2
import numpy as np

img=cv2.imread("apple.jpg",1)

print(img.shape)


height,width,channel=img.shape

for i in range (height):
    for j in range(width):
        for k in range(channel):
            img[i,j,k]=255-img[i,j,k]

cv2.imshow("Output",img)
cv2.waitKey(0)

cv2.imwrite("Output.jpg",img)
