from pytube import YouTube
import re
import os

def run(yt_url):
    video_url = YouTube(str(yt_url))
    video_name = video_url.title
    # audioStream = video_url.streams.get_audio_only()
    # audioStream.download()
    # print(f"Download completed")
    # convert_to_mp3(video_name)
    # to_delete=f"{video_name}.mp4"
    # os.remove(to_delete)
    # print(f"Convert completed ---> {video_name}.mp3")

# def convert_to_mp3(output_file):
#     input_file = f"{output_file}.mp4"
#     output_file = f"{output_file}.mp3"
#     video = AudioFileClip(input_file)
#     video.write_audiofile(output_file)

def convert_streams_to_dicts(streams):
        # Define the pattern to extract key-value pairs
    pattern = r'(\w+)="([^"]+)"'
    
    # Initialize an empty list to hold dictionaries
    list_of_dicts = []
    
    for stream in streams:
        # Remove the '<Stream:' prefix and '>' suffix if present
        clean_stream = stream.replace('<Stream:', '').replace('>', '').strip()
        
        # Find all matches and convert to dictionary
        matches = dict(re.findall(pattern, clean_stream))
        
        # Add the dictionary to the list
        list_of_dicts.append(matches)
    
    return list_of_dicts
def download_stream(yt_url):
    index = None
    video_url = YouTube(str(yt_url))
    streams = convert_streams_to_dicts(video_url.streams.filter(progressive=True))
    print(streams)
    print(type(streams))
#def get_url_from_discord
#def push_files_to_external_storage
#def clean_files_in_external_storage
yt_url='https://www.youtube.com/watch?v=6YZvp2GwT0A&ab_channel=DevOpsJourney'
run(yt_url)
#https://www.youtube.com/watch?v=6YZvp2GwT0A&ab_channel=DevOpsJourney