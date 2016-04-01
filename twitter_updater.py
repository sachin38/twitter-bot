#!/usr/bin/env python

from twython import Twython

def twitter_updater():
    twitter = Twython(
                "APP KEY",
                "APP SECRET KEY",
                "AUTH TOKEN",
                "AUTH SECRET TOKEN"
            )
    twitter.update_status(status="You status here")

twitter_updater()
