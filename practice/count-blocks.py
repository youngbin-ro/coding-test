def count_blocks(arr):
    for idx, row in enumerate(arr.copy()):
        arr[idx] = list(row)

    def dfs(i, j, char):
        if i < 0 or i >= len(arr) or j < 0 or j >= len(arr[0]):
            return
        if arr[i][j] == ' ':
            return
        if arr[i][j] != char:
            return

        arr[i][j] = ' '
        dfs(i, j + 1, char)
        dfs(i, j - 1, char)
        dfs(i + 1, j, char)
        dfs(i - 1, j, char)

    count = 0
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == ' ':
                continue
            else:
                dfs(row, col, arr[row][col])
                count += 1

    return count


if __name__ == "__main__":
    arr_ = [
        'aaaba',
        'ababa',
        'aaaca'
    ]
    print(count_blocks(arr_))
