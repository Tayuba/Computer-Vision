import cv2
import numpy as np

"""Load and read image"""
img = cv2.imread("images/ayuba_profile_pic.png", 1)

"""Show image"""
cv2.imshow("ayuba",  img)
cv2.waitKey(1000)

"""Showing video"""
frameWidth = 1280
frameHeight = 720

cap = cv2.VideoCapture(0)

while True:
    sucess, imag = cap.read()
    imag = cv2.resize(imag, (frameWidth, frameHeight))
    cv2.imshow("vidoe", imag)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break