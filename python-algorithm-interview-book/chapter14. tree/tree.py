import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_binary_tree_old(values: list) -> TreeNode:
    root = TreeNode(values[0])
    nodes = [root]
    for idx in range(1, len(values)):
        if values[idx] is None:
            nodes.append(None)
            continue
        node = TreeNode(values[idx])
        div, mod = divmod(idx, 2)
        if mod == 0:
            nodes[div - 1].right = node
        else:
            nodes[div].left = node
        nodes.append(node)
    return root


def make_binary_tree(values: list) -> TreeNode or None:
    if not (values and values[0] is not None):
        return None

    root = TreeNode(values[0])
    node_queue = collections.deque([root])
    value_queue = collections.deque(values[1:])

    while node_queue:
        node = node_queue.popleft()
        if node is None:
            continue

        left_check, right_check = False, False
        while value_queue and not (left_check and right_check):
            value = value_queue.popleft()
            if not left_check:
                node.left = TreeNode(value) if value is not None else None
                node_queue.append(node.left)
                left_check = True
            elif not right_check:
                node.right = TreeNode(value) if value is not None else None
                node_queue.append(node.right)
                right_check = True
    return root


def tree2list(root: TreeNode) -> list:
    if not root:
        return []
    queue = collections.deque([root])
    result = [root.val]
    while queue:
        node = queue.popleft()
        if not node:
            continue
        for child in [node.left, node.right]:
            if child:
                result.append(child.val)
                queue.append(child)
            else:
                result.append(None)

    last_idx = 0
    for idx, value in enumerate(reversed(result)):
        if value is not None:
            last_idx = -(idx + 1)
            break
    last_idx += 1
    return result if last_idx == 0 else result[:last_idx]
