def countingValleys(steps, path):
    level, count = 0, 0
    for hill in path:
        if hill == 'D':
            level -= 1
        elif hill == 'U':
            level += 1
        if level == 0 and hill == 'U':
            count += 1
    return count


if __name__ == "__main__":
    steps_ = 8
    path_ = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']
    print(countingValleys(steps_, path_))
    print('-------------------')

    steps_ = 8
    path_ = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
    print(countingValleys(steps_, path_))
