from collections import Counter
from typing import Dict


def count_mention(mention_counter: Counter[str], tweet: Dict) -> None:
    """Count a mention for a given user. Handles the case when no users are mentioned (i.e.: "mentionedUsers": null)

    :param mention_counter: Mention counter.
    :param tweet: Tweet which may or may not mention users.
    """    
    mentioned_users = tweet.get('mentionedUsers') or []

    for user in mentioned_users:
        mention_counter[user['username']] += 1


__all__ = [
    "count_mention"
]
