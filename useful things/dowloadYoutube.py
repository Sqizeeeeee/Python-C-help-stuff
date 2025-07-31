import yt_dlp
import os

downloads_path = os.path.expanduser("~/Downloads")

url = input("Enter YouTube link: ")

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])