#!/usr/bin/env python3

# region Module Description And Imports.
"""Simple auto clicker."""

import sys
import time

import pyautogui  # type: ignore
from playsound3 import playsound, playsound3

import constants as cons
from args import ClickerArgs

# Aliases for the Enums of constants.py.
Timings = cons.Timings
GuiTexts = cons.GuiTexts
RuntimeMsgs = cons.RuntimeMsgs
ExitMsgs = cons.ExitMsgs
SoundCons = cons.SoundCons

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
        clicker_args = ClickerArgs().parse_args()
        self.pause = clicker_args.pause_every_10
        self.sound_path = clicker_args.sound_on_exit

    def start_clicker(self) -> None:
        """Asks the user to start the clicker."""
        if pyautogui.confirm(GuiTexts.START_MSG) == GuiTexts.START_CLICKING:  # type: ignore
            self._allow_time_to_move()
        else:
            self._quit_early()

    def _allow_time_to_move(self) -> None:
        """Allows time to position the mouse before clicking."""
        print(RuntimeMsgs.COUNTDOWN_MSG)
        pyautogui.countdown(Timings.COUNTDOWN)

    def _quit_early(self) -> None:
        """Quits the program if the clicker was not started."""
        self.print_and_exit(ExitMsgs.QUIT_EARLY_MSG)

    def print_and_exit(self, exit_msg: str) -> None:
        """Prints the exit message and exits the program.

        Args:
            exit_msg: The message to print before exiting.
        """
        print(exit_msg)
        sys.exit(0)

    def run_clicker(self) -> None:
        """Runs the clicker application.

        Clicks repeatedly every 0.2 seconds at current cursor position.
        """
        print(RuntimeMsgs.CLICKING)
        starting_time = time.monotonic()

        try:
            while True:
                pyautogui.click(interval=Timings.CLICKS_INTERVAL)

                now = time.monotonic()
                if self.pause and now - starting_time >= Timings.TIME_ELAPSED:
                    if self._stop_clicking():
                        self.print_and_exit(ExitMsgs.QUIT_MSG)
                    else:
                        time.sleep(Timings.PAUSE_TIME)  # Pause to avoid immediate clicks.
                        starting_time = time.monotonic()  # Reset starting_time.

        except pyautogui.FailSafeException:
            self._fail_safe_exit()

    def _stop_clicking(self) -> bool:
        """Prompts the user whether they want stop the application.

        Returns:
            True if user wants to quit the clicker; False otherwise.
        """
        return pyautogui.confirm(GuiTexts.STOP_MSG) == GuiTexts.STOP_CLICKING  # type: ignore

    def _fail_safe_exit(self) -> None:
        """Exits the program when mouse is moved to a corner of the screen.

        Plays a sound and prints a message before exiting.
        """
        try:
            # Sound added since this is the only exit that isn’t immediately obvious.
            playsound(self.sound_path)
        except playsound3.PlaysoundException as err:
            print(SoundCons.SOUND_NOT_PLAYED.format(error=err))
        self.print_and_exit(ExitMsgs.FAILSAFE_QUIT_MSG)


# endregion.

if __name__ == "__main__":
    auto_clicker = AutoClicker()

    try:
        auto_clicker.start_clicker()
        auto_clicker.run_clicker()
    except KeyboardInterrupt:
        auto_clicker.print_and_exit(ExitMsgs.CTRLC_QUIT_MSG)
