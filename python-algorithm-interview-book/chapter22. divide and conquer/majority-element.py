from typing import List
from collections import Counter


def first_solution(nums: List[int]) -> int:
    return Counter(nums).most_common(1)[0][0]


def second_solution(nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = second_solution(nums[:half])
    b = second_solution(nums[half:])
    return [b, a][nums.count(a) > half]


if __name__ == "__main__":
    nums = [3, 2, 3]
    print(second_solution(nums))

    nums = [2, 2, 1, 1, 1, 2, 2]
    print(second_solution(nums))


