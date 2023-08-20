from pytube import YouTube
from sys import argv
from rich.progress import Progress
from rich.console import Console
import questionary

console = Console()
progress = Progress(console=console)

# Create a task outside the callback to avoid creating it multiple times.
task = progress.add_task("[cyan]Downloading...", total=0)  # Initialize with total=0, we'll update it later.


def rich_progress_callback(stream, chunk, bytes_remaining):
    # Update the progress
    progress.update(task, advance=len(chunk))


def main():
    link = input("Enter the link of YouTube video you want to download:  ")
    yt = YouTube(link)

    # prompt user if he wants to download the video or just the audio
    download_type = questionary.select(
        "Do you want to download the video or just the audio?",
        choices=['Video', 'Audio'],
    ).ask()

    if download_type == "Video":
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length, "seconds")

        print("Downloading video...")
        yd = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        file_size = yd.filesize
        progress.update(task, total=file_size)
        yt.register_on_progress_callback(rich_progress_callback)
        with progress:
            yd.download('/Users/Peter/ytDownloads/downloadedVideos')
    else:
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length, "seconds")

        print("Downloading audio...")
        yd = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        file_size = yd.filesize
        progress.update(task, total=file_size)
        yt.register_on_progress_callback(rich_progress_callback)
        with progress:
            yd.download('/Users/Peter/ytDownloads/downloadedAudios')


if __name__ == '__main__':
    main()
