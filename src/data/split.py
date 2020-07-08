import random
from typing import List


def split_data(data: List, weights: List = (0.8, 0.2, 0.0)):
    split = {
        'train': [],
        'test': [],
        'validation': []
    }
    for word in data:
        subset = random.choices(['train', 'test', 'validation'], weights=weights)[0]
        split[subset].append(word)

    return split

