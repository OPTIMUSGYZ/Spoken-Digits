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

