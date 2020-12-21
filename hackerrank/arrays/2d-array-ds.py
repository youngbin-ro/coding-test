import sys


def hourglassSum(arr):

    def hourglass(i, j):
        answer = 0
        for row_ in range(i - 1, i + 2):
            for col_ in range(j - 1, j + 2):
                if row_ == i and col_ != j:
                    continue
                answer += arr[row_][col_]
        return answer

    max_sum = -sys.maxsize
    for row in range(1, 5):
        for col in range(1, 5):
            max_sum = max(max_sum, hourglass(row, col))
    return max_sum


if __name__ == "__main__":
    arr_ = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]
    print(hourglassSum(arr_))
