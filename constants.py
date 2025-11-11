# region Module Description And Imports.
"""Constants for the AutoClicker program."""

from enum import IntEnum, StrEnum
from pathlib import Path
from textwrap import dedent

# endregion.

# region AutoClicker Constants.


class Timings(IntEnum):
    """Timing related constants for the AutoClicker.

    Attributes:
        COUNTDOWN (int): Seconds before clicking starts.
        PAUSE_TIME (int): Pause duration after resuming clicking.
        CLICKS_INTERVAL (float): Delay between each automated click.
        TIME_ELAPSED (float): Interval to trigger optional pause dialog.
    """

    COUNTDOWN = 5
    PAUSE_TIME = 2
    CLICKS_INTERVAL = 0.2
    TIME_ELAPSED = 10.0


class GuiTexts(StrEnum):
    """GUI messages and button labels displayed to the user.

    Attributes:
        START_MSG (str): Message shown before clicking starts.
        STOP_MSG (str): Message shown when pausing to ask whether to continue.
        START_CLICKING (str): Label for confirming to start clicking.
        STOP_CLICKING (str): Label for canceling or stopping the clicker.
    """

    START_MSG = """
    Press OK to START the AutoClicker.

    Then, you will have 5 seconds to position the cursor.

    If you enabled the 10-second pause option, the program
    will periodically ask whether to continue clicking.

    You can always move the mouse to any screen corner
    to quit immedidately.
    """
    STOP_MSG = """
    Press CANCEL to quit, or OK to continue clicking.

    If you press OK, you have 2 seconds to move the cursor
    back to the desired position.
    """
    START_CLICKING = "OK"
    STOP_CLICKING = "Cancel"


class ArgsText(StrEnum):
    """Command-line arguments constants.

    Attributes:
        ARGS_DESCRIPTION (str): Description shown in argparse help.
        PAUSE_ARG_NAME (str): Name of the pause flag.
        PAUSE_ARG_HELP (str): Help text for the pause flag.
        SOUND_ARG_NAME (str): Name of the sound flag.
        SOUND_ARG_HELP (str): Help text for the sound flag.
    """

    ARGS_DESCRIPTION = "Simple auto clicker."
    PAUSE_ARG_NAME = "--pause-every-10"
    PAUSE_ARG_HELP = "Enable periodic pauses to check if the user wants to continue clicking."
    SOUND_ARG_NAME = "--sound-on-exit"
    SOUND_ARG_HELP = (
        "Path to a sound file to play when PyAutoGUI failsafe stops the program. "
        "Defaults to a ping sound."
    )


class RuntimeMsgs(StrEnum):
    """Messages displayed during program execution.

    Attributes:
        COUNTDOWN_MSG (str): Countdown message before clicking starts.
        CLICKING (str): Message shown when clicking begins.
    """

    COUNTDOWN_MSG = f"\nStarting clicking in {Timings.COUNTDOWN} seconds..."
    CLICKING = "\nClicking..."


class ExitMsgs(StrEnum):
    """Messages printed when the program exits or is interrupted.

    Attributes:
        QUIT_EARLY_MSG (str): Message when the user cancels before starting.
        QUIT_MSG (str): Message when the user stops the clicker manually.
        FAILSAFE_QUIT_MSG (str): Message when PyAutoGUI failsafe is triggered.
        CTRLC_QUIT_MSG (str): Message when interrupted with Ctrl+C.
    """

    QUIT_EARLY_MSG = "\nClicker not started. Restart the program to run again."
    QUIT_MSG = "\nProgram stopped by user. Exiting..."
    FAILSAFE_QUIT_MSG = "\nMouse moved to a corner. Exiting..."
    CTRLC_QUIT_MSG = "\nKeyboard interrupt detected. Exiting..."


class SoundCons(StrEnum):
    """Sound-related constants and messages.

    Attributes:
        SOUND_PATH (Path): Default path to the bundled sound file.
        WRONG_SOUND_PATH (str): Warning shown if the provided sound path is invalid.
        SOUND_NOT_PLAYED (str): Message shown if playing the sound fails.
    """

    SOUND_PATH = str(Path(__file__).resolve().parent / "sound" / "stop.ogg")
    WRONG_SOUND_PATH = "\n" + dedent(
        """
    ⚠️  Warning: Sound file not found at '{expanded_path}'.
    Falling back to default sound '{default_path}'.
    """
    )
    SOUND_NOT_PLAYED = "Sound failed to play ({error})."


# endregion.
