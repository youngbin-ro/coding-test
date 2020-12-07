def hammingDistance1(x: int, y: int) -> int:
    x_bin, y_bin = bin(x)[2:], bin(y)[2:]
    max_len = max(len(x_bin), len(y_bin))
    x_bin = (max_len - len(x_bin)) * '0' + x_bin
    y_bin = (max_len - len(y_bin)) * '0' + y_bin
    return sum([x_bit != y_bit for x_bit, y_bit in zip(x_bin, y_bin)])


def hammingDistance(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


if __name__ == "__main__":
    x_, y_ = 12, 7
    print(hammingDistance(x_, y_))
