import cv2
import numpy as np


"""Showing video"""
cap = cv2.VideoCapture(0)
frameWidth = 1280
frameHeight = 720


"""Create empty function"""
def empty(a):
    pass


"""Name window, and define all the various track of HSV"""
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)

while True:
    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    """save the values of HSV into variables"""
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE Max", "HSV")

    min_values = np.array([h_min, s_min, v_min])
    max_values = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, min_values, max_values)
    results = cv2.bitwise_and(img, img, mask=mask)

    mask_con = cv2.cvtColor(mask,cv2.COLOR_GRAY2RGB)
    hstack = np.hstack([img, mask_con, results])
    hstack = cv2.resize(hstack, (1500, 400))

    # cv2.imshow("vidoeHSV", imgHSV)
    # cv2.imshow("vidoemask", mask)
    # cv2.imshow("vidoe", img)
    # cv2.imshow("vidoeresults", results)
    cv2.imshow("vidoerestack", hstack)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyWindow()


"""Show image"""
# cv2.imshow("ayuba",  img)
# cv2.waitKey(1000)
