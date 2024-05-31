import json
from typing import Dict, Generator, List


def load_all_tweets(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line for line in file]


def stream_tweets(file_path: str) -> Generator[Dict, None, None]:
    with open(file_path, 'r') as file:
        for tweet in file:
            yield json.loads(tweet)
