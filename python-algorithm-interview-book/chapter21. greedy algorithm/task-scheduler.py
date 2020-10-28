from typing import List
from collections import Counter


def first_solution(tasks: List[str], n: int) -> int:
    if n == 0:
        return len(tasks)

    counter = Counter(tasks)
    result = 0
    while True:
        sub_count = 0
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1
            counter.subtract(task)
            counter += Counter()

        if not counter:
            break
        result += n - sub_count + 1
    return result


if __name__ == "__main__":
    tasks, n = ["A", "A", "A", "B", "B", "B"], 2
    print(first_solution(tasks, n))    # answer: 8
    print()

    tasks, n = ["A", "A", "A", "B", "B", "B"], 0
    print(first_solution(tasks, n))    # answer: 6
    print()

    tasks, n = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2
    print(first_solution(tasks, n))    # answer: 16
    print()

    tasks, n = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2
    print(first_solution(tasks, n))  # answer: 12
