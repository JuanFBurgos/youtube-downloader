import getpass
import os

from pytube import YouTube


username = getpass.getuser()

parent_dir= f"/home/{username}/Videos/"

print("Enter the URL: ")
url= str(input())

print("Where do you want to download the video: ")
download_path= str(input())

youtube = YouTube(url)
youtube_stream= youtube.streams.get_highest_resolution()

try:

   dir = os.path.join(parent_dir, download_path)

   if os.path.isdir(dir):
   
    print("Downloading video...")
    youtube_stream.download(dir)
    print("Download completed!!!")
   else:
    os.mkdir(dir)
    print("Creating folder...")
    print("Downloading video...")
    youtube_stream.download(dir)
    print("Download completed!!!")

except:
    print(f'Video {youtube.title} can\'t be downloaded.')





