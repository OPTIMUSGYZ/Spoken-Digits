# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q8ieC63Q8GcNLaSSzVC4bwJFFo5Qj9KX
"""

import time

import matplotlib.pyplot as plt  # for plotting
import torch
import torch.nn as nn
import torch.optim as optim  # for gradient descent

import CNN_Model
import data_loading


def get_model_name(name, bs, learning_rate, ep):
    """ Generate a name for the model consisting of all the hyperparameter values"""

    path = "model_{0}_bs{1}_lr{2}_epoch{3}".format(name,
                                                   bs,
                                                   learning_rate,
                                                   ep)
    return path


def get_accuracy(model, dataloader, use_cuda, use_metal):
    correct = 0
    total = 0
    for imgs, labels in dataloader:
        #############################################
        # To Enable GPU Usage
        if use_cuda and torch.cuda.is_available():
            torch.cuda.empty_cache()
            imgs = imgs.cuda()
            labels = labels.cuda()
        if use_metal and torch.backends.mps.is_available():
            imgs = imgs.to('mps')
            labels = labels.to('mps')
        #############################################
        output = model(imgs)

        # select index with maximum prediction score
        pred = output.max(1, keepdim=True)[1]
        correct += pred.eq(labels.view_as(pred)).sum().item()
        total += imgs.shape[0]
    return correct / total


# This function also calculates the accuracy for each letter
def get_each_accuracy(model, dataloader):
    Zero_correct = 0
    Zero_total = 0
    One_correct = 0
    One_total = 0
    Two_correct = 0
    Two_total = 0
    Three_correct = 0
    Three_total = 0
    Four_correct = 0
    Four_total = 0
    Five_correct = 0
    Five_total = 0
    Six_correct = 0
    Six_total = 0
    Seven_correct = 0
    Seven_total = 0
    Eight_correct = 0
    Eight_total = 0
    Nine_correct = 0
    Nine_total = 0
    correct = 0
    total = 0

    classes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for imgs, labels in dataloader:

        output = model(imgs)

        # select index with maximum prediction score
        pred = output.max(1, keepdim=True)[1]

        if str(classes[labels[0]]) == '0':
            Zero_correct += pred.eq(labels.view_as(pred)).sum().item()
            Zero_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '1':
            One_correct += pred.eq(labels.view_as(pred)).sum().item()
            One_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '2':
            Two_correct += pred.eq(labels.view_as(pred)).sum().item()
            Two_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '3':
            Three_correct += pred.eq(labels.view_as(pred)).sum().item()
            Three_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '4':
            Four_correct += pred.eq(labels.view_as(pred)).sum().item()
            Four_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '5':
            Five_correct += pred.eq(labels.view_as(pred)).sum().item()
            Five_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '6':
            Six_correct += pred.eq(labels.view_as(pred)).sum().item()
            Six_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '7':
            Seven_correct += pred.eq(labels.view_as(pred)).sum().item()
            Seven_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '8':
            Eight_correct += pred.eq(labels.view_as(pred)).sum().item()
            Eight_total += imgs.shape[0]

        elif str(classes[labels[0]]) == '9':
            Nine_correct += pred.eq(labels.view_as(pred)).sum().item()
            Nine_total += imgs.shape[0]

        correct += pred.eq(labels.view_as(pred)).sum().item()
        total += imgs.shape[0]

    if Zero_total != 0:
        print("Accuracy for 0: ", Zero_correct / Zero_total)
    if One_total != 0:
        print("Accuracy for 1: ", One_correct / One_total)
    if Two_total != 0:
        print("Accuracy for 2: ", Two_correct / Two_total)
    if Three_total != 0:
        print("Accuracy for 3: ", Three_correct / Three_total)
    if Four_total != 0:
        print("Accuracy for 4: ", Four_correct / Four_total)
    if Five_total != 0:
        print("Accuracy for 5: ", Five_correct / Five_total)
    if Six_total != 0:
        print("Accuracy for 6: ", Six_correct / Six_total)
    if Seven_total != 0:
        print("Accuracy for 7: ", Seven_correct / Seven_total)
    if Eight_total != 0:
        print("Accuracy for 8: ", Eight_correct / Eight_total)
    if Nine_total != 0:
        print("Accuracy for 9: ", Nine_correct / Nine_total)
    print("Total Accuracy: ", correct / total)

    return correct / total


def evaluate(net, loader, criterion, use_cuda, use_metal):
    """ Evaluate the network on the validation set.

     Args:
         net: PyTorch neural network object
         loader: PyTorch data loader for the validation set
         criterion: The loss function
     Returns:
         err: A scalar for the avg classification error over the validation set
         loss: A scalar for the average loss function over the validation set
     """
    total_loss = 0.0
    total_epoch = 0
    for i, data in enumerate(loader, 0):
        inputs, labels = data
        if use_cuda and torch.cuda.is_available():
            inputs = inputs.cuda()
            labels = labels.cuda()
        if use_metal and torch.backends.mps.is_available():
            inputs = inputs.to('mps')
            labels = labels.to('mps')
        labels = torch.Tensor(labels)
        labels = normalize_label(labels)  # Convert labels to 0/1
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        total_loss += loss.item()
        total_epoch += len(labels)
    loss = float(total_loss) / (i + 1)
    return loss


def normalize_label(labels):
    """
    Given a tensor containing 2 possible values, normalize this to 0/1

    Args:
        labels: a 1D tensor containing two possible scalar values
    Returns:
        A tensor normalize to 0/1 value
    """
    max_val = torch.max(labels)
    min_val = torch.min(labels)
    norm_labels = (labels - min_val) / (max_val - min_val)
    return norm_labels.long()


def train(model, train_data, val_data, bs=10, learning_rate=0.01, num_epochs=30, use_cuda=False, use_metal=False):
    torch.manual_seed(1)  # set the random seed
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=bs, shuffle=False)
    val_loader = torch.utils.data.DataLoader(val_data, batch_size=bs, shuffle=False)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

    torch.manual_seed(1000)

    iters, losses, train_acc, val_acc, train_loss, val_loss = [], [], [], [], [], []
    epochs = range(num_epochs)

    # training
    n = 0  # the number of iterations
    start_time = time.time()

    for ep in range(num_epochs):
        total_train_loss = 0
        for imgs, labels in iter(train_loader):

            #############################################
            # To Enable GPU Usage
            if use_cuda and torch.cuda.is_available():
                torch.cuda.empty_cache()
                imgs = imgs.cuda()
                labels = labels.cuda()
            if use_metal and torch.backends.mps.is_available():
                imgs = imgs.to('mps')
                labels = labels.to('mps')
            #############################################

            out = model(imgs)  # forward pass

            loss = criterion(out, labels)  # compute the total loss
            loss.backward()  # backward pass (compute parameter updates)
            optimizer.step()  # make the updates for each parameter
            optimizer.zero_grad()  # a cleanup step for PyTorch

            # save the current training information
            iters.append(n)
            losses.append(float(loss) / bs)  # compute *average* loss

            total_train_loss += loss.item()
            n += 1

        # Compute the train and validation losses
        train_loss.append(float(total_train_loss) / n)
        val_loss.append(evaluate(model, val_loader, criterion, use_cuda, use_metal))

        train_acc.append(get_accuracy(model, train_loader, use_cuda, use_metal))  # compute training accuracy
        val_acc.append(get_accuracy(model, val_loader, use_cuda, use_metal))  # compute validation accuracy

        print("Epoch {}: Train acc: {} Validation acc: {}".format(
            ep,
            train_acc[-1],
            val_acc[-1]))

        model_path = "./models/state_dict/" + str(get_model_name(model.name, bs, learning_rate, ep))
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
    plt.savefig("./models/plots/model_{}_{}_{}_Train_Loss.png".format(model.name, bs, learning_rate))
    plt.show()

    # plotting training curve of Loss and epochs
    plt.title("Training Curve")
    plt.plot(epochs, train_loss, label="Train")
    plt.plot(epochs, val_loss, label="Validation")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend(loc='best')
    plt.savefig("./models/plots/model_{}_{}_{}_Train_and_Val_Loss.png".format(model.name, bs, learning_rate))
    plt.show()

    # plotting training curve of training accuracy and iterations
    plt.title("Training Curve")
    plt.plot(epochs, train_acc, label="Train")
    plt.plot(epochs, val_acc, label="Validation")
    plt.xlabel("Epochs")
    plt.ylabel("Training Accuracy")
    plt.legend(loc='best')
    plt.savefig("./models/plots/model_{}_{}_{}_Train_Val_Accuracy.png".format(model.name, bs, learning_rate))
    plt.show()

    print("Final Training Accuracy: {}".format(train_acc[-1]))
    print("Final Validation Accuracy: {}".format(val_acc[-1]))


def start_training(bs, l_r, ep, use_cuda=False, use_metal=False):
    train_data, val_data = data_loading.load_train_val_data()
    CNN = CNN_Model.CNN_Spoken_Digit()
    if use_cuda and torch.cuda.is_available():
        torch.cuda.empty_cache()
        CNN.cuda()
        print("Training on GPU...")
    if use_metal and torch.backends.mps.is_available():
        CNN.to('mps')
        print("Training using Metal")
    train(CNN, train_data, val_data, bs, l_r, ep, use_cuda, use_metal)


def show_model_test_accuracy(bs, l_r, ep):
    model = CNN_Model.CNN_Spoken_Digit()
    model_path = "./models/state_dict/" + str(get_model_name(model.name, bs, l_r, ep))
    state = torch.load(model_path)
    model.load_state_dict(state)
    test_loader = data_loading.load_test_data_loader()
    acc = get_each_accuracy(model, test_loader)
    print("{} with bs={} lr={} epoch={} test accuracy: {}".format(model.name, bs, l_r, ep, acc))
