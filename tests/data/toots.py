"""Collection of Mastodon toot responses."""
import datetime

from dateutil import tz


# Response from the Mastodon API after sending a simple toot.
TOOT_SIMPLE = {
    'id': 99608959135870828,
    'created_at': datetime.datetime(2018, 3, 1, 13, 48, 16, 199000, tzinfo=tz.tzutc()),
    'in_reply_to_id': None,
    'in_reply_to_account_id': None,
    'sensitive': False,
    'spoiler_text': '',
    'visibility': 'private',
    'language': 'en',
    'uri': 'https://chaos.social/users/flowfx_testet/statuses/99608959135870828',
    'content': '<p>I am a toot.</p>',
    'url': 'https://chaos.social/@flowfx_testet/99608959135870828',
    'reblogs_count': 0,
    'favourites_count': 0,
    'favourited': False,
    'reblogged': False,
    'muted': False,
    'reblog': None,
    'application': {
        'name': 'twit2toot',
        'website': 'https://github.com/FlowFX/twit2toot',
        },
    'account': {
        'id': 44841,
        'username': 'flowfx_testet',
        'acct': 'flowfx_testet',
        'display_name': 'FlowFX TESTET',
        'locked': True,
        'created_at': datetime.datetime(2018, 2, 28, 18, 15, 52, 579000, tzinfo=tz.tzutc()),
        'note': '<p></p>',
        'url': 'https://chaos.social/@flowfx_testet',
        'avatar': 'https://chaos.social/avatars/original/missing.png',
        'avatar_static': 'https://chaos.social/avatars/original/missing.png',
        'header': 'https://chaos.social/headers/original/missing.png',
        'header_static': 'https://chaos.social/headers/original/missing.png',
        'followers_count': 1,
        'following_count': 0, 'statuses_count': 15,
        },
    'media_attachments': [],
    'mentions': [],
    'tags': [],
    'emojis': [],
}
