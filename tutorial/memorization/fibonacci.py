from functools import wraps
from time import perf_counter
import sys


def fibonacci(n) -> int:
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print("fff")
    start = perf_counter()
    f = fibonacci(35)
    end = perf_counter()

    print(f)
    print(f'time : {end- start} sec ')
