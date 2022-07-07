# For generating mel spectrogram from an audio file
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

##################################


nPeople = 26  # total number of people


##################################

def generate(person, digit):
    for n in range(10):
        # load file
        file = "./audio/{}/{}_{}.wav".format(digit, person, n)
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
        imgPath = "./mel_spectrogram/{}/{}_{}.jpg".format(digit, person, n)
        plt.savefig(imgPath)
        plt.close()


for idxPerson in range(nPeople):
    for d in range(10):
        generate(idxPerson, d)
