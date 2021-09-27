import cv2
import numpy as np

"""Load and read image"""
img = cv2.imread("images/ayuba_profile_pic.png", 1)

"""Confirm image shape"""
img_shape = img.shape
print(img_shape)

"""Resizing the image"""
width, height = (400, 400)
img_resized = cv2.resize(img, (width, height))

"""Crop the image"""
img_crop = img[0:300, 0:500]

"""Show image"""
cv2.imshow("ayuba",  img)
cv2.imshow("ayuba resized",  img_resized)
cv2.imshow("ayuba cropped",  img_crop)
cv2.waitKey(8000)