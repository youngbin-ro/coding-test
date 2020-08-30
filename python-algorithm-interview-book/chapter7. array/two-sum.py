def first_solution(nums, target):
    for idx1 in range(len(nums) - 1):
        for idx2 in range(idx1 + 1, len(nums)):
            if nums[idx1] + nums[idx2] == target:
                return [idx1, idx2]


def second_solution(nums, target):
    for idx1, num in enumerate(nums):
        try:
            idx2 = nums[idx1 + 1:].index(target - num)
        except ValueError:
            continue
        return [idx1, idx1 + idx2 + 1]


def third_solution(nums, target):
    nums_dict = {}
    for idx, num in enumerate(nums):
        if target - num in nums_dict:
            return [nums_dict[target - num], idx]
        nums_dict[num] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(third_solution(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(third_solution(nums, target))

    nums = [3, 3]
    target = 6
    print(third_solution(nums, target))


"""
Findings
- 만약 nums가 정렬되어 있다면 투 포인터 방식으로 빠르게 풀이 가능
- dictionary를 잘 활용하자
"""
