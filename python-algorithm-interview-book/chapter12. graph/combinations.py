import itertools, collections


def first_solution(n: int, k: int):
    return list(itertools.combinations([i + 1 for i in range(n)], k))


def second_solution(n: int, k: int):
    results, path, prev = [], [], 0
    queue = collections.deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        if prev >= node:
            path[-1] += 1
        for child in range(node + 1, n + 1):
            queue.append(child)
        if node not in path:
            path.append(node)
        if len(path) == k:
            results.append(path[:])
            prev = path.pop()
    return results


def third_solution(n: int, k: int):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results


if __name__ == "__main__":
    n1, k1 = 4, 2
    print(third_solution(n1, k1))

    n1, k1 = 4, 3
    print(third_solution(n1, k1))
