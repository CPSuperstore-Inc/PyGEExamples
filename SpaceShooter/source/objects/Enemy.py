"""
Description:
    The "Enemy" object. This object flies towards the player. 
    If shot, 100 points are issued
    If it leaves the screen, 50 points are lost

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
from PyGE.Objects import ObjectBase, Text
from PyGE.Globals import get_image

import source.GlobalVariable as GlobalVariable

class Enemy(ObjectBase):
    """
    The "Enemy" object. This object flies towards the player. 
    If shot, 100 points are issued
    If it leaves the screen, 50 points are lost
    """

    velocity = 100
    def oncreate(self):
        # rotate the enemy image to face the player (-90 degrees)
        self.image = self.rotate_object(get_image("enemy"), -90)
        self.w, self.h = self.image.get_size()

        # get the scoreboard object
        self.scoreboard = self.get_all_type("Text")[0]     # type: Text

        self.angle = 0

    def update(self, pressed_keys):
        # move the player along its angle at its set velocity
        self.move_angle_time(self.velocity)

    def oncollide(self, obj:'ObjectBase'):
        if obj.object_type == "Bullet":
            # if this object collides with a bullet
            # delete both this object and the bullet
            # add 100 points to the scoreboard
            self.delete()
            self.delete(obj)

            self.change_score(100)

    def onscreenleave(self):
        # if this ship leaves the screen, remove 50 points, and delete this ship
        self.delete()
        self.change_score(-50)

    def draw(self):
        # draw the image to the screen
        self.draw_to_screen(self.image)

    def change_score(self, delta:int):
        # change the score, and update the scoreboard's text
        GlobalVariable.score += delta
        self.scoreboard.set_text("Score: {}".format(GlobalVariable.score))
