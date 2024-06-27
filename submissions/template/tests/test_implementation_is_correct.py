import random
import time
from pathlib import Path

import pytest
from tqdm import tqdm

from results.solution import is_prime

TEST_TIMEOUT = 10 * 60  # 10 minutes


# --------------- reference implementation --------------------- #


def reference_is_prime(n: int) -> bool:
    # source: https://stackoverflow.com/a/46844461/3081328
    if n == 1 or n & 1 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 2
    return True


# -------------------------------------------------------------- #


def test_edge_conditions():
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert is_prime(13)
    assert not is_prime(99_987)
    assert is_prime(99_989)
    assert is_prime(99_991)
    assert not is_prime(100_000)


def test_results_in_finite_time():
    start = time.time()

    with tqdm(total=250) as bar:
        for _ in range(250):
            n = random.randint(1, 100_000)
            assert is_prime(n) is reference_is_prime(n), f"Result for {n} is incorrect"

            if time.time() - start > TEST_TIMEOUT:
                raise RuntimeError("Execution time exceeded. Your implementation is too slow!")

            bar.update(1)


if __name__ == "__main__":
    test_edge_conditions()
    test_results_in_finite_time()
