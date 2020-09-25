def first_solution(logs):
    let_logs = [log for log in logs if ''.join(log.split(' ')[1:]).isalpha()]
    dig_logs = [log for log in logs if not ''.join(log.split(' ')[1:]).isalpha()]
    let_logs_sorted = sorted(let_logs, key=lambda x: x.split(' ')[0])
    let_logs_sorted = sorted(let_logs_sorted, key=lambda x: ' '.join(x.split(' ')[1:]))
    return let_logs_sorted + dig_logs


def second_solution(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


if __name__ == "__main__":
    input1 = [
        "dig1 8 1 5 1",
        "let3 art can",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dog"
    ]
    print(second_solution(input1))

    input2 = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    print(second_solution(input2))


"""
Findings
- 리스트를 특정 조건에 따라 둘로 나눌 때 두번 list comprehension하지 말고 한번만 돌기
- 우선순위가 다른 두개의 조건으로 정렬할 경우 튜플 형태의 반환값을 갖는 람다 함수로 코드 작성 가능
"""