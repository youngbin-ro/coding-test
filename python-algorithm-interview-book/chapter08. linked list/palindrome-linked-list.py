import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def first_solution(head):
    if not head:
        return True
    values = []
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next
    return values == values[::-1]


def second_solution(head):
    if not head:
        return True
    deque = collections.deque()
    node = head
    while node is not None:
        deque.append(node.val)
        node = node.next

    while len(deque) > 1:
        if deque.popleft() != deque.pop():
            return False
    return True


def third_solution(head):
    # handle empty list
    if not head:
        return True

    # use fast and slow runner
    rev = None
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    # ignore mid-element
    if fast:
        slow = slow.next

    # check slow and rev linked list match
    while rev and rev.val == slow.val:
        rev, slow = rev.next, slow.next
    return not rev


if __name__ == "__main__":
    # input1
    node1 = ListNode(val=1)
    node2 = ListNode(val=2)
    node1.next = node2
    print(third_solution(node1))

    # input2
    node1 = ListNode(val=1)
    node2 = ListNode(val=2)
    node3 = ListNode(val=2)
    node4 = ListNode(val=1)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    print(third_solution(node1))


"""
Findings
- 리스트 자료형의 경우 pop(0)은 모든 값의 인덱스를 이동시켜야 하므로 O(n)의 복잡도 발생 ~ deque사용
- 런너(runner)는 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
"""