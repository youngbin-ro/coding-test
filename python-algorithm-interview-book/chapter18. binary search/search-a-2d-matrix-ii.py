from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return True
    return False


if __name__ == "__main__":
    matrix_ = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target_ = 23
    print(searchMatrix(matrix_, target_))

    target_ = 20
    print(searchMatrix(matrix_, target_))
