import os
import torch
import torchvision
from torch.utils import data
from torchvision.transforms import transforms as trans
import net

path = "splited_data/"
EPOCH = 20
BATCH_SIZE = 64
LR = 0.001
RESIZE = (80, 80)
DEGREE = 10
CROP_SIZE = 60
TRAIN_RATIO = 0.8
choice = 0
devices = ["cuda", "cpu"]
device = devices[choice]
print (device)

transform = trans.Compose (
    [   
        trans.Resize (RESIZE),
        trans.RandomRotation (DEGREE),
        trans.RandomHorizontalFlip (),
        trans.CenterCrop (CROP_SIZE),
        trans.ToTensor (),
        trans.Normalize (
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ]
)

train_set = torchvision.datasets.DatasetFolder (
    root=path + "train", 
    loader=torchvision.datasets.folder.default_loader,
    transform=transform,
    extensions=".png"
)


numdata = len (train_set)
train_len = int (numdata * 0.8)
val_len = numdata - train_len
train_set, val_set = data.random_split (train_set, [train_len, val_len])


train_loader = data.DataLoader (
    dataset=train_set,
    batch_size=BATCH_SIZE,
    shuffle=True
)
vali_loader = data.DataLoader (
    dataset=val_set,
    batch_size=BATCH_SIZE,
    shuffle=True
)


net_num = 4
if net_num == 1 :
    cnn = net.Net ()
elif net_num == 2 :
    cnn = net.Net2 ()
elif net_num == 3 :
    cnn = net.Net3 ()
elif net_num == 4 :
    cnn = net.Net4 ()
print (cnn)
cnn.to (device)

optimizer = torch.optim.Adam (cnn.parameters (), lr=LR)
loss_func = torch.nn.CrossEntropyLoss ()

# start the train
def traininCUDA () :
    print ("--------------------Start Training--------------------")
    
    for epoch in range (EPOCH) :
        for step, (x, y) in enumerate (train_loader) :
            # print (x.shape)
            x = x.cuda ()
            y = y.cuda ()
            
            out = cnn (x)
            loss = loss_func (out, y)
            
            optimizer.zero_grad ()
            loss.backward ()
            optimizer.step ()
            
            if step % 50 == 0 :
                accu_sum = 0
                total = len (vali_loader)
                for vali_x, vali_y in vali_loader :
                    vali_x = vali_x.cuda ()
                    vali_y = vali_y.cuda ()
                    
                    prediction = cnn (vali_x)
                    prediction = torch.max (prediction, dim=1)[1]
                    # the prediction is a date of 64 batch size, so the first dimension is the batch size
                    # set dim=1 tells the function to get the max value and its index from the 1st dimension
                    # torch.max return a tensor [maxvalue, index], we need the index as the prediction
                    
                    comparison = (prediction == vali_y).sum ().cpu ()
                    accu = comparison / float (vali_loader.batch_size)
                    accu_sum += accu
                accuracy = accu_sum / float (total)
                print (f"Epoch : {epoch} \t Loss : {loss} \t Accuracy : {accuracy}")
    
def traininCPU () :
    print ("--------------------Start Training--------------------")
    
    for epoch in range (EPOCH) :
        for step, (x, y) in enumerate (train_loader) :
            out = cnn (x)
            loss = loss_func (out, y)
            
            optimizer.zero_grad ()
            loss.backward ()
            optimizer.step ()
            
            if step % 50 == 0 :
                accu_sum = 0
                total = len (vali_loader)
                for vali_x, vali_y in vali_loader :
                    prediction = cnn (vali_x)
                    prediction = torch.max (prediction, dim=1)[1]
                    # the prediction is a date of 64 batch size, so the first dimension is the batch size
                    # set dim=1 tells the function to get the max value and its index from the 1st dimension
                    # torch.max return a tensor [maxvalue, index], we need the index as the prediction
                    
                    comparison = (prediction == vali_y).sum ()[0]
                    accu = comparison / float (vali_loader.batch_size)
                    accu_sum += accu
                accuracy = accu_sum / float (total)
                print (f"Epoch : {epoch} \t Loss : {loss} \t Accuracy : {accuracy}")

if not choice :
    traininCUDA ()
else :
    traininCPU ()

save_path = f"model/net{net_num}"
if not os.path.exists (save_path) :
    os.mkdir (save_path)
to_which = f"{save_path}/epoch{EPOCH}"
if not os.path.exists (to_which) :
    os.mkdir (to_which)
torch.save (cnn, f"{to_which}/net{net_num}_{EPOCH}.pt")
torch.save (cnn.state_dict (), f"{to_which}/net{net_num}_para_{EPOCH}.pt")