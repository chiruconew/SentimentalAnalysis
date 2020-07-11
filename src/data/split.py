import math
import random
from typing import Dict, List, Tuple


def split_data(data: List[str], weights: Tuple = (0.8, 0.2, 0.0), seed: int = 100) -> Dict:
    split = {}

    new_data = data.copy()

    random.seed(seed)
    random.shuffle(new_data)

    total_words = len(new_data)
    train_limit = math.floor(total_words * weights[0])
    test_limit = math.floor(total_words * weights[1] + total_words * weights[0])

    split['train'] = new_data[:train_limit]
    split['test'] = new_data[train_limit:test_limit]
    split['validation'] = new_data[test_limit:]

    return split
