import cv2
import numpy as np

def region_growing(img,seed,thres):
    h,w=img.shape
    mask=np.zeros((h,w),dtype=np.uint8)
    stack=[seed]
    seed_intensity=img[seed]
    while stack:
        x,y=stack.pop()
        if 0<=x<h and 0<=y<w and mask[x,y]==0:
            if abs(int(img[x,y])-int(seed_intensity))<thres:
                mask[x,y]=255
                stack.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
    return mask
org_img=cv2.imread("D:/DIP PRACTICALS\OPEN CV/dip/apple.jpg",0)
seed_point=(100,100)
segmented_region=region_growing(org_img,seed_point,30)
cv2.imshow("Segmented Image",segmented_region)
cv2.waitKey(0)