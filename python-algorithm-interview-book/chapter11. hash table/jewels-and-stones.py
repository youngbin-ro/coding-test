import collections


def first_solution(J: str, S: str) -> int:
    count = 0
    s_stats = collections.Counter(S)
    for j in set(J):
        count += s_stats[j]
    return count


def second_solution(J: str, S: str) -> int:
    return sum([s in J for s in S])


if __name__ == "__main__":
    j1, s1 = "aA", "aAAbbbb"
    print(second_solution(j1, s1))

    j2, s2 = "z", "ZZ"
    print(second_solution(j2, s2))
