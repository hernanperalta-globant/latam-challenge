from collections import Counter
from typing import List, Tuple

from src.q2.utils import extract_emojis
from src.utils import stream_tweets


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()

    for tweet in stream_tweets(file_path):
        emojis = extract_emojis(tweet['content'])
        emoji_counter.update(emojis)

    return emoji_counter.most_common(10)
