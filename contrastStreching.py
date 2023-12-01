import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('apple.jpg',0)
test=img.copy()
height,width=img.shape

bit_depth=img.dtype.itemsize*8
print(bit_depth)

Lmax=(2**bit_depth)-1
Lmin=0
Mmax=np.max(img)
Mmin=np.min(img)

print(Lmax,Lmin,Mmax,Mmin,end=" ")
result=np.zeros((height,width),dtype='uint8')
for i in range(height):
    for j in range(width):
        p=img[i,j]
        streched_value=int((((Lmax-Lmin)*(p-Mmin))/(Mmax-Mmin))+Lmin)
        result[i,j]=np.clip(streched_value,0,255)

result=np.uint8(result)


fig,axes=plt.subplots(1,2,figsize=(10,5))
axes[0].imshow(test,cmap='gray')
axes[0].set_title("Original Image")

axes[1].imshow(result,cmap='gray')
axes[1].set_title("Streched Image")

plt.show()
