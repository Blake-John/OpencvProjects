import cv2
import numpy as np
# from pyzbar.pyzbar import decode

path = r"imgs/Qr.png"
img = cv2.imread (path)
cv2.imshow ("Image", img)
cv2.waitKey (0)