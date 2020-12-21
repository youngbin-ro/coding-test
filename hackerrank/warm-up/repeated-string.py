def repeatedString(s, n):
    count = 0
    rest_count = 0
    rest = n % len(s)
    for idx, char in enumerate(s):
        if char == 'a':
            count += 1
            if idx <= rest - 1:
                rest_count += 1

    return count * (n // len(s)) + rest_count


if __name__ == "__main__":
    s_, n_ = 'aba', 10
    print(repeatedString(s_, n_))
    print('----------------------')

    s_, n_ = 'a', 1000000000000
    print(repeatedString(s_, n_))
