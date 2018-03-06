"""Test conversion of tweets to toots."""
import re

import pytest

from tweepy.models import Status

from twit2toot import crosspost_to_mastodon
from twit2toot.utils import linebreaks

# t.co/ links
t_co = re.compile(r'.*t\.co/.*')


def test_can_read_tweets_from_sample_file(sample_tweets):  # noqa: D103
    # GIVEN a list of tweets
    tweets = sample_tweets

    # THEN we get a list of tweets as Status objects
    assert len(tweets) > 1
    assert isinstance(tweets[-1], Status)


@pytest.mark.api
def test_can_toot_a_simple_tweet(mastodon, sample_tweets):  # noqa: D103
    # GIVEN a simple tweet that only contains text
    #
    # "Hallo, ich bin ein linksversiffter Gutmensch und wenn du das als
    # Beleidigung zu mir sagst, bist du wohl ein braunverkackter Schlechtmensch."
    tweet = sample_tweets[0]

    assert not tweet.retweeted
    assert not tweet.in_reply_to_user_id
    assert not tweet.in_reply_to_status_id

    assert tweet.entities['hashtags'] == []
    assert tweet.entities['symbols'] == []
    assert tweet.entities['user_mentions'] == []
    assert tweet.entities['urls'] == []

    # WHEN cross-posting this tweet to Mastodon
    response = crosspost_to_mastodon(tweet, mastodon)

    # THEN the response is a clean toot dict
    assert type(response['id']) == int

    assert response['content'] == linebreaks(tweet.text)
    assert response['tags'] == []

    assert not response['in_reply_to_id']
    assert not response['reblogged']


@pytest.mark.api
def test_can_toot_a_tweet_with_one_link(mastodon, sample_tweets):  # noqa: D103
    # GIVEN a tweet that only contains text and one link
    #
    # "Please: Forget your EV or other certs and just run Let’s Encrypt.
    # Thanks! https://t.co/7NkDnQRYdq"
    tweet = sample_tweets[1]

    assert not tweet.in_reply_to_user_id
    assert not tweet.in_reply_to_status_id

    assert tweet.entities['hashtags'] == []
    assert tweet.entities['symbols'] == []
    assert tweet.entities['user_mentions'] == []
    assert len(tweet.entities['urls']) == 1

    link = tweet.entities['urls'][0]
    assert link['url'].startswith('https://t.co/')
    # print(link)

    # WHEN cross-posting this tweet to Mastodon
    response = crosspost_to_mastodon(tweet, mastodon)

    # THEN the response content shows a clean URL
    assert not t_co.match(response['content'])

    # assert response['content'] == linebreaks(tweet.text)
    # assert response['tags'] == []

    # assert not response['in_reply_to_id']
    # assert not response['reblogged']

# Mastodon.status_post(
#     status,
#     in_reply_to_id=None,
#     media_ids=None,
#     sensitive=False,
#     visibility='',
#     spoiler_text=None,
#     )


# {
#     'id': # Numerical id of this toot
#     'uri': # Descriptor for the toot
#         # EG 'tag:mastodon.social,2016-11-25:objectId=<id>:objectType=Status'
#     'url': # URL of the toot
#     'account': # User dict for the account which posted the status
#     'in_reply_to_id': # Numerical id of the toot this toot is in response to
#     'in_reply_to_account_id': # Numerical id of the account this toot is in response to
#     'reblog': # Denotes whether the toot is a reblog. If so, set to the original toot dict.
#     'content': # Content of the toot, as HTML: '<p>Hello from Python</p>'
#     'created_at': # Creation time
#     'reblogs_count': # Number of reblogs
#     'favourites_count': # Number of favourites
#     'reblogged': # Denotes whether the logged in user has boosted this toot
#     'favourited': # Denotes whether the logged in user has favourited this toot
#     'sensitive': # Denotes whether media attachments to the toot are marked sensitive
#     'spoiler_text': # Warning text that should be displayed before the toot content
#     'visibility': # Toot visibility ('public', 'unlisted', 'private', or 'direct')
#     'mentions': # A list of users dicts mentioned in the toot, as Mention dicts
#     'media_attachments': # A list of media dicts of attached files
#     'emojis': # A list of custom emojis used in the toot, as Emoji dicts
#     'tags': # A list of hashtag used in the toot, as Hashtag dicts
#     'application': # Application dict for the client used to post the toot (Does not federate
#                    # and is therefore always None for remote toots, can also be None for
#                    # local toots for some legacy applications).
#     'language': # The language of the toot, if specified by the server.
#     'muted': # Boolean denoting whether the user has muted this status by
#              # way of conversation muting
# }
