"""Testing our usage of the Twitter API using tweepy."""
from twit2toot import api

from tweepy.models import Status



def test_get_user_timeline():
    """Exploratory test to get started with using tweepy."""
    # GIVEN any state
    # WHEN using the tweepy to get the user timeline from Twitter
    response = api.user_timeline(count=5)

    # THEN it's a list of the correct length
    assert isinstance(response, list)
    assert len(response) == 5

    # AND it's members are tweet objects
    tweet = response[0]
    assert isinstance(tweet, Status)


def test_get_user_timeline_while_mocking_the_api_response():
    """Rewrite the test above w/o hitting the Twitter API."""
    pass
