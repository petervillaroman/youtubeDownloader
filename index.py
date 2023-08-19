from pytube import YouTube
from sys import argv
from tqdm import tqdm

class TqdmUpTo(tqdm):
    def update_to(self, stream, chunk, bytes_remaining):
        self.update(len(chunk))  # update the size of the chunk downloaded

def main():
    link = argv[1]
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length, "seconds")

    yd = yt.streams.get_highest_resolution()
    file_size = yd.filesize

    with TqdmUpTo(total=file_size, unit='B', unit_scale=True, desc="Download In Progress", ascii=True) as t:
        yt.register_on_progress_callback(t.update_to)
        yd.download('/Users/Peter/downloadedVideos')

    print("Download completed!!")

if __name__ == '__main__':
    main()
