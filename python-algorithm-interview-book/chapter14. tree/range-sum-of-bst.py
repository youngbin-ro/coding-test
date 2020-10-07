import collections
from tree import TreeNode, make_binary_tree, tree2list


val = [0]


def first_solution(root: TreeNode, L: int, R: int) -> int:
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if not node:
            continue
        if L <= node.val <= R:
            val[0] += node.val
        queue.append(node.left)
        queue.append(node.right)
    return val[0]


def second_solution(root: TreeNode, L: int, R: int) -> int:
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if not node:
            continue
        if L <= node.val <= R:
            val[0] += node.val
        if node.val > L:
            queue.append(node.left)
        if node.val < R:
            queue.append(node.right)
    return val[0]


if __name__ == "__main__":
    values = [10, 5, 15, 3, 7, None, 18]
    l, r = 7, 15
    tree = make_binary_tree(values)
    print(second_solution(tree, l, r))

    val[0] = 0
    values = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
    l, r = 6, 10
    tree = make_binary_tree(values)
    print(second_solution(tree, l, r))
