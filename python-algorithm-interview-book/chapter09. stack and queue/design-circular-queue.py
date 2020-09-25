class MyFirstCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.max = k
        self.queue = [None] * k
        self.front, self.rear = 0, 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        elif not self.isEmpty():
            self.rear = (self.rear + 1) % self.max
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        if self.front != self.rear:
            self.front = (self.front + 1) % self.max
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return None not in self.queue


class MySecondCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.max = k
        self.queue = [None] * k
        self.front, self.rear = 0, 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.rear]:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % self.max
            return True
        else:
            return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.front] is None:
            return False
        else:
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.queue[self.front] is None else self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.queue[self.rear] is None else self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.front == self.rear and self.queue[self.front] is None

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.front == self.rear and self.queue[self.rear] is not None


if __name__ == "__main__":
    queue = MySecondCircularQueue(6)
    print(queue.enQueue(6))
    print(queue.Rear())
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.enQueue(5))
    print(queue.Rear())
    print(queue.deQueue())
    print(queue.Front())
    print(queue.deQueue())
    print(queue.deQueue())
    print(queue.deQueue())
