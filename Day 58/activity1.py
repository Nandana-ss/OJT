import numpy as np
import cv2
image = cv2.imread("apple.jpeg")
if image is None:
    print("Could not read the image")
    exit()
# cv2.imshow("Original image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#convert to graycale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply gaussian blur
blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#edge detection using canny
edges = cv2.Canny(blur_image, 100, 200)

# original image
cv2.imshow("gray scale image:",image)
cv2.waitKey(0)

cv2.imshow("gray scale image:", gray_image)
cv2.waitKey(0)

cv2.imshow("gray scale image:", blur_image)
cv2.waitKey(0)

cv2.imshow("gray scale image:", edges)
cv2.waitKey(0)

cv2.destroyAllWindows()