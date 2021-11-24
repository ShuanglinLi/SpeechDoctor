import speech_recognition as sr
import os
import numpy as np
import sys
import wave
import contextlib
from glob import glob

# Convert the wav file into txt file
file_path = "/home/sli/PycharmProjects/SpeechDoctor/test_speech"
filename = os.listdir(file_path)
part= []

for file in filename:
    print(file)
    # initialize the recognizer
    r = sr.Recognizer()
    # Load the wave file and use Google Speech Recognition transfer the wav into text
    with sr.AudioFile(file) as source:
         audio = r.record(source)
    try:
         s = r.recognize_google(audio)
         part.append(s)
         print(""+s)
    except Exception as e:
         print("Exception: "+str(e))

with open('recognition.txt', 'w') as f:
    for item in part:
        f.write("%s\n" % item)

# # Calculate how many words in a txt file
# def count_words(filename):
#
#     try:
#         with open(filename) as file:
#             contents = file.read()
#     except FileNotFoundError:
#         msg = 'Sorry, the file' + filename + 'does not exist'
#         print(msg)
#     else:
#         words = contents.split()
#         n_words = len(words)
#         print("Total number of words = ", n_words)
#
# txtfiles = ['recognition.txt']
# for filename in txtfiles:
#     count_words(filename)

# Calculate the total time of the uttterances
def find_files(directory, pattern='**/*.wav'):
    '''
    Rcursively finds all files matching the pattern
    :param directory:
    :param pattern:
    :return:
    '''
    return glob(os.path.join(directory, pattern), recursive=True)

wav_path = "/home/sli/PycharmProjects/SpeechDoctor/test_speech"
file_wav = find_files(wav_path)
total_time = 0

for file in file_wav:
    with contextlib.closing(wave.open(file, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        total_time = total_time + duration
        # print("duration = ", duration)
        # print("total_time = ", total_time)
        # print("Total number of wav files = ", len(file_wav))

# # Calculate how many words per minutes

# Calculate how many words in a txt file
def count_words(filename):

    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        msg = 'Sorry, the file' + filename + 'does not exist'
        print(msg)
    else:
        words = contents.split()
        n_words = len(words)
        total_min = total_time / 60
        wpm = n_words /total_min
        print("Total number of words = ", n_words)
        print("Words per minutes = ", wpm)

txtfiles = ['recognition.txt']
for filename in txtfiles:
    count_words(filename)


