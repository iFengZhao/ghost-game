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


# Implement a Player class
class Player:

    def __init__(self, name):
        self.name = name
        self.__strike_count = 0
        self.entry = None

    def get_strike_count(self):
        return self.__strike_count

    def set_strike_count(self, new_value: int) -> None:
        self.__strike_count = new_value

    def enter_letter(self) -> None:
        """
        Prompt the player to enter a letter.
        """
        print(f"\n\n{self.name}, it's your turn.\n")
        self.entry = input("Please enter a single letter:\n")
        while not self.correct_entry(self.entry):
            self.error_messages(self.entry)
            self.entry = input("Please enter a single letter:\n")

    @staticmethod
    def correct_entry(entry: str) -> bool:
        """
        Examine whether the entry is a single letter.
        """
        if len(entry) == 1 and entry.isalpha():
            return True
        return False

    @staticmethod
    def error_messages(entry: str) -> None:
        """
        Show error messages.
        """
        if len(entry) > 1:
            print("\nYou entered more than one character.")
        if not entry.isalpha():
            print("\nThat's not a letter")