"""Utility functions."""
import re
from html import escape


re_newlines = re.compile(r'\r\n|\r') # Used in normalize_newlines


def normalize_newlines(text):
    """Normalize CRLF and CR newlines to just LF.

    Copied from the Django source code.
    https://github.com/django/django/blob/master/django/utils/text.py#L261
    """
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
