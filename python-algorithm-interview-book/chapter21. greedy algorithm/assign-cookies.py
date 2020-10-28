from typing import List


# incorrect
def first_solution(g: List[int], s: List[int]) -> int:
    if not s:
        return 0

    s.sort()
    result = 0
    max_size = s.pop()
    for child in g:
        if child > max_size:
            continue
        else:
            result += 1
            if not s:
                break
            max_size = s.pop()
    return result


def second_solution(g: List[int], s: List[int]) -> int:
    g.sort(reverse=True)
    s.sort(reverse=True)
    result = 0
    while s:
        max_size = s.pop()
        if g and max_size >= g[-1]:
            result += 1
            g.pop()
    return result


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    print(second_solution(g, s))

    g = [1, 2]
    s = [1, 2, 3]
    print(second_solution(g, s))

    g = [10, 6, 9, 7]
    s = [1, 3, 5, 7]
    print(second_solution(g, s))

    g = [10, 9, 8, 7, 10, 9, 8, 7]
    s = [10, 9, 8, 7]
    print(second_solution(g, s))
