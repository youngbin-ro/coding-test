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


# incorrect
def first_solution(head: ListNode) -> ListNode:
    current, prev_temp = head.next, head
    while current:
        compare = head
        next_temp = current.next
        compare_prev = ListNode()

        while compare:
            if compare.val > current.val:
                compare_prev.next, current.next = current, compare
                prev_temp.next = current.next
                prev_temp = compare
                break
            compare, compare_prev = compare.next, compare

        # update root node
        if current.val != head.val:
            head = current
        current = next_temp

    return head


def second_solution(head: ListNode) -> ListNode:
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        if head and cur.val > head.val:
            cur = parent
    return parent.next


if __name__ == "__main__":
    values = [4, 2, 1, 3]
    linked_list = make_input(values)
    output = second_solution(linked_list)
    print(to_list(output))

    values = [-1, 5, 3, 4, 0]
    linked_list = make_input(values)
    output = second_solution(linked_list)
    print(to_list(output))
