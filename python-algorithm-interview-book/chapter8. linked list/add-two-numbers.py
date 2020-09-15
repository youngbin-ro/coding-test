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
    # get l1 number
    l1_num = ''
    node = l1
    while node:
        l1_num += str(node.val)
        node = node.next

    # get l2 number
    l2_num = ''
    node = l2
    while node:
        l2_num += str(node.val)
        node = node.next

    # get final values and make linked list
    values = str(int(l1_num[::-1]) + int(l2_num[::-1]))[::-1]
    head = ListNode(int(values[0]))
    node = head
    for val in values[1:]:
        node.next = ListNode(int(val))
        node = node.next
    return to_list(head)


def second_solution(l1, l2):
    root = head = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        sum = 0
        if l1:
            sum += l1.val



if __name__ == "__main__":
    head1, head2 = make_input([2, 4, 3], [5, 6, 4])
    print(to_list(head1), to_list(head2))
    print(first_solution(head1, head2))
