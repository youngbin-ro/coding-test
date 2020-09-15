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


def make_input(l1, l2):
    lists = []
    for l in [l1, l2]:
        nodes = []
        for val in l:
            nodes.append(ListNode(val=val))
        for idx in range(len(nodes)):
            if idx == len(nodes) - 1:
                break
            nodes[idx].next = nodes[idx + 1]
        lists.append(nodes[0])
    return lists[0], lists[1]


def first_solution(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1

    node1, node2 = l1, l2
    while node2:
        if node2.next is None:
            temp_node = None
        else:
            temp_node = ListNode(val=node2.next.val, next=node2.next.next)
        if node2.val < node1.val:
            node2.next = node1
            node2 = temp_node
        elif node1.next and node1.val <= node2.val <= node1.next.val:
            node2.next = node1.next
            node1.next = node2
            node2 = temp_node
        else:
            if node1.next is None:
                node1.next = node2
                node2.next = temp_node
                node2 = None
            else:
                node1 = node1.next
    return to_list(l1)


def second_solution(l1, l2):
    # handle empty list
    if not l1:
        return l2
    elif not l2:
        return l1

    # find first node
    if l1.val <= l2.val:
        head = ListNode(val=l1.val)
        l1_node, l2_node = l1.next, l2
    else:
        head = ListNode(val=l2.val)
        l1_node, l2_node = l1, l2.next

    node = head
    while l1_node or l2_node:
        if l1_node is None:
            min_val, l2_node = l2_node.val, l2_node.next
        elif l2_node is None:
            min_val, l1_node = l1_node.val, l1_node.next
        elif l1_node.val <= l2_node.val:
            min_val, l1_node = l1_node.val, l1_node.next
        else:
            min_val, l2_node = l2_node.val, l2_node.next
        node.next = ListNode(val=min_val)
        node = node.next
    return to_list(head)


def third_solution(l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = third_solution(l1.next, l2)
    return to_list(l1)


if __name__ == "__main__":
    list1, list2 = make_input([1, 2, 4], [1, 3, 4])
    print(to_list(list1), to_list(list2))
    print(third_solution(list1, list2))
    print()

    list1, list2 = make_input([5], [1, 2, 4])
    print(to_list(list1), to_list(list2))
    print(third_solution(list1, list2))
