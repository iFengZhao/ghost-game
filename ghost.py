# Implement a Trie data structure
class Trie:
    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        tree = self.dict
        for char in word:
            if char not in tree:
                tree[char] = {}
            tree = tree[char]
        tree['@'] = '@'

    def is_word(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.dict
        for char in word:
            if char not in tree:
                return False
            tree = tree[char]
        if '@' in tree:
            return True
        return False

    def is_prefix(self, prefix: str) -> bool:
        """
        Returns if prefix is the prefix of any word in the trie.
        """
        tree = self.dict
        for char in prefix:
            if char not in tree:
                return False
            tree = tree[char]
        return True