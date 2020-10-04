from tree import TreeNode, make_binary_tree, tree2list


def first_solution(root: TreeNode) -> bool:
    result = []

    def dfs(node):
        if not node:
            return -1
        left = dfs(node.left)
        right = dfs(node.right)
        if abs(left - right) > 1:
            result.append(False)
        return max(left, right) + 1

    dfs(root)
    return len(result) == 0


def second_solution(root: TreeNode) -> bool:

    def check(root):
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1


if __name__ == "__main__":
    tree = [3, 9, 20, None, None, 15, 7]
    root = make_binary_tree(tree)
    print(first_solution(root))

    tree = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = make_binary_tree(tree)
    print(first_solution(root))
