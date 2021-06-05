#!/usr/bin/env python
"""
Instantiate objects from classes Trie, Player, and Ghost.
Start the game.
"""
__author__ = "Feng Zhao"
__version__ = "1.0.1"
__email__ = "fengzhao@gatech.edu"


if __name__ == '__main__':

    from ghost import Trie, Player, Ghost

    # Create Trie object with data from text file
    with open('wordlist_kevin_atkinson.txt') as f:
        word_list = f.read().splitlines()

    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)

    # Start game and initialize players.
    Ghost.welcome()

    read_rules = input("Hit 'y' to read rules of the game. \n"
                       "Hit any other keys to skip the rules.\n")

    Ghost.show_rules(read_rules)

    player_list = []
    name1 = input("Player1, please enter your name when you are ready.\n")
    player1 = Player(name1)
    player_list.append(player1)

    name2 = input("\nPlayer2, please enter your name when you are ready.\n")
    # Make sure the name is not duplicate
    while name2 == name1:
        print("\nSorry, the name you entered has been taken.\n")
        name2 = input("\nPlayer2, please enter your name when you are ready.\n")
    player2 = Player(name2)
    player_list.append(player2)

    # Instantiate a Ghost game object
    game = Ghost(player_list, word_trie)
    game.play()

    # Ask whether players would like to play next round
    next_round = input("Hit 'y' to play next round; any other keys to exit.\n")
    Ghost.replay(next_round, player1, player2, game)


