import collections
import re


def first_solution(paragraph, banned):
    for punct in ["!", "?", "'", ",", ";", '.']:
        paragraph = paragraph.replace(punct, ' ')
    words = paragraph.replace('  ', ' ').lower().split()
    for count in collections.Counter(words).most_common(len(words)):
        if count[0] not in banned:
            return count[0]


def second_solution(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
             if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(second_solution(paragraph1, banned1))


"""
Findings
- 정규식에서 ^은 not을 의미하며, \w는 단어 문자를 의미
"""