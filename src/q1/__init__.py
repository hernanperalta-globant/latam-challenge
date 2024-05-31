from collections import Counter
from datetime import date, datetime
from typing import DefaultDict, Dict, List, Tuple


TweetDateCounter = DefaultDict[date, Counter]


def count_user_by_date(date_counter: TweetDateCounter, tweet: Dict) -> None:
    """Count a tweet from a user for a given date. The counter keeps track of dates and how many tweets a user performed that day.

    :param date_counter: Date counter which keeps track of dates and users that tweeted that day.
    :param tweet: Tweet.
    """    
    date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
    user = tweet['user']['username']

    date_counter[date][user] += 1


def top_most_tweeted_dates(date_counter: TweetDateCounter) -> List[Tuple[datetime.date, Counter]]:
    """Get 10 most tweeted dates in descending order.

    :param date_counter: Date counter which keeps track of dates and users that tweeted that day.
    :return: List with top 10 most tweeted dates.
    """    
    top_tweeted_dates = sorted(date_counter.items(), key=get_tweet_count, reverse=True)
    return top_tweeted_dates[:10]


def top_users_per_date(date_counter: List[Tuple[datetime.date, Counter]]) -> List[Tuple[datetime.date, str]]:
    return [(date, top_user(counter)) for date, counter in date_counter]


def top_user(counter: Counter) -> str:
    # the brackets are for unpacking the user
    return counter.most_common(1)[0][0]


def get_tweet_count(date_counter: Tuple[datetime.date, Counter]) -> int:
    # sum(counter.values()) gives you the counter's total count
    return sum(date_counter[1].values())


__all__ = [
    "TweetDateCounter",
    "get_tweet_count",
    "count_user_by_date",
    "top_user",
    "top_users_per_date",
    "top_most_tweeted_dates"
]