def jumpingOnClouds(c):
    count, idx = 0, 0
    while idx < len(c) - 1:
        if idx + 2 < len(c) and c[idx + 2] == 0:
            idx = idx + 2
        elif idx + 1 < len(c) and c[idx + 1] == 0:
            idx += 1
        count += 1
    return count


if __name__ == "__main__":
    c_ = [0, 0, 1, 0, 0, 1, 0]
    print(jumpingOnClouds(c_))
    print('------------------------')

    c_ = [0, 0, 0, 0, 1, 0]
    print(jumpingOnClouds(c_))
