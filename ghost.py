#!/usr/bin/env python
"""
Implement classes： Trie, Player, and Ghost.
"""
__author__ = "Feng Zhao"
__version__ = "1.0.1"
__email__ = "fengzhao@gatech.edu"

import random


# Implement a Trie data structure
class Trie:
    """
    Trie is an efficient information reTrieval data structure.
    Using Trie, search complexities can be brought to optimal limit (key length).
    """
    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Insert a word to the trie.
        """
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

    def __init__(self, name: str):
        self.name = name
        self.__strike_count = 0
        self.entry = None

    def get_strike_count(self):
        return self.__strike_count

    def set_strike_count(self, new_value: int) -> None:
        self.__strike_count = new_value

    def up_strike_count(self) -> None:
        self.__strike_count += 1

    def enter_letter(self) -> None:
        """
        Prompt the player to enter a letter.
        """
        print("\n***************************************************\n"
              f"{self.name}, it's your turn.")
        self.entry = input("Please enter a single letter:\n")
        while not self.is_correct_entry(self.entry):
            self.show_error_messages(self.entry)
            self.entry = input("Please enter a single letter:\n")

    @staticmethod
    def is_correct_entry(entry: str) -> bool:
        """
        Examine whether the entry is a single letter.
        """
        if len(entry) == 1 and entry.isalpha():
            return True
        return False

    @staticmethod
    def show_error_messages(entry: str) -> None:
        """
        Show error messages.
        """
        if len(entry) > 1:
            print("\nYou entered more than one character.")
        if not entry.isalpha():
            print("\nThat's not a letter")


# Implement a Ghost class for the game
class Ghost:

    def __init__(self, player_list: list, word_trie: Trie):
        self.player_list = player_list
        self.current_player = None
        self.next_player = None
        self.trie = word_trie
        self.round_number = 1

    def play(self) -> None:
        """
        Main method in the class.
        """

        print("***************************************************\n"
              f"                    Round{self.round_number}")

        prefix = ""

        self.draw_starting_player()

        game_on = True
        while game_on:
            self.current_player.enter_letter()

            temp_prefix = (prefix + self.current_player.entry).lower()

            while not self.is_valid_move(temp_prefix):

                print("\nThe letter entered will not form the beginning of a\n"
                      "valid word.Try again!\n")
                self.current_player.up_strike_count()
                strike_count = self.current_player.get_strike_count()
                print(f"You've got {strike_count} strike(s)!")
                if strike_count == 3:
                    game_on = False
                    self.show_game_over_message()
                    break
                else:
                    self.current_player.enter_letter()
                    temp_prefix = (prefix + self.current_player.entry).lower()

            prefix = (prefix + self.current_player.entry).lower()
            print(f"The current prefix is {prefix.upper()}-. It's a valid move.")

            if self.is_longer_valid_word(prefix):
                self.show_game_over_message()
                break
            else:
                self.change_turns()

        self.round_number += 1

    def draw_starting_player(self) -> None:
        """
        Randomly assign a player to enter first.
        """
        self.current_player = random.choice(self.player_list)
        if self.current_player == self.player_list[0]:
            self.next_player = self.player_list[1]
        else:
            self.next_player = self.player_list[0]

    def change_turns(self) -> None:
        """
        Take turns for the players.
        """
        self.current_player, self.next_player = self.next_player, self.current_player

    def is_valid_move(self, prefix: str) -> bool:
        """
        Returns if the letter entered will form the beginning of a valid word.
        """
        if self.trie.is_prefix(prefix):
            return True
        return False

    def is_longer_valid_word(self, prefix: str) -> bool:
        """
        Returns if the game is over.
        """
        if len(prefix) > 3 and self.trie.is_word(prefix):
            print(f"\n{prefix.upper()} is a real word with more than 3 letters.")
            return True
        return False

    def show_game_over_message(self) -> None:
        print("***************************************************\n"
              "                   **Gave over**\n\n"
              f"{self.current_player.name}, you lost! {self.next_player.name} won the game!\n"
              "***************************************************\n")

    @staticmethod
    def welcome() -> None:
        print("***************************************************\n"
              "            Welcome to the Ghost game!\n"
              "Make sure you understand the rules before playing.\n"
              "***************************************************\n")

    @staticmethod
    def replay(next_round: str, player1: Player, player2: Player, game) -> None:
        while next_round.lower() == 'y':
            player1.set_strike_count(0)
            player2.set_strike_count(0)
            game.play()
            next_round = input("Hit 'y' to play next round; \n"
                               "any other keys to exit.\n")

        print("***************************************************\n"
                  "Thanks for playing Ghost. See you next time.\n"
              "***************************************************\n")

    @staticmethod
    def show_rules(read_rules: str) -> None:
        if read_rules.lower() == 'y':
            print("***************************************************\n"
                  "                The rules of GHOST:\n\n"
                  "- GHOST is a two-player word game\n"
                  "- Player 1 starts by entering a letter\n"
                  "- Player 2 adds a letter to the first letter\n"
                  "- The players continue taking turns adding letters\n"
                  "- Each new letter must continue to spell\n"
                  "   the beginning of a real word\n"
                  "- If a player adds an invalid letter to the word\n"
                  "   this player gets a strike and need to repeat\n"
                  "   their turn\n"
                  "- Once a player gets 3 strikes, or completes a valid\n"
                  "   word longer than 3 letters, that player loses and\n"
                  "   the other player wins\n"
                  "***************************************************")
        else:
            print("***************************************************\n"
                  "                The game starts now")
