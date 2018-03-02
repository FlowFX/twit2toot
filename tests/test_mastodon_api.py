"""Test writing to the Mastodon API."""
from unittest.mock import patch

import pytest

from twit2toot import get_mastodon


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
