import collections
from tree import TreeNode, make_binary_tree, tree2list


class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ' '
        queue = collections.deque([root])
        result = [str(root.val)]
        while queue:
            node = queue.popleft()
            if not node:
                continue
            for child in [node.left, node.right]:
                if child:
                    result.append(str(child.val))
                    queue.append(child)
                else:
                    result.append(' ')
        return '*'.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = [int(value) if value != ' ' else None
                  for value in data.split('*')]
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


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']

        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '# #':
            return None

        nodes = data.split()
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2

        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1
        return root


if __name__ == "__main__":
    codec = Codec2()

    values = []
    root = make_binary_tree(values)
    print(codec.serialize(root))
    print(tree2list(codec.deserialize(codec.serialize(root))))

    values = [1]
    root = make_binary_tree(values)
    print(codec.serialize(root))
    print(tree2list(codec.deserialize(codec.serialize(root))))

    values = [1, 2]
    root = make_binary_tree(values)
    print(codec.serialize(root))
    print(tree2list(codec.deserialize(codec.serialize(root))))

    values = [1, 2, 3, None, None, 4, 5]
    root = make_binary_tree(values)
    print(codec.serialize(root))
    print(tree2list(codec.deserialize(codec.serialize(root))))
