from abc import ABC


class RedditAPIInterface(ABC):

    def __init__(self):
        self.client_id = None
        self.client_secret = None
        self.password = None
        self.user_agent = None
        self. username = None

    def auth(self):
        raise NotImplementedError


