from unittest import TestCase
import os
from datetime import datetime
import shutil

from downloader import DownloadVideos
from scraper.scrape_subreddit import ScrapeSubreddit


class DownloadVideosTests(TestCase):

    def setUp(self) -> None:
        self.project_directory = os.path.dirname(os.path.realpath(__file__))

        self.subreddit = "PublicFreakout"

        # When testing, actual credentials need to be supplied.
        self.connection_info = {
            "client_id": "test",
            "client_secret": "test",
            "user_agent": "test"
        }
        self.hot_limit = 5

        self.dv_instance = DownloadVideos()

    def tearDown(self) -> None:
        os.chdir(self.project_directory)

        for directory in os.listdir():
            if directory.startswith(datetime.now().strftime("%Y%m%d")):
                shutil.rmtree(directory, ignore_errors=True)

    def test_init_sets_the_expected_path(self):
        """

        Verifies that the path set in the constructor is the expected path

        """

        self.assertEqual(
            self.dv_instance.project_directory,
            self.project_directory
        )

    def test_mkdir_for_videos_creates_expected_dir(self):
        """

        Verifies that the expected directory is created

        """

        count = 0
        for directory in os.listdir():
            if directory.startswith(datetime.now().strftime("%Y%m%d")):
                count += 1

        self.assertTrue(count > 0)

    def test_download_videos_downloads_videos(self):
        """

        Verifies that a video was downloaded.

        """

        scraper_instance = ScrapeSubreddit(
            self.subreddit,
            self.connection_info,
            self.hot_limit
        )
        video_data = scraper_instance.get_videos()

        downloaded = self.dv_instance.downloader(video_data)

        count = 0
        for file in os.listdir():
            if file.endswith(".mp4"):
                count += 1

        self.assertEqual(
            count,
            len(video_data) - downloaded
        )
