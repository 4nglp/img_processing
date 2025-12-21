import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../imgs/sunflowers_field.jpg")  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
], dtype=np.float32)

kernel /= kernel.sum()

blurred_img = cv2.filter2D(img, -1, kernel) # -1 for ddepth it's just like telling opencv to keep the same data type as the input img

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(img)
plt.axis('off')

plt.subplot(1,2,2)
plt.title("Blurred Image")
plt.imshow(blurred_img)
plt.axis('off')

plt.show()

# its effect is simillar to gaussian blur, it gives more weight to the center pixel and less to the neighbors 
# useful on noise reduction especially gaussian, pre-processing for edge detection
# disadvantages: blurs edges and fine details, not effective for all noise types and may reduce the img's contrast if overused
# the contrast of an image is the difference in brightness or color between pixels