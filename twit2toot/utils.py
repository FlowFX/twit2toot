"""Utility functions."""
import re
from html import escape

from tweepy.models import Status


def normalize_newlines(text):
    """Normalize CRLF and CR newlines to just LF.

    Copied from the Django source code.
    https://github.com/django/django/blob/master/django/utils/text.py#L261
    """
    re_newlines = re.compile(r'\r\n|\r')

    return re_newlines.sub('\n', str(text))


def linebreaks(value, autoescape=False):
    """Convert newlines into <p> and <br>s.

    Copied from the Django source code.
    https://github.com/django/django/blob/master/django/utils/html.py#L141
    """
    value = normalize_newlines(value)
    paras = re.split('\n{2,}', str(value))
    if autoescape:
        paras = ['<p>%s</p>' % escape(p).replace('\n', '<br>') for p in paras]
    else:
        paras = ['<p>%s</p>' % p.replace('\n', '<br>') for p in paras]

    return '\n\n'.join(paras)


def process_tweet(tweet):
    """Process a tweet and provide a dictionary of values for the tooting.

    status,
    in_reply_to_id=None,
    media_ids=None,
    sensitive=False,
    visibility='',
    spoiler_text=None,
    """
    assert isinstance(tweet, Status)

    urls = tweet.entities.get('urls')

    try:
        # first URL
        url = urls[0]

        expanded_url = url['expanded_url']
        url = url['url']
        text = tweet.text.replace(url, expanded_url)
    except IndexError:
        text = tweet.text

    result = {
        'status': text,
        'in_reply_to_id': None,
        'media_ids': None,
        'sensitive': False,
        'visibility': '',
        'spoiler_text': None,
    }

    return result
