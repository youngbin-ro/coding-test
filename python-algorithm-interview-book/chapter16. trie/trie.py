import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = collections.defaultdict(TrieNode)


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


class TrieNode4Palindrome:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode4Palindrome)
        self.word_id = -1
        self.palindrome_word_ids = []


class Trie4Palindrome:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode4Palindrome()

    @staticmethod
    def is_palindrome(word: str) -> bool:
        return word[::] == word[::-1]

    def insert(self, word: str, index: int) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i, char in enumerate(reversed(word)):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            node.val = char
        node.word_id = index

    def search(self, word: str, index: int) -> List[List[int]]:
        """
        Returns if the word is in the trie.
        """
        results = []
        node = self.root

        while word:
            if node.word_id >= 0:
                if self.is_palindrome(word):
                    results.append([index, node.word_id])
            if not word[0] in node.children:
                return results
            node = node.children[word[0]]
            word = word[1:]

        if node.word_id >= 0 and node.word_id != index:
            results.append([index, node.word_id])

        for palindrome_word_id in node.palindrome_word_ids:
            results.append([index, palindrome_word_id])

        return results

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")
    print(trie.search("app"))      # True
