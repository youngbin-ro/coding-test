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
    odd_head, even_head = head, head.next
    odd_node, even_node = odd_head, even_head
    node = head.next.next
    idx = 3
    while node:
        if idx % 2 == 0:
            even_node.next = node
            even_node = node
        elif idx % 2 != 0:
            odd_node.next = node
            odd_node = node
        node = node.next
        idx += 1

    # handle odd number of elements
    if idx % 2 == 0:
        even_node.next = None

    # merge even and odd lists
    odd_node.next = even_head
    return odd_head


def second_solution(head):
    if head is None:
        return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return head


if __name__ == "__main__":
    head1 = make_input([2, 1, 3, 5, 6, 4])
    print(to_list(head1))
    print(to_list(second_solution(head1)))
