"""Test calls to the external Twitter and Mastodon APIs."""
from mock import patch

import pytest

from tweepy.models import Status

from twit2toot import get_mastodon, get_twitter


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


class TestWritingToMastodon:  # noqa: D101

    @pytest.mark.skip(reason="This hits the Mastodon API.")
    def test_can_send_toot(self):
        """Exploratory test to get used to the Mastodon.py wrapper."""
        # GIVEN a mastodon API instance
        mastodon = get_mastodon()

        # WHEN writing a toot to the API
        text = 'I am a toot.'
        response = mastodon.toot(text)

        # THEN it works and returns the toot id
        assert isinstance(response.id, int)
        assert text in response['content']

    @patch('twit2toot.Mastodon.toot')
    def test_can_send_toot_with_mock(self, mock_response):
        """Test correct usage of Mastodon.py.

        Mocking the response from the Mastodon API.
        """
        from .data.toots import TOOT_SIMPLE
        mock_response.return_value = TOOT_SIMPLE

        # GIVEN a mastodon API instance
        mastodon = get_mastodon()

        # # WHEN writing a toot to the API
        text = 'I am a toot.'
        response = mastodon.toot(text)

        # # THEN it works and returns the toot id
        assert isinstance(response['id'], int)
        assert text in response['content']


class TestTwitter2MastodonBridge:  # noqa: D101

    @pytest.mark.skip(reason="This hits the Twitter and Mastodon APIs.")
    def test_bridge_latest_tweet_to_mastodon(self):
        """Test that we can copy a Tweet to a Toot.

        This one hits that Twitter and Mastodon APIs.
        """
        # GIVEN access to the Twitter and Mastodon APIs
        twitter = get_twitter()
        mastodon = get_mastodon()

        # WHEN writing the latest tweet to mastodon
        tweet = twitter.user_timeline(count=1)[0]
        text = tweet.text
        response = mastodon.toot(text)

        # THEN it works and returns the toot id
        assert isinstance(response.id, int)
        assert text[-20:] in response['content']

    def test_bridge_latest_tweet_to_mastodon_using_mocks(self):
        """Test that we can copy a Tweet to a Toot.

        This one hits that Twitter and Mastodon APIs.
        """
        # GIVEN access to the Twitter and Mastodon APIs
        twitter = get_twitter()

        # WHEN writing the latest tweet to mastodon
        with patch('tweepy.binder.requests.Session.request') as mock_response:
            with open('tests/data/Twitter_User_Timeline-1519822598460.json') as f:
                json_data = f.read()
            mock_response.return_value.status_code = 200
            mock_response.return_value.text = json_data

            tweet = twitter.user_timeline(count=1)[0]
            text = tweet.text

        mastodon = get_mastodon()

        with patch('twit2toot.Mastodon.toot') as mock_response:
            from .data.toots import TOOT_SIMPLE
            mock_response.return_value = TOOT_SIMPLE

            response = mastodon.toot(text)

        # THEN it works and returns the toot id
        assert isinstance(response['id'], int)
