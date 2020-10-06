from urllib.request import urlretrieve
import os
from datetime import datetime


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

    def download_videos(self, video_data: list):
        """

        Responsible for downloading videos from urls scraped from Reddit.

        """

        os.chdir(self.video_directory)

        for video in video_data:
            url = video[0]
            name = video[1]
            urlretrieve(url, name)
