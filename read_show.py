import cv2, os

# defining the path
img_path = os.path.join('imgs', 'serious_cat.jpg')
# then we reading 
cat = cv2.imread(img_path)
# doing all the prev steps in a single cmd
dog = cv2.imread('imgs/cooked_dog.jpg')
# after that  we showing
cv2.imshow('Cat', cat)
cv2.imshow('Dog', dog)
# closing after a key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
