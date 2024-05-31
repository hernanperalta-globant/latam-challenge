from collections import Counter
from typing import List, Tuple

from src import stream_tweets
from src.q3 import count_mention


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter: Counter[str] = Counter()

    for tweet in stream_tweets(file_path):
        count_mention(mention_counter, tweet)
    
    top_mentions = mention_counter.most_common(10)

    return top_mentions
