import collections
from tree import TreeNode, make_binary_tree, tree2list


# incorrect
def first_solution(n: int, edges: list) -> list:
    if not edges:
        return [0]

    # construct graph
    graph = collections.defaultdict(set)
    degrees = [0] * n
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    searched = set()

    def dfs(node):
        if not (graph[node] - searched):
            return -1

        searched.add(node)
        cur_heights = []
        for child in graph[node]:
            if child in searched:
                cur_heights.append(-1)
            else:
                cur_heights.append(dfs(child))
        return max(cur_heights) + 1

    heights = {}
    for root in range(n):
        if degrees[root] not in heights:
            heights[degrees[root]] = dfs(root)
        searched = set()

    min_height = min(heights.values())
    min_degrees = [degree for degree in heights if heights[degree] == min_height]
    return [idx for idx, degree in enumerate(degrees) if degree in min_degrees]


def second_solution(n: int, edges: list) -> list:
    if not edges:
        return [0]

    # construct graph
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # add first leaf nodes
    leaves = []
    for node in range(n):
        if len(graph[node]) == 1:
            leaves.append(node)

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        leaves = new_leaves

    return leaves


if __name__ == "__main__":
    n, edges = 4, [[1, 0], [1, 2], [1, 3]]
    print(second_solution(n, edges))
    print()

    n, edges = 6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    print(second_solution(n, edges))
    print()

    n, edges = 6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]
    print(second_solution(n, edges))
    print()
