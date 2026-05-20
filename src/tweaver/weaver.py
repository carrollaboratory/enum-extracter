import logging
import sys
from argparse import ArgumentParser  # , FileType
from . import init_logging

def exec(args: list[str] | None = None):
    parser = ArgumentParser(
        prog="term-weaver",
        description="""Materializing Enumerations since 2026""",
    )
    parser.add_argument(
        "-log",
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Logging level tolerated (default is INFO)",
    )

    args = parser.parse_args(args)
    # Initialize the logger with whatever the user requested
    init_logging(args.log_level)

    logging.info(f"You have chose to use: {args}")
    logging.warn(f"Hello")
    logging.error("world")
    logging.debug("Goodbye")
