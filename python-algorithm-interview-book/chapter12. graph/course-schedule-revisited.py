import collections


def first_solution(numCourses: int, prerequisites: list) -> bool:
    if not prerequisites:
        return True

    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)

    traced = set()
    visited = set()

    def dfs(course):
        if course in traced:
            return False
        if course in visited:
            return True
        traced.add(course)

        for precourse in graph[course]:
            if not dfs(precourse):
                return False
        traced.remove(course)
        visited.add(course)
        return True

    for a in list(graph):
        if not dfs(a):
            return False
    return True


if __name__ == "__main__":
    numCourses1 = 2
    prerequisites1 = [[0, 1]]
    print(first_solution(numCourses1, prerequisites1))    # True

    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(first_solution(numCourses2, prerequisites2))    # False

    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(first_solution(numCourses3, prerequisites3))    # True

    numCourses4 = 3
    prerequisites4 = [[1, 0], [0, 2], [2, 1]]
    print(first_solution(numCourses4, prerequisites4))    # False
