import cv2
import numpy as np

# Load the image
image = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)

# Robert operator kernels
kernel_gx = np.array([[-1, 0,1], [-2,0,2],[-1,0,1]], dtype=np.float32)
kernel_gy = np.array([[-1, -2,-1], [0,0, 0],[1,2,1]], dtype=np.float32)

# Apply convolution manually
robert_gx = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT)
robert_gy = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_CONSTANT)
result = np.zeros_like(image, dtype=np.float32)

for i in range(1, image.shape[0] + 1):
    for j in range(1, image.shape[1] + 1):
        result[i-1, j-1] = np.abs(np.sum(robert_gx[i-1:i+2, j-1:j+2] * kernel_gx) + np.sum(robert_gy[i-1:i+2, j-1:j+2] * kernel_gy))

# Convert result to uint8 for display
result = np.uint8(result)

# Display the original and result images
cv2.imshow('Original Image', image)
cv2.imshow('Robert Magnitude', result)
cv2.waitKey(0)
cv2.destroyAllWindows()