import cv2
from torch.utils import data
import torch
import torchvision
from torchvision.transforms import transforms as trans
import net

transform = trans.Compose (
    [
        trans.Resize ((60, 60)),
        trans.ToTensor ()
    ]
)

path = "splited_data/"
x_test = torchvision.datasets.DatasetFolder (
    root=path + "test", 
    loader=torchvision.datasets.folder.default_loader,
    transform=transform,
    extensions=".png"
)
test_loader = data.DataLoader (
    x_test,
    batch_size=10,
    shuffle=1
)
model = net.Net3 ()
# model.to ("cuda")
model.load_state_dict (torch.load ("model/net3/epoch200/net3_para_200.zip"))
# model.to ("cpu")
model.eval ()

for step, (x, y) in enumerate (test_loader) :
    # x = x.cuda ()
    # y = y.cuda ()
    out = model (x)
    # print (out[0])
    out = torch.softmax (out, 1)
    # print (out[0])
    prob, predi = torch.max (out, 1)
    
    if step % 10 == 0 :
        # print (f"Real : {y[1]} \t Prediction : {predi[1]} \t Probability : {prob[1]}")
        print (f"{y} \n {predi} \n\n")
    
