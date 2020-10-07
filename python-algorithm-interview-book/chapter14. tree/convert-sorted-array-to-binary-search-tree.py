import collections
from typing import List
from tree import TreeNode, make_binary_tree, tree2list


def first_solution(nums: List[int]) -> TreeNode:

    def make_bst(values):
        if not values:
            return None

        root_idx = len(values) // 2
        root = TreeNode(values[root_idx])
        root.left = make_bst(values[:root_idx])
        root.right = make_bst(values[root_idx + 1:])
        return root

    return make_bst(nums)


def second_solution(nums: List[int]) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = second_solution(nums[:mid])
    node.right = second_solution(nums[mid + 1:])
    return node


if __name__ == "__main__":
    nums1 = [-10, -3, 0, 5, 9]
    print(tree2list(first_solution(nums1)))
