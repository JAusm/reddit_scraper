from abc import ABC


class RedditAuthInterface(ABC):

    def __init__(self, connection_info):
        self.connection_info = connection_info

    def _auth(self):
        raise NotImplementedError


class PrawAuth(RedditAuthInterface):
    def __init__(self, connection_info):
        super().__init__(connection_info)


