from pathlib import Path

import pytest

from results.solution import is_prime


def get_code() -> str:
    solutions_file = Path(__file__).parent.parent / "results" / "solution.py"
    data = solutions_file.read_text().split("\n")
    return "".join(line for line in data if not line.strip() or not line.strip().startswith("#"))


def test_not_using_forbidden_instructions():
    assert "for" not in get_code(), "Used forbidden instruction: `for`"
    assert "while" not in get_code(), "Used forbidden instruction: `while`"
    assert "filter" not in get_code(), "Used forbidden instruction: `filter`"


def test_check_initial_conditions():
    with pytest.raises(ValueError):
        is_prime(0)

    with pytest.raises(ValueError):
        is_prime(100_001)

    assert not is_prime(1)


if __name__ == "__main__":
    test_not_using_forbidden_instructions()
    test_check_initial_conditions()
