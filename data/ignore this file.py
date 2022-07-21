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
# import shutil

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

nPeople = 28
people = list(range(28))
data = []
dataDir = "/Users/gyz/Library/Mobile Documents/com~apple~CloudDocs/U of T/2022 Summer/APS360/Spoken-Digits/data/audio/"

for n in range(nPeople):
    data.append([])
    for i in range(10):
        for j in range(10):
            data[n].append("{}/{}_{}.wav".format(i, n, j))
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
n = 0
for p in train:
    n += 1
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

import librosa
import matplotlib.pyplot as plt
import noisereduce as nr
import os
import numpy as np
from scipy.io.wavfile import read, write

for digit in range(10):
    for person in range(28):
        for idx in range(10):
            signal, sampleRate = librosa.load("./audio/{}/{}_{}.wav".format(digit, person, idx))
            write("./audio/{}/{}_{}.wav".format(digit, person, idx), sampleRate, signal)
            sampleRate, recording = read("./audio/{}/{}_{}.wav".format(digit, person, idx))
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
            thd = (thd+recAvg)/2
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
            """if len(recording) < sampleRate:
                return False"""

            """plt.plot(range(len(recording)), recording)
            plt.savefig("./ga/{}_{}_{}.png".format(digit, person, idx))
            plt.close()"""
            #os.remove("./audio/{}/{}_{}.png".format(digit, person, idx))
            write("./audio/{}/{}_{}.wav".format(digit, person, idx), sampleRate, recording)
            print(digit, person, idx)