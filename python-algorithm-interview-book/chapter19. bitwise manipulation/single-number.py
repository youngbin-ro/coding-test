from typing import List
from collections import defaultdict


def singleNumber1(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    counts = defaultdict(int)
    for num in nums:
        counts[num] += 1

    return sorted(counts.items(), key=lambda x: x[1])[0][0]


def singleNumber(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
        print(result)


if __name__ == "__main__":
    nums_ = [2, 2, 1]
    print(singleNumber(nums_))
    print('---------------------')

    nums_ = [4, 1, 2, 1, 2]
    print(singleNumber(nums_))
    print('---------------------')

    nums_ = [4, 1, 2, 1, 4, 2, 3]
    print(singleNumber(nums_))
    print('---------------------')

    nums_ = [1]
    print(singleNumber(nums_))
