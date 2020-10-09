import collections
from typing import List
from tree import TreeNode, make_binary_tree, tree2list


def first_solution(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    root_idx = inorder.index(preorder[0])

    root.left = first_solution(preorder[1:root_idx + 1], inorder[:root_idx])
    root.right = first_solution(preorder[root_idx + 1:], inorder[root_idx + 1:])
    return root


def second_solution(preorder: List[int], inorder: List[int]) -> TreeNode:
    if inorder:
        index = inorder.index(preorder.pop(0))
        node = TreeNode(inorder[index])
        node.left = second_solution(preorder, inorder[:index])
        node.right = second_solution(preorder, inorder[index + 1:])
        return node


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = second_solution(preorder, inorder)
    print(tree2list(tree))
