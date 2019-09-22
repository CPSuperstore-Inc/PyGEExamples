"""
Description:
    The "Button" object. This is a click-able region on the screen with some text

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
from PyGE.Misc import AlarmClock
from PyGE.DisplayMethods import Text


class Button(ObjectBase):
    """
    This is a click-able region on the screen with some text. Clicking executes an action
        :param font: The name of the font to use from the cache
        :param text: The text to render on the button
        :param supplementary: The action ID to execute on click
    """
    color = (0, 255, 0)
    buffer = 5

    def oncreate(self):
        # set the display method as a new text object
        # use the font and text specified as params
        self.set_display_method(
            Text(
                self.screen,
                self.get_mandatory_arguement("font", str),
                self.get_mandatory_arguement("text"),
                self.color
            )
        )

        self.w = 300

        # create an alarm clock which expires every 0.125s (8x/s) and start the clock
        self.spawn_countdown = AlarmClock(0.125)
        self.spawn_countdown.start()

        # get the supplementary action to take on click
        self.sup = self.get_mandatory_arguement("supplementary", str)

        # recalculate the button's position
        self.recalculate_position()

    def draw(self):
        # draw the bordering text to the screen, and text in the center of the border
        self.draw_rect(self.color, *self.rect, 1)
        self.draw_to_screen(x=self.calculate_center(self.display.w)[0], y=self.y + self.buffer)

    @property
    def rect(self):
        # return the rect data (x, y, w, h) of the border of the button
        return self.x, self.y, self.w + 2 * self.buffer, self.h + 2 * self.buffer

    def onclick(self, button, pos):
        # when clicked, execute the appropriate action

        if self.sup == "1":
            # start a singleplayer game
            self.change_room("arenaSingle")

        elif self.sup == "2":
            # start a multiplayer game
            self.change_room("arenaDouble")

        elif self.sup == "3":
            # quit the game
            self.attempt_quit()

    def onroomleave(self, next_room):
        # when the room containing this button is left, reload the next room
        # (preventing the previous room from being resumed)
        self.reload_room(next_room)