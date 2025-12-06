import cv2

# dec
img = cv2.imread("../imgs/serious_cat.jpg")
portion = img[0:10,0:10]
size = img.shape

print("size: ",size)
print("10x10 portion: ",portion)

cv2.imshow('poor david',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4
# if gray
# 0 black weak lighting 128 gray med ich 255 black we up 0~255
# if colored
# 0,0,0 black and no light 255,255,255 white with maximal lighting 255,0,0 red mid 

