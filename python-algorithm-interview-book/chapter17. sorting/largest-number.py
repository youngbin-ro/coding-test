import collections, itertools
from typing import List


# incorrect
def first_solution(nums: List[int]) -> str:
    nums.sort(key=lambda x: str(x), reverse=True)
    print(nums)
    for idx, num in enumerate(nums[:-1]):
        if len(str(num)) == 1:
            continue
        origin = int(str(num) + str(nums[idx + 1]))
        compare = int(str(nums[idx + 1]) + str(num))
        if origin < compare:
            nums[idx], nums[idx + 1] = nums[idx + 1], nums[idx]

    result = ''.join(map(str, nums))
    return '0' if int(result) == 0 else result


# incorrect
def second_solution(nums: List[int]) -> str:
    nums.sort(key=lambda x: str(x)[0], reverse=True)
    print(nums)

    def sort(numbers):
        if len(numbers) == 1:
            return str(numbers[0])

        if len(numbers) == 2:
            a, b = numbers
            ab = int(str(a) + str(b))
            ba = int(str(b) + str(a))
            if ab > ba:
                return str(a) + str(b)
            else:
                return str(b) + str(a)

        div1 = numbers[:len(numbers) // 2]
        div2 = numbers[len(numbers) // 2:]
        return sort(div1) + sort(div2)

    result = sort(nums)
    return '0' if int(result) == 0 else result


# incorrect
def third_solution(nums: List[int]) -> str:
    dic = collections.defaultdict(list)
    for num in nums:
        dic[int(str(num)[0])].append(str(num))

    result = ''
    for i in reversed(range(10)):
        if not dic[i]:
            continue
        permutes = itertools.permutations(dic[i], len(dic[i]))
        max_val, max_idx = -1, 0
        max_permute = None
        for idx, permute in enumerate(permutes):
            cur_val = int(''.join(permute))
            if cur_val > max_val:
                max_val, max_idx = cur_val, idx
                max_permute = permute
        result += ''.join(max_permute)
    return ''.join(result)


def fourth_solution(nums: List[int]) -> str:

    def need_swap(a, b):
        return int(str(a) + str(b)) < int(str(b) + str(a))

    i = 1
    while i < len(nums):
        j = i
        while j > 0 and need_swap(nums[j - 1], nums[j]):
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
        i += 1

    return str(int(''.join(map(str, nums))))


if __name__ == "__main__":
    nums = [10, 2]
    print(fourth_solution(nums))

    nums = [3, 30, 34, 5, 9]
    print(fourth_solution(nums))

    nums = [7543,5328,9834,1940,9387,871,5208,7,543]
    print(fourth_solution(nums))
