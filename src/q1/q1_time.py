from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
from multiprocessing import Pool, cpu_count

from src.q1.utils import TweetDateCounter, count_tweet_user_by_date, find_top_user_by_date, sort_dates_by_count
from src.utils import load_all_tweets



def process_tweets_batch(tweets_batch: List[str]) -> dict:
    date_counter = defaultdict(Counter)

    for raw_tweet in tweets_batch:
        tweet = json.loads(raw_tweet)
        count_tweet_user_by_date(date_counter, tweet)
    
    return date_counter


def merge_counters(date_counters: List[TweetDateCounter]) -> TweetDateCounter:
    merged = defaultdict(Counter)

    for counter in date_counters:
        for date, user_counter in counter.items():
            merged[date] += user_counter

    return merged


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    tweets = load_all_tweets(file_path)
    num_workers = cpu_count()
    batch_size = len(tweets) // num_workers

    with Pool(num_workers) as pool:
        batch = [tweets[i:i + batch_size] for i in range(0, len(tweets), batch_size)]
        results = pool.map(process_tweets_batch, batch)
    
    merged_counters = merge_counters(results)

    top_dates = sort_dates_by_count(merged_counters)
    result = find_top_user_by_date(top_dates)

    return result
