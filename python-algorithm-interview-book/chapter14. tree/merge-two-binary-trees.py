import collections
from tree import TreeNode, make_binary_tree, tree2list


def first_solution(t1: TreeNode, t2: TreeNode) -> TreeNode:
    queue1 = collections.deque([(t1, None, None)])
    queue2 = collections.deque([t2])

    while queue1 or queue2:
        node1, prev, dir = queue1.popleft()
        node2 = queue2.popleft()

        if node1 and node2:
            node1.val += node2.val
        elif (not node1) and node2:
            node1 = TreeNode(node2.val)
            if dir == 'left':
                prev.left = node1
            else:
                prev.right = node1
        elif not (node1 or node2):
            continue

        queue1.append((node1.left, node1, 'left') if node1 else ([None] * 3))
        queue1.append((node1.right, node1, 'right') if node1 else ([None] * 3))
        queue2.append(node2.left if node2 else None)
        queue2.append(node2.right if node2 else None)
    return t1


def second_solution(t1: TreeNode, t2: TreeNode) -> TreeNode:

    def merge(node1, node2):
        if not node1:
            return node2
        elif not node2:
            return node1
        elif not (node1 or node2):
            return None

        node1.val += node2.val
        node1.left = merge(node1.left, node2.left)
        node1.right = merge(node1.right, node2.right)
        return node1

    return merge(t1, t2)


def third_solution(t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = third_solution(t1.left, t2.left)
        node.right = third_solution(t1.right, t2.right)
        return node
    else:
        return t1 or t2


if __name__ == "__main__":
    tree1 = [1, 3, 2, 5, None, None, None]
    tree2 = [2, 1, 3, None, 4, None, 7]
    root1 = make_binary_tree(tree1)
    root2 = make_binary_tree(tree2)
    print(tree2list(third_solution(root1, root2)))

    tree1 = [1, 2, None, 3]
    tree2 = [1, None, 2, None, 3]
    root1 = make_binary_tree(tree1)
    root2 = make_binary_tree(tree2)
    print(tree2list(third_solution(root1, root2)))
