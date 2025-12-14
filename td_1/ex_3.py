import numpy as np
import cv2
from matplotlib import pyplot as plt

read = cv2.imread('../imgs/poor_david.jpg')
img = cv2.cvtColor(read, cv2.COLOR_BGR2RGB)

R = img[:,:,0]
G = img[:,:,1]
B = img[:,:,2]

gray_avg =  ((R+G+B)/3).astype(np.uint8)
gray_lum =  (0.299*R+0.587*G+0.114*B).astype(np.uint8)
gray_light = ((np.maximum(np.maximum(R,G),B) + np.minimum(np.minimum(R,G),B)) / 2).astype(np.uint8)

# w and h in inches 
plt.figure(figsize=(10,5))

# rows cols index
plt.subplot(1,4,1)
plt.imshow(img)
plt.title("Original")
plt.axis("off")

plt.subplot(1,4,2)
plt.imshow(gray_avg, cmap="gray")
plt.title("Average")
plt.axis("off")

plt.subplot(1,4,3)
plt.imshow(gray_lum, cmap="gray")
plt.title("Luminosity")
plt.axis("off")

plt.subplot(1,4,4)
plt.imshow(gray_light, cmap="gray")
plt.title("Lightness")
plt.axis("off")

plt.show()

reg_avg = gray_avg[0:15,0:15]
reg_lum = gray_lum[0:15,0:15]
reg_light = gray_light[0:15,0:15]

def stats(name,img):
    print(f"{name}")
    print("min :", np.min(img))
    print("max :", np.max(img))
    print("avg:", np.mean(img))
    print("std :", np.std(img))

stats("Average",   gray_avg)
stats("Luminosity", gray_lum)
stats("Lightness", gray_light)

cv2.waitKey(0)
cv2.destroyAllWindows()
