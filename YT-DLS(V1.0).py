import os
import subprocess

# Function to display options and get user input
def get_choice(prompt, choices):
    while True:
        print(prompt)
        for key, value in choices.items():
            print(f"{key}. {value}")
        choice = input("Choose an option: ").strip()
        if choice in choices:
            return choice
        print("Invalid choice. Please try again.")

# Function to download using yt-dlp
def download_video(download_type, audio_format, url, output_dir):
    print("\nStarting download...")

    # Build the yt-dlp command
    if download_type == "1":
        # Single Video
        output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
    else:
        # Playlist
        output_template = os.path.join(output_dir, "%(playlist_title)s", "%(playlist_index)s - %(title)s.%(ext)s")

    command = [
        "yt-dlp",
        "--extract-audio",
        f"--audio-format={audio_format}",
        "--add-metadata",
        "--embed-thumbnail",
        "-o", output_template,
        url
    ]

    # Run the command
    try:
        subprocess.run(command, check=True)
        print("\nDownload complete!")
    except subprocess.CalledProcessError:
        print("\nAn error occurred during the download process.")
    except FileNotFoundError:
        print("\nError: yt-dlp is not installed or not in the system PATH.")

# Main script
if __name__ == "__main__":
    print("YouTube Downloader with yt-dlp\n")

    # Step 1: Choose download type
    type_choices = {"1": "Download Single Video", "2": "Download Playlist"}
    download_type = get_choice("Select the type of download:", type_choices)

    # Step 2: Choose audio format
    format_choices = {"1": "FLAC", "2": "MP3"}
    format_choice = get_choice("Select the audio format:", format_choices)
    audio_format = "flac" if format_choice == "1" else "mp3"

    # Step 3: Enter YouTube URL
    url = input("\nEnter the YouTube URL: ").strip()
    if not url:
        print("No URL entered. Exiting...")
        exit(1)

    # Step 4: Set output directory
    output_dir = r"D:\YT-DLP\Audio\Script-dl"  # Change this to your desired output path
    os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

    # Step 5: Start the download
    download_video(download_type, audio_format, url, output_dir)