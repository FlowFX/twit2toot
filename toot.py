"""Command-line app that toots the latest tweets."""
import click

from twit2toot import get_mastodon, get_twitter


@click.command()
def toot_latest_tweet():
    """Get the latest tweet from Twitter and toot it to Mastodon."""
    twitter = get_twitter()
    mastodon = get_mastodon()

    tweet = twitter.user_timeline(count=1)[0]
    response = mastodon.toot(tweet.text)

    click.echo(response)


if __name__ == "__main__":
    """Toot the latest tweet."""
    toot_latest_tweet()
