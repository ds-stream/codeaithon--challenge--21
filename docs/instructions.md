# Task 21: Checking prime number

## Short description

The goal of the current task is to implement an algorithm, that checks if the given integer number
is prime or not.

Sounds easy, right? That's why few requirements for the algorithm were added:

- it must be implemented in Python
- it must NOT contain `for` loops
- it must NOT contain `while` loops
- it must NOT contain `filter` function

Now, it sounds more like fun, isn't it? 😉

> Important note
>
> The solution code is tested against specific phrases like: "for", "while", "filter".  
> Thus, those phrases should not be used as a part of code at all, especially variable names, strings, etc.  
> The only exception is for the lines starting as comments.

## Solution development

All the code should be put inside the given function template `is_prime` from the `solution.py` module.

Please replace `### PUT YOUR CODE HERE` with the final implementation

The code should be executable, as there are implemented some unit tests, that will be running
against implemented method.

### Testing implementation

It is recommended to provide additional test functions to check the implementation correctness.
User-defined tests should be put inside the `tests` module.

Existing tests may be used to verify the implementation locally, simply by running:

```shell
python tests/test_implementation_is_correct.py
python tests/test_implementation_meets_requirements.py
# or with pytest module
pytest -vvv .
```

All the tests from `tests` module would be used for automatic code verification.

> Important note:
>
> Existing tests can NOT be removed. It is also forbidden to change the tests behavior, except to solve the import-related issues.
