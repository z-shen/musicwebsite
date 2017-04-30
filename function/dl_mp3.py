import youtube_dl

#ydl_ops = {'outtmpl': '/video/%(title)s.%(ext)s'}
ydl_ops = {'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}
with youtube_dl.YoutubeDL(ydl_ops) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=nkv4lRSmIj4'])

