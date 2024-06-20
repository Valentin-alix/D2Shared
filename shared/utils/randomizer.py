import random
import string
from time import sleep

import numpy as np

PAUSE: float = 0.05
RANGE_DURATION_ACTIVITY: tuple[float, float] = (0.6, 1.4)
RANGE_NEW_MAP: tuple[float, float] = (0.5, 6)
RANGE_OFFSET: tuple[float, float] = (0.95, 1)
RANGE_WAIT: tuple[float, float] = (0.3, 0.7)


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


def wait(range: tuple[float, float] = RANGE_WAIT):
    time = pick_random_weighted_time(*range)
    sleep(time)


def get_random_id(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
