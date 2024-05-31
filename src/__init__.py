import json
from multiprocessing import Pool, cpu_count
from typing import Callable, Dict, Generator, List, TypeVar


T = TypeVar('T')


def load_all_tweets(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line for line in file]


def stream_tweets(file_path: str) -> Generator[Dict, None, None]:
    with open(file_path, 'r') as file:
        for tweet in file:
            yield json.loads(tweet)


def multiprocess_tweets(file_path: str, process_tweets: Callable[[List[str]], T]) -> List[T]:
    tweets = load_all_tweets(file_path)
    num_workers = cpu_count()
    batch_size = len(tweets) // num_workers

    with Pool(num_workers) as pool:
        batch = [tweets[i:i + batch_size] for i in range(0, len(tweets), batch_size)]
        results = pool.map(process_tweets, batch)
    
    return results


__all__ = [
    "load_all_tweets",
    "stream_tweets",
    "multiprocess_tweets"
]