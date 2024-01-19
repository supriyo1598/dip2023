import cv2
import numpy as np

def add_gaussian(img,mean=0,sigma=25):
    row,col=img.shape
    gauss=np.random.normal(mean,sigma,(row,col))
    noisy=np.clip(img+gauss,0,255)
    noisy=noisy.astype(np.uint8)
    return noisy

org_img=cv2.imread("D:/DIP PRACTICALS\OPEN CV/dip/apple.jpg",0)

noisy_img=add_gaussian(org_img)
cv2.imshow("Noisy Image",noisy_img)
cv2.waitKey(0)