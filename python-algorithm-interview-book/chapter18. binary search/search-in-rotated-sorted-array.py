from typing import List


def search1(nums: List[int], target: int) -> int:
    try:
        return nums.index(target)
    except ValueError:
        return -1


def search(nums: List[int], target: int) -> int:
    if len(nums) == 1:
        return 0 if target in nums else -1

    def binary_search(nums__, target__):
        left = 0
        right = len(nums__) - 1
        while left <= right:
            mid = (left + right + 1) // 2
            if nums__[mid] < target__:
                left = mid + 1
            elif nums__[mid] > target__:
                right = mid - 1
            else:
                return mid
        return -1

    pivot = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            pivot = i
            break

    if pivot is None:
        return binary_search(nums, target)

    if nums[0] < target:
        searched = binary_search(nums[1:pivot + 1], target)
        return 1 + searched if searched != -1 else -1
    elif nums[0] > target:
        searched = binary_search(nums[pivot + 1:], target)
        return 1 + searched + pivot if searched != -1 else -1
    else:
        return 0


if __name__ == "__main__":
    nums_ = [7, 8, 10, 2, 5]
    target_ = 3
    print(search(nums_, target_))  # output: 4

    nums_ = [4, 5, 6, 7, 0, 1, 2]
    target_ = 0
    print(search(nums_, target_))    # output: 4

    nums_ = [4, 5, 6, 7, 0, 1, 2]
    target_ = 3
    print(search(nums_, target_))    # output: -1

    nums_ = [1]
    target_ = 0
    print(search(nums_, target_))    # output: -1

    nums_ = [3, 1]
    target_ = 3
    print(search(nums_, target_))  # output: 0

    nums_ = [3, 5, 1]
    target_ = 5
    print(search(nums_, target_))  # output: 1
