import cv2
import math


#? How to calculate the angle between two lines ?
#* if we have two lines with gradient of slope k_1 and k_2
#* we can use the equation "k = tan(theta) = abs((k_1 - k_2) / (1 + k_1 * k_2))"


path = "imgs/test.jpg"
img = cv2.imread (path)
pointsList = [] #* to store all the points we click

#todo write a function to trace the mouse's motion
def mousePoints (event, x, y, flags, params) :
    if event == cv2.EVENT_LBUTTONDOWN : #* to monitor the event of the left button
        
        cv2.circle (img, (x, y), 2, (0, 0, 255), cv2.FILLED)
        size = len (pointsList)
        if size % 3 == 1:
            cv2.line (img, pointsList[size - 1], (x, y), (0, 0, 255), 1)
        if size % 3 == 2 :
            cv2.line (img, pointsList[size - 2], (x, y), (0, 0, 255), 1)
        pointsList.append ([x, y])
        # print (pointsList)
        # print (x, y)
        #* this will print out the point we click


#todo write a function to calculate the gradient
def gradient (pt1, pt2) :
    if (pt2[0] - pt1[0]) == 0 :
        return 90
    return (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])

#todo write a function to calculate the angle
def getAngle (pointsList) :
    pt1, pt2, pt3 = pointsList [-3:]
    if pt1 == pt2 or pt1 == pt3 or (pt1 == pt2 and pt1 == pt3) :
        print ("Error !")
        return
    # print (pt1, pt2, pt3)
    k_1 = gradient (pt1, pt2)
    k_2 = gradient (pt1, pt3)
    
    # if k_1 != 90 and k_2 != 90 :
    #     thetaR = math.atan ((k_1 - k_2) / (1 + k_1 * k_2))
    #     #* the result of calculatioin is in radians
    #     thetaD = round (math.degrees (thetaR))
    #     #* convert the radians into angular
    #     if thetaD < 0 :
    #         if thetaD > -90 :
    #             thetaD = -thetaD
    #         else :
    #             thetaD = 180 + thetaD
    # else :
    #     if k_2 != 90 and k_1 == 90:
    #         if pt3[0] < pt1[0] :
    #             if pt3[1] > pt1[1] :
    #                 thetaR = math.atan (k_2)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD =  - thetaD
    #             else :
    #                 thetaR = math.atan (k_2)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = 270 - thetaD
    #         if pt3[0] > pt1[0] :
    #             if pt3[1] > pt1[1] :
    #                 thetaR = math.atan (k_2)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = thetaD - 90
    #             else :
    #                 thetaR = math.atan (k_2)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = thetaD + 90
    #     elif k_1 != 90 and k_2 == 90:
    #         if pt2[0] < pt1[0] :
    #             if pt2[1] > pt1[1] :
    #                 thetaR = math.atan (k_1)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = 90 - thetaD
    #             else :
    #                 thetaR = math.atan (k_1)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = 270 - thetaD
    #         if pt2[0] > pt1[0] :
    #             if pt2[1] > pt1[1] :
    #                 thetaR = math.atan (k_1)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = thetaD - 90
    #             else :
    #                 thetaR = math.atan (k_1)
    #                 thetaD = round (math.degrees (thetaR))
    #                 thetaD = thetaD + 90
    #     else :
    #         if pt2[1] > pt1[1] and pt3[1] > pt1[1] :
    #             thetaD = 0
    #         elif pt2[1] < pt1[1] and pt3[1] < pt1[1] :
    #             thetaD = 0
    #         else :
    #             thetaD = 180
    
    thetaR = math.atan ((k_1 - k_2) / (1 + k_1 * k_2))
    #* the result of calculatioin is in radians
    thetaD = round (math.degrees (thetaR))
    #* convert the radians into angular
    if thetaD < 0 :
        if thetaD > -90 :
            thetaD = -thetaD
        else :
            thetaD = 180 + thetaD
    # print (thetaD)
    
    cv2.putText (img, str (thetaD), pt1, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 1)




width = int (img.shape[1] / 2)
height = int (img.shape[0] / 2)
img = cv2.resize (img, (width, height))

while True :
    
    if len (pointsList) % 3 == 0 and len (pointsList) != 0 :
        getAngle (pointsList)
    
    
    cv2.imshow ("Image", img)
    cv2.setMouseCallback ("Image", mousePoints)
    if cv2.waitKey (20) & 0xFF == ord ('q') : 
        #* cv2.waitKey (20) will wait 20 ms for a Key being pressed
        #* when a key is pressed, it will return the ASCII code of this key
        #* cv2.waitKey (20) & 0xFF will calculate the last 8 bit of the ASCII returned by waitKey
        #* because the binary type of the 0xFF is 11111111
        #* ord ('q') return the ASCII code of 'q'
        pointsList = []
        img = cv2.imread (path)
        img = cv2.resize (img, (width, height))
    if cv2.waitKey (20) == 27 :
        #* 27 is the number of 'Esc' in ASCII code
        exit ()