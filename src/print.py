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

import time

from args import Args
from log import LOG

# pylint: disable=too-many-instance-attributes


class Print:
    def __init__(self, Args: Args):
        self.PrintBanner()
        self._physt_version = Args.CONFIG["physt"]["version"]
        self._release_date = Args.CONFIG["physt"]["releaseDate"]
        self._release_year = Args.CONFIG["physt"]["releaseYear"]
        self._initial_software = Args.MP_SOFTWARE
        self._msa_path = Args.MSA_INPUT_PATH
        self._number_initial_trees = Args.NUM_INIT_TREES
        self._number_mp_trees = Args.NUM_MP_TREES
        self._refinement_software = Args.ML_SOFTWARE
        self._timestamp = Args.TIMESTAMP
        self._cores = Args.HARDWARE
        self.PrintStartup()

    def PrintBanner(self) -> None:
        print("")
        LOG.info("######  #     # #       #  #####  ####### ")
        LOG.info("#     # #     #  #     #  #     #    #    ")
        LOG.info("#     # #     #   #   #   #          #    ")
        LOG.info("######  #######    # #     #####     #    ")
        LOG.info("#       #     #     #           #    #    ")
        LOG.info("#       #     #     #     #     #    #    ")
        LOG.info("#       #     #     #      #####     #    ")
        print("")

    def PrintStartup(self) -> None:
        self.PrintHeader()
        self.PrintSoftwareConfig()

    def PrintHeader(self) -> None:
        LOG.info(
            "PHYST (v%s, %s %s)",
            self._physt_version,
            self._release_date,
            self._release_year,
        )
        LOG.info("Developed by Joe,")
        LOG.info("Barker Lab,")
        LOG.info("School of Biological Science")
        LOG.info("University")
        LOG.info("Copyright (c) %s Joe", self._release_year)

    def PrintSoftwareConfig(self) -> None:
        print("")
        LOG.info("PHYST configuration:")
        LOG.info("  Initial Trees")
        LOG.info("    Software: %s", self._initial_software)
        LOG.info("    MSA: %s", self._msa_path)
        LOG.info("    Trees evaluated: %d", self._number_initial_trees)
        LOG.info("    Trees retained: %d", self._number_mp_trees)
        print("")
        LOG.info("  Likelihood Analysis")
        LOG.info("    Software: %s", self._refinement_software)
        print("")
        LOG.info("  Resources")
        LOG.info("    Cores: %d", self._cores)
        print("")
        LOG.info("Start time: %s", self._timestamp)
        print("")
        LOG.info(
            "MPBoot provided by Hoang, et al., 2018; "
            "https://doi.org/10.1186/s12862-018-1131-3"
        )
        LOG.info(
            "IQ-Tree provided by Minh, et al., 2020; "
            "https://doi.org/10.1093/molbev/msaa015"
        )
        print("")

    @staticmethod
    def PrintDictionary(dictionary: dict) -> None:
        for key, value in dictionary.items():
            LOG.info("%s : %s", key, value)

    @staticmethod
    def PrintRuntime(program_runtime: float) -> None:
        LOG.info(
            "Wall-clock time : %s",
            time.strftime("%H:%M:%S", time.gmtime(program_runtime)),
        )
