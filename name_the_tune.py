from pydub import AudioSegment
#from pydub.playback import play
#import simpleaudio as sa
import os
import time
import random

direct = "C:/Users/Balaji's Laptop/Music/Songs"

onlyfiles = os.listdir(direct)

songnum = len(onlyfiles)

songint = random.randint(0, songnum)

songname = onlyfiles[songint]

name, ext = os.path.splitext(songname)

if ext == '.mp3':
	song = AudioSegment.from_mp3(songname)
elif ext == '.wav':
	song = AudioSegment.from_wav(songname)
elif ext == '.m4a':
	song = AudioSegment.from_file(songname, "m4a")

songlength = len(song)

cliprand = random.randint(0,songlength)

if cliprand+2500>songlength:
	clip = song[songlength-5000:]
elif cliprand-2500<0:
	clip = song[:5000]
else:
	clip = song[cliprand-2500:cliprand+2500]

clip1 = list(clip)

#play_obj = sa.play_buffer(clip1, 2, 2, 44100)
#
#play_obj.stop()

clip.export("1.mp3", format="mp3")

time.sleep(15)
print(songname)



    


