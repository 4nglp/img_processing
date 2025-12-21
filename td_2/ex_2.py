import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../imgs/cooked_dog.jpg")

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
r,g,b = cv.split(img_rgb)
L = 0.299 * r + 0.587 * g + 0.114 * b 
s = 150

result = img_rgb.copy()
mask = L > s # 2d bool arr same hieght and width as the img
gray = L.astype(np.uint8)
result[mask] = np.stack(
    (gray[mask],
     gray[mask],
     gray[mask]),
    axis=1 # creates cols that stack horizontally like RGB channels
)

plt.figure(figsize=(10,5))
imgs = [img_rgb,result]
titles = ["original","con"]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.axis("off")
plt.show()
