from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import re

file_path = "/home/sli/PycharmProjects/SpeechDoctor/test_segment/"  #  Speech need segment
finish_path = "/home/sli/PycharmProjects/SpeechDoctor/segment_export/" # Segmented speech output

# Read all the files under the folder
for each in os.listdir("/home/sli/PycharmProjects/SpeechDoctor/test_segment"):
    filename = re.findall(r"(.*?)\.wav", each)
    print(each)
    if each:
       path1 = file_path + each
       wav = AudioSegment.from_file(path1, format="wav")
       size = 10000  # Length of the segmented wave file (10000ms=10s)
       chunks = make_chunks(wav, size)
    #
       for i, chunk in enumerate(chunks):
           chunk_name = "{}-{}.wav".format(each.split(".")[0],i)
           print(chunk_name)
           path2 = finish_path + each
           chunk.export(path2, format="wav")

