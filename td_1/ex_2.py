import numpy as np
import cv2

img = np.zeros((150, 150), dtype=np.uint8)

center = (75, 75)
cv2.circle(img, center, 30, 255, -1)  
cv2.rectangle(img, (0,0), (40,20), 255, -1)
cv2.line(img, (0, 0), (149, 149), 255, 1)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
