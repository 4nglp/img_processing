import cv2

#load
img = cv2.imread('../imgs/poor_david.jpg', cv2.IMREAD_GRAYSCALE)

# img size: height and width
print("shape or size: ", img.shape)

# 10x10 portion of the img
portion = img[0:10, 0:10]

# displaying that portion as a matrix
print("\n10x10 portion of the img:\n", portion)

cv2.imshow('poor david', img)
cv2.imshow('10x10 portion', portion)
cv2.waitKey(0)
cv2.destroyAllWindows()

