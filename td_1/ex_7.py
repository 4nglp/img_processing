import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_bgr = cv.imread("../imgs/cooked_dog.jpg")
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)

h, w, _ = np.shape(img_rgb)
num_pixels = h * w

def reduce_depth(img, r_bits, g_bits, b_bits):
    # right shifting
    r = img[:,:,0] >> (8 - r_bits)   
    g = img[:,:,1] >> (8 - g_bits)
    b = img[:,:,2] >> (8 - b_bits)
    # shift back to the left and add an offset to center the color
    r = (r << (8 - r_bits)) + (1 << (7 - r_bits))
    g = (g << (8 - g_bits)) + (1 << (7 - g_bits))
    b = (b << (8 - b_bits)) + (1 << (7 - b_bits))
    # 0 h 1 r 2 c
    return np.stack([r,g,b], axis=2).astype(np.uint8)

img_16bit = reduce_depth(img_rgb, 5, 6, 5)
img_8bit  = reduce_depth(img_rgb, 3, 3, 2)
img_4bit  = reduce_depth(img_rgb, 2, 1, 1)
img_2bit  = reduce_depth(img_rgb, 1, 1, 0) 

plt.figure(figsize=(12,6))
plt.subplot(1,5,1)
plt.title("original 24-bit")
plt.axis("off")
plt.imshow(img_rgb)

plt.subplot(1,5,2)
plt.title("16-bit")
plt.axis("off")
plt.imshow(img_16bit)

plt.subplot(1,5,3)
plt.title("8-bit")
plt.axis("off")
plt.imshow(img_8bit)

plt.subplot(1,5,4)
plt.title("4-bit")
plt.axis("off")
plt.imshow(img_4bit)

plt.subplot(1,5,5)
plt.title("2-bit")
plt.axis("off")
plt.imshow(img_2bit)

plt.show()

def calc_stats(r_bits, g_bits, b_bits):
    depth = r_bits + g_bits + b_bits
    num_colors = 2**depth
    mem_size = num_pixels * depth / 8  
    return num_colors, mem_size

depths = [(5,6,5), (3,3,2), (2,1,1), (1,1,0)]
names = ["16-bit", "8-bit", "4-bit", "2-bit"]

for name, d in zip(names, depths):
    colors, size = calc_stats(*d)
    print(f"{name}: {colors}  possible colors, size= {size:.0f} octs")
