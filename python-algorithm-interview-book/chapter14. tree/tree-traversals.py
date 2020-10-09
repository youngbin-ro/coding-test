from typing import List
from tree import TreeNode, make_binary_tree, tree2list


def pre_order(root: TreeNode, searched=[]) -> List:
    if not root:
        return searched

    searched.append(root.val)
    searched = pre_order(root.left, searched)
    searched = pre_order(root.right, searched)
    return searched


def in_order(root: TreeNode, searched=[]) -> List:
    if not root:
        return searched

    searched = in_order(root.left, searched)
    searched.append(root.val)
    searched = in_order(root.right, searched)
    return searched


def post_order(root: TreeNode, searched=[]) -> List:
    if not root:
        return searched

    searched = post_order(root.left, searched)
    searched = post_order(root.right, searched)
    searched.append(root.val)
    return searched


if __name__ == "__main__":
    values = ['F', 'B', 'G', 'A', 'D', None, 'I', None, None, 'C', 'E', 'H']
    tree = make_binary_tree(values)
    print(pre_order(tree))
    print(in_order(tree))
    print(post_order(tree))
