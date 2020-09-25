def first_solution(nums):
    nums.sort()
    result = 0
    if len(nums) % 2 == 0:
        for i in range(0, len(nums) - 1, 2):
            result += nums[i]
    else:
        for i in range(1, len(nums) - 1, 2):
            result += nums[i]
    return result


def second_solution(nums):
    nums.sort()
    result = 0
    for i, num in enumerate(nums):
        if i % 2 == 0:
            result += num
    return result


def third_solution(nums):
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    input1 = [1, 4, 3, 2]
    print(third_solution(input1))


"""
Findings
- 리스트 정렬 시 sort() 외 sorted()도 고려
- 짝수 인덱싱 시 [::2] 사용
"""