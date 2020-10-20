from typing import List


def first_solution(points: List[List[int]], K: int) -> List[List[int]]:
    points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
    return points[:K]


if __name__ == "__main__":
    points, k = [[1, 3], [-2, 2]], 1
    print(first_solution(points, k))

    points, k = [[3, 3], [5, -1], [-2, 4]], 2
    print(first_solution(points, k))
