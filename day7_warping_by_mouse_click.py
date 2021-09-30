import cv2
import numpy as np


"""Defining zero arrays"""
circle = np.zeros((4, 2), np.int)
counter = 0

"""Function for mouse clicks"""
def mouse_click(events, x, y, flag, params):
    global counter

    try:
        if events == cv2.EVENT_LBUTTONDOWN:
            circle[counter] = x, y
            counter = counter + 1
            print(circle)
    except IndexError:
        print(f"You have clicked the maximum number {counter}, press q to exit")


"""Load and read image"""
img = cv2.imread("images/malcolmx.jpg", 1)

"""Resizing the image"""
width, height = (300, 400)
img_resized = cv2.resize(img, (width, height))

while True:

    if counter == 4:
        width, height = (250, 350)
        pt1 = np.float32([circle[0], circle[1], circle[2], circle[3]])
        pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        img_warp = cv2.warpPerspective(img_resized,  matrix, (width, height))
        cv2.imshow("malcolmx wrap",  img_warp)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # view the points on the card
    for x in range(4):
        cv2.circle(img_resized, (int(circle[x][0]), int(circle[x][1])), 3, (0, 0, 255), cv2.FILLED)

    """Show image"""
    cv2.imshow("malcolmx",  img_resized)
    cv2.setMouseCallback("malcolmx", mouse_click)
    cv2.waitKey(1)