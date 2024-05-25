# YouTube-Downloader-CLI by keyfrog@outlook.kr

# Modules import
from yt_dlp import YoutubeDL

# Video Download function
def download_video(video_url):
    options = {
        "outtmpl": "D:/video/source/%(id)s_%(title)s.%(ext)s",
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
    }
    YoutubeDL(options).download(video_url)

# work
download_video('https://www.youtube.com/watch?v=F2Ib564MBFo')