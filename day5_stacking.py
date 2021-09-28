import cv2
import numpy as np
import image_stack_lib


stack = image_stack_lib

"""Showing video"""
frameWidth = 1280
frameHeight = 1000

cap = cv2.VideoCapture(0)

while True:
    sucess, imag = cap.read()
    img = cv2.resize(imag, (frameWidth, frameHeight))
    cv2.imshow("vidoe", imag)


    kernel = np.ones((5, 5), np.uint8)

    """Load and read image"""
    # img = cv2.imread("images/ayuba_profile_pic.png", 10)

    """Convert image to gray, Using BGR2GRAY"""
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    """Making image blur"""
    img_blur = cv2.GaussianBlur(img, (9, 9), 0)

    """Detecting edge in image using canny function"""
    img_canny = cv2.Canny(img, 50, 50)

    """Image dilation"""
    img_dilation = cv2.dilate(img, kernel, iterations=1)

    """Creating bland image using numpy"""
    blankimg = np.zeros((515, 515, 3), np.uint8)

    """Image eroding"""
    img_eroded = cv2.erode(img_dilation, kernel, iterations=1)


    stacked_img = stack.stackImVideo(0.2, ([img, img_gray, img_blur, img_dilation,img_eroded, img],
                                     [img_canny, img_gray, img_blur, img_dilation,img_eroded, img_eroded],
                                     [img_canny, img_gray, img_blur, img_dilation,img_eroded, img_eroded],
                                     [img_canny, img_gray, img_blur, img_dilation,img_eroded, img_eroded],
                                     [img_canny, img_gray, img_blur, img_dilation,img_eroded, img_eroded]))
    cv2.imshow("ayuba",  stacked_img)
    """Show image"""
    # original
    # cv2.imshow("ayuba",  img)
    # # gray
    # cv2.imshow("ayuba gray",  img_gray)
    # # blur
    # cv2.imshow("ayuba blur",  img_blur)
    # # edge detecting
    # cv2.imshow("ayuba edge",  img_canny)
    # # dilation
    # cv2.imshow("ayuba dilate",  img_dilation)
    # # eroding
    # cv2.imshow("ayuba eroded",  img_eroded)
    # cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
