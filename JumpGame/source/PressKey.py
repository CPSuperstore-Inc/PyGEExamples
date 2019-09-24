"""
Description:
    The "PressKey" object. This object handles the "Press Any Key To Continue..." text and action handler

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


class PressKey(ObjectBase):
    """
    This object handles the "Press Any Key To Continue..." text and action handler
        :param next: The name of the room to switch to on keypress
    """
    def oncreate(self):
        # set the display method of the instructions, and recalculate the text position
        self.set_display_method(Text(self.screen, "comfortaa20", "Press Any Key To Continue...", (255, 255, 255)))
        self.recalculate_position()

        # get the name of the room to switch to when a key is pressed
        self.next = self.get_mandatory_arguement("next")

    def draw(self):
        # draw the text to the screen
        self.draw_to_screen()

    def onkeydown(self, unicode, key, modifier, scancode):
        # when the user presses a key, reload and switch to the next room
        self.reload_room(self.next)
        self.change_room(self.next)
