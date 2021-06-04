## Above the project

**GHOST** is a word game where players take turn adding letters to a word. The first to spell a complete word that is greater than 3 letters loses. When adding a letter to the word, you must ensure that you are spelling the beginning of a valid word. The strategy is to corner your opponent into having no choice but to complete the word and lose the game.  
  
This doc shares some technical details about the programming implementation. 

Three essential files are required to successfully play the game.
- **wordlist_kevin_atkinson**: The word list used to construct a Trie object to aid the search and validation in the game.
- **ghost.py**: Includes three classes I created for the project: Trie, Player, and Ghost
- **play_ghost.py**: Instantiate objects from classes Trie, Player, and Ghost. **Execute this file to start the game**.  
## Requirements and usage
- Python 3.9 or higher. No other package is needed to be installed. 
- To play the game, make sure the three files above are in the same directory and execute the **play_ghost.py** file.
## Brief Object-oriented analysis and design (OOAD) 
Since this is a basic and very straigtforward project, I only wrote three classes for the programming implementation. I will explain below why I designed the game this way.
### Trie Class
Upon reading the game instruction file, I realized this would be a perfect use case for the data structure **Trie**. 
In the game, the system need to constantly two types of checking and validation:
- whether the input will form a valid word
- whether the input will form the begining of a valid word  

Whereas we need to creat a Trie object using the word list, the time complxity is not that bad.  
In the worst senario, the run time for creating a Trie would be ***O(mn)*** where m is the length of the longest key in the trie, and n, the total number of keys in the trie.  
Once the Word Trie was implemented, it will greatly improve the time efficiency of the two tasks mentioned above.
The time complexity of searching from a trie would be ***O(an)***, where a is the length of the word and n is the number of total words.
### Player Class
The Player Class was designed to have three attributes: 
player's name, player's strike count, and the letter a player entered.
In terms of the class method, only the enter_letter method is the essiential and it was used to prompt the palyer to enter a single letter and verify whether the input is allowed. 
Considering the strike_count is one of the two conditions that one palyer will lose, I made it a private attribute and the system would need to use the getter and setter methods to retrive and change it's value.
### Ghost Class
The Ghost Class is a system class and it has four attributes: 
- `player_list`: record which two players are playing
- `current_player`: at the begining of the game, it was randomly assigned by the system, in the following games, two palyers will take turn to be the current player
- `dict`: this is a Trie object that the system used to search and validate player's input
- `round_number`: once the game was started, the players may want to play multiple rounds. Hence added a function to ask whether they would like play next round and this attribute is used to record the number of rounds.  
  
There are many methods in this class, but the play method is the only essential one. The play method is designed to actrually start the game, assign which player enter first, verify whether the input is valid, and decide whether the game is over.
There are other methods in the class and they are utility functions. You may refer to the docstrings for these functions.
## User interaction walkthrough
Once the play_ghost.py was executed, a Trie object with data from text file will be created. This Trie object will be passed when a Ghost class is instantiated.
The game starts by showing a welcome message (via the static method `welcome` in the Ghost class)

## Known issues
Currently none.
## Next steps
Save a record for each round of the game.

## References
[Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)
[Wikipedia - Trie](https://en.wikipedia.org/wiki/Trie)
