import heapq
from typing import List


def first_solution(people: List[List[int]]) -> List[List[int]]:
    people.sort(key=lambda x: (-x[0], x[1]))
    print(people)
    new = []
    for idx in range(len(people)):
        h, k = people[idx]
        if idx != k:
            new.insert(k, [h, k])
        else:
            new.append([h, k])
    return new


def second_solution(people: List[List[int]]) -> List[List[int]]:
    heap = []
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))

    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result


if __name__ == "__main__":
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(second_solution(people))
