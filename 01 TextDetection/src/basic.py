from cnocr import CnOcr
import cv2

path = r"imgs/1.png"
ocrer = CnOcr ()
img = cv2.imread (path)
# imgCrop = img[400:1000,100:]
imgGray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

out = ocrer.ocr (imgGray)
# [{'text' : value, 'score' : value, 'position' : array ([tl, tr, br, bl])]

# text_list = []

for i in out :
    print (i)
    # text_list.append (i['text'])
    pt1 = (int (i['position'][0][0]), int (i['position'][0][1]))
    pt2 = (int (i['position'][2][0]), int (i['position'][2][1]))
    
    cv2.rectangle (img, pt1, pt2, (255,255,0), 3)
    cv2.putText (img, i['text'], pt1, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

print (img.shape)
cv2.imshow ("img", img)
cv2.waitKey (0)

