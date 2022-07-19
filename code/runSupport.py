import os

import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import torch
from PIL import Image
from scipy.io.wavfile import write
from torchvision import transforms

import CNN_Model
import trainSupport

t = True
path = os.path.abspath(__file__)
path = path[:-14]
print(path)


def generateMelSpec(filePath, savePath):
    if not os.path.exists(os.path.join(path + savePath)):
        print("Invalid path")
        return None
    # load file
    signal, sampleRate = librosa.load(path + filePath + "out.wav")

    melSpec = librosa.feature.melspectrogram(y=signal, sr=sampleRate,
                                             hop_length=512)  # hop length 512 is better for speech processing
    melSpec = librosa.power_to_db(melSpec, ref=np.max)
    # remove default white padding around the image
    fig, ax = plt.subplots()
    fig.subplots_adjust(0, 0, 1, 1)  # left,bottom,right,top
    ax.axis('off')
    # save mel spectrogram as jpg
    melSpecImg = librosa.display.specshow(melSpec)
    plt.savefig(os.path.join(path + savePath + "out.jpg"))
    plt.close()
    return os.path.join(path + savePath + "out.jpg")


def recordAudio(sampleRate, duration, savePath):
    if not os.path.exists(os.path.join(path + savePath)):
        os.makedirs(os.path.join(path + savePath))
    print("Recording...")
    recording = sd.rec(int(duration * sampleRate), samplerate=sampleRate, channels=1)
    # sd.wait()
    print("Finished")
    return recording


def trimAudio(sampleRate, savePath, recording):
    plt.plot(range(len(recording)), recording)
    plt.savefig(os.path.join(path+'/temp/out1.jpg'))
    plt.close()
    thd = 0.018
    i = 0
    idx1, idx2 = 0, 0
    while i < len(recording):
        if abs(recording[i]) > thd:
            subRec = np.abs(recording[i + 10:int(i + 0.1 * sampleRate)])
            yes = np.average(subRec) > thd
            if yes:
                idx1 = i
                i = len(recording)
        i += 1
    i = len(recording) - 1
    while i > 0:
        if abs(recording[i]) > thd:
            subRec = np.abs(recording[int(i - 0.1 * sampleRate):i - 10])
            yes = np.average(subRec) > thd
            if yes:
                idx2 = i
                i = 0
        i -= 1
    recording = recording[idx1:idx2]
    """if len(recording) < sampleRate:
        return False"""
    plt.plot(range(len(recording)), recording)
    plt.savefig(os.path.join(path + '/temp/out2.jpg'))
    plt.close()
    write(os.path.join(path + savePath + "out.wav"), sampleRate, recording)


def createModel(bs, lr, ep):
    model = CNN_Model.CNN_Spoken_Digit()
    model_path = os.path.join(path + "/models/state_dict/") + str(trainSupport.get_model_name("CNN_Spoken_Digit", bs, lr, ep))
    state = torch.load(model_path)
    model.load_state_dict(state)
    return model


def predict(model, img):
    # resize all images to 224 x 224
    img = Image.open(img)
    transform = transforms.Compose([transforms.Resize((640, 480)),  # Combine different transformations together
                                    transforms.ToTensor()])  # Convert jpeg to tensor
    img = transform(img)
    img = img.unsqueeze(0)

    probList = model(img).squeeze().tolist()
    prediction = probList.index(max(probList))
    return prediction
