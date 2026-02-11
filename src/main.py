#!/usr/bin/env python3
#
# Copyright 2024 The PHYST Authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import traceback

from log import LOG, Log
from physt import Physt


# pylint: disable=broad-exception-caught
def main() -> None:
    Log()
    try:
        physt = Physt()
        physt.execute()

    except Exception as err:
        LOG.critical("%s: %s", type(err).__name__, err)
        traceback.print_tb(err.__traceback__)
        sys.exit(1)


if __name__ == "__main__":
    main()
