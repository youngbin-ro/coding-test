from typing import List


def first_solution(nums: List[int]) -> None:
    nums.sort()
    print(nums)


def second_solution(nums: List[int]) -> None:
    red, white, blue = 0, 0, len(nums)

    while white < blue:
        if nums[white] < 1:
            nums[red], nums[white] = nums[white], nums[red]
            red += 1
            white += 1
        elif nums[white] > 1:
            blue -= 1
            nums[white], nums[blue] = nums[blue], nums[white]
        else:
            white += 1

    print(nums)


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    second_solution(nums)

    nums = [2, 0, 1]
    second_solution(nums)

    nums = [0]
    second_solution(nums)

    nums = [1]
    second_solution(nums)
