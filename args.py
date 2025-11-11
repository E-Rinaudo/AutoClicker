""""""

import argparse
import constants as cons
from playsound3 import playsound3


def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Simple auto clicker.")
    parser.add_argument(
        "--pause-every-10",
        action="store_true",
        help="Every 10 seconds, stop and ask whether to keep or stop clicking.",
    )
    parser.add_argument(
        "--sound-on-exit",
        metavar="PATH",
        type=str,
        default=cons.SOUND_PATH,
        help="Path to a short sound file to play when the clicker stops if the PyAutoGui fail-safe feature is triggered. Defaults to a short ping sound.",
    )

    args = parser.parse_args()

    # Only expand ~ if the user actually provided a path
    # Check if it's different from the default.
    if args.sound_on_exit != cons.SOUND_PATH:
        import pathlib
        args.sound_on_exit = str(pathlib.Path(args.sound_on_exit).expanduser())
    return args
 


