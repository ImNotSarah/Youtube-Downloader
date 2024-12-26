from pytubefix import YouTube
from pytubefix.cli import on_progress
from customtkinter import *


yt_downloader = CTk()
yt_downloader.geometry("600x700")
yt_downloader.title("Youtube Downloader")
yt_downloader.iconbitmap("YouTube.ico")
yt_downloader.resizable(False, False)


welcome = CTkLabel(yt_downloader,
                   text="Welcome to Youtube Downloader",
                   width=100,
                   height=20,
                   anchor=W,
                   font=("Roboto", 24))

welcome.place(relx=0.5, rely=0.1, anchor=CENTER)

link = CTkEntry(yt_downloader,
                width=400,
                height=40,
                placeholder_text="Cole a URL do video aqui...",
                corner_radius=9)

link.place(relx=0.5, rely=0.2, anchor=CENTER)

url = ""

def download_video():
    
    url = link.get()

    yt = YouTube(url, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download()
    
    return print("Prontinho")


btn_ok = CTkButton(yt_downloader,
                   text="    ✔️",
                   font=("Roboto", 16),
                   width=40,
                   height=40,
                   anchor=W,
                   corner_radius=9,
                   fg_color="#ff0033",
                   hover_color="#ff0033",
                   cursor="hand2",
                   background_corner_colors=["#ff0033", "#242424", "#242424", "#ff0033"],
                   command=download_video)

btn_ok.place(relx=0.8, rely=0.2, anchor=CENTER)

yt_downloader.mainloop()

# url = "https://youtu.be/1vs1yCkDskg?si=a4MiAVgVXbzISrdV"


