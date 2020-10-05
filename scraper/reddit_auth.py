from abc import ABCMeta
import praw


class RedditAuthInterface(object, metaclass=ABCMeta):
    """

    Abstract base class for authenticating with Reddit

    """

    def __init__(self, connection_info: dict):
        """

        connection_info is a dictionary containing the following params:
            client_id
            client_secret
            user_agent

        """
        self.connection_info = connection_info

    def _auth(self):
        raise NotImplementedError


class PrawAuth(RedditAuthInterface):
    """

    This class is responsible for authenticating with Reddit via
    the praw python library.

    """
    def __init__(self, connection_info):
        super().__init__(connection_info)

        self.auth = self._auth()

    def _auth(self):
        """

        Authenticate using praw with the self.connection info

        """
        reddit_connection = praw.Reddit(
            client_id=self.connection_info["client_id"],
            client_secret=self.connection_info["client_secret"],
            user_agent=self.connection_info["user_agent"]
        )

        return reddit_connection

