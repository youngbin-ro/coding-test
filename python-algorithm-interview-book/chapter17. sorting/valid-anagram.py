def first_solution(s: str, t: str) -> bool:
    return set(s) == set(t)


if __name__ == "__main__":
    s, t = "anagram", "nagaram"
    print(first_solution(s, t))

    s, t = "rat", "car"
    print(first_solution(s, t))
pycharm 