import itertools


def first_solution(nums):
    def dfs(index, path):
        if len(path) == len(nums):
            results.append(path)
            return

        for i in range(index, len(nums)):
            for num in nums:
                if num not in path:
                    dfs(i + 1, path + [num])
    if not nums:
        return []
    results = []
    dfs(0, [])
    return results


def second_solution(nums):
    def dfs(elements):
        if len(elements) == 0:
            results.append(prev_elements[:])
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    results = []
    prev_elements = []
    dfs(nums)
    return results


def third_solution(nums):
    return list(itertools.permutations(nums))


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    print(third_solution(nums1))
