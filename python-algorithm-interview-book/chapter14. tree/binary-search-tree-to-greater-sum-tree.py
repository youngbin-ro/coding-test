from tree import TreeNode, make_binary_tree, tree2list


# incorrect
def first_solution(root: TreeNode) -> TreeNode:

    def right_sum(node, parent_val):
        if not node:
            return 0

        left, right = 0, 0
        if node.left:
            left = node.left.val if node.left.val > parent_val else 0
        if node.right:
            right = right_sum(node.right, node.val)
        return node.val + left + right

    if not root:
        return root

    root.val += right_sum(root.right, root.val)
    if root.left:
        root.left.val += root.val
        root.left = first_solution(root.left)
    if root.right:
        root.right = first_solution(root.right)
    return root

    """
    def right_sum(node, parent_val):
        if not node:
            return 0

        left, right = 0, 0
        if node.left:
            left = node.left.val if node.left.val > parent_val else 0
        if node.right:
            right = right_sum(node.right, node.val)
        return node.val + left + right
    
    def dfs(node, parent_val):
        if not node:
            return 0
        node.val += dfs(node.right, node.val)
        if node.left and node.left.val > parent_val:
            return node.val + dfs(node.left, node.val)
        else:
            return node.val

    if not root:
        return root

    root.val = dfs(root, root.val + 1)
    #root.left = first_solution(root.left)
    #root.left = first_solution(root.left)
    return root
    """


val = [0]


def second_solution(root: TreeNode) -> TreeNode:
    if root:
        second_solution(root.right)
        val[0] += root.val
        root.val = val[0]
        second_solution(root.left)
    return root


if __name__ == "__main__":
    null = None
    values = [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8]
    sum_tree = second_solution(make_binary_tree(values))
    print(tree2list(sum_tree))
