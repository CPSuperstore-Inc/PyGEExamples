"""
Description:
    The "Player" object. This object is the object the player controls. It must jump over barriers it comes across
    And attempt to avoid the laser which follows it

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
from time import time

from PyGE.DisplayMethods import SpriteSheet
from PyGE.Objects import ObjectBase

from source.Barrier import Barrier

PLAYER_WIDTH = 75       # the width of the player

g = -9.80665            # the acceleration due to gravity constant (same as on Earth)


class Player(ObjectBase):
    """
    This object is the object the player controls. It must jump over barriers it comes across
    And attempt to avoid the laser which follows it
    """
    def modify_args(self, args:dict):
        # place the player on the ground
        args["y"] = self.get_var("ground-y")
        return args

    def oncreate(self):
        # calculate the player's position with respect to the ground
        # remember that an object's x and y refer to the top-left corner
        self.ground_y = self.get_var("ground-y") - (PLAYER_WIDTH * 2)
        self.ground = self.get_var("ground-y")

        # the player's vertical velocity (used in jump physics)
        self.vv = 0

        # the time the player has started jumping (0 for no jump)
        self.t = 0

        # the time to stop using the "damaged" spritesheet
        self.damaged_until = None

        # set the display method to the player running animation
        self.set_display_method(SpriteSheet(self.screen, "player_running"))

        # the total distance the player has walked
        self.distance = 0

        # if the player is currently walking
        self.walking = False

    def draw(self):
        if self.damaged_until is not None:
            # if the player should still be in a damaged state, switch to the player_running spritesheet
            if self.damaged_until - time() <= 0:

                # if the time is up, change back to the regular spritesheet, and reset the damaged counter
                self.set_display_method(SpriteSheet(self.screen, "player_running"))
                self.damaged_until = None

        # draw the player to the screen
        self.draw_to_screen()

    def onkeydown(self, unicode, key, modifier, scancode):
        if key == 100:
            # if the "D" key is pressed, set the walking state to True
            self.walking = True

        if key == 32 and self.vv == 0:
            # if the "SPACE" key is pressed, and the player's vertical velocity is 0 (not jumping), jump
            self.jump()

    def onkeyup(self, key, modifier, scancode):
        if key == 100:
            # if the player releases the "D" key, set the walking state to False
            self.walking = False

    def update(self, pressed_keys):
        if pressed_keys[100]:
            # if the "D" key is being pressed, add to the player's distance
            self.distance += 1

        if self.t != 0:
            # if the player is jumping, calculate the timedelta, and update the time of last jump process
            delta = time() - self.t
            self.t = time()

            # calculate the new vertical velocity (v2 = v1 + 2aΔd) and apply it to the player
            self.vv += (g * delta)
            self.y -= self.vv

        if self.y + (PLAYER_WIDTH * 2) > self.ground:
            # if the player touches the ground, reset jump physics properties
            self.y = self.ground_y
            self.t = 0
            self.vv = 0

    def jump(self, velocity=8):
        # start the player's jump path with the given initial velocity
        self.t = time()
        self.vv = velocity

    def oncollide(self, obj:'ObjectBase'):
        if type(obj) is Barrier:
            # if the player collides with a barrier, delete the barrier
            obj.delete()

            # switch to the damaged spritesheet, and keep it like so for 3s
            self.set_display_method(SpriteSheet(self.screen, "player_hurt"))
            self.damaged_until = time() + 3

            # remove 1 life from the player
            self.broadcast_message("remove_life")
