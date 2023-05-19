from pytube import YouTube
from moviepy.editor import *
import os

def run():
    video_url = YouTube(str(input("please enter youtube url:")))
    video_name = video_url.title
    audioStream = video_url.streams.get_audio_only()
    audioStream.download()
    print(f"Download completed")
    convert_to_mp3(video_name)
    to_delete=f"{video_name}.mp4"
    os.remove(to_delete)
    print(f"Convert completed ---> {video_name}.mp3")

def convert_to_mp3(output_file):
    input_file = f"{output_file}.mp4"
    output_file = f"{output_file}.mp3"
    video = AudioFileClip(input_file)
    video.write_audiofile(output_file)

if __name__=='__main__':
    run()
