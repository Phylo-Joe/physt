import logging
import sys
from typing import Optional

LOGGER_NAME = "physt"
LOG = logging.getLogger(LOGGER_NAME)


# pylint: disable=too-few-public-methods
class Log:
    logger: Optional[logging.Logger] = None

    def __init__(self) -> None:
        if Log.logger is not None:
            return

        formatter = logging.Formatter(
            fmt="%(message)s",
            datefmt="%H:%M:%S",
        )

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)

        logger = logging.getLogger(LOGGER_NAME)
        logger.addHandler(stream_handler)
        logger.setLevel(logging.DEBUG)

        logging.basicConfig(
            filename="physt.log",
            filemode="w",
            level=logging.DEBUG,
            format="%(message)s",
            datefmt="%H:%M:%S",
        )

        Log.logger = logger
