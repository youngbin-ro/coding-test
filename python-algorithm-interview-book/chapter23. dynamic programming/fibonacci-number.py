def fib(N: int) -> int:
    dp = [0] * (N + 1)
    if N > 0:
        dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[N]


if __name__ == "__main__":
    print(fib(2))
    print(fib(3))
    print(fib(4))
