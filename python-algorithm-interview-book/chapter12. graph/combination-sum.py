def first_solution(candidates: list, target: int) -> list:
    result = []
    candidates.sort()

    def dfs(combination, nums, k):
        if k == 0:
            result.append(combination[:])
            return

        for idx in range(len(nums)):
            if nums[idx] <= k:
                combination.append(nums[idx])
            else:
                break
            dfs(combination, nums[idx:], k - nums[idx])
            combination.pop()

    dfs([], candidates, target)
    return result


def second_solution(candidates: list, target: int) -> list:
    result = []

    def dfs(csum, index, path):
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result


if __name__ == "__main__":
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    print(second_solution(candidates1, target1))

    candidates2 = [2, 3, 5]
    target2 = 8
    print(second_solution(candidates2, target2))

    candidates3 = [2]
    target3 = 1
    print(second_solution(candidates3, target3))

    candidates4 = [1]
    target4 = 1
    print(second_solution(candidates4, target4))

    candidates5 = [1]
    target5 = 2
    print(second_solution(candidates5, target5))
