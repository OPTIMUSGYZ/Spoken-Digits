from trainSupport import start_training, show_model_test_accuracy

#################
train_mode = False
use_cuda = True
use_metal = False
#################


batch_size = 256
lr = 0.00049
epoch = 7
if train_mode:
    start_training(batch_size, lr, epoch, use_cuda, use_metal)
show_model_test_accuracy(batch_size, lr, epoch - 1)  # default load to last epoch
