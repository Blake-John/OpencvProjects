import os
import torch
import torch.utils.data as data
import torchvision.transforms as trans
import dataset
import net


path = "splited_data_gray/"
EPOCH = 20
BATCH_SIZE = 64
LR = 0.001
RESIZE = (80, 80)
DEGREE = 10
CROP_SIZE = 60
TRAIN_RATIO = 0.8
if torch.cuda.is_available () :
    choice = 0
else :
    choice = 1
devices = ["cuda", "cpu"]
device = devices[choice]
print (device)

transform = trans.Compose (
    [
        trans.Resize (RESIZE),
        trans.RandomHorizontalFlip (0.5),
        trans.RandomRotation (DEGREE),
        trans.CenterCrop (CROP_SIZE),
        trans.ToTensor (),
        trans.Normalize (
            mean=[0.5,],
            std=[0.225,]
        )
        
    ]
)

train_set = dataset.Mydataset (root_dir="splited_data/train", transform=transform)

train_len = int (len (train_set) * TRAIN_RATIO)
val_len = int (len (train_set) - train_len)

train_set, val_set = data.random_split (train_set, [train_len, val_len])

train_loader = data.DataLoader (
    dataset=train_set,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = data.DataLoader (
    dataset=val_set,
    batch_size=BATCH_SIZE,
    shuffle=True
)

cnn = net.Net4 ()
cnn.to (device)
print (cnn)

optimizer = torch.optim.Adam (cnn.parameters (), lr=LR)
loss_func = torch.nn.CrossEntropyLoss ()

def trainCUDA () :
    for epoch in range (EPOCH) :
        for step, (x, y) in enumerate (train_loader) :
            x = x.cuda ()
            y = y.cuda ()
            
            out = cnn (x)
            loss = loss_func (out, y)
            
            optimizer.zero_grad ()
            loss.backward ()
            optimizer.step ()
            
            if step % 20 == 0 :
                accu_sum = 0
                total = len (val_loader)
                for val_x, val_y in val_loader :
                    val_x = val_x.cuda ()
                    val_y = val_y.cuda ()
                    
                    pre = cnn (val_x)
                    pre = torch.max (pre, 1)[1]
                    compare = (pre == val_y).sum ()
                    accu_sum += compare / float (val_loader.batch_size)
                accuracy = accu_sum / float (total)
                print (f"Epoch : {epoch} \t Train Loss : {loss} \t Accuracy : {accuracy}")


def trainCPU () :
    for epoch in range (EPOCH) :
        for step, (x, y) in enumerate (train_loader) :
            out = cnn (x)
            loss = loss_func (out, y)
            
            optimizer.zero_grad ()
            loss.backward ()
            optimizer.step ()
            
            if step % 20 == 0 :
                accu_sum = 0
                total = len (val_loader)
                for val_x, val_y in val_loader :
                    
                    pre = cnn (val_x)
                    pre = torch.max (pre, 1)[1]
                    compare = (pre == val_y).sum ()
                    accu = compare / float (val_loader.batch_size)
                    accu_sum += accu
                accuracy = accu_sum / float (total)
                print (f"Epoch : {epoch} \t Train Loss : {loss} \t Accuracy : {accuracy}")


if not choice :
    trainCUDA ()
else :
    trainCPU ()


path = f"model/epoch{EPOCH}"
if not os.path.exists (path=path) :
    os.makedirs (path)

torch.save (cnn, f"{path}/e{EPOCH}.pt")
torch.save (cnn.state_dict (), f"{path}/e{EPOCH}_para.pt")