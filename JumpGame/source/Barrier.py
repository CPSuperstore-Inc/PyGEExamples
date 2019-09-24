"""
Description:
    The "Barrier" object. This object spawns each time the player moves a random distance
    On collision with the player, the player will loose a life
    
    The "BarrierManager" abstract object. This handles the spawning of barriers
    It also handles the drawing of the ground
    
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
import random

from PyGE.Objects import ObjectBase, AbstractObjectBase
from PyGE.DisplayMethods import Image, Color
from PyGE.Globals import get_var
from PyGE import get_optional


BARRIER_SIZE = 64

class Barrier(ObjectBase):
    """
    This object spawns each time the player moves a random distance
    On collision with the player, the player will loose a life
    """
    def oncreate(self):
        # set the display method to be the "crate" image (loaded into cache)
        self.set_display_method(Image(self.screen, "crate"))

        # get the player and laser
        self.player = self.get_all_type("Player")[0]
        self.laser = self.get_all_type("Laser")[0]

        # set that this object has not issued any points to the player
        self.point_issued = False

    def modify_args(self, args:dict):
        # set the x and y position of the player (the x value is optional)
        # the x value has an inset, because starting off screen will result in it being destroyed
        args["x"] = get_optional(args, "x", "sw - 2")
        args["y"] = get_var("ground-y") - BARRIER_SIZE
        return args


    def draw(self):
        # draw the image to the screen
        self.draw_to_screen()

    def update(self, pressed_keys):
        if pressed_keys[100]:
            # if the player presses the "d" key, move at a velocity of 200 towards the player
            self.time_move(-200, 0)

        if self.x <= self.laser.x + self.laser.w:
            # if the barrier collides with the laser, delete the barrier
            # note that the oncollide was not used due to a bug which we are working on a fix for
            self.delete()

        if self.point_issued is False:
            if self.x + BARRIER_SIZE + 5 < self.player.x:
                # if this object has not issued any points, and has passed the player with a buffer of 5px
                # broadcast to add points for the player
                self.broadcast_message("add_point")
                self.point_issued = True

    def onscreenleave(self):
        # if the barrier leaves the screen, delete it
        self.delete()


class BarrierManager(AbstractObjectBase):
    """
    This object handles the spawning of barriers and also handles the drawing of the ground
    """
    def oncreate(self):
        # get the player object
        self.player = self.get_all_type("Player")[0]

        # calculate the distance to travel before spawning the next barrier
        self.calculate_next_spawn()

        # set the display method to be a solid color to represent the ground
        self.set_display_method(Color(self.screen, (0, 255, 255), self.screen_w, self.screen_h - get_var("ground-y")))

        # set the y position
        self.y = get_var("ground-y")

    def calculate_next_spawn(self):
        # calculate the distance the player must travel before spawning a new barrier
        # this can be between 50 and 100 units
        self.next_spawn = self.player.distance + random.randint(50, 100)

    def update(self, pressed_keys):
        if self.next_spawn <= self.player.distance:
            # if the player has passed the spawn threshold, spawn the next barrier
            # also, calculate the next position
            self.calculate_next_spawn()
            self.add_object("Barrier", {})

    def draw(self):
        # draw the barrier to the screen
        self.draw_to_screen()
