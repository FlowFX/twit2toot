"""Test utility functions."""
import datetime

from tweepy.models import Status, User

from twit2toot.factories import UserFactory, StatusFactory


def test_can_create_sample_tweet():  # noqa: D103
    user = UserFactory.build()

    tweet = StatusFactory.build()
    # tweet = Status()

    print(tweet)

    assert isinstance(tweet, Status)
    assert isinstance(tweet.id, int)
    assert isinstance(tweet.author, User)

    import pytest
    pytest.fail("Finish the test!")
