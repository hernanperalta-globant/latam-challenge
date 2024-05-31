import re
from typing import List


def extract_emojis(text: str) -> List[str]:
    emoji_pattern = re.compile(
        r'['
        r'\U0001F600-\U0001F64F'  # emoticons
        r'\U0001F300-\U0001F5FF'  # symbols & pictographs
        r'\U0001F680-\U0001F6FF'  # transport & map symbols
        r'\U0001F1E0-\U0001F1FF'  # flags (iOS)
        r'\U00002702-\U000027B0'  # dingbats
        r'\U000024C2-\U0001F251' 
        r']+',
        flags=re.UNICODE
    )

    return emoji_pattern.findall(text)
