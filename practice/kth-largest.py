import numpy as np
from typing import List


def kth_largest(nums: List[int], k) -> int:
    nums = list(set(nums))
    pivot = nums[len(nums) // 2]
    lower, equal, higher = [], [], []
    for num in nums:
        if num < pivot:
            lower.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            higher.append(num)

    if len(higher) == k - 1:
        return equal[0]
    elif len(higher) < k - 1:
        return kth_largest(lower, k - len(higher) - len(equal))
    else:
        return kth_largest(higher, k)


if __name__ == "__main__":
    nums = np.random.randint(0, 100, size=20).tolist()

    nums_copy = list(set(nums)).copy()
    nums_copy.sort()
    print(nums_copy[-4])

    k = 4
    print(kth_largest(nums, k))
