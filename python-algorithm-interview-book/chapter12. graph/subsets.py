import collections


def first_solution1(nums: list) -> list:
    result = [[]]
    queue = collections.deque()
    queue.append(nums[0])


def first_solution(nums: list) -> list:
    result = []

    def dfs(subset, candidates):
        result.append(subset[:])
        if not candidates:
            return

        for idx in range(len(candidates)):
            subset.append(candidates[idx])
            dfs(subset, candidates[idx + 1:])
            subset.pop()

    dfs([], nums)
    return result


def second_solution(nums: list) -> list:
    result = []

    def dfs(index, path):
        result.append(path)

        for i in range(index, len(nums)):
            dfs(i + 1, path + [nums[i]])

    dfs(0, [])
    return result


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    print(second_solution(nums1))
