import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../imgs/poor_david.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

h, w, c = image.shape
print("dimensions:", h, w, c)

r, g, b = cv2.split(image)

red_image = cv2.merge([r, np.zeros_like(g), np.zeros_like(b)])
green_image = cv2.merge([np.zeros_like(r), g, np.zeros_like(b)])
blue_image = cv2.merge([np.zeros_like(r), np.zeros_like(g), b])

plt.figure(figsize=(10,5))

plt.subplot(1,4,1)
plt.imshow(image)
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(red_image)
plt.title("Red")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(green_image)
plt.title("Green")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(blue_image)
plt.title("Blue")
plt.axis("off")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

cy, cx = h // 2, w // 2
# rows from to then cols y,x 
portion = image[cy-5:cy+5, cx-5:cx+5]
b_p, g_p, r_p = cv2.split(portion)

print("r portion:\n", r_p)
print("g portion:\n", g_p)
print("b portion:\n", b_p)

new_image = cv2.merge([b, np.zeros_like(g), r])
cv2.imshow('new image', new_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
