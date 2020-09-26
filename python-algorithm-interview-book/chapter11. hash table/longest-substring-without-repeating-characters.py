def first_solution(s: str) -> int:
    if len(set(s)) == len(s):
        return len(s)

    curstr = s[0]
    maxlen = 0
    for idx in range(len(s) - 1):
        if s[idx + 1] not in curstr:
            curstr += s[idx + 1]
        else:
            if len(curstr) > maxlen:
                maxlen = len(curstr)
            if curstr[-1] == s[idx + 1]:
                curstr = ''
            else:
                curstr = curstr[list(curstr).index(s[idx + 1]) + 1:]
            curstr += s[idx + 1]

    if len(curstr) > maxlen:
        maxlen = len(curstr)
    return maxlen


def second_solution(s: str) -> int:
    if len(set(s)) == len(s):
        return len(s)

    maxlen, start, used = 0, 0, {}
    for idx, char in enumerate(s):
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            maxlen = max(maxlen, idx - start + 1)
        used[char] = idx
    return maxlen


if __name__ == "__main__":
    s1 = "abcabcbb"
    print(second_solution(s1))

    s2 = "bbbbb"
    print(second_solution(s2))

    s3 = "pwwkew"
    print(second_solution(s3))

    s4 = ""
    print(second_solution(s4))

    s5 = "tmmzuxt"
    print(second_solution(s5))
