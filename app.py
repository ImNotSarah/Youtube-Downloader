from pytubefix import YouTube
from pytubefix.cli import on_progress
from customtkinter import *
from PIL import Image
from io import BytesIO
import requests

yt_downloader = CTk()
yt_downloader.geometry("600x650")
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

def get_video():
    url = link.get()
    yt = YouTube(url, on_progress_callback=on_progress)

    video_title = yt.title
    title = CTkLabel(yt_downloader,
                   text=video_title,
                   anchor=W,
                   font=("Roboto", 16, "bold"))

    title.place(relx=0.18, rely=0.39, anchor=W)

    thumb_url = yt.thumbnail_url
    
    thumb_img = get_video_thumbnail(thumb_url)
    
    thumb_ctk = CTkImage(thumb_img, size=(180, 180))
    
    thumb_label = CTkLabel(yt_downloader, image=thumb_ctk, text="")
    thumb_label.place(relx=0.32, rely=0.56, anchor=CENTER)
    
    return yt

def get_video_thumbnail(url):
    response = requests.get(url)
    response.raise_for_status()
    image = Image.open(BytesIO(response.content))
    return image

def selected_video():
    yt = get_video()
    streams = yt.streams
    options = []

    for stream in streams:

        if stream.type == "video":
            options.append(f"{stream.type} | {stream.resolution}")
        else:
            options.append(f"{stream.type} | {stream.abr}")

    unique_options = list(set(options))
    return unique_options

def selected_option():
    selected_option = variavel.get()
    return selected_option

variavel = StringVar(value="Select an option")

def show_options():

    instruction.place(relx=0.5, rely=0.3, anchor=CENTER)

    unique_options = selected_video()

    option_menu = CTkOptionMenu(yt_downloader,
                               values=unique_options,
                               font=("Roboto", 14),
                               width=150,
                               fg_color="gray20",
                               button_color="#ff0033",
                               button_hover_color="gray30",
                               text_color="white",
                               dropdown_fg_color="gray20",
                               dropdown_hover_color="gray30",
                               variable=variavel,
                               command=lambda _: selected_option())

    option_menu.place(relx=0.73, rely=0.45, anchor=CENTER)
    
    download_button = CTkButton(yt_downloader,
                                text="Download",
                                fg_color="#ff0033",
                                width=300,
                                height=32,
                                hover_color="#c50033",
                                font=("Roboto", 20, "bold"),
                                command=lambda: (download_video(),selected_option()))

    download_button.place(relx=0.5, rely=0.78, anchor=CENTER)

def download_video():
    yt = get_video()
    download_option = variavel.get()
    streams = yt.streams
    audio_or_video = download_option[:5]
    resolution = download_option[8:]

    for stream in streams:
        if audio_or_video == 'video':
            if stream.resolution == resolution:
                itag = str(stream.itag)
        else:
            if stream.abr == resolution:
                itag = str(stream.itag)
    
    video = yt.streams.get_by_itag(itag)
    
    video.download()
    print("Pronto para download")


button_ok = CTkButton(yt_downloader,
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
                   command=lambda: (selected_video(), show_options()))

button_ok.place(relx=0.8, rely=0.2, anchor=CENTER)


instruction = CTkLabel(yt_downloader,
                 text="Select an option and click Download.",
                 width=100,
                 height=20,
                 anchor=W,
                 font=("Roboto", 20))

yt_downloader.mainloop()


