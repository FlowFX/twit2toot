"""Test writing to the Mastodon API."""
from twit2toot import get_mastodon


class TestWritingToMastodon:  # noqa: D101

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
