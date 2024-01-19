import cv2
import numpy as np

def enhance_brightness(img,alpha):
    enhanced_img=np.clip(img*alpha,0,255).astype(np.uint8)
    return enhanced_img

def supress_brightness(img,beta):
    enhanced_img=np.clip(img+beta,0,255).astype(np.uint8)
    return enhanced_img

def manipulate_contrast(img,alpha,beta):
    contrast=np.clip(img*alpha+beta,0,255).astype(np.uint8)
    return contrast

img=cv2.imread("D:/DIP PRACTICALS\OPEN CV/dip/apple.jpg",0)
alpha=1.5
beta=5
enhanced_img=enhance_brightness(img,alpha)
supressed=supress_brightness(img,beta)
contrast_img=manipulate_contrast(img,alpha,beta)

cv2.imshow("Contrast Image",contrast_img)
cv2.waitKey(0)
