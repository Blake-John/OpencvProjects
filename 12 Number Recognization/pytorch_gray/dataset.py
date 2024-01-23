from PIL import Image
import os
from torch.utils.data import Dataset
import torchvision.transforms as trans

default_trans = trans.Compose ([trans.ToTensor ()])

class Mydataset (Dataset) :
    def __init__ (self, root_dir, transform=default_trans) :
        self.root_dir = root_dir
        self.trans = transform
        self.path = os.listdir (root_dir) # ["0", "1", "2", ...]
        self.file = [os.listdir (f"{root_dir}/{self.path[i]}") for i in range (len (self.path))]
        self.tar_labs = self.make_label ()
        
    def make_label (self) :
        tar_labs = []
        for i in self.path :
            label = int (i)
            for j in self.file[label] :
                tar_lab = [f"{self.root_dir}/{i}/{j}", label]
                tar_labs.append (tar_lab)
        
        return tar_labs
        
    def __len__ (self) :
        l = 0
        for files in self.path :
            file = os.listdir (f"{self.root_dir}/{files}")
            l += len (file)
        
        return l

    def __getitem__(self, index) :
        img = Image.open (self.tar_labs[index][0])
        img = img.convert ("L")
        label = self.tar_labs[index][1]
        
        img = self.trans (img)            
        
        return img, label
    
# data = Mydataset (root_dir="splited_data/train")