from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)

# To get the length of video
print("Length of video: ", yt.length, "seconds")


yd = yt.streams.get_highest_resolution()
yd.download('/Users/Peter/downloadedVideos')
print("Download completed!!")
