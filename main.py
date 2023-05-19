from pytube import YouTube
def run():
    video_url = YouTube(str(input("please enter youtube url:")))
    video_name = video_url.title
    #videoToAudioStream = video_url.streams.filter(only_audio=True)
    audioStream = video_url.streams.get_audio_only()
    audioStream.download()
    print(f"Download completed ---> {video_name}")

if __name__=='__main__':
    run()