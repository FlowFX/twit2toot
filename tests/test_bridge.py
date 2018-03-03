"""Test main functionality of this Twitter to Mastodon bridge."""
import pytest

from twit2toot import get_mastodon, get_twitter


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
