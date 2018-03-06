"""pytest fixtures."""
from mock import patch

import pytest

from twit2toot import get_twitter


@pytest.fixture(scope="session")
def sample_tweets():
    """Return a list of sample tweets."""
    with patch('tweepy.binder.requests.Session.request') as mock_response:
        with open('tests/data/sample_tweets.json') as f:
            json_data = f.read()
        mock_response.return_value.status_code = 200
        mock_response.return_value.text = json_data

        twitter = get_twitter()

        return twitter.user_timeline()
