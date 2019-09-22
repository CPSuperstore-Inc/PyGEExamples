"""
Description:
    The "Player" object. This object is controllable by the player. It shoots bullets towards the oncoming enemies

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
from PyGE.Objects import ObjectBase
from PyGE.Globals import get_image
from PyGE.Misc import AlarmClock
from PyGE import rect_a_in_b

import pygame


class Player(ObjectBase):
    """
    This object is controllable by the player. It shoots bullets towards the oncoming enemies
        :param number: The player number (1 for player 1, 2 for player 2...)
    """
    def oncreate(self):
        # set object's angle and velocity
        self.angle = 90
        self.velocity = 100

        # get the player number, and image (based on the number)
        self.number = self.get_mandatory_arguement("number", int)
        self.image = self.rotate_object(get_image("player{}".format(self.number)))

        # update the player's size after the rotation
        self.w, self.h = self.image.get_size()

        # set the shot countdown to a delay of 0.125s (8x/s), and start it
        self.shot_cool_down = AlarmClock(0.125)
        self.shot_cool_down.start()

    @property
    def bullet_y(self):
        # get the y position of the center of the player, which is where the bullet can spawn
        return self.y + (self.h / 2)

    def draw(self):
        # draw to screen
        self.draw_to_screen(self.image)

    def update(self, pressed_keys):
        if (pressed_keys[pygame.K_w] == 1 and self.number == 1) or (pressed_keys[pygame.K_UP] == 1 and self.number == 2):
            # if the "move up" key is pressed (different for player 1 and 2) move the player up
            # also, check to ensure it has not left the screen
            self.time_move(0, self.velocity)
            self.boundary_check()

        if (pressed_keys[pygame.K_s] == 1 and self.number == 1) or (pressed_keys[pygame.K_DOWN] == 1 and self.number == 2):
            # if the "move down" key is pressed (different for player 1 and 2) move the player down
            # also, check to ensure it has not left the screen
            self.time_move(0, -self.velocity)
            self.boundary_check()

        if self.shot_cool_down.finished:
            # if the player is able to shoot, add the bullet, and reset the counter
            self.add_object("Bullet", {"angle": self.angle + 90}, x=self.x, y=self.bullet_y)
            self.shot_cool_down.restart()

    def boundary_check(self):
        # check if the player is completely inside the screen
        # if not, undo the previous movement
        if not rect_a_in_b(self.rect, self.screen.get_rect()):
            self.undo_last_move()

    def onkeydown(self, unicode, key, modifier, scancode):
        # if the player presses the "escape" key, return to the menu
        if key == pygame.K_ESCAPE:
            self.change_room("menu")