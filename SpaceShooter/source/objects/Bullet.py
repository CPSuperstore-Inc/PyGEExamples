"""
Description:
    The "Bullet" object. This object is shot by the player at the enemy ships

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


class Bullet(ObjectBase):
    """
    This object is shot by the player at the enemy ships. When shot the player gains points
        :param angle: The angle to shoot the bullet in radians
        :param velocity: The velocity to shoot the bullet
    """
    def oncreate(self):
        # Get the angle and velocity if the bullet from the provided arguments
        self.angle = self.get_mandatory_arguement("angle", float)
        self.velocity = self.get_optional_arguement("velocity", 200, float)

        # calculate the bullet's width and height
        self.radius = 1
        self.w = self.radius * 2
        self.h = self.radius * 2

    def draw(self):
        # draw the circle which represents the bullet to the screen
        self.draw_circle((255, 255, 255), int(self.x), int(self.y), self.radius)

    def update(self, pressed_keys):
        # move the bullet across the screen using time-based movement
        self.move_angle_time(self.velocity)

    def onscreenleave(self):
        # when the bullet leaves the screen, delete it
        self.delete(self)