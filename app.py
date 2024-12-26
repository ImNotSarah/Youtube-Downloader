from pytubefix import *
from pytubefix.cli import on_progress

url = "https://youtu.be/1vs1yCkDskg?si=a4MiAVgVXbzISrdV"

yt = YouTube(url, on_progress_callback=on_progress)

ys = yt.streams.get_highest_resolution()
ys.download()

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()