# slowsort

One of the slowest sorting algorithms has been brought to Python.

- Supports Python 2.7+ and Python 3.5+
- 100% code coverage
- Thoroughly tested using [Hypothesis](https://github.com/HypothesisWorks/hypothesis)
- Continuous integration with CircleCI
- Uses Poetry for dependencies
- Uses tox with py.test
- Uses Black for formatting
- Uses isort for consistent imports
- Flake8 makes sure we don't mess up
- The Unlicense because I don't care

## Installation

    $ pip install slowsort

## Usage

```pycon
>>> from slowsort import slowsort
>>> my_values = [3, 1, 5, 4]
>>> slowsort(my_values)  # wait for it...
>>> print(my_values)
[1, 3, 4, 5]
```

## Documentation

The sorting is done destructively. There are currently no plans to implement a
non-destructive version.

I have no idea if the algorithm is stable, I just took it from Wikipedia. 

## License

- [The Unlicense](https://unlicense.org/)
