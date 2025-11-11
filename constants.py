"""Constants for the AutoClicker program."""

import os
from enum import StrEnum, IntEnum

START_MSG = """
Press OK to START the AutoClicker.

Then, you will have 5 seconds to move the mouse desired position.

If you enabled the 10-second pause option, the program will periodically ask whether to continue.

You can always move the mouse to any corner of the screen to stop the program immedidately.
"""
STOP_MSG = """
Press CANCEL to quit, or OK to continue clicking.

If you press OK, you will have 2 seconds to move the cursor back to the desired position.
"""
START_CLICKING = "OK"
STOP_CLICKING = "Cancel"

COUNTDOWN = 5
PAUSE_TIME = 2
CLICKS_INTERVAL = 0.2
TIME_ELAPSED = 10.0

SOUND_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sound/stop.ogg")
