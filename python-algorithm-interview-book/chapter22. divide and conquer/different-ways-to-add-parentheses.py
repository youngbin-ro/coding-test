from typing import List


def first_solution(input: str) -> List[int]:

    def is_integer(string):
        if '+' in string:
            return False
        elif '-' in string:
            return False
        elif '*' in string:
            return False
        return True

    if is_integer(input):
        return [int(input)]

    def aggregate(num1s, num2s, operator):
        aggregated = []
        for num1 in num1s:
            for num2 in num2s:
                if operator == '+':
                    cur_num = num1 + num2
                elif operator == '-':
                    cur_num = num1 - num2
                else:
                    cur_num = num1 * num2
                aggregated.append(cur_num)
        return aggregated

    results = []
    for idx, char in enumerate(input):
        if char in ['+', '-', '*']:
            lefts = first_solution(input[:idx])
            rights = first_solution(input[idx + 1:])
            results += aggregate(lefts, rights, char)

    return results


if __name__ == "__main__":
    input = "2-1-1"
    print(first_solution(input))

    input = "2*3-4*5"
    print(first_solution(input))
