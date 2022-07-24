import os

import librosa.display
import matplotlib.pyplot as plt
import noisereduce as nr
import numpy as np
import sounddevice as sd
import torch
from PIL import Image
from scipy.io.wavfile import write, read
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
    signal, sampleRate = librosa.load(path + filePath + "outTrim.wav")

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
    return recording


def trimAudio(savePath):
    sampleRate, recording = read(os.path.join(path + savePath + "orgOut.wav"))
    plt.plot(range(len(recording)), recording)
    plt.savefig(os.path.join(path + savePath + 'orgOut.jpg'))
    plt.close()
    recording = nr.reduce_noise(y=recording, sr=sampleRate)
    plt.plot(range(len(recording)), recording)
    plt.savefig(os.path.join(path + savePath + 'outNR.jpg'))
    plt.close()
    write(os.path.join(path + savePath + "outNR.wav"), sampleRate, recording)
    absRecording = np.abs(recording)
    recAvg = np.mean(absRecording)
    scale = 0.05 / recAvg
    recording *= scale
    absRecording *= scale
    absRecording = np.clip(absRecording, 0.008, np.max(absRecording))
    recAvg = np.mean(absRecording)
    thd1 = np.mean(absRecording[:int(sampleRate * 0.5)])
    thd2 = np.mean(absRecording[len(recording) - int(sampleRate * 0.5):])
    print(recAvg, thd1, thd2)
    if thd1 < recAvg:
        if thd1 < thd2 < recAvg:
            thd = thd2
        else:
            thd = thd1
    else:
        thd = thd2
    thd = (thd + recAvg) / 2
    i = 0
    idx1, idx2 = 0, 0
    while i < len(recording):
        if absRecording[i] > thd:
            subRec = absRecording[i + 10:int(i + 0.2 * sampleRate)]
            yes = np.mean(subRec) > thd
            if yes:
                idx1 = i
                break
        i += 1
    i = len(recording) - 1
    while i > 0:
        if absRecording[i] > thd:
            subRec = absRecording[int(i - 0.2 * sampleRate):i - 10]
            yes = np.mean(subRec) > thd
            if yes:
                idx2 = i
                break
        i -= 1
    print(idx1, idx2)
    recording = recording[idx1:idx2]
    """if len(recording) < sampleRate:
        return False"""

    plt.plot(range(len(recording)), recording)
    plt.savefig(os.path.join(path + savePath + 'outTrim.jpg'))
    plt.close()
    write(os.path.join(path + savePath + "outTrim.wav"), sampleRate, recording)


def createModel(bs, lr, ep):
    model = CNN_Model.CNN_Spoken_Digit()
    model_path = os.path.join(path + "/models/state_dict/") + str(
        trainSupport.get_model_name(model.name, bs, lr, ep))
    state = torch.load(model_path, 'cpu')
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
    for i in range(10):
        print("{}: {}%".format(i, round(probList[i] * 100, 2)))
    maxProb = max(probList)
    prediction = probList.index(maxProb)
    if maxProb < 0.2:
        prediction = -1
    return prediction
