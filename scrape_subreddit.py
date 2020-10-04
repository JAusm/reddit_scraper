from abc import ABCMeta
from reddit_auth import PrawAuth


class ScrapeSubredditInterface(object, metaclass=ABCMeta):
    """

    Abstract base class for scraping a subreddit for content.

    """

    def __init__(self, subreddit: str):
        """

        subreddit: List of subreddits to scrape.

        """
        self.subreddit = subreddit

    def query_subreddit(self, hot_limit: int):
        pass

    def get_videos(self):
        pass


class ScrapeSubreddits(ScrapeSubredditInterface):
    """

    This class is responsible for scraping subreddits for content.

    """

    def __init__(self, subreddit: str, connection_info: dict, hot_limit: int):
        super().__init__(subreddit)

        self.auth_instance = PrawAuth(connection_info)
        self.reddit_auth = self.auth_instance.auth
        self.posts = self.query_subreddit(hot_limit)

    def query_subreddit(self, hot_limit: int):
        """

        For each subreddit, get post data.

        hot_limit: Int for how many results you want to return.

        Return:
            posts: A number of posts from a given subreddit and hot_limit

        """

        subreddit = self.reddit_auth.subreddit(self.subreddit)
        posts = subreddit.hot(limit=hot_limit)

        return posts

    def get_videos(self):
        """

        posts: A number of posts for a given subreddit and hot_limit

        Returns:
            videos: A list with tuples containing the url and name of the video

        """
        videos = []
        for post in self.posts:
            url = post.media['reddit_video']['fallback_url']
            url = url.split("?")[0]
            name = post.title[:30].rstrip() + ".mp4"
            videos.append((url, name))
        return videos
