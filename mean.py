import cv2
import numpy as np

img=cv2.imread("apple.jpg",0)

def mean_filter(image,kernal):
    height,width=image.shape[:2]

    result=np.zeros_like(image,dtype=np.float32)
    for i in range(kernal//2,height-kernal//2):
        for j in range(kernal//2,width-kernal//2):
            result[i,j]=np.mean(image[i-kernal//2:i+kernal//2+1,j-kernal//2:j+kernal//2+1])

    result=result.astype(np.uint8)

    cv2.imshow("Output",result)
    cv2.waitKey(0)

mean_filter(img,3)
