from unittest import TestCase
from scraper.reddit_auth import RedditAuthInterface, PrawAuth
import praw


class RedditAPIInterfaceTest(TestCase):

    def setUp(self) -> None:
        self.connection_info = {
            "client_id": None,
            "client_secret": None,
            "user_agent": None,
        }

    def test_reddit_api_interface_exists(self):
        actual = RedditAuthInterface(self.connection_info)

        self.assertIsInstance(actual, RedditAuthInterface)

    def test_interface_has_the_expected_init_values(self):
        actual = RedditAuthInterface(self.connection_info)

        self.assertEqual(
            actual.connection_info['client_id'],
            None
        )
        self.assertEqual(
            actual.connection_info["client_secret"],
            None
        )
        self.assertEqual(
            actual.connection_info["user_agent"],
            None
        )

    def test_auth_raises_expected_exception(self):
        interface = RedditAuthInterface(self.connection_info)

        with self.assertRaises(NotImplementedError):
            interface._auth()


class TestPrawAPI(TestCase):

    def setUp(self) -> None:
        self.connection_info = {
            "client_id": "test_client_id",
            "client_secret": "test_client_secret",
            "user_agent": "test_user_agent",
        }

    def test_praw_api_exists(self):
        actual = PrawAuth(self.connection_info)

        self.assertIsInstance(actual, PrawAuth)

    def test_int_has_expected_init_values(self):
        actual = PrawAuth(self.connection_info)

        self.assertEqual(
            actual.connection_info['client_id'],
            "test_client_id"
        )
        self.assertEqual(
            actual.connection_info["client_secret"],
            "test_client_secret"
        )
        self.assertEqual(
            actual.connection_info["user_agent"],
            "test_user_agent"
        )

    def test_auth_is_the_expected_praw_object(self):
        instance = PrawAuth(self.connection_info)
        actual = instance._auth()

        self.assertIsInstance(actual, praw.reddit.Reddit)
