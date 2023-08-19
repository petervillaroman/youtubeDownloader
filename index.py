from pytube import YouTube
from sys import argv
from rich.progress import Progress
from rich.console import Console

console = Console()
progress = Progress(console=console)

# Create a task outside of the callback to avoid creating it multiple times.
task = progress.add_task("[cyan]Downloading...", total=0)  # Initialize with total=0, we'll update it later.

def rich_progress_callback(stream, chunk, bytes_remaining):
    # Update the progress
    progress.update(task, advance=len(chunk))

def main():
    link = argv[1]
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Number of views: ", yt.views)
    print("Length of video: ", yt.length, "seconds")

    yd = yt.streams.get_highest_resolution()
    file_size = yd.filesize

    # Update the total filesize of the task now that we have it.
    progress.update(task, total=file_size)

    # Register the callback and start the download.
    yt.register_on_progress_callback(rich_progress_callback)
    with progress:
        yd.download('/Users/Peter/downloadedVideos')

    print("Download completed!!")

if __name__ == '__main__':
    main()
