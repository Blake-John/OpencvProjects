#       [        116,         174],
#       [       1653,         198],
#       [       1651,         338],
#      [        114,         313] 
#

import cv2
from cnocr import CnOcr

path = r"imgs/1.png"
ocrer = CnOcr ()
img = cv2.imread (path)
imgGray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

out = ocrer.ocr (imgGray)

a = input ("Please input what you want : \n")

list_a = list (a)

score = 0

for i in out :
    list_text = list (i['text'])
    total = len (list_text)
    for j in list_a :
        if j in list_text :
            score += 1
    accu = score / total
    if accu > 0.5 :
        start_x = int (i['position'][0][0])
        end_x = int (i['position'][2][0])
        start_y = int (i['position'][0][1])
        end_y = int (i['position'][2][1])
        imgCrop = img[start_y:end_y, start_x:end_x]

cv2.imshow ("Img", imgCrop)
cv2.waitKey(0)