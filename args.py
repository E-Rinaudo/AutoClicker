# region Module Description And Imports.
"""Module for parsing command-line arguments for the auto clicker."""

import argparse
from pathlib import Path

import constants as cons

# Aliases for the Enums of constants.py.
ArgsText = cons.ArgsText
SoundCons = cons.SoundCons

# endregion

# region AutoClicker Command Line Arguments.


class ClickerArgs:  # pylint: disable=too-few-public-methods
    """Class to hold command-line arguments.

    Attributes:
        parser (argparse.ArgumentParser): The argument parser instance.
        args (argparse.Namespace): The parsed arguments.
    """

    parser: argparse.ArgumentParser
    args: argparse.Namespace

    def __init__(self) -> None:
        """Initializes the argument parser."""
        self.parser = argparse.ArgumentParser(description=ArgsText.ARGS_DESCRIPTION)
        self.args = argparse.Namespace()

    def parse_args(self) -> argparse.Namespace:
        """Parses command-line arguments.

        Returns:
            The parsed arguments.
        """
        self._add_pause_argument()
        self._add_sound_argument()
        self.args = self.parser.parse_args()
        self._process_sound_path()
        return self.args

    def _add_pause_argument(self) -> None:
        """Adds the pause-every-10 seconds argument to the parser."""
        self.parser.add_argument(
            ArgsText.PAUSE_ARG_NAME,
            action="store_true",
            help=ArgsText.PAUSE_ARG_HELP,
        )

    def _add_sound_argument(self) -> None:
        """Adds the sound-on-exit argument to the parser."""
        self.parser.add_argument(
            ArgsText.SOUND_ARG_NAME,
            metavar="PATH",
            type=str,
            default=SoundCons.SOUND_PATH,
            help=ArgsText.SOUND_ARG_HELP,
        )

    def _process_sound_path(self) -> None:
        """Expands user directory and validates the provided sound file path.

        If the argument is the default sound path, no changes are made.
        """
        sound_path = self.args.sound_on_exit

        if sound_path == SoundCons.SOUND_PATH:
            return  # Skip validation if using the default path

        expanded_path = Path(sound_path).expanduser()

        # Validate path.
        if not expanded_path.exists():
            print(
                SoundCons.WRONG_SOUND_PATH.format(
                    expanded_path=expanded_path, default_path=SoundCons.SOUND_PATH
                )
            )
            self.args.sound_on_exit = SoundCons.SOUND_PATH
        else:
            self.args.sound_on_exit = str(expanded_path)


# endregion.
