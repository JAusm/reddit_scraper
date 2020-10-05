from unittest import TestCase
from scraper.scrape_subreddit import ScrapeSubredditInterface, ScrapeSubreddit
from scraper.reddit_auth import PrawAuth


class ScrapeSubredditInterfaceTest(TestCase):

    def setUp(self):
        self.subreddit = "PublicFreakout"

    def test_scrape_subreddit_interface_exists(self):
        actual = ScrapeSubredditInterface(self.subreddit)

        self.assertIsInstance(actual, ScrapeSubredditInterface)

    def test_scrape_subreddit_assigns_list(self):
        actual = ScrapeSubredditInterface(self.subreddit)

        self.assertEqual(
            actual.subreddit,
            "PublicFreakout"
        )


class ScrapeSubredditsTests(TestCase):

    def setUp(self) -> None:
        self.subreddit = "PublicFreakout"

        # When testing, actual credentials need to be supplied.
        self.connection_info = {
            "client_id": "test",
            "client_secret": "test",
            "user_agent": "test"
        }
        self.hot_limit = 6

    def test_ScrapeSubreddit_returns_expected_results(self):
        actual = ScrapeSubreddit(
            self.subreddit,
            self.connection_info,
            self.hot_limit
        )

        self.assertEqual(
            actual.subreddit,
            self.subreddit
        )

        self.assertIsInstance(
            actual.auth_instance,
            PrawAuth
        )

    def test_query_subreddit_returns_data(self):
        """
        Verifies for each post we get a reddit video url in the fallback
        """
        scrape_instance = ScrapeSubreddit(
            self.subreddit,
            self.connection_info,
            self.hot_limit
        )
        posts = scrape_instance.query_subreddit(self.hot_limit)

        for post in posts:
            self.assertEqual(
                post.media['reddit_video']['fallback_url'].startswith("https://v.redd.it/"),
                True
            )

    def test_get_videos_returns_expected_list_length(self):
        """
        Verifies that get_videos returns the expected amount of videos
        given the hot_limit.

        """

        scrape_instance = ScrapeSubreddit(
            self.subreddit,
            self.connection_info,
            self.hot_limit
        )

        videos = scrape_instance.get_videos()

        self.assertEqual(
            len(videos),
            self.hot_limit
        )

        for video in videos:
            self.assertEqual(
                video[0].startswith('https://v.redd.it/'),
                True
            )

    def test_get_videos_exception_reason(self):
        """
        Verify we get the expected exception reason

        """

        bad_connection = {
            "client_id": "bad_id",
            "client_secret": "bad_secret",
            "user_agent": "bad_user"
        }

        scrape_instance = ScrapeSubreddit(
            self.subreddit,
            bad_connection,
            self.hot_limit
        )

        actual = scrape_instance.get_videos()

        self.assertEqual(
            "received 401 HTTP response",
            actual[0]
        )
