from collections import Counter
from typing import Dict


def count_mention(mention_counter: Counter[str], tweet: Dict) -> None:
    mentioned_users = tweet.get('mentionedUsers') or []

    for user in mentioned_users:
        mention_counter[user['username']] += 1


__all__ = [
    "count_mention"
]