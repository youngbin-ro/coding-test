import collections


def first_solution(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + first_solution(suffix.replace(char, ''))
    return ''


def second_solution(s):
    counter, stack = collections.Counter(s), []
    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)
        print(stack)
    return ''.join(stack)


if __name__ == "__main__":
    s1 = "bcabc"
    print(second_solution(s1))
    print()

    s2 = "cbacdcbc"
    print(second_solution(s2))
