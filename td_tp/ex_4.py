import cv2

def modify_light(img,val):
    modified_img = cv2.add(img,val) if val>=0 else cv2.subtract(img,abs(val))
    return modified_img

colored_img = cv2.imread('../imgs/cooked_dog.jpg')
grayed_img = cv2.imread('../imgs/cooked_dog.jpg',cv2.IMREAD_GRAYSCALE)

lighter_colored = modify_light(colored_img,50)
darker_colored = modify_light(colored_img,-50)
lighter_grayed = modify_light(grayed_img,50)
darker_grayed = modify_light(grayed_img,-50)

cv2.imshow("lighter_colored",lighter_colored)
cv2.imshow("darker_colored",darker_colored)
cv2.imshow("lighter_grayed",lighter_grayed)
cv2.imshow("darker_grayed",darker_grayed)

cv2.waitKey(0)
cv2.destroyAllWindows()