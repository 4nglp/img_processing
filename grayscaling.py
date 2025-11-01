import cv2

# yep that's it
dog = cv2.imread('imgs/cooked_dog.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('doggy',dog)
cv2.waitKey(0)
cv2.destroyAllWindows()

