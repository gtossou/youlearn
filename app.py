import os
import getpass
from pytubefix import YouTube
import whisper


class YT_Audio_Downloader:
    def __init__(self, url):
        self.url = url

    def download_audio(self):
        try:
            yt_audio = YouTube(self.url).streams.get_audio_only()
            yt_audio.download()
            # TODO: delete the file
        except Exception as e:
            raise e
        return yt_audio.default_filename

    def save_to_db(self):
        pass


class AudioConverter:
    def __init__(self, audiopath):
        self.audiopath = audiopath

    def convert(self):
        model = whisper.load_model("base")
        result = model.transcribe(self.audiopath)
        return result["text"]


if __name__ == "__main__":
    video_url = input("Enter the youtube video url: ")
    video = YT_Audio_Downloader(video_url)
    audio_path = video.download_audio()
    text = AudioConverter(audio_path).convert()
    print(text)
