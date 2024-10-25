# YouTube Video Downloader with Progress Bar

This Python script allows users to download YouTube videos or extract audio in MP3 format. The script uses the `yt-dlp` library for downloading videos and the `rich` library for displaying a progress bar. Users can choose to download either the full video or just the audio in high-quality MP3 format.

## Features

- Download YouTube videos or extract audio.
- Displays a progress bar during the download.
- Automatically opens the download directory after the download completes.

## Prerequisites

Ensure you have the following installed on your machine:

### 1. Python 3.x
You will need Python 3.x installed. You can download the latest version of Python from [python.org](https://www.python.org/).

### 2. Install Required Python Libraries

To run this script, you need to install the following dependencies:

- **yt-dlp**: A YouTube downloader that provides high-quality downloads.
- **questionary**: A library for asking interactive questions.
- **rich**: A library for pretty terminal output including a progress bar.
- **ffmpeg**: Required by `yt-dlp` for audio extraction when downloading audio.

You can install the Python dependencies using `pip`:

```bash
pip install yt-dlp questionary rich
```

### 3. Install FFmpeg

FFmpeg is required for converting video to audio (MP3 format). Install it according to your operating system:

- **Windows**: Download and follow the instructions to install FFmpeg from FFmpeg for Windows.
- **macOS**: You can install FFmpeg using Homebrew:

```bash
brew install ffmpeg
```

- **Linux**:  Install FFmpeg via your package manager (e.g., apt for Ubuntu):
```bash
sudo apt install ffmpeg
```

## How to Use
1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the Python script:
```
python ytDownloader.py
```
4. Enter the link of the YouTube video you want to download.
5. Choose whether to download the video or just the audio.
6. The download will start, and a progress bar will be displayed.
7. After the download completes, the file will be saved in the ~/ytDownloads/ (or whatever you name it) directory, and the folder will automatically open.


### License
This project is licensed under the MIT License. 
