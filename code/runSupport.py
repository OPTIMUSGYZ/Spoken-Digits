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
import training


def generateMelSpec(filePath, savePath):
    if not os.path.exists(savePath):
        print("Invalid path")
        return None
    # load file
    signal, sampleRate = librosa.load(filePath + "out.wav")

    melSpec = librosa.feature.melspectrogram(y=signal, sr=sampleRate,
                                             hop_length=512)  # hop length 512 is better for speech processing
    melSpec = librosa.power_to_db(melSpec, ref=np.max)
    # remove default white padding around the image
    fig, ax = plt.subplots()
    fig.subplots_adjust(0, 0, 1, 1)  # left,bottom,right,top
    ax.axis('off')
    # save mel spectrogram as jpg
    melSpecImg = librosa.display.specshow(melSpec)
    plt.savefig(savePath + "out.jpg")
    plt.close()
    return savePath + "out.jpg"


def recordAudio(sampleRate, duration, savePath):
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    print("Recording...")
    recording = sd.rec(int(duration * sampleRate), samplerate=sampleRate, channels=1)
    sd.wait()
    write(savePath + "out.wav", sampleRate, recording)
    print("Finished")


def createModel(bs, lr, ep):
    model = CNN_Model.CNN_Spoken_Digit()
    model_path = "./models/state_dict/" + str(training.get_model_name("CNN_Spoken_Digit", bs, lr, ep))
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
    print(probList)
    prediction = probList.index(max(probList))
    return prediction
