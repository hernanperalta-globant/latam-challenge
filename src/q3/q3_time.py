from collections import Counter
import json
from multiprocessing import Pool, cpu_count
from typing import List, Tuple

from src import load_all_tweets, multiprocess_tweets
from src.q3 import count_mention


def count_mentions(tweets_batch: List[str]) -> Counter[str]:
    mention_counter: Counter[str] = Counter()

    for raw_tweet in tweets_batch:
        tweet = json.loads(raw_tweet)
        count_mention(mention_counter, tweet)

    return mention_counter


def merge_counters(mention_counters: List[Counter]) -> Counter:
    merged: Counter[str] = Counter()

    for counter in mention_counters:
        merged.update(counter)
    
    return merged


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    results = multiprocess_tweets(file_path, count_mentions)
    merged_counters = merge_counters(results)
    top_mentions = merged_counters.most_common(10)

    return top_mentions
