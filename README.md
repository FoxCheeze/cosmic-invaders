# Cosmic Invaders
### Video Demo: <https://youtu.be/xZ_Qmt5XS3o>
### Description:

Cosmic Invaders is a very simple video game where you control a little ship and need to destroy
the alien invaders that are trying to destroy you planet. It was inspired by the game Asteroid and
Space Invaders.

Cosmic Invaders is a studing project made as the final project for CS50x course in 2022 by me
(Iago de Carvalho Damasceno aka. FoxCheeze)

#### Controls

> Use the arrow keys to rotate the ship to left or right.
> Press UP to rotate the ship in 180 degrees (fliping it)
> Press Space to shoot
> Use WASD to move the ship for any deired direction

### Project Structure

Cosmic Invaders was made in **Python**, using the **pyglet** framework, it was also used **Poetry** to manage
the virtual environment and **Blue** to keep the formating according to python's PEP 8.

All the necessary packages are in the file **pyproject.toml**

The game will save your highscore in a file called **cosmic-invaders-highscore.csv**

#### /audio/
This folder contains all the SFX used in the game

#### /cosmic_invaders/

##### main.py
The game is executed by running **main.py** located in **/cosmic_invaders/main.py**.
**main.py** contains the main loop of the game and all the initializer functions that set up the objects on the
scene

#### /cosmic_invaders/game/

##### bullet.py
This file contains the basic bullet class used as the super class for the player and enemies bullets

##### enemy_bullet.py
The class for the bullets used by the enemies to kill the player

##### enemy.py
The base class for every enemy (it is acuatually used to avoid cyclic dependency, it does nothing alone)

##### invader_alien.py
The Class for the fastest and hardest enemy of the game, killing it gives 500 points

##### invader_ship.py
The Class for the second hardest enemy of the game, killing it gives 250 points, it splits in 2 **invader_alien**
on death

##### invader_ufo.py
The Class for the easier enemy of the game, killing it gives 100 points, it splits in 2 **invader_ship** on death

##### invader.py
The base class for every enemy on the game

##### physical_object.py
The base class for every object that needs collision detecting

##### player_bullet.py
The class for the player's bullet

##### player.py
The base class for the player (it is acuatually used to avoid cyclic dependency, it does nothing alone)

##### resources.py
This file loads every image and audio used as the objects resources

##### settings.py
This file contains global variables and objects for the free (as in freedom) acess of the game's objects

##### ship.py
The Class used to construct the player, in other words, the real player class

##### utils.py
This file contains helper functions used by the other files

#### /fonts/
This folder contains all the fonts used in the game

#### /image/
This folder contains all the images used in the game
