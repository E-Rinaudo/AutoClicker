# region Module Description And Imports.
"""Constants for the AutoClicker program."""

from enum import IntEnum, StrEnum
from pathlib import Path
from textwrap import dedent

# endregion.

# region AutoClicker Constants.

# Path for the log file
LOG_FILE = str(Path(__file__).resolve().parent / "log_file.txt")


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
        STOP_CLICKING (str): Label for stopping the clicker.
    """

    START_MSG = """
    Press OK to START the AutoClicker.

    Then, you will have 5 seconds to position the cursor.

    If you enabled the 10-second pause option, the program
    will periodically ask whether to continue clicking.

    You can always move the mouse to any screen corner
    to quit immediately.
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

    ARGS_DESCRIPTION = (
        "AutoClicker: a simple tool to automatically click at the current mouse position. "
        "The program supports optional periodic pauses to confirm whether you want to continue, "
        "and includes PyAutoGUI failsafe protection with an optional sound notification. "
        "Command-line arguments can be used to enable the pauses or sound."
    )
    PAUSE_ARG_NAME = "--pause-every-10"
    PAUSE_ARG_HELP = "Enable periodic pauses to check whether to continue clicking."
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
    """Messages printed when the program exits.

    Attributes:
        QUIT_EARLY (str): Message when the user cancels before starting.
        QUIT (str): Message when the user stops the clicker manually.
        FAILSAFE_QUIT (str): Message when PyAutoGUI failsafe is triggered.
        CTRLC_QUIT (str): Message when interrupted with Ctrl+C.
    """

    QUIT_EARLY = "\nClicker not started. Restart the program to run again."
    QUIT = "\nProgram stopped by user. Exiting..."
    FAILSAFE_QUIT = "\nMouse moved to a corner. Exiting..."
    CTRLC_QUIT = "\nKeyboard interrupt detected. Exiting..."


class SoundCons(StrEnum):
    """Sound-related constants and messages.

    Attributes:
        DEFAULT_SOUND_PATH (str): Default path to the bundled sound file.
        INVALID_SOUND_PATH (str): Warning shown if the custom sound path is invalid.
        SOUND_NOT_PLAYED (str): Message shown if playing the sound fails.
    """

    DEFAULT_SOUND_PATH = str(Path(__file__).resolve().parent / "sound" / "stop.ogg")
    INVALID_SOUND_PATH = dedent(
        """
    ⚠️  Warning: Sound file not found at '{custom_path}'.
    Falling back to default sound '{default_path}'.
    """
    )
    SOUND_NOT_PLAYED = "Sound failed to play ({error})."


class LogMsgs(StrEnum):
    """Logging messages used throughout the AutoClicker.

    Attributes:
        QUIT_EARLY (str): Log message when the user quits before starting.
        CLICKER_STARTED (str): Log message when the clicker starts.
        QUIT (str): Log message when the user quits the program.
        USER_CHOICE (str): Log message recording user's GUI choice.
        PAUSE (str): Log message when the clicker pauses.
        RESUMED_CLICKING (str): Log message when the clicker resumes.
        SOUND_NOT_PLAYED (str): Log message when sound playback fails.
        FAILSAFE_QUIT (str): Log message when the failsafe is triggered.
        CTRLC_QUIT_LOG (str): Log message when the clicker is interrupted with Ctrl+C.
        USING_DEFAULT_SOUND (str): Log message when using the default sound file.
        INVALID_SOUND_PATH (str): Log message when a custom sound path is invalid.
        CUSTOM_SOUND_SET (str): Log message when a custom sound path is set.
        RUNTIME_ERR (str): Log message for runtime errors during path expansion.
        SOUND_NOT_FOUND_ERR (str): Log message when the sound file is not found.
    """

    QUIT_EARLY = "User quit before starting the clicker."
    CLICKER_STARTED = "AutoClicker started."
    QUIT = "User quit the clicker."
    USER_CHOICE = "User clicked %s when %s was called."  # (PyAutoGUI Button, Method Name)
    PAUSE = "Pausing to prompt user whether to keep clicking."
    RESUMED_CLICKING = "AutoClicker resumed clicking after pause."
    SOUND_NOT_PLAYED = "Sound failed to play (%s)."  # (Error)
    FAILSAFE_QUIT = "AutoClicker quit due to PyAutoGUI failsafe."
    CTRLC_QUIT_LOG = "AutoClicker quit due to KeyboardInterrupt."
    USING_DEFAULT_SOUND = "Using default sound file."
    INVALID_SOUND_PATH = "Invalid custom path: {path}. " + USING_DEFAULT_SOUND  # (Custom Path)
    CUSTOM_SOUND_SET = "Custom sound path set to: {path}"  # (Custom Path)
    RUNTIME_ERR = "Could not determine home directory for '%s'."
    SOUND_NOT_FOUND_ERR = "Sound file not found at '%s'."  # (Custom Path)


# endregion.
