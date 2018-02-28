"""Main functionality of the twit2toot package."""
import json

import tweepy


try:
    with open('secrets.json') as f:
        secrets = json.loads(f.read())
except FileNotFoundError:  # pragma: no cover
    error_msg = 'secrets.json file is missing.'
    raise FileNotFoundError(error_msg)


auth = tweepy.OAuthHandler(
    secrets['twitter']['consumer_key'],
    secrets['twitter']['consumer_secret'],
    )
auth.set_access_token(
    secrets['twitter']['access_token'],
    secrets['twitter']['access_token_secret'],
    )

api = tweepy.API(auth)
