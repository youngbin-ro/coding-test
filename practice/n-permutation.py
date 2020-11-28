from typing import List


def permutation(nums: List[int]) -> List[List[int]]:
    if len(nums) <= 1:
        return [nums]

    answer = []
    for idx in range(len(nums)):
        rest = nums[:idx] + nums[idx + 1:]
        for permuted in permutation(rest):
            answer.append([nums[idx]] + permuted)

    return answer


if __name__ == "__main__":
    nums_ = [5, 2]
    print(permutation(nums_))
