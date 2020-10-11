import heapq
from typing import List


def first_solution(nums: List[int], k: int) -> int:
    for idx in range(len(nums)):
        nums[idx] *= -1
    heapq.heapify(nums)
    for _ in range(k):
        answer = heapq.heappop(nums)
    return -answer


def second_solution(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]


if __name__ == "__main__":
    nums, k = [3, 2, 1, 5, 6, 4], 2
    print(second_solution(nums, k))

    nums, k = [3, 2, 3, 1, 2, 4, 5, 5, 6], 4
    print(second_solution(nums, k))
