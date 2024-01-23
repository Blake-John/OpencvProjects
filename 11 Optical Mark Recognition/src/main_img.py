import cv2
import numpy as np
import utilis

# parameters
widthImg = 700
heightImg = 700
questions = 5
choices = 5
answer = [1, 2, 0, 1, 4]

# load the img and resize it
img = cv2.imread("1.png")
img = cv2.resize(img, (widthImg, heightImg))
imgContours = img.copy()


# process the img
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
imgCanny = cv2.Canny(imgBlur, 10, 50)


# find the contours
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3)
# the index -1 means all the list


# find the rectangle's points
rects = utilis.rectcontours(contours)
# markrect = rects[0]
# graderect = rects[1]
# print (biggestrect)
# cv2.drawContours(imgContours, rects, 0, (0, 0, 255), 3)
# cv2.drawContours(imgContours, rects, 1, (0, 0, 255), 3)
# print (markrect, markrect.shape)
reorrect = utilis.reorder(rects[:2])
# print (reorrect[0])


# warp the iamge
dstpoint = [np.float32 ([[0, 0], [500, 0], [0, 500], [500, 500]]), np.float32 ([[0, 0], [300, 0], [0, 150], [300, 150]])]
# print (dstpoint)

# get the matrix to warp the image
matrix = [cv2.getPerspectiveTransform(reorrect[0], dstpoint[0]), cv2.getPerspectiveTransform(reorrect[1], dstpoint[1])]
# the function receive two parameters : source_point, destination_point

mark = cv2.warpPerspective(img, matrix[0], np.int32 (dstpoint[0][3]))
grade = cv2.warpPerspective(img, matrix[1], np.int32 (dstpoint[1][3]))


# apply threshold to find the marking circle
imgWarpGray = cv2.cvtColor(mark, cv2.COLOR_BGR2GRAY)
imgThr = cv2.threshold(imgWarpGray, 175, 255, cv2.THRESH_BINARY_INV)[1]
# THRESH_BINARY : if the value exceeds the threshold, the value will be set to the maxval
# THRESH_BINARY_INV : the case is the inverse of above, if the value within the threshold, the value will be set to the maxval


# split the img into smaller one which include only one circle
boxes = utilis.splitimg(imgThr)
# cv2.imshow("Box", boxes[1])


# find the marked answer by the nonzero pixel value
# print (cv2.countNonZero(boxes[2]), cv2.countNonZero(boxes[1]), cv2.countNonZero(boxes[0]))
# countNonZero will tell you the number of nonzero pixels
mypixelval = np.zeros((questions, choices))
countR, countC = 0, 0
for image in boxes :
    pixel = cv2.countNonZero(image)
    mypixelval[countR][countC] = pixel
    countC += 1
    if countC == choices :
        countR += 1
        countC = 0
# print (mypixelval)
index = []
for x in range (questions) :
    index.append(np.argmax (mypixelval[x]))
# print (index)


# compare the index with the answer to get score
grading = []
for i in range (questions) :
    if answer[i] == index[i] :
        grading.append(1)
    else :
        grading.append(0)
# print (grading)
score = sum (grading) / questions * 100
# print (score)


# display the answer and score in the img
# imgshowmark = mark.copy()
utilis.showanswer(mark, answer, index, questions, choices)
utilis.showscore(grade, score)

# display the answer in the original image -> inverse the perspective
# to create a hollow img to get the answer and grade
imgshowan = np.zeros_like (mark)
imgshowscore = np.zeros_like (grade)

# get the answer and score in the hollow img
utilis.showanswer(imgshowan, answer, index, questions, choices)
utilis.showscore(imgshowscore, score)

#? How to create the inverse matrix to inverse the perspective ?
invmatrix = [cv2.getPerspectiveTransform(dstpoint[0], reorrect[0]), cv2.getPerspectiveTransform(dstpoint[1], reorrect[1])]
imginvWarp = [cv2.warpPerspective(imgshowan, invmatrix[0], (widthImg, heightImg)), cv2.warpPerspective(imgshowscore, invmatrix[1], (widthImg, heightImg))]

# to combine the image and the imginvWarp
imgFinal = img.copy()
imgFinal = cv2.addWeighted(imgFinal, 1, imginvWarp[0], 0.5, 0)
imgFinal = cv2.addWeighted(imgFinal, 1, imginvWarp[1], 1, 0)
# cv2.addWeighted (src1: Mat | ndarray[Any, dtype[generic]] | ndarray,
#                 alpha: float, 第一张图片的权重
#                 src2: Mat | ndarray[Any, dtype[generic]] | ndarray,
#                 beta: float, 第二张图片的权重
#                 gamma: float, 结果中添加的值，即对整个融合后的图片进行颜色的调整，值越大，图片变得越白
#                 dst: Mat | ndarray[Any, dtype[generic]] | ndarray | None = ...,
#                 dtype: int = ...
#                 )


imgs = [img, mark, imgshowan, imgshowscore, imginvWarp[0], imginvWarp[1], imgFinal]
utilis.display(imgs)
if cv2.waitKey(0) == 27 :
    exit()