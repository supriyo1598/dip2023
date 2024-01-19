import cv2
import numpy as np

def grey_level_slicing(img,min_inten,max_inten):
    mask=np.logical_and(img>=min_inten,img<=max_inten)
    result=np.where(mask,img,0)
    return result.astype(np.uint8)

org_img=cv2.imread("D:/DIP PRACTICALS\OPEN CV/dip/apple.jpg",0)
segmented_region=grey_level_slicing(org_img,100,200)
cv2.imshow("Segmented Image",segmented_region)
cv2.waitKey(0)