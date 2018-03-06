"""Test conversion of tweets to toots."""
from mock import patch

from tweepy.models import Status

from twit2toot import get_twitter


def test_can_read_tweets_from_sample_file():  # noqa: D103
    # GIVEN a list of tweets
    with patch('tweepy.binder.requests.Session.request') as mock_response:
        with open('tests/data/sample_tweets.json') as f:
            json_data = f.read()
        mock_response.return_value.status_code = 200
        mock_response.return_value.text = json_data

        # WHEN reading a timeline
        twitter = get_twitter()

        tweets = twitter.user_timeline()

    # THEN we get a list of tweets as Status objects
    assert len(tweets) > 1
    assert isinstance(tweets[0], Status)
