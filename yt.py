from __future__ import unicode_literals
import pytube, youtube_dl, os

#linkList = input('Link to list:')
linkList = 'https://www.youtube.com/watch?v=oCAnsyde6nM&list=FLy-cDmfx06KQIkO7P8Qy3pQ'

#savePath = input ('Save path: ')
savePath = 'c:\\Users\\CalinNUTU\\Desktop\\yt'
os.chdir(savePath
         )
pl = pytube.Playlist(linkList)

#get the links from the playlist
pl.populate_video_urls()
links = pl.video_urls
print (len(links))
i=1
for link in links:
    print(str(i)+' '+ link)
    i = i+1

print('Download Playlist: ' + str(pl.title))

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


for link in links:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
