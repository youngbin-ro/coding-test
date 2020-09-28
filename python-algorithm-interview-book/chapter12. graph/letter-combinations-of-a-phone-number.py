def first_solution(digits: str):
    digit_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not digits:
        return ['']
    elif len(digits) == 1:
        return digit_dict[digits[0]]

    letters = []
    for idx in range(len(digits) - 1):
        chars = digit_dict[digits[idx]]
        for char in chars:
            letters += [char + letter
                        for letter in first_solution(digits[idx + 1:])
                        if len(char + letter) == len(digits)]
    return letters


def second_solution(digits: str):
    digit_dict = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not digits:
        return []

    letters = []
    cur_letter = []
    stack = [(char, 0) for char in digit_dict[digits[0]]]
    while stack:
        node = stack.pop()
        cur_letter.append(node)
        if len(cur_letter) == len(digits):
            letters.append(''.join(list(zip(*cur_letter))[0]))
            if not (stack and cur_letter):
                continue
            while cur_letter and stack[-1][-1] <= cur_letter[-1][-1]:
                cur_letter.pop()
            continue
        for child in digit_dict[digits[len(cur_letter)]]:
            stack.append((child, len(cur_letter)))
    return letters


def third_solution(digits: str):
    def dfs(index, path):
        if len(path) == len(digits):
            letters.append(path)
            return

        for i in range(index, len(digits)):
            for char in dic[digits[i]]:
                dfs(i + 1, path + char)

    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    letters = []
    dfs(0, "")
    return letters


if __name__ == "__main__":
    str1 = "23"
    print(third_solution(str1))
