import heapq


class ListNode:
    def __init__(self, val=None, next=None):
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


def first_solution(lists) -> ListNode:
    # return None if lists is empty
    if not lists:
        return None

    # gather nodes in heap
    nodes = []
    for list_idx, node in enumerate(lists):
        if node is None:
            continue
        count = 0
        while node:
            heapq.heappush(nodes, (node.val, list_idx, count, node))
            node = node.next
            count += 1

    # return None there is no node.
    if len(nodes) == 0:
        return None

    # connect nodes
    head = node = heapq.heappop(nodes)[-1]
    for i in range(len(nodes)):
        node.next = heapq.heappop(nodes)[-1]
        node = node.next
    return head


def second_solution(lists) -> ListNode:
    root = result = ListNode(None)
    heap = []

    for i in range(len(lists)):
        heapq.heappush(heap, (lists[i].val, i, lists[i]))

    while heap:
        _, idx, result.next = heapq.heappop(heap)
        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))
    return root.next


if __name__ == "__main__":
    linked1 = make_input([1, 4, 5])
    linked2 = make_input([1, 3, 4])
    linked3 = make_input([2, 6])
    lists1 = [linked1, linked2, linked3]
    output1 = second_solution(lists1)
    print(to_list(output1))
