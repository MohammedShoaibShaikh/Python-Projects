import moviepy.editor as mv

# We Used tkinter to access the Video File
from tkinter.filedialog import *

vid = askopenfilename()
video = mv.VideoFileClip(vid)

aud = video.audio
aud.write_audiofile("test.mp3")

print("Sucessfully Converted !!")