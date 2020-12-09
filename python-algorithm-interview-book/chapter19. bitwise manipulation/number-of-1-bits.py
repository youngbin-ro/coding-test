def hammingWeight1(n: int) -> int:
    return sum(map(int, list(str(bin(n)))[2:]))


def hammingWeight2(n: int) -> int:
    return bin(n).count('1')


def hammingWeight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


if __name__ == "__main__":
    n_ = 0b00000000000000000000000000001011
    print(hammingWeight(n_))

    n_ = 0b00000000000000000000000010000000
    print(hammingWeight(n_))

    n_ = 0b11111111111111111111111111111101
    print(hammingWeight(n_))
