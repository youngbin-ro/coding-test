from tree import TreeNode, make_binary_tree


def first_solution(root: TreeNode) -> int:
    if not root or not (root.left or root.right):
        return 0

    def dfs(node):
        if not (node.left or node.right):
            return 1

        left_len, right_len = 0, 0
        if node.left:
            left_len = dfs(node.left)
        if node.right:
            right_len = dfs(node.right)

        maximum = max(left_len, right_len) + 1
        if node == root:
            maximum -= 1
        return max(maximum, left_len + right_len)

    return dfs(root)


def second_solution(root: TreeNode) -> int:
    if not root:
        return 0
    candidates = []

    def dfs(node):
        if not node:
            return -1
        left_len = dfs(node.left)
        right_len = dfs(node.right)
        candidates.append(left_len + right_len + 2)
        return max(left_len, right_len) + 1

    dfs(root)
    return max(candidates)


if __name__ == "__main__":
    tree = [1, 2, 3, 4, 5, None, None]
    root = make_binary_tree(tree)
    print(second_solution(root))

    tree = [1, 2]
    root = make_binary_tree(tree)
    print(second_solution(root))
