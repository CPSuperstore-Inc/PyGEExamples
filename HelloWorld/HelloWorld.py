"""
Usage:
    python HelloWorld.py
    python3 HelloWorld.py
    
Description:
    Hello World tech test for the PyGE engine. Ensures the most basic functionality is working as expected.
    If successful, the text "Hello, World!" will appear in the center of the screen in blue, 30pt Arial font.
    Feel free to modify this application to learn more about PyGE and how it works
    
Author(s): 
    Christopher Palazzolo.

File History:
    9/17/2019 - Initial file creation
    
Dependencies:
    The PyGE library. You can install it via "PyGEPull" application (http://pyge.pythonanywhere.com/downloads)
    The "PyGEPull" application will handle PyGE dependencies.
    
Additional Notes:
    This file was created to help users learn about PyGE, and its many capabilities
    Feel free to modify and make this file your own. Good luck :)
"""
from PyGE import pyge_application

# define the font(s) used in the application
# Note that this will cause a warning. System fonts should not be used in distributed applications
# but one was used for sake of example
font = {"Arial30": {"path": "Arial", "size": 30}}

# the XML which stores the structure of the items to be drawn on screen
# in this example, we have some text which will be displayed in our font we created above
# cw, and ch will automatically place our text in the center of the screen
# the color can be RGB, CMYK (if so, surround in parentheses),
# HEX (if so, prepend the octothorpe # character),
# or the name of a color (based on the HTML color names: https://www.rapidtables.com/web/color/html-color-codes.html)

# this text is placed in a room (a screen), which is named "start"
# which is stored in a "building" (the entire collection of rooms)
xml = """
<building>
    <room name="start">
        <Text font="Arial30" text="Hello, World!" x="cw" y="ch" color="Blue"/>
    </room>
</building>
"""

# The PyGE application is started. The XML and starting room are set,
# we are importing our font dictionary, and setting the window caption

# we are also ensuring the window will be exactly 800x600px.
# when development is complete, remove thee fullscreen, auto_scale, and development_screen_size arguements
# and the screen, and everything will automatically scale to the user's screen
pyge_application(
    xml, "start", font=font, caption="PyGE Hello World Application",
    fullscreen=False, auto_scale=False, development_screen_size=(800, 600)
)