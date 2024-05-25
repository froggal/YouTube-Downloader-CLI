# YouTube-Downloader-CLI by keyfrog@outlook.kr

# Modules import
from yt_dlp import YoutubeDL

# Video Download function
def download_video():
    # Input video's URL and video type
    url = input('Enter the video url: ')
    type = input('Enter the video type(mp4|mp3): ')
    # Setup
    options = {
        "outtmpl": "D:/video/source/%(id)s_%(title)s.%(ext)s",
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": type}],
    }

    # Download
    YoutubeDL(options).download(url)

# Work
download_video()