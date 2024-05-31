from typing import List, Tuple
from datetime import datetime
from collections import defaultdict, Counter
import json

from q1.utils import count_tweet, find_top_user_by_date, sort_dates_by_count


def read_tweets(file_path: str):
    """TODO Document that each line is a tweet."""

    with open(file_path, 'r') as file:
        for tweet in file:
            yield json.loads(tweet)


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:    
    date_count = defaultdict(Counter)

    for tweet in read_tweets(file_path):
        count_tweet(date_count, tweet)

    top_dates = sort_dates_by_count(date_count)
    result = find_top_user_by_date(top_dates)

    return result
