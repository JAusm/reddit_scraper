from abc import ABCMeta
from reddit_auth import PrawAuth


class ScrapeSubredditInterface(object, metaclass=ABCMeta):
    """

    Abstract base class for authenticating with Reddit

    """

    def __init__(self, subreddit: str):
        """

        subreddits: List of subreddits to scrape.

        """
        self.subreddit = subreddit

    def download_media(self):
        pass


class ScrapeSubreddits(ScrapeSubredditInterface):
    """

    This class is responsible for scraping subreddits for content.

    """
    def __init__(self, subreddit: str, connection_info):
        super().__init__(subreddit)

        self.auth_instance = PrawAuth(
            connection_info
        )
        self.reddit_auth = self.auth_instance.auth

    def query_subreddit(self, hot_limit: int):
        """

        For each subreddit, get post data.

        hot_limit: Int for how many results you want to return.

        """

        access_subreddit = self.reddit_auth.subreddit(
            self.subreddit
        )
        hot_posts = access_subreddit.hot(
            limit=hot_limit
        )

        return hot_posts







