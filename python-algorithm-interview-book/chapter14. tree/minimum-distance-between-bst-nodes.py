import heapq, collections, sys
from tree import TreeNode, make_binary_tree, tree2list


def first_solution(root: TreeNode) -> int:
    queue = collections.deque([root])
    heap = []
    while queue:
        node = queue.popleft()
        if not node:
            continue
        heapq.heappush(heap, node.val)
        queue.append(node.left)
        queue.append(node.right)

    min_diff = sys.maxsize
    cur_val = heapq.heappop(heap)
    while heap:
        next_val = heapq.heappop(heap)
        min_diff = min(min_diff, next_val - cur_val)
        cur_val = next_val
    return min_diff


if __name__ == "__main__":
    values = [4, 2, 6, 1, 3, None, None]
    print(first_solution((make_binary_tree(values))))
