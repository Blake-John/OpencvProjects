import cv2
import torch
import numpy as np
import torch.nn as nn
import torchvision

class Net4 (nn.Module) :
    def __init__(self) -> None:
        super(Net4, self).__init__()
        self.conv1 = nn.Sequential (
            nn.Conv2d (1, 16, 5, 1, 2), # (16, 60, 60)
            nn.ReLU (),
            nn.MaxPool2d (2) # (16, 30, 30)
        )
        self.conv2 = nn.Sequential (
            nn.Conv2d (16, 32, 5, 1, 2), # (32, 30, 30)
            nn.ReLU (),
            nn.MaxPool2d (2) # (32, 15, 15)
        )
        self.out = nn.Sequential (
            nn.Linear (32 * 15 * 15 * 1, 32 * 15),
            nn.ReLU (),
            nn.Linear (32 * 15, 10),
        )
        
    def forward (self, x) :
        x = self.conv1 (x)
        x = self.conv2 (x)
        x = x.view (x.size (0), -1)
        x = self.out (x)
        
        return x

model = Net4 ()
model.load_state_dict (torch.load ("model/epoch20/e20_para.pt"))
model.eval ()

cap = cv2.VideoCapture (1)

while True :
    _, img = cap.read ()
    img_inter = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)
    # print (img_input.shape)
    img_inter = cv2.resize (img_inter, (80, 80))
    img_inter = img_inter[10:70, 10:70]
    img_normalize = cv2.normalize (img_inter, None, 0, 1, cv2.NORM_MINMAX)
    
    # print (img_input.shape)
    img_input = np.array (img_normalize, np.float32)
    # print (img_input.shape)
    img_input = torch.from_numpy (img_input)
    img_input = img_input.unsqueeze (0).unsqueeze (0)
    # print (img_input.shape)
    
    out = model (img_input)
    out = torch.softmax (out, 1)
    prob, predi = torch.max (out, 1)
    
    if prob > 0.5 :
        print (f"Prob : {prob} \t Predict : {predi}")
        cv2.putText (img, f"{int (prob[0] * 100)}%  {predi[0]}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    
    
    cv2.imshow ("Img", img)
    cv2.imshow ("img_input", img_inter)
    if cv2.waitKey (30) == 27 :
        break
    