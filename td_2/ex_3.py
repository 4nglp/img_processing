import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../imgs/sunflowers_field.jpg")
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

mean_filter = cv.blur(img_rgb,(5,5)) # kernel size / blur edges, replaces each pixel with the avg of its neighbor
median_filter = cv.medianBlur(img_rgb,5) # excellent for salt and pepper noise, preserves edges 
gauss_filter = cv.GaussianBlur(img_rgb,(5,5),0) # + sigma the smaller the better for the edges / slight edge blur
bilateral_filter = cv.bilateralFilter(img_rgb, d=9, sigmaColor=75, sigmaSpace=75) # delimiter, similarity and closness / best for detailed imgs preserves edges

titles = ["original","mean filter","median filter","gaussian filter","bilateral filter"]
imgs = [img_rgb,mean_filter,median_filter,gauss_filter,bilateral_filter]
plt.figure(figsize=(15,5))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(imgs[i])
    plt.title(titles[i])
    plt.axis('off')
plt.show()

# mean & gauss -> blur edges
# median -> preserves edges better
# bilateral -> the best