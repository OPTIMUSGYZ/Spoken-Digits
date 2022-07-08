# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8ieC63Q8GcNLaSSzVC4bwJFFo5Qj9KX
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt  # for plotting
import torch.optim as optim  # for gradient descent
import time
import CNN_Model
import data_loading

torch.manual_seed(1)  # set the random seed
use_cuda = True


def get_model_name(name, batch_size, learning_rate, epoch):
    """ Generate a name for the model consisting of all the hyperparameter values"""

    path = "model_{0}_bs{1}_lr{2}_epoch{3}".format(name,
                                                   batch_size,
                                                   learning_rate,
                                                   epoch)
    return path


def get_accuracy(model, dataloader):
    correct = 0
    total = 0
    for imgs, labels in dataloader:
        output = model(imgs)

        # select index with maximum prediction score
        pred = output.max(1, keepdim=True)[1]
        correct += pred.eq(labels.view_as(pred)).sum().item()
        total += imgs.shape[0]
    return correct / total


def train(model, trainData, valData, batch_size=10, learning_rate=0.01, num_epochs=30):
    train_loader = torch.utils.data.DataLoader(trainData, batch_size=batch_size)
    val_loader = torch.utils.data.DataLoader(valData, batch_size=batch_size)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

    torch.manual_seed(1000)

    iters, losses, train_acc, val_acc = [], [], [], []

    # training
    n = 0  # the number of iterations
    start_time = time.time()

    for epoch in range(num_epochs):
        for imgs, labels in iter(train_loader):

            #############################################
            # To Enable GPU Usage
            if use_cuda and torch.cuda.is_available():
                imgs = imgs.cuda()
                labels = labels.cuda()
            #############################################

            out = model(imgs)  # forward pass

            loss = criterion(out, labels)  # compute the total loss
            loss.backward()  # backward pass (compute parameter updates)
            optimizer.step()  # make the updates for each parameter
            optimizer.zero_grad()  # a clean up step for PyTorch

            # save the current training information
            iters.append(n)
            losses.append(float(loss) / batch_size)  # compute *average* loss
            n += 1

        train_acc.append(get_accuracy(model, train_loader))  # compute training accuracy
        val_acc.append(get_accuracy(model, val_loader))  # compute validation accuracy

        print(("Epoch {}: Train acc: {} Validation acc: {}").format(
            epoch + 1,
            train_acc[-1],
            val_acc[-1]))

        model_path = get_model_name(model.name, batch_size, learning_rate, epoch)
        torch.save(model.state_dict(), model_path)

    print('Finished Training')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Total time elapsed: {:.2f} seconds".format(elapsed_time))

    # plotting training curve of Loss and iterations
    plt.title("Training Curve")
    plt.plot(iters, losses, label="Train")
    plt.xlabel("Iterations")
    plt.ylabel("Loss")
    plt.show()

    # plotting training curve of training accuracy and iterations
    plt.title("Training Curve")
    plt.plot(num_epochs, train_acc, label="Train")
    plt.plot(num_epochs, val_acc, label="Validation")
    plt.xlabel("Epochs")
    plt.ylabel("Training Accuracy")
    plt.legend(loc='best')
    plt.show()

    print("Final Training Accuracy: {}".format(train_acc[-1]))
    print("Final Validation Accuracy: {}".format(val_acc[-1]))

train_data,val_data = data_loading.load_data()
CNN = CNN_Model.CNN_Spoken_Digit()
train(CNN, train_data, val_data, 10, 0.01, 2)
