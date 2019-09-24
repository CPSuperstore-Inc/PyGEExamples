from PyGE import pyge_application

from source.Player import Player, PLAYER_WIDTH
from source.Barrier import Barrier, BarrierManager, BARRIER_SIZE
from source.LifeCounter import LifeCounter
from source.Laser import Laser
from source.PressKey import PressKey

# create the spritesheet dictionary for the cache
spritesheets = {
    "player_running": {
        "path": "static/images/player/running.png", "w": 2, "h": 1, "duration": 0.125,
        "final_size": (PLAYER_WIDTH, PLAYER_WIDTH * 2)
    },
    "player_hurt": {
        "path": "static/images/player/hurt.png", "w": 2, "h": 1, "duration": 0.125,
        "final_size": (PLAYER_WIDTH, PLAYER_WIDTH * 2)
    }
}

# create the image dictionary for the cache
image = {
    "crate": {"path": "static/images/barrier/default.png", "w": BARRIER_SIZE, "h": BARRIER_SIZE}
}

# create the font dictionary for the cache
font = {
    "comfortaa20": {"path": "static/font/comfortaa/Comfortaa-Regular.ttf", "size": 20},
    "comfortaa50": {"path": "static/font/comfortaa/Comfortaa-Regular.ttf", "size": 50},
    "comfortaa45": {"path": "static/font/comfortaa/Comfortaa-Regular.ttf", "size": 45}
}

pyge_application(
    open("level.xml").read(),                                                           # The XML level data to use (you can pass in a string of XML instead of a file if you wish)
    "start",                                                                            # The room to start the application in
    custom_objects=[Player, Barrier, BarrierManager, LifeCounter, PressKey, Laser],     # The custom objects used in this application
    sprite_sheets=spritesheets,                                                         # The spritesheets which are cached before the application begins
    images=image,                                                                       # The images which are cached before the application begins
    font=font,                                                                          # The font which is cached before the application begins
    fullscreen=False,                                                                   # Do not use FullScreen mode
    auto_scale=False,                                                                   # Do not scale the screen to match the size of the monitor
    development_screen_size=(800, 600),                                                 # The size of the screen to develop on
    initial_variables={                                                                 # The initial variables to use in the application (used across many objects)
        "ground-y": 500
    },
    background_color=(255, 0, 255)                                                      # The background color of a room to use unless one is specified in the room tag of the XML (color="[some color]")
)