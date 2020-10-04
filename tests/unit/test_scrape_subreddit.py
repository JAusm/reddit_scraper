from unittest import TestCase
from scrape_subreddit import ScrapeSubredditInterface, ScrapeSubreddits
from reddit_auth import PrawAuth

from praw.models import ListingGenerator


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

        self.connection_info = {
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "password": "test_password",
            "user_agent": "test_user_agent",
            "username": "test_username"
        }

    def test_ScrapeSubreddits_returns_expected_results(self):
        actual = ScrapeSubreddits(self.subreddit, self.connection_info)

        self.assertEqual(
            actual.subreddit,
            self.subreddit
        )

        self.assertIsInstance(
            actual.auth_instance,
            PrawAuth
        )

    def test_query_subreddit_returns_data(self):

        scrape_instance = ScrapeSubreddits(self.subreddit, self.connection_info)
        actual = scrape_instance.query_subreddit(6)

        self.assertIsInstance(
            actual,
            ListingGenerator
        )

        self.assertEqual(actual.__dict__["yielded"], 6)

