from typing import List
from trie import Trie4Palindrome


def first_solution(words: List[str]) -> List[List[int]]:
    results = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            concat = words[i] + words[j]
            if concat == concat[::-1]:
                results.append([i, j])
    return results


def second_solution(words: List[int]) -> List[List[int]]:
    trie = Trie4Palindrome()
    for idx, word in enumerate(words):
        trie.insert(word, idx)

    results = []
    for idx, word in enumerate(words):
        results.extend(trie.search(word, idx))
    return results


if __name__ == "__main__":
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print(second_solution(words))

    words = ["bat", "tab", "cat"]
    print(second_solution(words))

    words = ["a", ""]
    print(second_solution(words))
