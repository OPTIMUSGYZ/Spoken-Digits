from trainSupport import start_training, show_model_test_accuracy

#################
train_mode = False
use_cuda = False
use_metal = True
#################


batch_size = 100
lr = 0.0002
epoch = 50
if train_mode:
    start_training(batch_size, lr, epoch, use_cuda, use_metal)
show_model_test_accuracy(batch_size, lr, epoch - 1, use_cuda, use_metal)  # default load to last epoch
