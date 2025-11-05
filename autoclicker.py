#!/usr/bin/env python3

"""Simple personal auto clicker."""

import sys
import time

import pyautogui  # type: ignore

import constants as cons


class Clicker:
    """A simple auto clicker that clicks at the current mouse position."""

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
        print("Clicker not started. Restart the program to run again.")
        sys.exit(0)

    def run_clicker(self) -> None:
        """Runs the clicker application.

        Clicks repeatedly every 0.2 seconds at current cursor position.
        Stops every 10 seconds to check whether the user wants to
        continue or stop clicking.
        """
        print("\nClicking...")
        starting_time = time.monotonic()

        try:
            while True:
                pyautogui.click(interval=cons.CLICKS_INTERVAL)

                now = time.monotonic()
                if now - starting_time >= cons.TIME_ELAPSED:
                    if self._stop_clicking():
                        print("Program stopped by user. Exiting...")
                        sys.exit(0)
                    else:
                        time.sleep(cons.PAUSE_TIME)  # Pause to avoid immediate clicks.
                        starting_time = time.monotonic()  # Reset starting_time.

        except pyautogui.FailSafeException:
            print("\nMouse moved to a corner. Exiting program.")
            sys.exit(0)

    def _stop_clicking(self) -> bool:
        """Prompts the user whether they want stop the app.

        Returns:
            True if user wants to quit the clicker; False otherwise.
        """
        return pyautogui.confirm(cons.STOP_MSG) == cons.STOP_CLICKING  # type: ignore


if __name__ == "__main__":
    auto_clicker = Clicker()

    try:
        auto_clicker.start_clicker()
        auto_clicker.run_clicker()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        sys.exit(0)
