from operator import add
from typing import List


# Time Limit Exceeded
def first_solution(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    table = [[0] * len(nums)]
    max_val = max(nums)
    for length in range(1, len(nums) + 1):
        if length == 1:
            table.append(nums)
            continue
        table.append([])
        for idx, num in enumerate(nums):
            if idx + 1 < length:
                cur_val = None
            else:
                cur_val = table[length - 1][idx - 1] + num
            if cur_val is not None and cur_val > max_val:
                max_val = cur_val
            table[length].append(cur_val)

    return max_val


# Time Limit Exceeded
def second_solution(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    max_val = max(nums)
    cur_len_sums = nums.copy()
    for length in range(1, len(nums) + 1):
        cur_len_sums = list(map(add, nums[length:], cur_len_sums[:-1]))
        if not cur_len_sums:
            continue

        cur_max = max(cur_len_sums)
        if cur_max > max_val:
            max_val = cur_max

    return max_val


def third_solution(nums: List[int]) -> int:
    new = [nums[0]]
    for idx in range(1, len(nums)):
        new.append(max(new[idx - 1] + nums[idx], nums[idx]))
    return max(new)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(third_solution(nums))

    nums = [1]
    print(third_solution(nums))

    nums = [0]
    print(third_solution(nums))

    nums = [-1]
    print(third_solution(nums))

    nums = [-2147483647]
    print(third_solution(nums))
