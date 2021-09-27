import cv2
import numpy as np


"""Creating bland image using numpy"""
img = np.zeros((515, 515, 3), np.uint8)
print(img)

"""Check image shape"""
img_shape = img.shape
print(img_shape)

"""Draw lines in the bland image"""
cv2.line(img, (0, 0), (100, 100), (0, 0, 255), 2)

"""Drawing rectangle"""
cv2.rectangle(img, (300, 200), (350, 250), (255, 0, 0), cv2.FILLED)

"""Drawing circle"""
cv2.circle(img, (200, 400), (80), (0, 0, 255), 2)

"""Write text"""
cv2.putText(img, "Ayuba Tahiru", (78, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (201, 20, 130), 2)

"""Show image"""
cv2.imshow("ayuba",  img)
cv2.waitKey(0)
