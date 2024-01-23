import cv2
import numpy as np

def display (imgs) :
    """the function to display the imgs in a list"""
    for i, j in enumerate (imgs) :
        cv2.imshow(f"{str (i)} Img", j)

def rectcontours (contours) :
    """find the rectangles"""
    rects = []

    for i in contours :
        area = cv2.contourArea(i)
        # print (area)
        if area > 10000 :
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if len(approx) == 4 :
                # print (approx)
                rects.append(approx)

    rects = sorted(rects, key=cv2.contourArea, reverse=True)
    # reverse is False by default, which will sort the elements from small to big

    # print (rects)
    return rects


def getpoints (rect, imgcontours) :
    """get the points"""
    for i in rect :
        for j in i :
            cv2.circle(imgcontours, (j[0][0], j[0][1]), 5, (0, 0, 255), cv2.FILLED)

def reorder (rects) :
    """reorder the points in the list and trun it into the numpy array"""
    reorrect = []
    for i in rects :
        i = i.reshape ((4, 2)) # reshape the shape to non addition dimension
        reorpoint = np.zeros((4,2), np.float32)

        # get the origin and the last by doing the sum of the position
        sumpoint = i.sum (1)
        # print (i)
        # print (sumpoint)

        # get the other two points of the image by doing substract of the position
        subpoint = np.diff(i, axis=1) # i[j] - i[i] when j > i 后面减去前面
        # print (subpoint)

        reorpoint[0] = i[np.argmin (sumpoint)]
        reorpoint[1] = i[np.argmin (subpoint)]
        reorpoint[2] = i[np.argmax (subpoint)]
        reorpoint[3] = i[np.argmax (sumpoint)]
        reorrect.append(reorpoint)

    return reorrect


def splitimg (img) :
    """split the warpped img into the boxex only including the circles"""
    rows = np.split (img, 5)
    boxes = []
    for r in rows :
        colssplit = np.hsplit (r, 5)
        for box in colssplit :
            boxes.append(box)
    return boxes
    # print (cols[4][4].shape)
    # cv2.imshow("Split", cols[len (rows) - 1][4])


def showanswer (img, answer, index, questions, choices) :
    """show the answer in the warpped image"""
    secW = img.shape[1] / questions
    secH = img.shape[0] / questions
    for i in range (questions) :
        myans = index[i]
        cX = int (secW * myans + secW / 2)
        cY = int (secH * i + secH / 2)
        if myans == answer[i] :
            cv2.circle(img, (cX, cY), 35, (0, 255, 0), cv2.FILLED)
        else :
            cv2.circle(img, (cX,cY), 35, (0, 0, 255), cv2.FILLED)
            rX = int (secW * answer[i] + secW / 2)
            rY = int (secH * i + secH / 2)
            cv2.circle(img, (rX, rY), 35, (0, 255, 0), cv2.FILLED)


def showscore (img, score) :
    """show the score in the img"""
    cv2.putText(img, str (score), (int (img.shape[1] / 50), int (img.shape[0] - img.shape[0] / 4)), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5)
