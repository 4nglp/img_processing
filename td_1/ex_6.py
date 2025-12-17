import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

read = cv.imread("../imgs/cooked_dog.jpg")
rgb_img = cv.cvtColor(read, cv.COLOR_BGR2RGB)
hsv_img = cv.cvtColor(rgb_img, cv.COLOR_RGB2HSV)

h,s,v = cv.split(hsv_img)

# arr min max if for ex after * a value becomes 400 it will be limited by 255 max val literally
s_up = np.clip(s*1.5,0,255).astype(np.uint8)
s_down = np.clip(s*0.5,0,255).astype(np.uint8)
empty_s = np.zeros_like(s)
full_s = np.full_like(s,255)

def hsv2rgb(h,s,v):
    hsv_img = cv.merge([h,s,v])
    return cv.cvtColor(hsv_img, cv.COLOR_HSV2RGB)

img_up = hsv2rgb(h, s_up, v)
img_down = hsv2rgb(h, s_down, v)
img_zero = hsv2rgb(h, empty_s, v)
img_max = hsv2rgb(h, full_s, v)

titles = ["hsv","s up","s down","empty s", "full s"]
imgs = [hsv_img,img_up,img_down,img_zero,img_max]

plt.figure(figsize=(10,5))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.title(titles[i])
    plt.imshow(imgs[i])
    plt.axis("off")
plt.show()
