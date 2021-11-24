import os
# import librosa
# import audioread
# import numpy as np
from ffmpeg import audio

audio_path = "/home/sli/PycharmProjects/SpeechDoctor/PatientSpeech/"
finish_path = "/home/sli/PycharmProjects/SpeechDoctor/PatientFast/"

def run():
    audio_file = os.listdir(audio_path)
    for i, audio1 in enumerate(audio_file):
        print(audio_path+audio1)
        audio.a_speed(audio_path+audio1, "2", finish_path+"2x_"+audio1)
run()