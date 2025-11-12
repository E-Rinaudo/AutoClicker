# region Module Description And Imports.
"""Module for parsing command-line arguments for the AutoClicker."""

import argparse
import logging
from pathlib import Path

from constants import ArgsText, LogMsgs, SoundCons

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

    def get_args(self) -> argparse.Namespace:
        """Parses and processes command-line arguments for the AutoClicker.

        Adds all relevant arguments to the parser and performs any necessary
        post-processing (validating and expanding the sound file path).

        Returns:
            The parsed and processed command-line arguments.
        """
        self._add_pause_argument()
        self._add_sound_argument()
        self.args = self.parser.parse_args()
        self._handle_sound_path()
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
            default=SoundCons.DEFAULT_SOUND_PATH,
            help=ArgsText.SOUND_ARG_HELP,
        )

    def _handle_sound_path(self) -> None:
        """Checks if the sound path is default and validate if custom.

        If the argument is the default sound path, no changes are made.
        """
        sound_path = self.args.sound_on_exit

        match sound_path:
            case SoundCons.DEFAULT_SOUND_PATH:
                # Skip validation if using the default path.
                logging.info(LogMsgs.USING_DEFAULT_SOUND)
            case _:
                self._validate_custom_path(sound_path)

    def _validate_custom_path(self, custom_path: str) -> None:
        """Validates a custom sound path, falling back to default if invalid.

        Args:
            custom_path: The custom sound file path to validate.
        """
        expanded_path = self._expand_path(custom_path)

        if expanded_path is None:
            print(
                SoundCons.INVALID_SOUND_PATH.format(
                    custom_path=custom_path, default_path=SoundCons.DEFAULT_SOUND_PATH
                ),
                end="",
            )
            self._set_path(
                SoundCons.DEFAULT_SOUND_PATH, LogMsgs.INVALID_SOUND_PATH.format(path=custom_path)
            )
        else:
            self._set_path(expanded_path, LogMsgs.CUSTOM_SOUND_SET.format(path=expanded_path))

    def _expand_path(self, custom_path: str) -> str | None:
        """Expands a user-provided path.

        Args:
            custom_path: The sound path string provided by the user.

        Returns:
            Custom path if valid, None if expansion fails or path doesn't exist.
        """
        try:
            sound_path = Path(custom_path).expanduser()
        except RuntimeError:
            logging.error(LogMsgs.RUNTIME_ERR, custom_path)
            return None

        if not sound_path.exists():
            logging.error(LogMsgs.SOUND_NOT_FOUND_ERR, sound_path)
            return None

        return str(sound_path)

    def _set_path(self, sound_path: str, log_msg: str) -> None:
        """Sets the sound path after validation.

        Args:
            sound_path: The validated sound file path to set.
            log_msg: The log message to record.
        """
        self.args.sound_on_exit = sound_path
        logging.info(log_msg)


# endregion.
