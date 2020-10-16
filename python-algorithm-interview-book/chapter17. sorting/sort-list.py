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
    return nodes[0] if nodes else None


def first_solution(head: ListNode) -> ListNode:
    values = to_list(head)
    values.sort()
    return make_input(values)


if __name__ == "__main__":
    values = [4, 2, 1, 3]
    head = make_input(values)
    sorted = first_solution(head)
    print(to_list(sorted))

    values = [-1, 5, 3, 4, 0]
    head = make_input(values)
    sorted = first_solution(head)
    print(to_list(sorted))

    values = []
    head = make_input(values)
    sorted = first_solution(head)
    print(to_list(sorted))
