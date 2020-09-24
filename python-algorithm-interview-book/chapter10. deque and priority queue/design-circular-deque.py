class ListNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyFirstCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.maxlen = k
        self.cur_size = 0
        self.head = self.tail = None

    def insertWhenEmpty(self, value: int) -> bool:
        """
        Adds an item when the deque is empty
        """
        new_node = ListNode(val=value)
        self.cur_size += 1
        self.head = self.tail = new_node
        return True

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        # handle when the deque is full or empty
        if self.isFull():
            return False
        elif self.isEmpty():
            return self.insertWhenEmpty(value)

        # ordinary case
        self.cur_size += 1
        new_node = ListNode(val=value, next=self.head)
        self.head.prev = new_node
        self.head = self.head.prev
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        # handle when the deque is full or empty
        if self.isFull():
            return False
        elif self.isEmpty():
            return self.insertWhenEmpty(value)

        # ordinary case
        self.cur_size += 1
        new_node = ListNode(val=value, prev=self.tail)
        self.tail.next = new_node
        self.tail = self.tail.next
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        # when the deque is empty
        if self.isEmpty():
            return False
        elif self.cur_size == 1:
            self.cur_size -= 1
            self.head = self.tail = None
            return True

        # ordinary case
        self.cur_size -= 1
        new_head = self.head.next
        new_head.prev, self.head = None, new_head
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        # when the deque is empty
        if self.isEmpty():
            return False
        elif self.cur_size == 1:
            self.cur_size -= 1
            self.head = self.tail = None
            return True

        # ordinary case
        self.cur_size -= 1
        new_tail = self.tail.prev
        new_tail.next, self.tail = None, new_tail
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return -1 if self.head is None else self.head.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return -1 if self.tail is None else self.tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cur_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_size >= self.maxlen


class MySecondCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.maxlen, self.cur_size = k, 0
        self.head, self.tail = ListNode(None), ListNode(None)
        self.head.next, self.tail.prev = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode) -> bool:
        next = node.next
        node.next = new
        new.prev, new.next = node, next
        next.prev = new
        return True

    def _del(self, node: ListNode) -> bool:
        next = node.next
        node.prev.next = next
        next.prev = node.prev
        return True

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.cur_size == self.maxlen:
            return False
        self.cur_size += 1
        return self._add(self.head, ListNode(value))

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        # return False if the deque is full
        if self.cur_size == self.maxlen:
            return False
        self.cur_size += 1
        return self._add(self.tail.prev, ListNode(value))

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        # return False if the deque is empty
        if self.cur_size == 0:
            return False
        self.cur_size -= 1
        return self._del(self.head.next)

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        # return False if the deque is empty
        if self.cur_size == 0:
            return False
        self.cur_size -= 1
        return self._del(self.tail.prev)

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.head.next.val if self.head.next.val is not None else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.tail.prev.val if self.tail.prev.val is not None else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.cur_size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.cur_size >= self.maxlen


if __name__ == "__main__":
    deque = MySecondCircularDeque(3)
    print(deque.insertLast(1))
    print(deque.insertLast(2))
    print(deque.insertFront(3))
    print(deque.insertFront(4))
    print(deque.getRear())
    print(deque.isFull())
    print(deque.deleteLast())
    print(deque.insertFront(4))
    print(deque.getFront())
