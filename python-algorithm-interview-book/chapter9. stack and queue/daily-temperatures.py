def first_solution(T):
    stack = []
    answer = [0 for _ in T]
    for day, temp in enumerate(T):
        while stack and stack[-1][0] < temp:
            _, prev = stack.pop()
            answer[prev] = day - prev
        stack.append((temp, day))
    return answer


def second_solution(T):
    stack = []
    answer = [0] * len(T)
    for day, temp in enumerate(T):
        while stack and T[stack[-1]] < temp:
            last = stack.pop()
            answer[last] = day - last
        stack.append(day)
    return answer


if __name__ == "__main__":
    T1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(second_solution(T1))
    # answer = [1, 1, 4, 2, 1, 1, 0, 0]
