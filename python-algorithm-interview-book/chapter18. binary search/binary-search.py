import bisect
from typing import List


class Solution:
    def search1(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        prev_mid = None
        while left <= right:

            # check each end is target
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            # check search span
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid

            # check breaking point
            if prev_mid is not None and prev_mid == mid:
                break
            prev_mid = mid

        return -1

    def search2(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid + 1
            elif nums[mid] < target:
                left = mid - 1
            else:
                return mid

        return -1

    def search3(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)

    def search4(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def search5(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1


if __name__ == "__main__":
    solver = Solution()

    nums_, target_ = [-1, 0, 3, 5, 9, 12], 9
    print(solver.search4(nums_, target_))    # answer = 4

    nums_, target_ = [-1, 0, 3, 5, 9, 12], 2
    print(solver.search4(nums_, target_))    # answer = -1
