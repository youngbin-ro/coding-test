def first_solution(s):
    if not s:
        return True
    elif s[0] in [')', '}', ']']:
        return False

    table = {')': '(', '}': '{', ']': '['}
    stack = [s[0]]
    for par in s[1:]:
        if par in table.values():
            stack.append(par)
        elif table[par] == stack[-1]:
            stack.pop()
    if stack:
        return False
    else:
        return True


def second_solution(s):
    if not s:
        return True
    elif s[0] in [')', '}', ']']:
        return False

    table = {')': '(', '}': '{', ']': '['}
    stack = [s[0]]
    for par in s[1:]:
        if par not in table:
            stack.append(par)
        elif table[par] != stack.pop():
            return False
    return len(stack) == 0


if __name__ == "__main__":
    s1 = "()"
    print(second_solution(s1))

    s2 = "()[]{}"
    print(second_solution(s2))
