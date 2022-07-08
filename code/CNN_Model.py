# This file contains a CNN model
import math

import torch.nn as nn
import torch.nn.functional as F


# Convolutional Neural Network Architecture
class CNN_Spoken_Digit(nn.Module):
    def __init__(self, kernels=None, channels=None, ker_pool=2, stride=2):
        super(CNN_Spoken_Digit, self).__init__()

        if channels is None:
            channels = [3, 5, 10, 20]
        if kernels is None:
            kernels = [7, 5, 3]

        # define convolutional layers and batch normalization layers
        self.conv1 = nn.Conv2d(channels[0], channels[1],
                               kernels[0])  # in_channels (coloured images), out_chanels, kernel_size
        self.batchNorm1 = nn.BatchNorm2d(channels[1])
        self.conv2 = nn.Conv2d(channels[1], channels[2], kernels[1])  # in_channels, out_chanels, kernel_size
        self.batchNorm2 = nn.BatchNorm2d(channels[2])
        self.conv3 = nn.Conv2d(channels[2], channels[3], kernels[2])  # in_channels, out_chanels, kernel_size
        self.batchNorm3 = nn.BatchNorm2d(channels[3])

        self.pool = nn.MaxPool2d(ker_pool, stride)  # kernel_size, stride

        # compute the input features
        self.conv1_channel_x = math.floor(640 - kernels[0] + 1)
        self.pool1_channel_x = math.floor((self.conv1_channel_x - ker_pool) / stride + 1)
        self.conv2_channel_x = math.floor(self.pool1_channel_x - kernels[1] + 1)
        self.pool2_channel_x = math.floor((self.conv2_channel_x - ker_pool) / stride + 1)
        self.conv3_channel_x = math.floor(self.pool2_channel_x - kernels[2] + 1)
        self.pool3_channel_x = math.floor((self.conv3_channel_x - ker_pool) / stride + 1)

        # compute the input features
        self.conv1_channel_y = math.floor(480 - kernels[0] + 1)
        self.pool1_channel_y = math.floor((self.conv1_channel_y - ker_pool) / stride + 1)
        self.conv2_channel_y = math.floor(self.pool1_channel_y - kernels[1] + 1)
        self.pool2_channel_y = math.floor((self.conv2_channel_y - ker_pool) / stride + 1)
        self.conv3_channel_y = math.floor(self.pool2_channel_y - kernels[2] + 1)
        self.pool3_channel_y = math.floor((self.conv3_channel_y - ker_pool) / stride + 1)

        self.in_features = self.pool3_channel_x * self.pool3_channel_y * channels[3]

        # define fully connected layers
        self.fc1 = nn.Linear(self.in_features, 64)
        self.fc2 = nn.Linear(64, 10)  # 10 outputs

        self.name = "CNN_Spoken_Digit"

    def forward(self, x):
        x = self.pool(self.batchNorm1(F.relu(self.conv1(x))))
        x = self.pool(self.batchNorm2(F.relu(self.conv2(x))))
        x = self.pool(self.batchNorm3(F.relu(self.conv3(x))))
        x = x.view(-1, self.in_features)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
