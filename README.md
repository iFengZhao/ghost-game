## About the project

**GHOST** is a word game where players take turn adding letters to a word. The first to spell a complete word that is greater than 3 letters loses. When adding a letter to the word, you must ensure that you are spelling the beginning of a valid word. The strategy is to corner your opponent into having no choice but to complete the word and lose the game.  
  
For more details about the game and its rules, please refer to the "GHOST interview question.pdf" file in the doc folder.  
For more technical details about the programming implementation, please refer to the "developer's doc.md" file in the doc folder. 

Three essential files are required to successfully play the game.
- **wordlist_kevin_atkinson**: The word list used to construct a Trie object to aid the search and validation in the game.
- **ghost.py**: Includes three classes I created for the project: Trie, Player, and Ghost
- **play_ghost.py**: Instantiate objects from classes Trie, Player, and Ghost. **Execute this file to start the game**.  
  
## Requirements
- Python 3.9 or higher
## Installation
No other package is needed to be installed. 
## Usage
To play the game, make sure the three files above are in the same directory and execute the **play_ghost.py** file.
## Known issues
Currently none.
## Next steps
Save a record for each round of the game.
## Note
This project was first hosted in my Gatech Github account. I moved it to my personal GitHub account to ease sharing.
