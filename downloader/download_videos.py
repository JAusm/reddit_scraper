from urllib.request import urlretrieve
import os
from datetime import datetime

from youtube_dl import YoutubeDL
from youtube_dl.utils import ExtractorError, DownloadError


class DownloadVideos:

    def __init__(self):
        self.project_directory = os.path.dirname(os.path.realpath(__file__))
        self.video_directory = self.mkdir_for_videos()

    def mkdir_for_videos(self):
        """

        Responsible for defining the placement of videos to be downloaded.

        """

        now_date = datetime.now().strftime("%Y%m%d-%H%M%S")

        video_directory = os.path.join(
            self.project_directory,
            now_date +
            "_reddit_videos"
        )

        os.mkdir(video_directory)

        return video_directory

    def downloader(self, video_data: list):

        os.chdir(self.video_directory)

        yt_dl_opts = {
            'format': 'bestvideo+bestaudio',
            'postprocessors': [{
                'key': 'FFmpegMerger',
            }]
        }

        download_errors = 0
        with YoutubeDL(yt_dl_opts) as ydl:
            for video in video_data:
                try:
                    ydl.download([video[0]])
                except (ExtractorError,
                        DownloadError,
                        FileNotFoundError) as error:
                    # I just want to keep track of how many of these I get.
                    # Eventually I'll write some logic to retry if we hit this.
                    if error.args[0] == "ERROR: requested format not available":
                        download_errors += 1
                        continue
                    # This is here because of error with the youtube-dl library.
                    # It merges the two files downloaded into a new file.
                    # It then deletes the two files. Then it tries to merge
                    # the two files that were deleted. Not sure why.
                    elif error.args[0] == "The system cannot find the file specified":
                        continue

        return download_errors
