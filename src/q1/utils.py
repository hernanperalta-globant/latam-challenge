from collections import Counter
from datetime import datetime
from typing import DefaultDict, Dict, List, Tuple

TweetDateCounter = DefaultDict[datetime.date, Counter]


def count_tweet_user_by_date(date_counter: TweetDateCounter, tweet: Dict) -> None:
    date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
    user = tweet['user']['username']
    
    date_counter[date][user] += 1


def find_top_user_by_date(date_counter: List[Tuple[datetime.date, Counter]]) -> List[Dict[datetime.date, str]]:
    return [(date, top_user(counter)) for date, counter in date_counter]


def sort_dates_by_count(date_counter: TweetDateCounter) -> TweetDateCounter:
    return sorted(date_counter.items(), key=get_tweet_count, reverse=True)[:10]


def top_user(counter: Counter) -> str:
    return counter.most_common(1)[0][0]


def get_tweet_count(date_counter: Tuple[datetime.date, Counter]) -> int:
    return sum(date_counter[1].values())

