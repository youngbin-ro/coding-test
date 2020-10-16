from typing import List


def first_solution(intervals: List[List[int]]) -> List[List[int]]:
    if len(intervals) <= 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    results = [intervals[0]]
    for interval in intervals[1:]:
        if results[-1][1] >= interval[0]:
            results[-1] = [min(results[-1][0], interval[0]),
                           max(results[-1][1], interval[1])]
        else:
            results.append(interval)
    return results


def second_solution(intervals: List[List[int]]) -> List[List[int]]:
    merged = []
    for i in sorted(intervals, key=lambda x: x[0]):
        if merged and merged[-1][1] >= i[0]:
            merged[-1][1] = max(merged[-1][1], i[1])
        else:
            merged += [i]
    return merged


if __name__ == "__main__":
    """
    Constraints: intervals[i][0] <= intervals[i][1]
    """

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(second_solution(intervals))

    intervals = [[1, 4], [4, 5]]
    print(second_solution(intervals))
