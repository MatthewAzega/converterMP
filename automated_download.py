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
        stream = str(stream)
        clean_stream = stream.replace('<Stream:', '').replace('>', '').strip()
        
        # Find all matches and convert to dictionary
        matches = dict(re.findall(pattern, clean_stream))
        
        # Add the dictionary to the list
        list_of_dicts.append(matches)
    
    return list_of_dicts

def download_stream(yt_url):
    identified_streams = {}
    video_url = YouTube(str(yt_url))
    streams = convert_streams_to_dicts(video_url.streams.filter(progressive=True))
    for stream in streams:
        if stream.get('res') == '1080p':
            identified_streams['stream_id_1080'] = stream.get('itag')
        elif stream.get('res') == '720p':
            identified_streams['stream_id_720'] = stream.get('itag')
        else:
            print(f"{stream.get('res')} -- no good quality stream")
    if identified_streams.get('stream_id_1080'):
        video_url.streams.get_by_itag(int(identified_streams.get('stream_id_1080')))
    else:
        try:
            to_download = video_url.streams.get_by_itag(int(identified_streams.get('stream_id_720')))
            to_download.download()
            print('Download successfull')
        except VideoUnavailable:
            print(f'Video with {identified_streams.get("stream_id_720")} itag is unavailable')

#def get_url_from_discord
#def push_files_to_external_storage
#def clean_files_in_external_storage
yt_url='https://www.youtube.com/watch?v=gjoAS66xQF4&ab_channel=ArminvanBuuren'
download_stream(yt_url)