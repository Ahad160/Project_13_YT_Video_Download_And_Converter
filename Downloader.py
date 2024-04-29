import pytube
from moviepy.editor import VideoFileClip
import os
import shutil

print("""\033[33m
__   _______   _   _ _     _               ____  _________ _____  ______                    _                 _           
\ \ / /_   _| | | | (_)   | |             / /  \/  || ___ \____ | |  _  \                  | |               | |          
 \ V /  | |   | | | |_  __| | ___  ___   / /| .  . || |_/ /   / / | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \ /   | |   | | | | |/ _` |/ _ \/ _ \ / / | |\/| ||  __/    \ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | |   | |   \ \_/ / | (_| |  __/ (_) / /  | |  | || |   .___/ / | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/   \_/    \___/|_|\__,_|\___|\___/_/   \_|  |_/\_|   \____/  |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                                                          
                                                                                                                          
\033[0m""")

user=int(input("1.Download Youtube Video\n2.Convert YT Video To MP3 And Download\nSelect-"))

if user==1:
    url=input("Enter URL:")
    Video_Intance=pytube.YouTube(url)
    steam=Video_Intance.streams.get_highest_resolution()
    path=input("\033[32mDefult/Custom Path To Download [D/C]\033[0m")
    if path=='D':
        download_path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
    elif path=='C':
        path=input("\033[32mEnter Custom Path To Download\033[0m--")     
        download_path = path
    steam.download(output_path=download_path)
    print("\033[31mYT Video Is Downloaded\033[0m\n")

elif user==2:
    url = input("Enter URL:")
    video_instance = pytube.YouTube(url)
    stream = video_instance.streams.get_highest_resolution()
    downloaded_file = stream.download()

    path = input("\033[32mDefault/Custom Path To Download [D/C]\033[0m")

    if path == 'D':
        Video_Path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
        converted_mp3_path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
    elif path == 'C':
        Video_Path = input("\033[32mEnter Custom Path To Download\033[0m--")
        converted_mp3_path = Video_Path

    # Create the full file paths
    downloaded_video_file = os.path.join(Video_Path, os.path.basename(downloaded_file))
    output_mp3_file = os.path.join(converted_mp3_path, 'Converted.mp3')

    # Move the downloaded file to the custom directory
    shutil.move(downloaded_file, downloaded_video_file)

    # Extract the audio from the downloaded video and save it as an MP3 file
    video_clip = VideoFileClip(downloaded_video_file)
    audio_clip = video_clip.audio

    # Save the audio as an MP3 file in the custom directory
    audio_clip.write_audiofile(output_mp3_file)

    # Close the video and audio clips
    video_clip.close()
    audio_clip.close()

    # Delete the downloaded video file
    os.remove(downloaded_video_file)

    print(f"Video converted to MP3 and saved as '{output_mp3_file}'")

