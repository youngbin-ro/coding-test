from collections import deque


def is_bipartite_graph(graph, root):
    colors = [0] * (len(graph) + 1)
    queue = deque([root])
    colors[root] = 1

    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if colors[child] == 0:
                colors[child] = 3 - colors[node]
                queue.append(child)
            else:
                if colors[node] == colors[child]:
                    return False
    return True


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
    print(is_bipartite_graph(graph, 1))
