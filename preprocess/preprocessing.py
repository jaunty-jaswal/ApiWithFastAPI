import cv2
import numpy as np

def deskew(image):
    #converting to grayscale, then inverting black to white and viceversa
    graycolor = cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    #finding boundaries(where value is more than 1)
    coords = np.column_stack(np.where(graycolor > 0))
    #extracting angle of rotation
    angle = cv2.minAreaRect(coords)[-1]  
    #angle to remain between -45 to 45  
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
     #height and width
    (h, w) = image.shape[:2]
    #center of image
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    #rotate the image on the bases of rotation matrix
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated