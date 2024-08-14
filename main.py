import cv2 as cv
import numpy as np

img = cv.imread("./omrSheet.jpg")
img = cv.resize(img, (400,400), None)

#Image preprocessing:
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img, (7,7), 1)
imgCanny = cv.Canny(imgBlur, 10, 70)
imgCountours = img.copy()
imgBlank = np.zeros_like(img)

#Contours:
countours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
cv.imshow("Win", img)
cv.waitKey(0)

import os 
print("Current Working Directory is: ", os.getcwd())