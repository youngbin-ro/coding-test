class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_list(head):
    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next
    return values


def make_input(values):
    nodes = []
    for val in values:
        nodes.append(ListNode(val=val))
    for idx in range(len(nodes)):
        if idx == len(nodes) - 1:
            break
        nodes[idx].next = nodes[idx + 1]
    return nodes[0]


def first_solution(head):
    if not head:
        return head
    node, next_node = head, head.next
    while next_node:
        temp = next_node.next
        next_node.next = node
        if node == head:
            node.next = None
        node, next_node = next_node, temp
    return to_list(node)


def second_solution(head):
    node, prev = head, None
    while node:
        next_node, node.next = node.next, prev
        prev, node = node, next_node
    return to_list(prev)


if __name__ == "__main__":
    head1 = make_input([1, 2, 3, 4, 5])
    print(to_list(head1))
    print()
    print(second_solution(head1))
