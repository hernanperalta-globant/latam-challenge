from collections import Counter
import json
from multiprocessing import Pool, cpu_count
from typing import List, Tuple

from src import load_all_tweets
from src.q2 import count_emoji


def process_tweets_batch(tweets_batch: List[str]) -> Counter[str]:
    emoji_counter: Counter[str] = Counter()

    for raw_tweet in tweets_batch:
        tweet = json.loads(raw_tweet)
        count_emoji(emoji_counter, tweet)

    return emoji_counter


def merge_counters(emoji_counters: List[Counter[str]]) -> Counter[str]:
    merged: Counter[str] = Counter()

    for counter in emoji_counters:
        merged.update(counter)
    
    return merged


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    tweets = load_all_tweets(file_path)
    num_workers = cpu_count()
    batch_size = len(tweets) // num_workers

    with Pool(num_workers) as pool:
        batch = [tweets[i:i + batch_size] for i in range(0, len(tweets), batch_size)]
        results = pool.map(process_tweets_batch, batch)
    
    merged_counters = merge_counters(results)
    top_emojis = merged_counters.most_common(10)

    return top_emojis
