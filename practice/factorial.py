import math
from functools import reduce


def in_cache(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]

    return wrapper


@in_cache
def factorial1(n: int) -> int:
    answer = 1
    for i in range(1, n + 1):
        answer *= i
    return answer


def factorial2(n: int) -> int:
    return math.factorial(n)


def factorial3(n: int) -> int:
    return n * factorial3(n - 1) if n > 1 else 1


def factorial4(n: int) -> int:
    if n == 0:
        return 1
    return reduce(lambda x, y: x * y, range(1, n + 1))


def factorial5(n: int) -> int:
    if n == 0:
        return 1
    return eval('*'.join(str(i) for i in range(1, n + 1)))


if __name__ == "__main__":
    n_ = 10
    print(factorial1(n_))
    print(factorial2(n_))
    print(factorial3(n_))
    print(factorial4(n_))
    print(factorial5(n_))

    print(factorial1(n_))
    print(factorial1(n_))
    print(factorial1(n_))
