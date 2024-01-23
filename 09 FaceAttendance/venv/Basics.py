import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file("imgsBasics/Elon Musk.png")
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgElon = cv2.resize(imgElon, None, None, 0.5, 0.5)
imgTest = face_recognition.load_image_file("imgsBasics/Bill Gates.png")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
imgTest = cv2.resize(imgTest, None, None, 0.5, 0.5)

faceLoc = face_recognition.face_locations(imgElon)[0]
# Returns:
# A list of tuples of found face locations in css (top, right, bottom, left) order
encodeElon = face_recognition.face_encodings(imgElon)[0]
# Returns:
# A list of 128-dimensional face encodings (one for each face in the image)
cv2.rectangle(imgElon, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)

# todo compare the face to find out whether they are one people
results = face_recognition.compare_faces([encodeElon], encodeTest)
# todo to find the similarity between two face
faceDis = face_recognition.face_distance([encodeElon], encodeTest)
print(results)
# print(faceDis)
cv2.putText(imgTest, f"{results} {np.round(faceDis[0], 2)}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow("Elon Musk", imgElon)
cv2.imshow("Elon Test", imgTest)
cv2.waitKey(0)
