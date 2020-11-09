from typing import List
from collections import OrderedDict


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp.popitem()[1]


if __name__ == "__main__":
    solver = Solution()
    nums = [1, 2, 3, 1]
    print(solver.rob(nums))

    nums = [2, 7, 9, 3, 1]
    print(solver.rob(nums))

    nums = [2, 1, 1, 2]
    print(solver.rob(nums))
