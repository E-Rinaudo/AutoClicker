#!/usr/bin/env python3

"""Simple auto clicker."""

import sys
import time

import pyautogui  # type: ignore
from playsound3 import playsound, playsound3

import constants as cons
from args import parse_args


# Add constants for all files' strings.
# Create an enum and put all fucking strings in there.
# Crea degli helper in args.py
# Read all files to make sure it's ok. README included.
# make sure it works.
# check with pylint etc
# Check how to write the attributes in init.


class AutoClicker:
    """A simple auto clicker that clicks at the current mouse position."""

    pause: str
    sound_path: str

    def __init__(self):
        """blabla

        Attributes:
            pause: If True, stops every 10 seconds to check whether the user
                wants to continue or stop clicking.
            sound_path: Path to a sound file to play when the program stops if
                the user triggered PyAutoGUI's failsafe feature.
        """
        args = parse_args()
        self.pause = args.pause_every_10
        self.sound_path = args.sound_on_exit

    def start_clicker(self) -> None:
        """Asks the user to start the clicker."""
        if pyautogui.confirm(cons.START_MSG) == cons.START_CLICKING:  # type: ignore
            self._allow_time_to_move()
        else:
            self._quit_early()

    def _allow_time_to_move(self) -> None:
        """Allows time to position the mouse before clicking."""
        print(f"\nStarting clicking in {cons.COUNTDOWN} seconds...")
        pyautogui.countdown(cons.COUNTDOWN)

    def _quit_early(self) -> None:
        """Quits the program if the clicker was not started."""
        print("\nClicker not started. Restart the program to run again.")
        sys.exit(0)

    def run_clicker(self) -> None:
        """Runs the clicker application.

        Clicks repeatedly every 0.2 seconds at current cursor position.
        """
        print("\nClicking...")
        starting_time = time.monotonic()

        try:
            while True:
                pyautogui.click(interval=cons.CLICKS_INTERVAL)

                now = time.monotonic()
                if self.pause and now - starting_time >= cons.TIME_ELAPSED:
                    if self._stop_clicking():
                        print("\nProgram stopped by user. Exiting...")
                        sys.exit(0)
                    else:
                        time.sleep(cons.PAUSE_TIME)  # Pause to avoid immediate clicks.
                        starting_time = time.monotonic()  # Reset starting_time.

        except pyautogui.FailSafeException:
            self._fail_safe_exit()

    def _stop_clicking(self) -> bool:
        """Prompts the user whether they want stop the application.

        Returns:
            True if user wants to quit the clicker; False otherwise.
        """
        return pyautogui.confirm(cons.STOP_MSG) == cons.STOP_CLICKING  # type: ignore

    def _fail_safe_exit(self) -> None:
        """Exits the program when mouse is moved to a corner of the screen.

        Plays a sound and prints a message before exiting.
        """
        try:
            playsound(self.sound_path)
        except playsound3.PlaysoundException as err:
            print(f"Sound failed to play ({err}).")
        print("\nMouse moved to a corner. Exiting program.")
        sys.exit(0)


if __name__ == "__main__":
    auto_clicker = AutoClicker()

    try:
        auto_clicker.start_clicker()
        auto_clicker.run_clicker()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
