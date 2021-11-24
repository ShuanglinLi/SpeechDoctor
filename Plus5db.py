

from pydub import AudioSegment
import os

def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

audio_path = "/home/sli/PycharmProjects/SpeechDoctor/PatientSpeech/"
finish_path = "/home/sli/PycharmProjects/SpeechDoctor/PatientLoud/"

filename = os.listdir(audio_path)

for file in filename:
    # path1 = audio_path +"\\" + file
    # path2 = finish_path + "\\" + file
    path1 = audio_path + file
    path2 = finish_path+ file
    sound = AudioSegment.from_file(path1, format="wav")   # Load .wav file
    db = sound.dBFS  # Get the .wav file db value
    normalized_sound = match_target_amplitude(sound, db + 5) # 5db higher than original
    normalized_sound.export(path2,  format="wav")

audio_path2 = "/home/sli/PycharmProjects/SpeechDoctor/PatientLoud/"
file_names = os.listdir(audio_path2)
print(file_names)

os.chdir(audio_path2)
for name in file_names:
    print(name)
    old_file_name = audio_path2 + '/' + name
    new_file_name = audio_path2 + '/' + 'Plus5db-' + name
    os.rename(old_file_name,new_file_name)