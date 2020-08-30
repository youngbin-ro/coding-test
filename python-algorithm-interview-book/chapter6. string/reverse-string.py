def first_solution(s):
    for idx in range(len(s) // 2):
        s[idx], s[-idx - 1] = s[-idx - 1], s[idx]
    print(s)


def second_solution(s):
    s.reverse()
    print(s)


def best_solution(s):
    s[:] = s[::-1]
    print(s)


if __name__ == "__main__":
    input1 = ["h", "e", "l", "l", "o"]
    best_solution(input1)

    input2 = ["H", "a", "n", "n", "a", "h"]
    best_solution(input2)


"""
Findings
- 단순 indexing으로 리스트 요소 swap 가능
- s[:] == s[::-1] 으로 할당할 경우 새로운 공간을 필요로 하지 않음
"""