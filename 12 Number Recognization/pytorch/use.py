import torch
import cv2
import net
import torchvision.transforms as trans
import numpy as np

model_path = ""
cap = cv2.VideoCapture (1)
RESIZE = (60, 60)

cnn = net.Net3 ()
cnn.load_state_dict (torch.load ("model/net3/epoch100/net3_para_100.pt"))
cnn.eval ()

while True :
    _, img = cap.read ()
    
    # convert the img to the rgb scale
    img_rgb = cv2.resize (img, (80, 80))
    img_crop = img_rgb[10:70, 10:70]
    img_rgb = cv2.cvtColor (img_crop, cv2.COLOR_BGR2RGB)
    # print (img_rgb.shape)
    
    # add a dimension of batch_size to meet the request of the net
    img_rgb = np.array (img_rgb, np.float32)
    img_rgb = torch.from_numpy (img_rgb)
    # print (img_rgb.shape)
    img_input = torch.transpose (img_rgb, 1, 2)
    img_input = torch.transpose (img_input, 0, 1)
    img_input = img_input.unsqueeze (0)
    # print (img_input.shape)



    out = cnn (img_input)
    out = torch.softmax (out, 1)
    prob, predi = torch.max (out, 1)
    
    if prob > 0.5 :
        # print (f"{prob} \t {predi}")
        print (f"{prob[0]} \t {predi[0]}")
    
    cv2.imshow ("Img", img)
    cv2.imshow ("Crop", img_crop)
    
    if cv2.waitKey (100) == 27 :
        break