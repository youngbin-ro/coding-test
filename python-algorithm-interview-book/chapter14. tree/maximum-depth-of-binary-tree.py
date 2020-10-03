import collections
from tree import TreeNode, make_binary_tree


def first_solution(root: TreeNode) -> int:
    if not root:
        return 0
    depths = []

    def dfs(node, depth):
        if node.left is None and node.right is None:
            depths.append(depth)
            return depth
        depth += 1

        for child in [node.left, node.right]:
            if child is not None:
                dfs(child, depth)
        return depth

    dfs(root, 1)
    return max(depths)


def second_solution(root: TreeNode) -> int:
    if not root:
        return 0
    max_depth = 0

    def dfs(node, depth, maximum):
        if node.left is None and node.right is None:
            return max(maximum, depth)
        depth += 1

        for child in [node.left, node.right]:
            if child is not None:
                maximum = dfs(child, depth, maximum)
        return maximum

    return dfs(root, 1, max_depth)


def third_solution(root: TreeNode) -> int:
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


if __name__ == "__main__":
    tree = [3, 9, 20, None, None, 15, 7]
    root = make_binary_tree(tree)
    print(third_solution(root))
