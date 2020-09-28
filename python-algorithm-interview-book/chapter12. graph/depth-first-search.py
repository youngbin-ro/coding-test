def dfs_recursive(graph, root, searched=[]):
    searched.append(root)
    for child in graph[root]:
        if child not in searched:
            searched = dfs_recursive(graph, child, searched)
    return searched


def dfs_stack(graph, root, searched=[]):
    searched = []
    stack = [root]
    while stack:
        node = stack.pop()
        searched.append(node)
        for child in graph[node]:
            if child not in searched:
                stack.append(child)
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
    print(dfs_recursive(graph, 1))
    print(dfs_stack(graph, 1))
