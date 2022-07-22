from trainSupport import start_training, show_model_test_accuracy

#################
train_mode = True
use_cuda = False
use_metal = False
#################


batch_size = 400
lr = 0.0005
epoch = 15
if train_mode:
    start_training(batch_size, lr, epoch, use_cuda, use_metal)
show_model_test_accuracy(batch_size, lr, epoch - 1)  # default load to last epoch
