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


def download_video():

    url = link.get()
    yt = YouTube(url, on_progress_callback=on_progress)
    
    streams = yt.streams

    options = []
    for stream in streams:

        if stream.type == "video":
            options.append(f"{stream.type} | {stream.resolution}")
        else:
            options.append(f"{stream.type} | {stream.abr}")
    unique_options = list(set(options))
    return unique_options


def show_options():

    instruction.place(relx=0.5, rely=0.3, anchor=CENTER)

    unique_options = download_video()

    optionmenu = CTkOptionMenu(yt_downloader,
                               values=unique_options,
                               font=("Roboto", 16),
                               fg_color="gray20",
                               button_color="#ff0033",
                               button_hover_color="gray30",
                               text_color="white",
                               dropdown_fg_color="gray20",
                               dropdown_hover_color="gray30")

    optionmenu.place(relx=0.73, rely=0.4, anchor=CENTER)


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
                   background_corner_colors=[
                       "#ff0033", "#242424", "#242424", "#ff0033"],
                   command=lambda: (download_video(), show_options()))

btn_ok.place(relx=0.8, rely=0.2, anchor=CENTER)


instruction = CTkLabel(yt_downloader,
                 text="Select an option and click Download.",
                 width=100,
                 height=20,
                 anchor=W,
                 font=("Roboto", 20))


yt_downloader.mainloop()

# https://www.youtube.com/watch?v=3AxBl2XDXuw
