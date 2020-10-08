from urllib.request import urlretrieve
import os
from datetime import datetime

from youtube_dl import YoutubeDL


class DownloadVideos:

    def __init__(self):
        self.project_directory = os.path.dirname(os.path.realpath(__file__))
        self.video_directory = self.mkdir_for_videos()

    def mkdir_for_videos(self):
        """

        Responsible for defining the placement of videos dowloaded

        """

        now_date = datetime.now().strftime("%Y%m%d-%H%M%S")

        new_directory_path = os.path.join(
            self.project_directory,
            now_date +
            "_reddit_videos"
        )

        os.mkdir(new_directory_path)

        return new_directory_path

    def downloader(self, video_data: list):

        os.chdir(self.video_directory)

        yt_dl_opts = {
            'format': 'bestvideo+bestaudio',
            'postprocessors': [{
                'key': 'FFmpegMerger',
            }]
        }

        with YoutubeDL(yt_dl_opts) as ydl:
            for video in video_data:
                try:
                    ydl.download([video[0]])
                # For some reason the youtube-dl tries more than once to merge the video and audio.
                # It throws a FileNotFound error because the audio and video files are deleted
                # after the two are merged into a new file.
                except FileNotFoundError:
                    continue
