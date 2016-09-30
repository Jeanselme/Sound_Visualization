"""
	Sound visualization
	by Vincent Jeanselme
	vincent.jeanselme@gmail.com
"""

import sys
import numpy as np
import scipy.misc
from scipy.fftpack import fft
from scipy.io import wavfile as wv


def frequencyAnalysis(sample):
    """
    Computes the transformation of the sound sample in frequency
    using FFT
    """
    return fft(sample)

def associatedColor(number, zeroColor = [0,0,255], oneColor = [255,0,0]):
    """
    Computes the gradient color between zeroColor and oneColor.
    If number is one you observe oneColor
    And if it is zero, you observe zeroColor
    """
    return [zeroColor[i] + number * (oneColor[i] - zeroColor[i]) for i in range(3)]

def colorRegion(img, color, ibeg, iend, jbeg, jend):
    """
    Colors the rectangle defined by ibeg, iend, jbeg, jend of the given image
    """
    for i in range(ibeg,iend):
        for j in range(jbeg,jend):
            img[i][j] = color

def visualSound(sounds, frequencyNumber, sampleNumber, dimension, output):
    """
    Displays a visualisation of the sound
    """

    height = frequencyNumber*dimension
    width = sampleNumber*dimension
    res = np.zeros((height, width, 3))

    for sample in range(len(sounds)):
        fft = frequencyAnalysis(sounds[sample])
        size = len(fft)//(frequencyNumber)
        fftSum = []
        # Gather frequencies
        for freq in range(frequencyNumber) :
            begin = freq * size
            end = begin + size
            fftSum.append(np.linalg.norm(sum(fft[begin:end]))/size)
        maxfft = max(fftSum)
        minfft = min(fftSum)

        # Complete the image
        for freq in range(frequencyNumber) :
            ibeg = freq*dimension
            iend = (freq+1)*dimension
            jbeg = sample*dimension
            jend = (sample+1)*dimension
            colorRegion(res, associatedColor((fftSum[freq]-minfft)/(maxfft-minfft)),
             ibeg, iend, jbeg, jend)

    scipy.misc.imshow(res)
    if (output != ""):
        try:
            scipy.misc.imsave(output, res)
        except:
            print("Output format not supported")

def soundTransform(fileName, frequencyNumber, sampleNumber, dimension, output):
    fs, sound = wv.read(fileName)
    # Change to mono sound
    try:
        newSound = []
        for i in range(len(sound)):
            mean = (sound[i][0] + sound[i][1])/2
            newSound.append(mean)
        print("Stereo sound")
        sound = np.array(newSound, dtype='int16')
    except:
        print("Mono sound")

    # Samples the extract
    sounds = []
    sampleLength = len(sound)//sampleNumber
    for sample in range(sampleNumber):
        sounds.append(sound[sample*sampleLength:(sample+1)*sampleLength])

    visualSound(sounds, frequencyNumber, sampleNumber, dimension, output)

def help():
    print("sound_visualisation FileName.wav [-f frequencyNumber > 0] [-s sampleNumber > 0] [-d heightOfResultInPixels > 0] [-o resultFileName]")
    quit()

def main():
    arg = sys.argv
    if len(arg) < 2:
        help()
    elif ".wav" in arg[1]:
        frequencyNumber = 15
        sampleNumber = 15
        dimension = 20
        fileName = arg[1]
        output = ""
        i = 2
        # Parse the command line
        while i+1 < len(arg):
            if arg[i] == "-f":
                frequencyNumber = int(arg[i+1])
                i+=2
            elif arg[i] == "-s":
                sampleNumber = int(arg[i+1])
                i+=2
            elif arg[i] == "-d":
                dimension = int(arg[i+1])
                i+=2
            elif arg[i] == "-o":
                output = arg[i+1]
                i+=2
            else :
                help()

        if (frequencyNumber <= 0 or sampleNumber <= 0 or dimension <= 0):
            help()
        else :
            soundTransform(fileName, frequencyNumber, sampleNumber, dimension, output)

    else:
        help()

if __name__ == '__main__':
    main()
