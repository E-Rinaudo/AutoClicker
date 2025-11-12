#!/usr/bin/env python3

# region Module Description And Imports.
"""Simple auto clicker that clicks at the current mouse position.

Includes optional periodic pauses and sound notification on exit.
"""

import logging
import sys
import time

import pyautogui  # type: ignore
from playsound3 import playsound, playsound3

import logging_file
from args import ClickerArgs
from constants import ExitMsgs, GuiTexts, LogMsgs, RuntimeMsgs, SoundCons, Timings

# Set up the logging configuration.
logging_file.logging_configuration()
# logging_file.disable_logging()

# endregion.

# region AutoClicker Implementation.


class AutoClicker:
    """A simple auto clicker that clicks at the current mouse position.

    Attributes:
        pause (str): If True, stops every 10 seconds to check whether the user
            wants to continue or stop clicking.
        sound_path (str): Path to a sound file to play when the program stops if
            the user triggered PyAutoGUI's failsafe feature.
    """

    pause: str
    sound_path: str

    def __init__(self) -> None:
        """Initializes the AutoClicker with command-line arguments."""
        clicker_args = ClickerArgs().get_args()
        self.pause = clicker_args.pause_every_10
        self.sound_path = clicker_args.sound_on_exit

    def start_clicker(self) -> None:
        """Handles the workflow to start the clicker.

        Shows a dialog and allows time to position the mouse if the user
        starts the program.

        Exits early if the user cancels.
        """
        if self._start_clicking():
            self._allow_time_to_move()
        else:
            self._quit_early()

    def _start_clicking(self) -> bool:
        """Prompts the user whether they want to start the application.

        Returns:
            True if user clicks 'OK' to start the clicker; False otherwise.
        """
        return self._confirm_choice(
            GuiTexts.START_MSG, GuiTexts.START_CLICKING, self._start_clicking.__name__
        )

    def _confirm_choice(self, gui_msg: str, expected_button: str, caller_name: str) -> bool:
        """Shows a PyAutoGUI confirm dialog and checks the clicked button.

        Args:
            gui_msg: The message to show in the dialog.
            expected_button: The button text for the expected response.
            caller_name: Name of the calling method for logging.

        Returns:
            True if the expected button was clicked; False otherwise.
        """
        choice = pyautogui.confirm(gui_msg)  # type: ignore
        logging.info(LogMsgs.USER_CHOICE, choice, caller_name)
        return choice == expected_button

    def _allow_time_to_move(self) -> None:
        """Allows time to position the mouse before clicking."""
        print(RuntimeMsgs.COUNTDOWN_MSG)
        pyautogui.countdown(Timings.COUNTDOWN)

    def _quit_early(self) -> None:
        """Quits the program if the clicker was not started."""
        self.print_and_exit(ExitMsgs.QUIT_EARLY, LogMsgs.QUIT_EARLY)

    def print_and_exit(self, exit_msg: str, log_msg: str) -> None:
        """Prints the exit message and exits the program.

        Args:
            exit_msg: The message to print before exiting.
            log_msg: The message to log before exiting.
        """
        print(exit_msg)
        logging.info(log_msg)
        sys.exit(0)

    def run_clicker(self) -> None:
        """Runs the clicker application.

        Clicks repeatedly every 0.2 seconds at current cursor position.
        """
        logging.info(LogMsgs.CLICKER_STARTED)
        print(RuntimeMsgs.CLICKING)
        starting_time = time.monotonic()

        try:
            while True:
                pyautogui.click(interval=Timings.CLICKS_INTERVAL)

                now = time.monotonic()
                if self.pause and now - starting_time >= Timings.TIME_ELAPSED:
                    logging.info(LogMsgs.PAUSE)
                    if self._stop_clicking():
                        self.print_and_exit(ExitMsgs.QUIT, LogMsgs.QUIT)
                    else:
                        time.sleep(Timings.PAUSE_TIME)  # Pause to avoid immediate clicks.
                        starting_time = time.monotonic()  # Reset starting_time.
                        logging.info(LogMsgs.RESUMED_CLICKING)

        except pyautogui.FailSafeException:
            self._fail_safe_exit()

    def _stop_clicking(self) -> bool:
        """Prompts the user whether they want stop the application.

        Returns:
            True if user clicks 'Cancel' to quit the clicker; False otherwise.
        """
        return self._confirm_choice(
            GuiTexts.STOP_MSG, GuiTexts.STOP_CLICKING, self._stop_clicking.__name__
        )

    def _fail_safe_exit(self) -> None:
        """Exits the program when mouse is moved to a corner of the screen.

        Plays a sound and prints a message before exiting.
        """
        try:
            # Sound added since this is the only exit that isn’t immediately obvious.
            playsound(self.sound_path)
        except playsound3.PlaysoundException as err:
            print(SoundCons.SOUND_NOT_PLAYED.format(error=err))
            logging.error(LogMsgs.SOUND_NOT_PLAYED, err)
        self.print_and_exit(ExitMsgs.FAILSAFE_QUIT, LogMsgs.FAILSAFE_QUIT)


# endregion.
