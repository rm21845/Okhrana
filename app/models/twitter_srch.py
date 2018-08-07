import requests
import tweepy as tpy


class twitter(object):
    def __init__(self, key, secret):
        self.key = key
        self.secret = secret
        self.auth = self.get_auth()
        self.api = self.get_api()

    def get_auth(self):
        return tpy.AppAuthHandler(self.key, self.secret)

    def get_api(self):
        return tpy.API(self.auth, wait_on_rate_limit=True,
                       wait_on_rate_limit_notify=True)

    def search_user(self, username):
        return self.api.get_user(username)
