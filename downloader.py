import yt_dlp
import questionary
import subprocess
from rich.progress import Progress
from rich.console import Console
import os

console = Console()
progress = Progress(console=console)

# Create a task for progress tracking
task = None


def rich_progress_hook(d):
    """Hook for yt-dlp to update progress bar"""
    global task
    if task is None:
        task = progress.add_task("[cyan]Downloading...", total=0)
    if d['status'] == 'downloading':
        # Update total size once available
        if d.get('total_bytes') and progress.tasks[task].total == 0:
            progress.update(task, total=d['total_bytes'])
        # Update progress
        progress.update(
            task, advance=d['downloaded_bytes'] - progress.tasks[task].completed)
    elif d['status'] == 'finished':
        progress.update(task, completed=progress.tasks[task].total)
        console.print("[green]Download completed![/green]")


def open_directory(directory):
    """Open the given directory in the default file explorer (e.g., Finder on macOS or Explorer on Windows)"""
    if os.name == 'posix':  # macOS or Linux
        subprocess.run(["open", directory])
    elif os.name == 'nt':   # Windows
        subprocess.run(["explorer", directory])


def main():
    link = input("Enter the link of YouTube video you want to download:  ")

    # Set the download directory to ~/ytDownloads/
    download_dir = os.path.expanduser('~/ytDownloads/')
    os.makedirs(download_dir, exist_ok=True)

    try:
        # Prompt for download type: Video or Audio
        download_type = questionary.select(
            "Do you want to download the video or just the audio?",
            choices=['Video', 'Audio'],
        ).ask()

        ydl_opts = {
            'progress_hooks': [rich_progress_hook],
            # Save to the specified directory
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
            'quiet': True
        }

        # Adjust options based on the user's choice
        if download_type == 'Audio':
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            })
        else:
            ydl_opts.update({'format': 'best'})

        with progress:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        # After download, open the directory where the file was saved
        open_directory(download_dir)

    except Exception as e:
        console.print(f"[red]An error occurred: {e}[/red]")


if __name__ == "__main__":
    main()
