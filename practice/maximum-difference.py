def findMaxDiff(arr):
    max_diff = 0
    for mid in range(len(arr)):
        left = mid - 1
        right = mid + 1
        ls, rs = 0, 0

        while left >= 0:
            if arr[left] < arr[mid]:
                ls = arr[left]
                break
            left -= 1

        while right < len(arr):
            if arr[right] < arr[mid]:
                rs = arr[right]
                break
            right += 1

        max_diff = max(max_diff, abs(ls - rs))

    return max_diff


if __name__ == "__main__":
    arr_ = [2, 1, 8]
    print(findMaxDiff(arr_))
    print('-------------------------')

    arr_ = [2, 4, 8, 7, 7, 9, 3]
    print(findMaxDiff(arr_))
