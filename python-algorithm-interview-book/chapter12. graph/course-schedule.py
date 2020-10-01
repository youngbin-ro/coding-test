import collections


# incorrect
def first_solution(numCourses: int, prerequisites: list) -> bool:
    if not prerequisites:
        return True

    graph1 = collections.defaultdict(list)
    graph2 = collections.defaultdict(list)
    for a, b in prerequisites:
        graph1[b].append(a)
        graph2[a].append(b)

    for course in range(numCourses):
        searched = []
        queue = collections.deque()
        queue.append(course)

        while queue:
            node = queue.popleft()
            searched.append(node)
            for child in graph1[node]:
                if child in searched:
                    return False
                searched.append(child)
                queue.append(child)


# incorrect
def second_solution(numCourses: int, prerequisites: list) -> bool:
    if not prerequisites:
        return True

    graph = [[0] * numCourses for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[b][a] = 1

    for edges in graph:
        if sum(edges) == 0:
            return True
    return False


def third_soluition(numCourses: int, prerequisites: list) -> bool:
    if not prerequisites:
        return True

    graph = collections.defaultdict(list)
    for a, b in prerequisites:
        graph[a].append(b)
    traced = set()
    visited = set()

    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return True
        traced.add(i)

        for node in graph[i]:
            if not dfs(node):
                return False
        traced.remove(i)
        visited.add(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True


if __name__ == "__main__":
    numCourses1 = 2
    prerequisites1 = [[0, 1]]
    print(third_soluition(numCourses1, prerequisites1))    # True

    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(third_soluition(numCourses2, prerequisites2))    # False

    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(third_soluition(numCourses3, prerequisites3))    # True

    numCourses4 = 3
    prerequisites4 = [[1, 0], [0, 2], [2, 1]]
    print(third_soluition(numCourses4, prerequisites4))    # False
