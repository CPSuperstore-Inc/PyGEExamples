"""
Usage:
    python SpaceShooter.py
    python3 SpaceShooter.py

Description:
    A small space battle game to showcase more of the engine's functionality.

Author(s): 
    Christopher Palazzolo.

File History:
    9/22/2019 - Initial file creation

Dependencies:
    The PyGE library. You can install it via "PyGEPull" application (http://pyge.pythonanywhere.com/downloads)
    The "PyGEPull" application will handle PyGE dependencies.

Additional Notes:
    This file was created to help users learn about PyGE, and its many capabilities
    Feel free to modify and make this file your own. Good luck :)
"""
from PyGE import pyge_application

from source.objects.EnemyHandler import EnemyHandler
from source.objects.Player import Player
from source.objects.Button import Button
from source.objects.Enemy import Enemy
from source.objects.Bullet import Bullet

# start the PyGE application
# see http://pyge.pythonanywhere.com/docs/PyGE#pyge_application for more information on the paramaters
pyge_application(
    open("rooms.xml").read(),                                                           # The XML level data to use (you can pass in a string of XML instead of a file if you wish)
    "menu",                                                                             # The room to start the application in
    images={                                                                            # The images which are cached before the application begins
        "player1": {"path": "static/images/player/player.png", "w": 32, "h": 32},
        "player2": {"path": "static/images/player/player2.png", "w": 32, "h": 32},
        "enemy":   {"path": "static/images/enemy/enemy.png", "w": 32, "h": 32}
    },
    font={                                                                              # The font files which are cached before the application begins
        "Querround16": {"path": "static/font/querround/QUERROUND.TTF", "size": 16}
    },
    custom_objects=[EnemyHandler, Player, Button, Enemy, Bullet],                       # The custom objects used in this application
    fullscreen=False,                                                                   # Do not use FullScreen mode
    auto_scale=False,                                                                   # Do not scale the screen to match the size of the monitor
    development_screen_size=(800, 600),                                                 # The size of the screen to develop on
)