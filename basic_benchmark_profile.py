import random
import math
import timeit


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


def random_all_array(length):
    arr = []
    for _ in range(length):
        arr.append(random.randint(1, 10**8))
    return arr


def benchmark_function(function, params):
    start = timeit.default_timer()
    result = function(params)
    end = timeit.default_timer()
    print("{0} - params: {1} #Result: {2} #Total time: {3}(second)".format(function.__name__, params, result, (end - start)))


if __name__ == "__main__":
    number = random.randint(1, 10**8)
    benchmark_function(is_prime_basic, number)
    benchmark_function(is_prime_sqrt, number)
    benchmark_function(is_prime_optimal, number)
