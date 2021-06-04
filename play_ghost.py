
if __name__ == '__main__':

    from ghost import Trie, Player, Ghost

    # Create Trie object with data from text file
    with open('wordlist_kevin_atkinson.txt') as f:
        word_list = f.read().splitlines()

    word_trie = Trie()
    for word in word_list:
        word_trie.insert(word)

    player_list = []

    # Start game and initialize players.
    print("***************************************************\n"
          "            Welcome to the Ghost game!\n"
          "Make sure you understand the rules before playing.\n"
          "***************************************************\n")

    name1 = input("Player1, please enter your name when you are ready.\n")
    player1 = Player(name1)
    player_list.append(player1)

    name2 = input("\nPlayer2, please enter your name when you are ready.\n")
    # make sure the name is not duplicate
    while name2 == name1:
        print("\nSorry, the name you entered has been taken.\n")
        name2 = input("\nPlayer2, please enter your name when you are ready.\n")
    player2 = Player(name2)
    player_list.append(player2)

    # Instantiate a Ghost game object
    game = Ghost(player_list, word_trie)
    game.play()

    # Ask whether players would like play next round
    next_round = input("Hit 'y' to play next round; any other keys to exit.\n")

    while next_round.lower() == 'y':
        player1.set_strike_count(0)
        player2.set_strike_count(0)
        game.play()
        next_round = input("Hit 'y' to play next round; any other keys to exit.\n")

    print("***************************************************\n"
              "Thanks for playing Ghost. See you next time.\n"
          "***************************************************\n")
