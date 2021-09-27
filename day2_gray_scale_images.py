import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)

"""Load and read image"""
img = cv2.imread("images/ayuba_profile_pic.png", 10)

"""Convert image to gray, Using BGR2GRAY"""
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""Making image blur"""
img_blur = cv2.GaussianBlur(img, (9, 9), 0)

"""Detecting edge in image using canny function"""
img_canny = cv2.Canny(img, 50, 50)

"""Image dilation"""
img_dilation = cv2.dilate(img, kernel, iterations=1)

"""Image eroding"""
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

"""Show image"""
# original
cv2.imshow("ayuba",  img)
# gray
cv2.imshow("ayuba gray",  img_gray)
# blur
cv2.imshow("ayuba blur",  img_blur)
# edge detecting
cv2.imshow("ayuba edge",  img_canny)
# dilation
cv2.imshow("ayuba dilate",  img_dilation)
# eroding
cv2.imshow("ayuba eroded",  img_eroded)
cv2.waitKey(0)


