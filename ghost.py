import random

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


class Ghost:

    lookup = None

    def __init__(self, word_trie):
        self.player_list = []
        self.current_player = None
        self.word_trie = word_trie

    def play(self) -> None:
        prefix = ""

        self.initialize_players()
        self.starts_first()

        while True:
            self.current_player.enter_letter()

            prefix = (prefix + self.current_player.entry).lower()

            strike_count = self.current_player.get_strike_count()
            while strike_count < 3:

                if not self.valid_move(prefix):
                    strike_count += 1
                    self.current_player.set_strike_count(strike_count)
                    print("Sorry, that's not a prefix of a real word. Try again!\n")
                    print(f"You've got {strike_count} strike(s)!")
                    if strike_count < 3:
                        self.current_player.enter_letter()
                else:
                    break

            if not self.game_over(self.current_player, prefix):
                self.change_turns()
            else:
                break

        print(f"\n{self.current_player.name}, you lost!")
        print("Game over!")

    def initialize_players(self) -> None:
        print("Welcome to the Ghost game!\n")
        name1 = input("Player1, please enter your name when you are ready.\n")
        player1 = Player(name1)
        self.player_list.append(player1)

        name2 = input("\nPlayer2, please enter your name when you are ready.\n")

        while not self.valid_name(name1, name2):
            name2 = input(
                "\nPlayer2, the name you entered has been taken. Please enter a different name when you are ready.\n")

        player2 = Player(name2)
        self.player_list.append(player2)

    def starts_first(self) -> None:
        self.current_player = random.choice(self.player_list)

    def change_turns(self) -> None:
        if self.current_player == self.player_list[0]:
            self.current_player = self.player_list[1]
        else:
            self.current_player = self.player_list[0]

    @staticmethod
    def valid_name(name1, name2) -> bool:
        if name2 != name1:
            return True
        return False

    def valid_move(self, prefix) -> bool:
        if self.word_trie.is_prefix(prefix):
            return True
        return False

    def game_over(self, player, prefix) -> bool:
        if player.get_strike_count() == 3:
            return True
        elif len(prefix) > 3 and self.word_trie.is_word(prefix):
            return True
        return False
