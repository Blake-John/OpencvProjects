import torch
import torchvision
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def check () :
    print (torch.__version__)
    print (torchvision.__version__)
    print (np.__version__)
    print (plt)
    print (pd.__version__)
    device = "cuda" if torch.cuda.is_available else "cpu"
    print (device)

# if __name__ == "__main__" :
check ()