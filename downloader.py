import pytube
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from rich.progress import Progress
from rich.console import Console
import questionary
import subprocess

console = Console()
progress = Progress(console=console)

# Create a task outside the callback to avoid creating it multiple times.
task = progress.add_task("[cyan]Downloading...", total=0)


def rich_progress_callback(stream, chunk, bytes_remaining):
    progress.update(task, advance=len(chunk))


def open_directory(directory):
    """Open the given directory in the default file explorer (e.g., Finder on macOS)"""
    subprocess.run(["open", directory])


def main():
    link = input("Enter the link of YouTube video you want to download:  ")
    try:
        yt = YouTube(link)
        download_type = questionary.select(
            "Do you want to download the video or just the audio?",
            choices=['Video', 'Audio'],
        ).ask()

        download_path = ''

        if download_type == "Video":
            print("Title: ", yt.title)
            print("Number of views: ", yt.views)
            print("Length of video: ", yt.length, "seconds")
            print("Downloading video...")
            yd = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            download_path = '/Users/Peter/ytDownloads/downloadedVideos'
        else:
            print("Title: ", yt.title)
            print("Number of views: ", yt.views)
            print("Length of video: ", yt.length, "seconds")

            # List all available audio streams
            audio_streams = yt.streams.filter(only_audio=True).all()
            choices = []
            for stream in audio_streams:
                choices.append(f"{stream.abr} - {stream.mime_type}")

            chosen = questionary.select(
                "Choose an audio format to download:",
                choices=choices,
            ).ask()

            # Match the user's choice with the correct stream
            for stream in audio_streams:
                if f"{stream.abr} - {stream.mime_type}" == chosen:
                    yd = stream
                    break
            isItABeat = questionary.confirm(
                "Is this a beat?"
            ).ask()
            if isItABeat:
                download_path = '/Users/Peter/Documents/raps/rippedBeats'
            else:
                download_path = '/Users/Peter/ytDownloads/downloadedAudios'

        file_size = yd.filesize
        progress.update(task, total=file_size)
        yt.register_on_progress_callback(rich_progress_callback)
        with progress:
            yd.download(download_path)

        console.print(f"[green]Download completed![/green]")

        # Ask the user if they'd like to open the folder containing the download.
        open_folder = questionary.confirm(
            "Would you like to open the folder containing the download?"
        ).ask()

        if open_folder:
            open_directory(download_path)

    except pytube.exceptions.VideoUnavailable:
        print(f"The video with the link {link} is unavailable.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
