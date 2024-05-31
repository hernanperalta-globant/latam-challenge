from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json

from src.q1 import count_user_by_date, top_users_per_date, top_most_tweeted_dates, TweetDateCounter
from src import multiprocess_tweets


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    results = multiprocess_tweets(file_path, count_users_by_date)
    merged_counters = merge_counters(results)

    top_dates = top_most_tweeted_dates(merged_counters)
    result = top_users_per_date(top_dates)

    return result


def count_users_by_date(tweets_batch: List[str]) -> TweetDateCounter:
    date_counter: TweetDateCounter = defaultdict(Counter)

    for raw_tweet in tweets_batch:
        tweet = json.loads(raw_tweet)
        count_user_by_date(date_counter, tweet)
    
    return date_counter


def merge_counters(date_counters: List[TweetDateCounter]) -> TweetDateCounter:
    merged: TweetDateCounter = defaultdict(Counter)

    for counter in date_counters:
        for date, user_counter in counter.items():
            merged[date] += user_counter

    return merged
