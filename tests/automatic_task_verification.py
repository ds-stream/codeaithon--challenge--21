import os
import pytest
import random
import time
from pathlib import Path
from tqdm import tqdm


def test_submission_files_exist(developer):
    base_path = f"submissions/developer-{developer}"
    folders = ["tests", "results"]

    for folder in folders:
        assert os.path.exists(
            os.path.join(base_path, folder)
        ), f"{folder.capitalize()} directory does not exist"

        files = os.listdir(os.path.join(base_path, folder))
        assert len(files) > 0, f"No {folder} files found"


# correctness
TEST_TIMEOUT = 10 * 60  # 10 minutes


# --------------- reference implementation --------------------- #
def reference_is_prime(n: int) -> bool:
    """Check if a number is prime - this is a reference implementation."""
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


def test_edge_conditions(solution):
    """Test edge conditions."""
    assert not solution.is_prime(1), "1 is not a prime number"
    assert solution.is_prime(2), "2 is a prime number"
    assert solution.is_prime(3), "3 is a prime number"
    assert not solution.is_prime(4), "4 is not a prime number"
    assert solution.is_prime(5), "5 is a prime number"
    assert solution.is_prime(13), "13 is a prime number"
    assert not solution.is_prime(99_987), "99,987 is not a prime number"
    assert solution.is_prime(99_989), "99,989 is a prime number"
    assert solution.is_prime(99_991), "99,991 is a prime number"
    assert not solution.is_prime(100_000), "100,000 is not a prime number"


def test_results_in_finite_time(solution):
    """Test that the solution runs in finite time."""
    start = time.time()

    with tqdm(total=250) as bar:
        for _ in range(250):
            n = random.randint(1, 100_000)
            assert solution.is_prime(n) is reference_is_prime(
                n
            ), f"Result for {n} is incorrect"

            if time.time() - start > TEST_TIMEOUT:
                raise RuntimeError(
                    "Execution time exceeded. Your implementation is too slow!"
                )

            bar.update(1)


def test_not_using_forbidden_instructions(code):
    assert "for" not in code, "Used forbidden instruction: `for`"
    assert "while" not in code, "Used forbidden instruction: `while`"
    assert "filter" not in code, "Used forbidden instruction: `filter`"


def test_check_initial_conditions(solution):
    with pytest.raises(ValueError):
        solution.is_prime(0)

    with pytest.raises(ValueError):
        solution.is_prime(100_001)

    assert not solution.is_prime(1)
