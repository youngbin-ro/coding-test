import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if key == p.key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if key == p.key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if key == p.key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if key == p.key:
                prev.next = p.next
                return
            prev, p = p, p.next


if __name__ == "__main__":
    hashmap = MyHashMap()
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    print(hashmap.get(1))
    print(hashmap.get(3))
    hashmap.put(2, 1)
    print(hashmap.get(2))
    hashmap.remove(2)
    print(hashmap.get(2))
