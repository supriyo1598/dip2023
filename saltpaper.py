import cv2
import numpy as np

def add_salt_and_paper(img , salt,paper):
    noisy=np.copy(img)

    salt_pixel=np.random.rand(*img.shape)<salt
    noisy[salt_pixel]=255

    paper_pixel=np.random.rand(*img.shape)<paper
    noisy[paper_pixel]=0
    return noisy

org_img=cv2.imread("D:/DIP PRACTICALS\OPEN CV/dip/apple.jpg",0)
salt=0.02
paper=0.02
noisy_img=add_salt_and_paper(org_img,salt,paper)
cv2.imshow("Noisy Image",noisy_img)
cv2.waitKey(0)