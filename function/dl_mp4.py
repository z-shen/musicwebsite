import youtube_dl

#ydl_ops = {'outtmpl': '/video/%(title)s.%(ext)s'}
ydl_ops = {}
with youtube_dl.YoutubeDL(ydl_ops) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=nkv4lRSmIj4'])

