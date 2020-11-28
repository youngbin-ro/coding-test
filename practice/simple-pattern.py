def simple_pattern(n: int) -> int:
    for i in range(n, 0, -1):
        for j in range(n, n - i, -1):
            print(j, end='')
        print()


if __name__ == "__main__":
    n = 9
    simple_pattern(n)
