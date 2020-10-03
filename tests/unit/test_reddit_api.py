from unittest import TestCase
from reddit_api import RedditAPIInterface


class RedditAPIInterfaceTest(TestCase):

    def test_reddit_api_interface_exists(self):
        actual = RedditAPIInterface()

        self.assertIsInstance(actual, RedditAPIInterface)

    def test_interface_has_the_expected_init_values(self):

        actual = RedditAPIInterface()

        self.assertEqual(actual.client_id, None)
        self.assertEqual(actual.client_secret, None)
        self.assertEqual(actual.password, None)
        self.assertEqual(actual.user_agent, None)
        self.assertEqual(actual.username, None)

    def test_auth_raises_expected_exception(self):

        interface = RedditAPIInterface()

        with self.assertRaises(NotImplementedError):
            interface.auth()
