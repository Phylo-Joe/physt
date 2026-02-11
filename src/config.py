import sys

import yaml

from log import LOG


# pylint: disable=too-few-public-methods
class Config:
    def __init__(self, config_path: str) -> None:
        try:
            with open(config_path, encoding="utf-8") as config_file:
                self.config = yaml.safe_load(config_file)
        except IOError as err:
            LOG.critical("%s: %s", type(err).__name__, err)
            sys.exit(1)
