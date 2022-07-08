#This file loads and splits data into training, validation, and testing sets

import numpy as np
import time
import torch
import math
import os
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import datasets, models, transforms
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
from torch import optim

def load_data():
    # define training and test data directories
    data_dir = '../data/mel_spectrogram/'
    #print("Current working directory: {0}".format(os.path.isdir(data_dir)))

    #Data are separated into  around 10% test, 10% validation, and 80% training
    train_dir = os.path.join(data_dir, 'train/') #train directory
    val_dir = os.path.join(data_dir, 'val/') #validation directory
    test_dir = os.path.join(data_dir, 'test/') #test directory

    # classes are folders in each directory with these names
    classes = ['0', '1', '2', '3', '4','5','6','7','8','9']

    # resize all images to 224 x 224
    data_transform = transforms.Compose([transforms.Resize((640,480)),  #Combine different transformations together
                                          transforms.ToTensor()])             #Convert jpeg to tensor

    #Define directory and transform for each dataset
    train_data = datasets.ImageFolder(train_dir, data_transform)
    val_data = datasets.ImageFolder(val_dir, data_transform)
    test_data = datasets.ImageFolder(test_dir, data_transform)

    # print out some data stats
    print('Number of training images: ', len(train_data))
    print('Number of validation images: ', len(val_data))
    print('Number of test images: ', len(test_data))

    # define dataloader parameters
    batch_size  = 32
    num_workers = 0

    # prepare data loaders with iterable
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size,
                                               num_workers=num_workers, shuffle=True)
    val_loader = torch.utils.data.DataLoader(val_data, batch_size=batch_size,
                                              num_workers=num_workers, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size,
                                              num_workers=num_workers, shuffle=True)
