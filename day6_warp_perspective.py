import cv2
import numpy as np


"""Load and read image"""
img = cv2.imread("images/spar.jpg", 1)

"""In other to warp the King card, x and y corners of the card must be noted """
width, height = (250, 350)
pt1 = np.float32([[199, 230], [408, 130], [335, 563], [553, 471]])
pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pt1, pt2)
img_warp = cv2.warpPerspective(img,  matrix, (width, height))


print(pt1)


# view the points on the card
for x in range(4):
    cv2.circle(img, (int(pt1[x][0]), int(pt1[x][1])), 5, (0, 0, 255), cv2.FILLED)

"""Show image"""
cv2.imshow("ayuba",  img)
cv2.imshow("ayuba warp",  img_warp)
cv2.waitKey(0)