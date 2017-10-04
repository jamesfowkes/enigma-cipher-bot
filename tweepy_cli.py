""" tweepy_cli.py

Usage:
    tweepy_cli.py --send <message>
    tweepy_cli.py --gettweets <tweet_count> [<since_id>]

Options:

    --send      Tweet <message>
    --gettweets Retrieve the last <tweet_count> tweets to the authed user and display them
    <since_id>  Only retrieve tweets more recent than this ID    
"""

import docopt
import logging

import tweepy_api

def get_logger():
    return logging.getLogger(__name__)

if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)

    opts = docopt.docopt(__doc__)

    api = tweepy_api.api()

    if opts["--send"]:
        msg = opts["<message>"]
        status = api.update_status(msg)
        get_logger().info("Tweeted '{}'' (ID {})".format(status.text, status.id))

    if opts["--gettweets"]:
        n = int(opts["<tweet_count>"])
        mentions = api.mentions_timeline(count=n)
        for mention in mentions:
            get_logger().info(mention.text)
        