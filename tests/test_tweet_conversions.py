"""Test conversion of tweets to toots."""
from tweepy.models import Status


def test_can_read_tweets_from_sample_file(sample_tweets):  # noqa: D103
    # GIVEN a list of tweets
    tweets = sample_tweets

    # THEN we get a list of tweets as Status objects
    assert len(tweets) > 1
    assert isinstance(tweets[0], Status)
