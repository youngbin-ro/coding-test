def first_solution(nums):
    to_right, to_left, result = [1], [1], []
    for i in range(len(nums) - 1):
        to_right.append(nums[i] * to_right[i])
        to_left.insert(0, nums[-i - 1] * to_left[0])
    for i in range(len(nums)):
        result.append(to_right[i] * to_left[i])
    return result


def second_solution(nums):
    result = []
    prod = 1
    for i in range(len(nums)):
        result.append(prod)
        prod *= nums[i]
    prod = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= prod
        prod *= nums[i]
    return result


if __name__ == "__main__":
    input1 = [1, 2, 3, 4]
    print(second_solution(input1))
