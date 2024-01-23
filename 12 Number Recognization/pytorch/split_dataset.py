import cv2
import os


path = "myData"
myList = os.listdir (path)
print (myList)
images = []
labels = []
test_ratio = 0.2
train_ratio = 0.8
# vali_ratio = 0.2

print ("Reading the images")
for list in myList :
    myImgs = os.listdir (f"{path}/{list}")
    imgs = []
    labs = []
    for img in myImgs :
        curImg = cv2.imread (f"{path}/{list}/{img}")
        curImg = cv2.cvtColor (curImg, cv2.COLOR_BGR2GRAY)
        # cv2.imshow (f"Image {img}", curImg)
        imgs.append (curImg)
        labs.append (list)
    images.append (imgs)
    labels.append (labs)


# if cv2.waitKey (0) == 27 :
#     exit ()


splited_path = "splited_data_gray"
train_path = splited_path + '/' +"train"
test_path = splited_path + '/' +"test"
# vali_path = splited_path + '/' +"vali"

if not os.path.exists (splited_path) :
    os.mkdir (splited_path)
    if not os.path.exists (train_path) :
        os.mkdir (train_path)
    if not os.path.exists (test_path) :
        os.mkdir (test_path)
    # if not os.path.exists (vali_path) :
    #     os.mkdir (vali_path)


print ("Sorting the images")

for label, group in enumerate (images) :
    if not os.path.exists (f"{train_path}/{label}") :
        os.mkdir (f"{train_path}/{label}")
    for i, target_img in enumerate (group[:int (len (group) * train_ratio)]) :
        cv2.imwrite (f"{train_path}/{label}/{i}.jpg", target_img)
    if not os.path.exists (f"{test_path}/{label}") :
        os.mkdir (f"{test_path}/{label}")
    for i, target_img in enumerate (group[int (len (group) * train_ratio):]) :
        cv2.imwrite (f"{test_path}/{label}/{i}.jpg", target_img)
    # if not os.path.exists (f"{vali_path}/{label}") :
    #     os.mkdir (f"{vali_path}/{label}")
    # for i, target_img in enumerate (group[int (len (group) * (1 - vali_ratio)):]) :
    #     cv2.imwrite (f"{vali_ratio}/{label}/{i}.png", target_img)
    print (f"Step {label}")

print ("Finished !")