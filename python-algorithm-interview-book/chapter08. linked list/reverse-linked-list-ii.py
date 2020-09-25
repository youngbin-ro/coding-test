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


def first_solution(head, m, n):
    if m == n or not head:
        return head

    node, prev = head, None
    rev_tail, rev_temp = None, None
    idx = 1
    while node:
        if idx < m - 1:
            node = node.next
        elif idx == m - 1:
            prev, node = node, node.next
        elif idx == m:
            rev_tail, rev_temp = node, node.next
            rev_temp.next, rev_temp, node = node, rev_temp.next, node.next
        elif m < idx < n:
            rev_temp.next, rev_temp, node = node, rev_temp.next, rev_temp
        elif idx == n:
            rev_tail.next = rev_temp
            if m != 1:
                prev.next = node
            break
        idx += 1
    return node if m == 1 else head


def second_solution(head, m, n):
    if m == n or not head:
        return head

    root = start = ListNode(None, head)
    for _ in range(m - 1):
        start = start.next
    end = start.next

    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp
    return root.next


if __name__ == "__main__":
    head1 = make_input([2, 1, 3, 5, 6, 4])
    print(to_list(head1))
    print(to_list(second_solution(head1, 2, 5)))
