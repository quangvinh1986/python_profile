import random
import math
import timeit


def benchmark_me():
    def decorator(function):
        def wraps(*args, **kwargs):
            start = timeit.default_timer()
            result = function(*args, **kwargs)
            end = timeit.default_timer()
            print("{0} - params: {1} {2} #Result: {3} #Total time: {4}(second)".format(function.__name__, str(*args), str(*kwargs) , result, (end - start)))
            return result
        return wraps
    return decorator


@benchmark_me()
def is_prime_basic(number):
    if number < 2:
        return False
    for value in range(2, number):
        if number % value == 0:
            return False
    return True


@benchmark_me()
def is_prime_sqrt(number):
    if number < 2:
        return False
    max_range = int(math.sqrt(number)) + 1
    for value in range(2, max_range):
        if number % value == 0:
            return False
    return True


@benchmark_me()
def is_prime_optimal(number):
    if number in [2, 3, 5]:
        return True
    if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number < 2: 
        return False
    if number < 49:
        return True
    if (number %  7) == 0 or (number % 11) == 0 or (number % 13) == 0 or (number % 17) == 0 or \
       (number % 19) == 0 or (number % 23) == 0 or (number % 29) == 0 or (number % 31) == 0 or \
       (number % 37) == 0 or (number % 41) == 0 or (number % 43) == 0 or (number % 47) == 0:
        return False
    
    if number < 2809:
        return True
    
    max_range = int(math.sqrt(number)) + 1
    for value in range(53, max_range, 2):
        if number % value == 0:
            return False
    return True


if __name__ == "__main__":
    number = random.randint(1, 10**8)
    is_prime_basic(number)
    is_prime_sqrt(number)
    is_prime_sqrt(number)
