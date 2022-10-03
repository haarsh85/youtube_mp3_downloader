from pytube import YouTube
import ffmpeg
import os

video_url = "https://www.youtube.com/watch?v=8oMPO_3DKNM"
yt = YouTube(video_url)

video_title = yt.title

#Get highest bitrate audio stream for given codec (defaults to mp4)
audio = yt.streams.get_audio_only()

""" if ' ' in audio.default_filename:
    audio = audio.default_filename.replace(' ', '_')
    print(audio) """

audio.download()

file_name = os.path.basename(audio.default_filename)

if ' ' in file_name:
    os.rename(file_name, file_name.replace(' ', '_'))


file_without_ext = os.path.splitext(file_name)[0]


command = f"ffmpeg -i {file_name} {file_without_ext}.mp3"

print(command)

os.system(command)



