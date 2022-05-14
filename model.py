import torch
import torch.nn as nn
import torch.nn.functional as F


def image2emb_navie(image, patch_size, weight):
    # image size: b * c * h * w
    patches = F.unfold(image, kernel_size=patch_size, stride=patch_size)
    
def image2emb_conv():
    pass
