from collections import Counter
from typing import List, Tuple

from src.q2 import count_emoji
from src import stream_tweets


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter: Counter[str] = Counter()

    for tweet in stream_tweets(file_path):
        count_emoji(emoji_counter, tweet)

    top_emojis = emoji_counter.most_common(10)

    return top_emojis
