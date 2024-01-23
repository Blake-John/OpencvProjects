import torch.nn as nn

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