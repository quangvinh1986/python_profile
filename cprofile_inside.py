import cProfile
import functools
import pstats
import tempfile
import random
import math


def cprofile_me(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        file = tempfile.mktemp()
        profiler = cProfile.Profile()
        profiler.runcall(func, *args, **kwargs)
        profiler.dump_stats(file)
        metrics = pstats.Stats(file)
        metrics.strip_dirs().sort_stats('time').print_stats(100)
    return wraps


@cprofile_me
def run_function(function, numbers):
    for number in numbers:
        function(number)


def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True


def is_prime_sqrt(number):
    if number < 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for value in range(2, max_range):
        if number % value == 0:
            return False
    return True


if __name__ == "__main__":
    numbers = [80909548, 64284912, 32561271, 59635875, 43704113, 42511163, 7564624, 62719360, 29119365, 49141585]
    run_function(is_prime_basic, numbers)
    run_function(is_prime_sqrt, numbers)
