import random
import string

import numpy as np

RANGE_OFFSET: tuple[float, float] = (0.95, 1)


def pick_random_weighted_time(mini: float, maxi: float) -> float:
    if mini == 0:
        return 0

    def pick_decreasing_random_in_range(mini: float, maxi: float) -> list[float]:
        steps: list[float] = [round(time, 3) for time in np.arange(mini, maxi, 0.05)]
        numbers = random.choices(steps, [1 / (step**2) for step in steps], k=1)
        return numbers

    wait_time = pick_decreasing_random_in_range(mini, maxi)[0]
    return random.uniform(wait_time, wait_time * 1.05)


def multiply_offset(range: tuple[float, float] = RANGE_OFFSET):
    return random.uniform(*range)


def get_random_id(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
