import re


def first_solution(input_):
    input_ = [char.lower() for char in input_ if char.isalnum()]
    input_front, input_back = None, None

    if len(input_) <= 1:
        return True
    if len(input_) % 2 == 0:
        input_front = input_[:len(input_) // 2]
        input_back = list(reversed(input_[len(input_) // 2:]))
    elif len(input_) % 2 == 1:
        input_front = input_[:len(input_) // 2]
        input_back = list(reversed(input_[len(input_) // 2 + 1:]))

    if input_front == input_back:
        return True
    else:
        return False


def second_solution(input_):
    input_ = [char.lower() for char in input_ if char.isalnum()]
    return input_ == input_[::-1]


def best_solution(input_):
    input_ = input_.lower()
    input_ = re.sub(r'[^a-z0-9]', '', input_)
    return input_ == input_[::-1]


if __name__ == "__main__":
    input1 = "A man, a plan, a canal: Panama"
    print(best_solution(input1))

    input2 = "race a car"
    print(best_solution(input2))


"""
Findings
- 문자열 슬라이싱이 reversed()보다 빠르게 문자열을 뒤집을 수 있음
- alnum()은 알파벳과 숫자인지 확인하는 함수 (정규표현식이 더 빠름)
"""
