from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
from multiprocessing import Pool, cpu_count

from src.q1 import count_user_by_date, find_top_user_by_date, sort_dates_by_count, TweetDateCounter
from src import load_all_tweets, multiprocess_tweets


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


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    results = multiprocess_tweets(file_path, count_users_by_date)    
    merged_counters = merge_counters(results)
    top_dates = sort_dates_by_count(merged_counters)
    result = find_top_user_by_date(top_dates)

    return result
