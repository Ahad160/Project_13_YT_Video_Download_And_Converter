import pytube
from moviepy.editor import VideoFileClip
import os
import shutil
import argparse
import Google_Drive_API
import socket


print("""\033[33m
__   _______   _   _ _     _               ____  _________ _____  ______                    _                 _           
\ \ / /_   _| | | | (_)   | |             / /  \/  || ___ \____ | |  _  \                  | |               | |          
 \ V /  | |   | | | |_  __| | ___  ___   / /| .  . || |_/ /   / / | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  \ /   | |   | | | | |/ _` |/ _ \/ _ \ / / | |\/| ||  __/    \ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | |   | |   \ \_/ / | (_| |  __/ (_) / /  | |  | || |   .___/ / | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/   \_/    \___/|_|\__,_|\___|\___/_/   \_|  |_/\_|   \____/  |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                                                                          
                                                                                                                          
\033[0m""")

print("Example: downloader--> -d -u https://www.youtube.com -cp C:/Users\PRO GADEGT/Videos/Captures")

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description="Download a file from a URL")

# Define the command-line arguments
parser.add_argument("-d", action="store_true", help="Download the file")
parser.add_argument("-c", action="store_true", help="Download the file And Convert It")
parser.add_argument("-u", type=str, help="URL to download from")
parser.add_argument("-cp", type=str, help="Custom Path to save the downloaded file")
parser.add_argument("-dp", action="store_true", help="Default Path to save the downloaded file")
parser.add_argument("-gd", action="store_true", help="Downloaded file And Save to Google Drive")



# Prompt the user for the command line input
user=input("\033[34mDownloader->\033[0m ")

# Split the user input into a list of arguments
user_args = user.split()

# Parse the user-supplied command-line arguments
args = parser.parse_args(user_args)


#Check For Internet Connections
def Internet_Connected():
    try:
        # Attempt to create a socket connection to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if Internet_Connected():
    pass
else:
    print("No Internet")
    exit()


# Check if the -d flag is provided to initiate the download
try:
    if args.d and args.u:
        if args.u:
            url = args.u
            Video_Intance=pytube.YouTube(url)
            steam=Video_Intance.streams.get_highest_resolution()
        
        if args.cp:
            path = args.cp
            
        if args.dp or args : #if user did not define path it will be default path
            path ='E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'

        steam.download(path)
        print(f"\033[32mDownloaded Is Completed \n Save to: {path}\033[0m\n")       
    elif args.u == None and args.d == None:
        print("Error: -d Or -c or -u option is required to initiate the download.")
        exit()
except Exception as Error:
    # print("Wrong URL\n")
    print(Error)
    exit()





try:
    if args.c and args.u:
        if args.u:
            url = args.u

        video_instance = pytube.YouTube(url)
        stream = video_instance.streams.get_highest_resolution()
        downloaded_file = stream.download()

        if args.cp:
            Video_Path = args.cp
            converted_mp3_path = Video_Path

        if args.dp:
            Video_Path ='E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
            converted_mp3_path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'

        if args.gd:
            Video_Path ='E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'
            converted_mp3_path = 'E:\Codeing\Python Language\Projects\Project_13_YT_Video_Download_Convert'



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

        if args.gd:
            Google_Drive_API.Google_Drive_API(output_mp3_file)
            os.remove(output_mp3_file)

        # Delete the downloaded video file
        os.remove(downloaded_video_file)

        print(f"Video converted to MP3 and saved as '{output_mp3_file}'")

    elif args.u == None and args.c == None and args.gd == None :
        print("Error: -c or -u option is required to initiate the download.")
        exit()
    
except Exception as Error:
    print("Wrong URL\n")
    exit()