import collections

def first_solution(strs):
    anagrams = []
    checked = []
    for idx1 in range(len(strs)):
        if strs[idx1] in checked:
            continue
        cur_anagrams = [strs[idx1]]
        cur_chars = list(cur_anagrams[0])
        cur_chars.sort()
        cur_chars = ''.join(cur_chars)
        for idx2 in range(idx1 + 1, len(strs)):
            compare_chars = list(strs[idx2])
            compare_chars.sort()
            compare_chars = ''.join(compare_chars)
            if cur_chars == compare_chars:
                cur_anagrams.append(strs[idx2])
                checked.append(strs[idx2])
        anagrams.append(cur_anagrams)
    return anagrams


def second_solution(strs):
    anagram_dict = collections.defaultdict(list)
    for word in strs:
        chars = list(word)
        chars.sort()
        anagram_dict[''.join(chars)].append(word)
    return list(anagram_dict.values())


def best_solution(strs):
    anagram_dict = collections.defaultdict(list)
    for word in strs:
        anagram_dict[''.join(sorted(word))].append(word)
    return list(anagram_dict.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(best_solution(strs))

    strs = [""]
    print(best_solution(strs))

    strs = ["a"]
    print(best_solution(strs))


"""
Findings
- anagram 문제는 dictionary 사용
- sorted()를 사용할 경우 word를 char단위로 sorting한 list를 반환 (굳이 list -> sort() 사용 x)
"""
