import cv2
import numpy as np

img= cv2.imread("apple.jpg",0)

height,width=img.shape

c=45

for i in range(height):
    for j in range(width):
        log_value=c*np.log(1+img[i,j])
        img[i,j]=np.clip(log_value,0,255)

img=np.uint8(img)

cv2.imshow("Output",img)
cv2.waitKey(0)
