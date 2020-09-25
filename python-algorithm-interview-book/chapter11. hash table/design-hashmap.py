class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """


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
