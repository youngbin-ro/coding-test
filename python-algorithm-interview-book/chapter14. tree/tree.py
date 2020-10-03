class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def make_binary_tree(values: list) -> TreeNode:
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
