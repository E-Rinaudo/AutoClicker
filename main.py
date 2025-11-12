# region Module Description And Imports.
"""Main module to run the AutoClicker application."""

import logging_file
from autoclicker import AutoClicker
from constants import ExitMsgs, LogMsgs

# Set up the logging configuration.
logging_file.logging_configuration()
logging_file.disable_logging()

# endregion.

if __name__ == "__main__":
    auto_clicker = AutoClicker()

    try:
        auto_clicker.start_clicker()
        auto_clicker.run_clicker()
    except KeyboardInterrupt:
        auto_clicker.print_and_exit(ExitMsgs.CTRLC_QUIT, LogMsgs.CTRLC_QUIT_LOG)
