def is_prime(n: int) -> bool:
    """Check if the given number is a prime number.

    Args:
        n (int): The positive integer number in range [1, 100_000] to be checked if it's prime.

    Returns:
        bool: True if `n` is a prime number, False otherwise.
    """
    if not isinstance(n, int) or not 1 <= n <= 100_000:
        raise ValueError(f"The input number is incorrect: {n}, expected integer in range [1, 100_000]")

    # all code (functions, classes, variables, etc.) has to be implemented within this file
    # you can NOT change the function name   (it has to remain `is_prime`)
    # you can NOT use the `for` loop         (tests are checking against `for` phrase)
    # you can NOT use the `while` loop       (tests are checking against `while` phrase)
    # you can NOT use the `filter` function  (tests are checking against `filter` phrase)

    ### PUT YOUR CODE HERE

    return
