# Import necessary modules
import tkinter as tk
from pytube import YouTube


# Define the function to download a YouTube video
def download_video():
    # Get the URL of the video from the user
    url = url_entry.get()

    # Use pytube to get the video from YouTube
    yt = YouTube(url)

    # Get the highest quality video available
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Download the video
    video.download()

    # Show a message to the user to indicate that the download is complete
    status_label.config(text="Download complete!")


# Create the tkinter window and set its title
root = tk.Tk()
root.title("YouTube Downloader")

# Create a label to prompt the user for the URL of the video
url_label = tk.Label(root, text="Enter the URL of the video:")
url_label.pack()

# Create a text entry field for the user to enter the URL
url_entry = tk.Entry(root)
url_entry.pack()

# Create a button to initiate the download
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack()

# Create a label to show the status of the download
status_label = tk.Label(root, text="")
status_label.pack()

# Start the tkinter event loop
root.mainloop()
