import cv2
from cnocr import CnOcr
from PIL import ImageGrab

cap = cv2.VideoCapture (0)

while True :
    timer = cv2.getTickCount ()
    _, img = cap.read ()
    ocr = CnOcr ()
    
    out = ocr.ocr (img)
    # for i in out :
    #     print (i['text'],i['position'])
    # cv2.imshow ("Image", img)
    # cv2.waitKey (10)
    for i in out :
        if len (out) != 0 :
            pt1 = (int (i['position'][0][0]),int (i['position'][0][1]))
            pt2 = (int (i['position'][2][0]),int (i['position'][2][1]))
            cv2.rectangle (img, pt1, pt2, (255, 0, 255), 2)
            cv2.putText (img, i['text'], pt1, cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
    cv2.imshow ("Image", img)
    if cv2.waitKey (2) & 0xFF == ord ('q') :
        exit ()