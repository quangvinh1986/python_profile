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


def run_basic_function(number):
    start = timeit.default_timer()
    result = is_prime_basic(number)
    stop = timeit.default_timer()
    print("Basic-function {0}: {1}: {2}(second)".format(number, result, (stop - start)))
    return stop - start


def run_sqrt_function(number):
    start = timeit.default_timer()
    result = is_prime_sqrt(number)
    stop = timeit.default_timer()
    print("Sqrt-function {0}: {1}: {2}(second)".format(number, result, (stop - start)))
    return stop - start    


def run_optimal_function(number):
    start = timeit.default_timer()
    result = is_prime_optimal(number)
    stop = timeit.default_timer()
    print("Optimal-function {0}: {1}: {2}(second)".format(number, result, (stop - start)))
    return stop - start


if __name__ == "__main__":
    number = random.randint(1, 10**8)
    run_basic_function(number)
    run_sqrt_function(number)
    run_optimal_function(number)
