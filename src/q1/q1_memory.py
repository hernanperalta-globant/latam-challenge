from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter

from src.q1 import TweetDateCounter, count_user_by_date, find_top_user_by_date, sort_dates_by_count
from src import stream_tweets


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:    
    date_counter: TweetDateCounter = defaultdict(Counter)

    for tweet in stream_tweets(file_path):
        count_user_by_date(date_counter, tweet)

    top_dates = sort_dates_by_count(date_counter)
    result = find_top_user_by_date(top_dates)

    return result
