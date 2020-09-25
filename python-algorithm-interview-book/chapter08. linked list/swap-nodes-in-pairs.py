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
    if head.next is None:
        return head
    head, node = head.next, head
    while node.next:
        next = node.next
        if next.next is None:
            next.next, node.next = node, None
            break
        next.next, node.next, node = node, next.next.next, next.next
        if node.next is None:
            next.next.next = node
        elif node.next.next is None:
            node.next.next = node
            node.next = None
    return head


def second_solution(head):
    if head and head.next:
        p = head.next
        head.next = second_solution(p.next)
        p.next = head
        return p
    return head


if __name__ == "__main__":
    head1 = make_input([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(to_list(head1))
    print(to_list(second_solution(head1)))
