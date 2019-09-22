"""
Description:
    The "EnemyHandler" object. This object handles the spawning of enemies at a set interval

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
from PyGE.Objects import AbstractObjectBase
from PyGE.Misc import AlarmClock

import source.GlobalVariable as GlobalVariable

import random


class EnemyHandler(AbstractObjectBase):
    """
    This object handles the spawning of enemies at a set interval
    It is Abstract, and not drawn to the screen
    """
    def oncreate(self):
        # set the spawn countdown to a delay of 0.125s (8x/s), and start it
        self.spawn_countdown = AlarmClock(0.125)
        self.spawn_countdown.start()

        # reset the player's score
        GlobalVariable.score = 0

    def update(self, pressed_keys):
        if self.spawn_countdown.finished:
            # if the countdown is complete, restart the clock, and spawn a new enemy
            self.spawn_countdown.restart()
            self.add_object("Enemy", {}, -30, random.randint(0, self.screen.get_height() - 32))
