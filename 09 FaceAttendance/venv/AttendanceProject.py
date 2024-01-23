import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

path = r"imgsAttendance/"
imgs = []
classnames = []
myList = os.listdir(path)
# print(myList)
for cls in myList :
    curImg = cv2.imread(path + cls)
    imgs.append(curImg)
    classnames.append(os.path.splitext(cls)[0]) # split the str by dot .
print(classnames)

def findEncoding (imges) :
    encodeList = []
    for img in imges :
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

def markAttendance (name) :
    with open("venv/Attendance.csv", 'r+') as f :
        myDataList = f.readlines()
        namelist = []
        for line in myDataList :
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist :
            now = datetime.now()
            dstring = now.strftime("%H:%M:%S")
            f.writelines(f"\n{name}, {dstring}")

markAttendance('Elon')

encodeListKnown = findEncoding(imgs)
print("Encoding Complete !")

cap = cv2.VideoCapture (0)

while True :
    success, img = cap.read()
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(img)
    encodeCurFrame = face_recognition.face_encodings(img, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame) :
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex] :
            name = classnames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2), (x2, y2 + 35), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

    cv2.imshow("Cam", img)
    if cv2.waitKey(2) == 27 :
        exit()