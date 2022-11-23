from pytube import YouTube
from sys import argv
import getpass

user = getpass.getuser()

# link = argv[1]
link = input('Wklej link youtube do pobrania' + '\n')
yt = YouTube(link)

print('Title: ', yt.title)

print('Views: ', yt.views)

yd = yt.streams.get_audio_only()

# yd.download(f"C:\\Users\\{user}\\Downloads")
yd.download()
