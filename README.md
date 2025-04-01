# quest-demo
A demo for an upcoming text adventure game, most things unfinished

# Requirements

- Python 3+ and the standard libraries
- that's it i think

# How it works

The game map is technically a 100x100 grid list, but I've made the player trapped in a 10x10 cage to make it easier to test.
In the grid, there are currently 2 materials
- 0, being a wall
- 1, being ground

In future versions, more materials will be added to be specific.

There are 3 files:
- main.py
- game_map.py
- update.py

main.py is the "handler" of the game. The main thing that it just does is it displays the Main Menu, prompts the user, and calls the update() function which tells the player about their stats and position.

game_map.py is the script that has functions to create the map (init_map()), to check what tiles are next to the player (find_neighbour()) and to change the material value in the code to human readable text (format_material()).

update.py is the script that has the update() function, which tells the player about stats and position, and also figures out the level of the player based on XP, and the amount of XP required for the next level.

# How to play

You play by typing w, a, s or d to move around the map then pressing enter. The health and hunger, and level values are irrelevant to this demo.
