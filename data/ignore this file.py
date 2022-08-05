# ignore this file
"""
import os

people = [12, 26, 28, 36, 43, 47, 52, 56, 57, 58, 59, 60]
n = 0
for p in people:
    for i in range(10):
        for j in range(10):
            file = "./audio/{}/{}_{}_{}.wav".format(i, i, p, j)
            out = "./audio/{}/{}_{}.wav".format(i, n, j)
            os.rename(file, out)
    n += 1
"""
# 9,14,15,18,19,24,25,27,32,35,37,38,41,42

"""
people = [0]
p = 26  # start
for person in people:
    for digit in range(10):
        for idx in range(10):
            file = "/Users/gyz/Downloads/data/{}/{}_{}.wav".format(digit, digit, idx+1)
            output = "/Users/gyz/Library/Mobile Documents/com~apple~CloudDocs/U of T/2022 Summer/APS360/Spoken-Digits/data/audio/{}/{}_{}.wav".format(
                digit, p, idx)
            shutil.copyfile(file, output)
    p += 1
"""
"""
import random
import os

nPeople = 28
people = list(range(28))
data = []
dataDir = os.path.join(os.path.abspath(__file__)[:-19],"mel_spectrogram/")
print(dataDir)

for n in range(nPeople):
    data.append([])
    for i in range(10):
        for j in range(10):
            data[n].append("{}/{}_{}.jpg".format(i, n, j))
train, val, test = [], [], []
tr, va, te = 7, 2, 1
tr = round(nPeople * tr / 10)
va = round(nPeople * va / 10)
print(tr, va)
for i in range(tr):
    n = random.randint(0, len(people) - 1)
    train.append(data[people[n]])
    people.pop(n)
for i in range(va):
    n = random.randint(0, len(people) - 1)
    val.append(data[people[n]])
    people.pop(n)
for i in people:
    test.append(data[i])
print(len(train), len(val), len(test))
"""
"""for d in data:
    ld = len(d)
    for i in range(int(ld*0.7)):
        n = random.randint(0,len(d)-1)
        train.append(d[n])
        d.pop(n)
    for i in range(int(ld*0.15)):
        n = random.randint(0,len(d)-1)
        val.append(d[n])
        d.pop(n)
    for i in d:
        test.append(i)"""
"""
dirs = ['train/','val/','test/']
for d in dirs:
    if os.path.isdir(dataDir+d):
        shutil.rmtree(dataDir+d)
    for i in range(10):
        os.makedirs(dataDir + d + str(i)+'/')
for p in train:
    for file in p:
        fromLoc = dataDir + file
        toLoc = dataDir + "train/" + file
        shutil.copyfile(fromLoc, toLoc)
for p in val:
    for file in p:
        fromLoc = dataDir + file
        toLoc = dataDir + "val/" + file
        shutil.copyfile(fromLoc, toLoc)
for p in test:
    for file in p:
        fromLoc = dataDir + file
        toLoc = dataDir + "test/" + file
        shutil.copyfile(fromLoc, toLoc)
print(len(train), len(val), len(test))
"""
"""
import librosa
import matplotlib.pyplot as plt
import noisereduce as nr
import numpy as np
from scipy.io.wavfile import read, write

for digit in range(10):
    for idx in range(1847):
        signal, sampleRate = librosa.load("./audio/test/{}/f{}.wav".format(digit, idx))
        write("./audio/test/{}/f{}.wav".format(digit, idx), sampleRate, signal)
        sampleRate, recording = read("./audio/test/{}/f{}.wav".format(digit, idx))
        recording = nr.reduce_noise(y=recording, sr=sampleRate)
        absRecording = np.abs(recording)
        recAvg = np.mean(absRecording)
        scale = 0.05 / recAvg
        recording *= scale
        absRecording *= scale
        absRecording = np.clip(absRecording, 0.008, np.max(absRecording))
        recAvg = np.mean(absRecording)
        thd1 = np.mean(absRecording[:int(sampleRate * 0.5)])
        thd2 = np.mean(absRecording[len(recording) - int(sampleRate * 0.5):])
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
            if abs(recording[i]) > thd:
                subRec = absRecording[i + 10:int(i + 0.2 * sampleRate)]
                yes = np.average(subRec) > thd
                if yes:
                    idx1 = i
                    break
            i += 1
        i = len(recording) - 1
        while i > 0:
            if abs(recording[i]) > thd:
                subRec = absRecording[int(i - 0.2 * sampleRate):i - 10]
                yes = np.average(subRec) > thd
                if yes:
                    idx2 = i
                    break
            i -= 1
        recording = recording[idx1:idx2]
        # if len(recording) < sampleRate:
        # return False
        
        #plt.plot(range(len(recording)), recording)
        #plt.savefig("./ga/{}_{}.png".format(digit, idx))
        #plt.close()
        
        # os.remove("./audio/{}/{}_{}.png".format(digit, person, idx))
        write("./audio/test/{}/f{}.wav".format(digit, idx), sampleRate, recording)
        print(digit, idx)
"""
"""
import shutil
pp = ["02","03","04","05","06","07","08","10","11","13","16","17","20","21","22","23","29","30","31","33","34","39","40","44","45","46","48","49","50","51","53","54","55"]
org = "/Users/gyz/Downloads/AudioMNIST-master/data/"
dst = "/Users/gyz/Spoken-Digits/data/audio/test/"
for p in pp:
    for i in range(50):
        for d in range(10):
            shutil.copyfile("{}{}/{}_{}_{}.wav".format(org,p,d,p,i),"{}{}/{}_{}_{}.wav".format(dst,d,d,p,i))
"""

import librosa.display
import matplotlib.pyplot as plt
import numpy as np

for digit in range(10):
    for n in range(1847):
        # load file
        file = "./audio/test/{}/f{}.wav".format(digit, n)
        signal, sampleRate = librosa.load(file)

        melSpec = librosa.feature.melspectrogram(y=signal, sr=sampleRate,
                                                 hop_length=512)  # hop length 512 is better for speech processing
        melSpec = librosa.power_to_db(melSpec, ref=np.max)
        # remove default white padding around the image
        fig, ax = plt.subplots()
        fig.subplots_adjust(0, 0, 1, 1)  # left,bottom,right,top
        ax.axis('off')
        # save mel spectrogram as jpg
        melSpecImg = librosa.display.specshow(melSpec)
        imgPath = "./mel_spectrogram/test/{}/t{}.jpg".format(digit, n)
        plt.savefig(imgPath)
        plt.close()
        print(digit, n)
