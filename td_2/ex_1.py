import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("../imgs/poor_david.jpg", cv.IMREAD_GRAYSCALE)

mean = 0 # no brightness shift
sigma = 50 # the higher the noisier
gaussian_noise = np.random.normal(mean, sigma, img.shape) # mean scale size
img_gaussian = img + gaussian_noise 
img_gaussian = np.clip(img_gaussian, 0, 255).astype(np.uint8)

img_sp = img.copy()
p = 0.05
num_pixels = int(p * img.size)
coords = (
    # low high size
    np.random.randint(0, img.shape[0], num_pixels), # img.shape[0] = height = number of rows = maximum row index
    np.random.randint(0, img.shape[1], num_pixels)  # img.shape[1] = width = number of cols = maximum col index
)
img_sp[coords] = np.random.choice([0, 255], num_pixels)
# salt and pepper concept is simply for salt values to equal 0 and the pepper to 255 = random black and white dots

plt.figure(figsize=(12,4))
imgs = [img,img_gaussian,img_sp]
titles = ["original","gauss","salt and pepper 5%"]
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.title(titles[i])
    plt.imshow(imgs[i],cmap="gray")
    plt.axis("off")
plt.show()
