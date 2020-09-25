def first_solution(nums):
    results = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
    return results


def second_solution(nums):
    results = []
    nums.sort()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if cur_sum < 0:
                left += 1
            elif cur_sum > 0:
                right -= 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return results


if __name__ == "__main__":
    input1 = [-1, 0, 1, 2, -1, -4]
    print(second_solution(input1))

    input2 = []
    print(second_solution(input2))


"""
Findings
- 투 포인터 기법은 정렬된 배열 및 리스트에서 더 유용함
- 정렬 시 원본 배열의 인덱스가 달라지므로 주의
"""
