"""
Description:
    The "Laser" object. This is laser which chases the player through the game
    On collision with the player, there is an instant game over
    On collision with a barrier, destroy it

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

from PyGE.DisplayMethods import Color
from PyGE.Objects import ObjectBase

LASER_WIDTH = 5         # the width of the laser
SPEED_FORWARD = 175     # the velocity to move the laser forward when the player is idle
SPEED_BACKWARD = -50    # the velocity to move the laser backward when the player is moving


class Laser(ObjectBase):
    """
    The "Laser" object. This is laser which chases the player through the game
    On collision with the player, there is an instant game over
    On collision with a barrier, destroy it
    """
    def modify_args(self, args:dict):
        # start the laser in the top left corner
        args["y"] = 0
        args["x"] = 0
        return args

    def oncreate(self):
        # set the display method to be a solid red color
        self.set_display_method(Color(self.screen, (255, 0, 0), LASER_WIDTH, self.get_var("ground-y")))

        # select the player object
        self.player = self.get_all_type("Player")[0]

    def draw(self):
        # draw the laser to the screen
        self.draw_to_screen()

    def update(self, pressed_keys):
        if self.player.walking:
            # if the player is walking, move the laser at its backwards velocity
            self.time_move(SPEED_BACKWARD, 0)
            if self.x < -LASER_WIDTH:
                # if the laser is off screen, stop moving it
                self.x = -LASER_WIDTH
        else:
            # if the player is not walking, move the laser forward
            self.time_move(SPEED_FORWARD, 0)

        if self.player.x <= self.x + LASER_WIDTH:
            # if the player touches the laser, kill the player
            self.change_room("died")


