from collections import Counter
from datetime import datetime
from typing import DefaultDict, Dict, List, Tuple

TweetDateCount = DefaultDict[datetime.date, Counter]


def tweet_count(date_count: Tuple[datetime.date, Counter]) -> int:
    return sum(date_count[1].values())


def top_user(counter: Counter) -> str:
    return counter.most_common(1)[0][0]


def count_tweet(date_count: TweetDateCount, tweet: Dict) -> None:
    date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S%z").date()
    user = tweet['user']['username']
    
    date_count[date][user] += 1


def sort_dates_by_count(date_count: TweetDateCount) -> TweetDateCount:
    return sorted(date_count.items(), key=tweet_count, reverse=True)[:10]


def find_top_user_by_date(date_count: List[Tuple[datetime.date, Counter]]) -> List[Dict[datetime.date, str]]:
    return [(date, top_user(counter)) for date, counter in date_count]
