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
import os

from args import Args
from initial_trees import InitialTrees
from print import Print
from refine_trees import RefineTrees
from log import LOG
from tnt import TNT_input

class Physt:
    def __init__(self) -> None:
        self.args = Args()

    def execute(self):
        os.system(f'mkdir {self.args.TIMESTAMP}')
        if self.args.VERBOSE is True:
            LOG.info('Starting in debug mode')

        Print(self.args)

        program_start = time.time()

        InitialTrees(self.args)

        RefineTrees(self.args)

        program_end = time.time()

        runtime = program_end - program_start
        Print.PrintRuntime(runtime)

        os.system(f'mv physt.log parsimony.treefile {self.args.MSA_INPUT_PATH}.* {self.args.TIMESTAMP}')
        os.system(f'rm tree.* initial_trees*')

        if self.args.MP_SOFTWARE == 'tnt':
            tnt_input = TNT_input(self.args.MSA_INPUT_PATH)
            os.system(f'rm {tnt_input}')
            os.system(f'mv tnt.log {self.args.TIMESTAMP}')
            
        if self.args.VERBOSE is True:
            LOG.info('Run completed')
