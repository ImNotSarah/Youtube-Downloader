from pytubefix import *
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=3AxBl2XDXuw"

yt = YouTube(url, on_progress_callback=on_progress)

streams = yt.streams

for stream in streams:
    if stream.type == "video":
        print(f"{stream.type} | {stream.resolution} | {stream.itag}")
    else:
        print(f"{stream.type} | {stream.abr} | {stream.itag}")


option_chosen = input("write the tag number of the resolution you want: ")

donwload = streams.get_by_itag(option_chosen)

donwload.download()