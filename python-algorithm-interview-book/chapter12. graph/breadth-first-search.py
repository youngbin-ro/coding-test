import collections


def bfs_iterative(graph, root):
    queue = collections.deque()
    searched = [root]
    queue.append(root)
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if child not in searched:
                searched.append(child)
                queue.append(child)
    return searched


if __name__ == "__main__":
    graph = {
        1: [2, 3, 4],
        2: [5],
        3: [5],
        4: [],
        5: [6, 7],
        6: [],
        7: [3]
    }
    print(bfs_iterative(graph, 1))
