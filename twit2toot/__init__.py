"""Main functionality of the twit2toot package."""
import json

from mastodon import Mastodon

import tweepy


try:
    with open('secrets.json') as f:
        secrets = json.loads(f.read())
except FileNotFoundError:  # pragma: no cover
    error_msg = 'secrets.json file is missing.'
    raise FileNotFoundError(error_msg)


# Twitter API instance
auth = tweepy.OAuthHandler(
    secrets['twitter']['consumer_key'],
    secrets['twitter']['consumer_secret'],
    )
auth.set_access_token(
    secrets['twitter']['access_token'],
    secrets['twitter']['access_token_secret'],
    )

api = tweepy.API(auth)


# Mastodon API instance
def get_mastodon():
    """Return a Mastodon API instance."""
    mastodon = Mastodon(
        client_id=secrets['mastodon']['client_key'],
        client_secret=secrets['mastodon']['client_secret'],
        access_token=secrets['mastodon']['access_token'],
        api_base_url=secrets['mastodon']['api_base_url'],
    )

    return mastodon
