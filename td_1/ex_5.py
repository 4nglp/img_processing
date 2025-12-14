import cv2 as cv
import matplotlib.pyplot as plt

read = cv.imread("../imgs/cooked_dog.jpg")
rgb_img = cv.cvtColor(read, cv.COLOR_BGR2RGB)
hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)

h,s,v = cv.split(hsv_img)

plt.figure(figsize=(10,5))
# hue color type r,g,b ...
plt.subplot(1,3,1)
plt.imshow(h,cmap="gray")
plt.title("h")
plt.axis("off")
# saturation color intensity pale or vivid
plt.subplot(1,3,2)
plt.imshow(s,cmap="gray")
plt.title("s")
plt.axis("off")
# value lum and brightness
plt.subplot(1,3,3)
plt.imshow(v,cmap="gray")
plt.title("v")
plt.axis("off")
plt.show()

gray_img_v = v
gray_img_rgb = cv.cvtColor(rgb_img, cv.COLOR_RGB2GRAY)

plt.figure(figsize=(8,4))
plt.subplot(1,2,1)
plt.title("gray img from v only")
plt.imshow(gray_img_v, cmap="gray")
plt.axis("off")
plt.subplot(1,2,2)
plt.title("gray from rgb")
plt.imshow(gray_img_rgb, cmap="gray")
plt.axis("off")
plt.show()

# v ≈ grayscaling cuz v represents the brightness of each pixel from black to white so does grayscaling
# we lose h color type or info and s the color's intensity we have only the brightness value left on v
# on v shadows r the low v values (dark) n the highlights r the high v values (bright)