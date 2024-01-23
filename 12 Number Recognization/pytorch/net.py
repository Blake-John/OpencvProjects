import torch
import torch.nn as nn

class Net (nn.Module) :
    def __init__(self) -> None:
        super(Net, self).__init__()
        self.conv1 = nn.Sequential (
            nn.Conv2d (
                in_channels=3,
                out_channels=12,
                kernel_size=5,
                stride=1,
                padding=2
            ), # (12, 60, 60)
            nn.ReLU (),
            nn.MaxPool2d (2), # (12, 30, 30)
            nn.Dropout (0.5)
        )
        self.conv2 = nn.Sequential (
            nn.Conv2d (
                in_channels=12,
                out_channels=32,
                kernel_size=5,
                stride=1,
                padding=2
            ), # (32, 30, 30)
            nn.ReLU (),
            nn.Conv2d (
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=1
            ), # (64, 30, 30)
            nn.ReLU (),
            nn.MaxPool2d (2) # (64, 15, 15)
        )
        self.out = nn.Sequential (
            nn.Linear (64 * 15 * 15, 64 * 15),
            nn.ReLU (),
            nn.Linear (64 * 15, 32 * 15),
            nn.ReLU (),
            nn.Linear (32 * 15, 256),
            nn.ReLU (),
            nn.Linear (256, 10)
        )
        
        
        

    def forward (self, x) :
        x = self.conv1 (x)
        x = self.conv2 (x)
        x = x.view (x.size (0), -1)
        x = self.out (x)
        
        return x
    
class Net2 (nn.Module) :
    def __init__ (self) :
        super (Net2, self).__init__ ()
        self.conv1 = nn.Sequential (
            nn.Conv2d (3, 6, 5, 3, 1), # (6, 20, 20)
            nn.ReLU (),
            nn.MaxPool2d (2), # (6, 10, 10)
            nn.Dropout (0.5)
        )
        self.conv2 = nn.Sequential (
            nn.Conv2d (6, 9, 3, 1, 1), # (9, 10, 10)
            nn.ReLU (),
            nn.MaxPool2d (2) # (9, 5, 5)
        )
        self.out = nn.Sequential (
            nn.Linear (9 * 5 * 5, 9 * 15),
            nn.ReLU (),
            nn.Linear (9 * 15, 64),
            nn.ReLU (),
            nn.Linear (64, 10)
        )
    
    def forward (self, x) :
        x = self.conv1 (x)
        x = self.conv2 (x)
        x = x.view (x.size (0), -1)
        x = self.out (x)
        
        return x
    
    
class Net3 (nn.Module) :
    def __init__(self) -> None:
        super(Net3, self).__init__()
        self.conv1 = nn.Sequential (
            nn.Conv2d (3, 12, 3, 1, 1), # (12, 60, 60)
            nn.ReLU (),
            nn.Conv2d (12, 24, 5, 1, 2), # (24, 60, 60)
            nn.ReLU (),
            nn.MaxPool2d (2), # (24, 30, 30)
            nn.Dropout2d (0.5)
        )
        self.conv2 = nn.Sequential (
            nn.Conv2d (24, 48, 3, 1, 1), # (36, 30, 30)
            nn.ReLU (),
            nn.Conv2d (48, 96, 5, 1, 2), # (96, 30, 30)
            nn.ReLU (),
            nn.MaxPool2d (2),
            nn.Dropout2d (0.2) # (96, 15, 15)
            
        )
        self.out = nn.Sequential (
            nn.Linear (96 * 15 * 15, 96 * 15 * 5),
            nn.ReLU (),
            nn.Linear (96 * 15 * 5, 96 * 5 * 5),
            nn.ReLU (),
            nn.Dropout (0.5),
            nn.Linear (96 * 5 * 5, 96 * 5),
            nn.ReLU (),
            nn.Linear (96 * 5 , 256),
            nn.ReLU (),
            nn.Dropout (0.5),
            nn.Linear (256, 128),
            nn.ReLU (),
            nn.Linear (128, 64),
            nn.ReLU (),
            nn.Dropout (0.2),
            nn.Linear (64, 32),
            nn.ReLU (),
            nn.Linear (32, 10)
        )
    
    def forward (self, x) :
        x = self.conv1 (x)
        x = self.conv2 (x)
        x = x.view (x.size (0), -1)
        x = self.out (x)
        
        return x
    
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