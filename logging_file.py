# region Module Description And Imports.
"""Creates the logging configuration for the Thermo Tracker app."""

import logging

from constants import LOG_FILE

# endregion.


# region Logging Configurations.


def logging_configuration() -> None:
    """Configures the logging settings for the clicker."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def disable_logging() -> None:
    """Disables logging by setting the level to INFO."""
    logging.disable(logging.INFO)


# endregion.
