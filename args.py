"""Module for parsing command-line arguments for the auto clicker."""

import argparse
from pathlib import Path

import constants as cons


class ClickerArgs:
    """Class to hold command-line arguments.

    Attributes:
        parser (argparse.ArgumentParser): The argument parser instance.
        args (argparse.Namespace):
    """

    parser: argparse.ArgumentParser
    args: argparse.Namespace

    def __init__(self) -> None:
        """Initializes the argument parser."""
        self.parser = argparse.ArgumentParser(description="Simple auto clicker.")
        self.args = argparse.Namespace()

    def parse_args(self) -> argparse.Namespace:
        """Parses command-line arguments."""
        self._add_pause_argument()
        self._add_sound_argument()
        self.args = self.parser.parse_args()
        self._clean_sound_path()
        return self.args

    def _add_pause_argument(self) -> None:
        """Adds the pause every 10 seconds argument to the parser."""
        self.parser.add_argument(
            "--pause-every-10",
            action="store_true",
            help="If set, the clicker will pause every 10 seconds to check if the user wants to continue or stop clicking.",
        )

    def _add_sound_argument(self) -> None:
        """Adds the sound on exit argument to the parser."""
        self.parser.add_argument(
            "--sound-on-exit",
            metavar="PATH",
            type=str,
            default=cons.SOUND_PATH,
            help="Path to a sound file to play when the program stops if the user triggered PyAutoGUI's failsafe feature. Defaults to a ping sound.",
        )

    def _process_sound_path(self) -> None:
        """Expands user directory and validates the provided sound file path.

        If the argument is the default sound path, no changes are made.
        """
        sound_path = self.args.sound_on_exit

        if sound_path == cons.SOUND_PATH:
            return  # Skip validation if using the default path

        expanded_path = Path(sound_path).expanduser()

        # Validate path.
        if not expanded_path.exists():
            print(
                f"\n Warning: Sound file not found at '{expanded_path}'. "
                f"Falling back to default sound.\n"
            )
            self.args.sound_on_exit = cons.SOUND_PATH
        else:
            self.args.sound_on_exit = str(expanded_path)
