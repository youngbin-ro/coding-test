def in_cache(func):
    memo = {}

    def wrapper(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = func(n)
            return memo[n]

    return wrapper


def fib_recur(n):
    if n <= 2:
        return 1
    return fib_recur(n - 1) + fib_recur(n - 2)


@in_cache
def fib_dp(n):
    memo = [0] * n
    memo[0], memo[1] = 1, 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo


def fib_iter(n):
    prev, cur = 1, 1
    for i in range(n - 2):
        prev, cur = cur, prev + cur
    return cur


if __name__ == "__main__":
    print(fib_dp(10))
    print(fib_dp(9))
    print(fib_dp(10))
