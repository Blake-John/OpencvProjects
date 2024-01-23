import cv2
import numpy as np
import os

mainpath = r"imgs/"

myfolders = os.listdir (mainpath)
# print (myfolders)

for folder in myfolders :
    path = mainpath + folder
    # print (path)
    
    images = []
    mylist = os.listdir (path)
    # print (mylist)
    # print (f"Total numbers of images detected : {len (mylist)}")
    
    for imgname in mylist :
        curImg = cv2.imread (f"{path}/{imgname}")
        curImg = cv2.resize (curImg,(0, 0), None, 0.2, 0.2)
        images.append (curImg)
        
    print (len (images))
    
    stitcher = cv2.Stitcher.create ()
    (status, result) = stitcher.stitch (images)
    if status == cv2.STITCHER_OK :
        print ("Panoroma Generated ! ")
        cv2.imshow (f"Panorama {folder}", result)
        # cv2.waitKey (0)
    else :
        print ("Panorama Generation Failed !")
    
cv2.waitKey (0)