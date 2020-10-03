import collections
from tree import TreeNode, make_binary_tree, tree2list


def first_solution(root: TreeNode) -> TreeNode:
    if not root:
        return None

    def invert(node):
        temp = node.left
        node.left = node.right
        node.right = temp
        return node

    root = invert(root)
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        for child in [node.left, node.right]:
            if child:
                child = invert(child)
                queue.append(child)
    return root


def second_solution(root: TreeNode) -> TreeNode:
    if root:
        root.right, root.left = \
            second_solution(root.left), second_solution(root.right)
        return root


def third_solution(root: TreeNode) -> TreeNode:
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if not node:
            continue
        node.left, node.right = node.right, node.left
        queue.append(node.left)
        queue.append(node.right)
    return root


if __name__ == "__main__":
    tree = [4, 2, 7, 1, 3, 6, 9]
    root = make_binary_tree(tree)
    print(tree2list(third_solution(root)))
