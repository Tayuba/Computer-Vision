import cv2
import numpy as np

def stackImVideo(scale, Img_Vid_Array):
    rows = len(Img_Vid_Array)
    cols = len(Img_Vid_Array[0])
    rowsAvailable = isinstance(Img_Vid_Array[0], list)
    width = Img_Vid_Array[0][0].shape[1]
    height = Img_Vid_Array[0][0].shape[0]

    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if Img_Vid_Array[x][y].shape[:2] == Img_Vid_Array[0][0].shape[:2]:
                    Img_Vid_Array[x][y] =cv2.resize(Img_Vid_Array[x][y], (0, 0), None, scale, scale)
                else:
                    Img_Vid_Array[x][y] = cv2.resize(Img_Vid_Array[x][y], (Img_Vid_Array[0][0].shape[1], Img_Vid_Array[0][0].shape[0]), None, scale, scale)
                if len(Img_Vid_Array[x][y].shape) == 2: Img_Vid_Array[x][y] = cv2.cvtColor(Img_Vid_Array[x][y], cv2.COLOR_BGR2RGB)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_cor = [imageBlank]*rows

        for x in range(0, rows):
            hor[x] = np.hstack(Img_Vid_Array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if Img_Vid_Array[x].shape[:2] == Img_Vid_Array[0].shape[:2]:
                Img_Vid_Array[x] = cv2.resize(Img_Vid_Array[x], (0, 0), None, scale, scale)
            else:
                Img_Vid_Array[x] = cv2.resize(Img_Vid_Array[x], (Img_Vid_Array[0].shape[1], Img_Vid_Array[0].shape[0]), None, scale, scale)
            if len(Img_Vid_Array[x].shape) == 2: Img_Vid_Array = cv2.cvtColor(Img_Vid_Array[x], cv2.COLOR_BGR2RGB)
        hor = np.hstack(Img_Vid_Array)
        ver = hor

    return ver
