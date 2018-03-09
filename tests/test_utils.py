"""Test utility functions."""
import re

from twit2toot.factories import StatusFactory
from twit2toot.utils import process_tweet


# t.co/ links
t_co = re.compile(r'.*t\.co/.*')


class TestProcessing:
    """Test twit2toot.utils.process_tweet."""

    def test_tweet_with_link(self):  # noqa: D102
        # GIVEN a simple tweet with one linked URL.
        tweet = StatusFactory.build(
            text='Just run Let’s Encrypt. https://t.co/7NkDnQRYdq',
            entities={
                'urls': [
                    {
                        "url": "https://t.co/7NkDnQRYdq",
                        "expanded_url": "http://blog.koehntopp.info/index.php/3075-how-not-to-run-a-ca/",
                        "display_url": "blog.koehntopp.info/index.php/3075…",
                    },
                ],
            },
        )

        # WHEN processing the tweet
        toot_dict = process_tweet(tweet)
        text = toot_dict['status']

        # THEN the content shows a clean URL
        # http://blog.koehntopp.info/index.php/3075-how-not-to-run-a-ca/
        assert not t_co.match(text)
        assert 'http://blog.koehntopp.info/index.php/3075-how-not-to-run-a-ca/' in text
