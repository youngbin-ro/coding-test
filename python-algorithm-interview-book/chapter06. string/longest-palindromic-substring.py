def first_solution(s):
    for length in reversed(range(len(s) + 1)):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                return substring


def best_solution(s):
    def expand(left, right):
        while 0 <= left and right <= len(s) and s[left] == s[right - 1]:
            left -= 1
            right += 1
        return s[left + 1:right - 1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''
    for i in range(len(s) - 1):
        result = max(
            result,
            expand(i, i + 1),
            expand(i, i + 2),
            key=len
        )
    return result


if __name__ == "__main__":
    input1 = "babad"
    print(best_solution(input1))

    input2 = "cbbd"
    print(best_solution(input2))


"""
Findings
- 함수 안에서 함수 사용하기 코딩테스트에서도 나쁘지 않음
- 해당 사항이 없을 때 빠르게 리턴하는 것도 성능에 큰 영향을 미침
- 팰린드롬 구할 때 슬라이딩 윈도우 방식으로 구할 수 있음
"""
