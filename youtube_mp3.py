from pytube import YouTube
import os

video_url = input("Please enter the video URL: ")
yt = YouTube(video_url)

#Get highest bitrate audio stream for given codec (defaults to mp4)
audio = yt.streams.get_audio_only()

audio.download()

file_name = audio.default_filename

if ' ' in file_name:
    os.rename(file_name, file_name.replace(' ', '_'))
    file_name = file_name.replace(' ','_')

file_without_ext = os.path.splitext(file_name)[0]

command = f"ffmpeg -i {file_name} {file_without_ext}.mp3"

os.system(command)

os.remove(file_name)



