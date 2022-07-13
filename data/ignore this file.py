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
import shutil
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
train,val,test = [],[],[]
tr,va,te = 7,2,1
tr = round(nPeople*tr/10)
va = round(nPeople*va/10)
print(tr,va)
for i in range(tr):
    n = random.randint(0,len(people)-1)
    train.append(data[people[n]])
    people.pop(n)
for i in range(va):
    n = random.randint(0,len(people)-1)
    val.append(data[people[n]])
    people.pop(n)
for i in people:
    test.append(data[i])
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
n = 0
for p in train:
    n+=1
    for file in p:
        fromLoc = dataDir+file
        toLoc = dataDir+"train/"+file
        shutil.copyfile(fromLoc, toLoc)
for p in val:
    for file in p:
        fromLoc = dataDir+file
        toLoc = dataDir+"val/"+file
        shutil.copyfile(fromLoc, toLoc)
for p in test:
    for file in p:
        fromLoc = dataDir+file
        toLoc = dataDir+"test/"+file
        shutil.copyfile(fromLoc, toLoc)
print(len(train),len(val),len(test))
