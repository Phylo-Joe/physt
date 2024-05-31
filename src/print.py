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
from log import LOG

class Print:
    def __init__(self, Args):
        self.PrintBanner()
        self._physt_version = Args.CONFIG['physt']['version']
        self._release_date = Args.CONFIG['physt']['releaseDate']
        self._release_year = Args.CONFIG['physt']['releaseYear']
        self._operating_system = Args.CONFIG['operatingSystem']['macos']
        self._initial_software = Args.MP_SOFTWARE
        self._msa_path = Args.MSA_INPUT_PATH
        self._number_initial_trees = Args.NUM_INIT_TREES
        self._number_mp_trees = Args.NUM_MP_TREES
        self._refinement_software = Args.ML_SOFTWARE
        self._timestamp = Args.TIMESTAMP
        self._cores = Args.HARDWARE
        self.PrintStartup()

    def PrintBanner(self) -> None:
        print('')
        LOG.info('######  #     # #       #  #####  ####### ')
        LOG.info('#     # #     #  #     #  #     #    #    ')
        LOG.info('#     # #     #   #   #   #          #    ')
        LOG.info('######  #######    # #     #####     #    ')
        LOG.info('#       #     #     #           #    #    ')
        LOG.info('#       #     #     #     #     #    #    ')
        LOG.info('#       #     #     #      #####     #    ')
        print('')

    def PrintStartup(self) -> None:
        self.PrintHeader()
        self.PrintSoftwareConfig()

    def PrintHeader(self) -> None:
        LOG.info(f'PHYST (v{self._physt_version}, {self._release_date} {self._release_year}) Built for {self._operating_system}')
        LOG.info('Developed by Joseph Guscott & David Bunn')
        LOG.info('Barker Lab,')
        LOG.info('School of Biological Science')
        LOG.info('University of Edinburgh')
        LOG.info(f'Copyright (c) {self._release_year} Joseph Guscott')

    def PrintSoftwareConfig(self) -> None:
        print('')
        LOG.info('PHYST configuration:')
        LOG.info('  Initial Trees')
        LOG.info(f'    Software: {self._initial_software}')
        LOG.info(f'    MSA: {self._msa_path}')
        LOG.info(f'    Trees evaluated: {self._number_initial_trees}')
        LOG.info(f'    Trees retained: {self._number_mp_trees}')
        print('')
        LOG.info('  Likelihood Analysis')
        LOG.info(f'    Software: {self._refinement_software}')
        print('')
        LOG.info('  Resources')
        LOG.info(f'    Cores: {self._cores}')
        print('')
        LOG.info(f'Start time: {self._timestamp}')
        print('')
        LOG.info('MPBoot provided by Hoang, et al., 2018; https://doi.org/10.1186/s12862-018-1131-3')
        LOG.info('LVB provided by Barker, 2004; https://doi.org/10.1093/bioinformatics/btg402')
        LOG.info('IQ-Tree provided by Minh, et al., 2020; https://doi.org/10.1093/molbev/msaa015')
        print('')

    @staticmethod
    def PrintDictionary(dictionary: dict) -> None:
        for key in dictionary:
            LOG.info (f'{key} : {dictionary[key]}')

    @staticmethod
    def PrintRuntime(program_runtime) -> None:
        LOG.info(f"Wall-clock time : {time.strftime('%H:%M:%S', time.gmtime(program_runtime))}") 
