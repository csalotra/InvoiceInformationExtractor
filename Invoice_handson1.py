import matplotlib.pyplot as plt
import os
import cv2
import pytesseract
import numpy as np
import math

img = cv2.imread("path to the image of invoice")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

th2= cv2.adaptiveThreshold(~img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15,-2)

horizontal = th2.copy()
vertical = th2.copy()

horizontalsize = math.ceil(horizontal.shape[1])/30)
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontalsize,1))
horizontal = cv2.erode(horizontal, horizontalSructure)
horizontal = cv2.dilate(horizontal, horizontalSructure)

verticalsize = math.ceil(vertical.shape[1])/30)
verticalalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1,verticalsize))
vertical = cv2.erode(vertical, verticalSructure)
vertical = cv2.dilate(vertical, verticalSructure)

result= horizontal+vertical
#cv2.imshow("result",result)
#cv2.waitKey(0)

final=th2-result
#cv2.imshow("final",final)
#cv2.waitKey(0)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(9,1))
connected = cv2.morphologyEx(final,cv2.MORPH_CLOSE, kernel)

contours,_ = cv2.findCountours(connected, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, contours, -1,(0,255,0),1)

print(pytesseract.image_to_string(connected))
