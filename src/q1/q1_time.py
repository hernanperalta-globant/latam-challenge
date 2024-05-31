# from typing import List, Tuple
# from datetime import datetime

# def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
#     pass


from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json
from multiprocessing import Pool, cpu_count

from q1.utils import TweetDateCount, count_tweet, find_top_user_by_date, sort_dates_by_count


def read_lines(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line for line in file]


def process_tweets_batch(tweets_batch: List[str]) -> dict:
    date_count = defaultdict(Counter)

    for line in tweets_batch:
        tweet = json.loads(line)

        count_tweet(date_count, tweet)
    
    return date_count


def merge_counts(date_counts: List[TweetDateCount]) -> TweetDateCount:
    merged = defaultdict(Counter)

    for counter in date_counts:
        for date, user_counter in counter.items():
            merged[date] += user_counter

    return merged


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    lines = read_lines(file_path)
    num_workers = cpu_count()
    batch_size = len(lines) // num_workers

    with Pool(num_workers) as pool:
        batch = [lines[i:i + batch_size] for i in range(0, len(lines), batch_size)]
        results = pool.map(process_tweets_batch, batch)
    
    merged_counts = merge_counts(results)

    top_dates = sort_dates_by_count(merged_counts)
    result = find_top_user_by_date(top_dates)

    return result
