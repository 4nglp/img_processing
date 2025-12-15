import cv2 as cv
import matplotlib.pyplot as plt

read = cv.imread("../imgs/cooked_dog.jpg")
rgb_img = cv.cvtColor(read, cv.COLOR_BGR2RGB)
hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)

h,s,v = cv.split(hsv_img)

gray_img_v = v
gray_img_rgb = cv.cvtColor(rgb_img, cv.COLOR_RGB2GRAY)

titles = ["rgb","h","s","v","gray from v","gray from rbg"]
imgs = [rgb_img,h,s,v,gray_img_v,gray_img_rgb]

plt.figure(figsize=(20,10))
for  i in range(6):
    plt.subplot(1,6,i+1)
    plt.imshow(imgs[i],cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.show()

# v ≈ grayscaling cuz v represents the brightness of each pixel from black to white so does grayscaling
# we lose h color type or info and s the color's intensity we have only the brightness value left on v
# on v shadows r the low v values (dark) n the highlights r the high v values (bright)