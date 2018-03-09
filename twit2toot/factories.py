"""Model factories."""
import datetime

import factory

from tweepy import models


class User(models.User):
    """User model from tweepy, altered for test usage."""

    def __init__(self, api=None, id=None):
        # super(User, self).__init__()
        self.id = id


class Status(models.Status):
    """Status model from tweepy, altered for test usage."""

    def __init__(self, id=None, created_at=None, author=None, text='', entities=[],
                 in_reply_to_status_id=False, in_reply_to_user_id=False):
        super(Status, self).__init__()

        self.id = id
        self.created_at = created_at
        self.author = author
        self.text = text
        self.entities = entities
        self.in_reply_to_status_id = in_reply_to_status_id
        self.in_reply_to_user_id = in_reply_to_user_id


class UserFactory(factory.Factory):
    """Model factory for tweepy.models.User."""

    class Meta:
        model = User

    id = 6712152


class StatusFactory(factory.Factory):
    """Model factory for tweepy.models.Status."""

    class Meta:
        model = Status

    id = 628469339801452544
    created_at = datetime.datetime(2015, 8, 4, 7, 35, 41)
    author = factory.SubFactory(UserFactory)
    text = 'Hallo. Ich bin ein Tweet.'
    entities = {
        'hashtags': [],
        'symbols': [],
        'user_mentions': [],
        'urls': [],
    }
    in_reply_to_status_id = False
    in_reply_to_user_id = False
# is_quote_status = False
