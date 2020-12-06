from typing import List


def twoSum1(numbers: List[int], target: int) -> List[int]:

    def binary_search(nums, tgt):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < tgt:
                left = mid + 1
            elif nums[mid] > tgt:
                right = mid - 1
            else:
                return mid
        return -1

    for idx1, num in enumerate(numbers):
        res = target - num
        idx2 = binary_search(numbers, res)
        if idx2 != -1 and idx1 != idx2:
            return [min(idx1, idx2) + 1, max(idx1, idx2) + 1]


def twoSum(numbers: List[int], target: int) -> List[int]:
    p1, p2 = 0, len(numbers) - 1
    while p1 <= p2:
        sum_ = numbers[p1] + numbers[p2]
        if sum_ == target:
            return [p1 + 1, p2 + 1]
        elif sum_ < target:
            p1 += 1
        else:
            p2 -= 1


if __name__ == "__main__":
    numbers_ = [2, 7, 11, 15]
    target_ = 9
    print(twoSum(numbers_, target_))
    print("-----------------")

    numbers_ = [2, 3, 4]
    target_ = 6
    print(twoSum(numbers_, target_))
    print("-----------------")

    numbers_ = [-1, 0]
    target_ = -1
    print(twoSum(numbers_, target_))
