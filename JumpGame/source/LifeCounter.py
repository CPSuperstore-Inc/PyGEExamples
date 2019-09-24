"""
Description:
    The "LifeCounter" object. This object is responsible for displaying some variable value on screen

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
from PyGE.DisplayMethods import Text
from PyGE.Objects import ObjectBase


class LifeCounter(ObjectBase):
    """
    This object is responsible for displaying some variable value on screen
        :param template: The string template to use where {l} is replaced with the player's lives, 
                         and {s} is replaced with the player's score
    """
    def modify_args(self, args:dict):
        # set the y position. The x position is specified in the XML
        args["y"] = 10
        return args

    def oncreate(self):
        # get the font
        self.font = "comfortaa20"

        # set the initial lives and points
        self.lives = 5
        self.points = 0

        # get the string template
        self.template = self.get_mandatory_arguement("template")

        # set the display method using some temporary text
        self.set_display_method(
            Text(self.screen, self.font, "loading...", (255, 255, 255))
        )

        # reload the text
        self.reload_font()

    def reload_font(self):
        # set the text to the specified string format replacing appropriate values
        self.display.set_text(
            self.template.format(l=self.lives, s=self.points)
        )

    def draw(self):
        # draw the text to the screen
        self.draw_to_screen()

    def onmessagerecieve(self, message:str):
        if message == "remove_life":
            # if this object receives the message to remove a life, remove a life and reload the font
            self.lives -= 1
            self.reload_font()

            if self.lives < 0:
                # if the number of lives is less than 0, switch to the loose room
                self.change_room("died")

        if message == "add_point":
            # if the the object receives the message to add a point, add the point and reload the font
            self.points += 1
            self.reload_font()
