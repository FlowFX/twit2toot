"""Testing our usage of the Twitter API using tweepy."""
from unittest.mock import patch

import pytest

from tweepy.models import Status

from twit2toot import get_twitter


class TestUserTimeline:  # noqa: D101

    @pytest.mark.skip(reason="This hits the Twitter API.")
    def test_get_user_timeline(self):
        """Exploratory test to get started with using tweepy."""
        # GIVEN any state
        # WHEN using the tweepy to get the user timeline from Twitter
        twitter = get_twitter()
        response = twitter.user_timeline(count=5)

        # THEN it's a list of the correct length
        assert isinstance(response, list)
        assert len(response) == 5

        # AND it's members are tweet objects
        tweet = response[0]
        assert isinstance(tweet, Status)

    @patch('tweepy.binder.requests.Session.request')
    def test_get_user_timeline_while_mocking_the_api_response(self, mock_response):
        """Test correct usage of tweepy.

        Mocking the GET request to the Twitter API.
        """
        with open('tests/data/Twitter_User_Timeline-1519822598460.json') as f:
            json_data = f.read()

        mock_response.return_value.status_code = 200
        mock_response.return_value.text = json_data

        # GIVEN any state
        # WHEN using the tweepy to get the user timeline from Twitter
        twitter = get_twitter()
        response = twitter.user_timeline()

        # THEN it's a list
        assert isinstance(response, list)

        # AND it's members are tweets
        assert isinstance(response[0], Status)
