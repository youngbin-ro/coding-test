from tree import TreeNode, make_binary_tree


def first_solution(root: TreeNode) -> int:
    if not root:
        return 0

    lengths = []

    def dfs(node):
        if not node:
            return -1

        left = dfs(node.left)
        right = dfs(node.right)
        if node.left and node.left.val != node.val:
            left = -1
        if node.right and node.right.val != node.val:
            right = -1
        lengths.append(left + right + 2)
        return max(left, right) + 1

    dfs(root)
    return max(lengths)


if __name__ == "__main__":
    tree = [5, 4, 5, 1, 1, None, 5]
    root = make_binary_tree(tree)
    print(first_solution(root))

    tree = [1, 4, 5, 4, 4, None, 5]
    root = make_binary_tree(tree)
    print(first_solution(root))
