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

import argparse
from datetime import datetime
from multiprocessing import cpu_count
from config import Config

class Args:
    def __init__(self) -> None:
        self.GetArgs()

    def GetArgs(self) -> None:
        PARSER = argparse.ArgumentParser()
        PARSER.add_argument('--msa', type=str, help='input MSA in Phylip/Fasta/Nexus/Clustal format', required=True)
        PARSER.add_argument('--init-trees', type=int, help='the number of initial trees generated', default=100, required=False)
        PARSER.add_argument('--mp-trees', type=int, help='number of MP trees passed to ML software', default=5, required=False)
        PARSER.add_argument('--init-software', type=str, help='software used to generate initial trees', default='mpboot', required=False)
        PARSER.add_argument('--ml-software', type=str, help='software used to generate ML trees', default='iqtree', required=False)
        PARSER.add_argument('--parallel', type=int, help='number of cores to be used', default=1, required=False)
        PARSER.add_argument('--max-parallel', type=bool, help='run PHYST using maximum resources', action=argparse.BooleanOptionalAction, default=False)
        PARSER.add_argument('--iqtree-options', type=str, help='give iq-tree any user specified options', default='', required=False)
        PARSER.add_argument('--verbose', type=bool, help='turn on verbose mode (debug logs)', default=False, action=argparse.BooleanOptionalAction, required=False)
        PARSER.add_argument('--config', type=str, help='path to config file from root directory', default='config/config.yaml', required=False)
        PARSER.add_argument('--tnt-level', type=int, choices=range(11), help='level of TNT search. Use 0-2 for easy datasets, 2-5 for medium, >5 for difficult.', default=1, required=False)

        args = vars(PARSER.parse_args())
        self.MSA_INPUT_PATH = args['msa']
        self.NUM_INIT_TREES = args['init_trees']
        self.NUM_MP_TREES = args['mp_trees']
        self.MP_SOFTWARE = args['init_software']
        self.ML_SOFTWARE = args['ml_software']
        self.TIMESTAMP = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
        self.IQ_TREE_OPTIONS = args['iqtree_options']
        self.VERBOSE = args['verbose']
        self.CONFIG = Config(args['config']).config
        self.TNT_LEVEL = args['tnt_level']
        self.TNT_HITS = (1+args['tnt_level'])//2
        if self.TNT_HITS == 0:
            self.TNT_HITS == 1

        if args['max_parallel'] is True:
            self.HARDWARE = cpu_count()
        else:
            self.HARDWARE = args['parallel']

        if args['init_software'] == 'lvb':
            self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = " -o tree.",".treefile"
        elif args['init_software'] == 'tnt':
            self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = "tree.",".treefile"
        else: self.MP_OUT_PREFIX, self.MP_OUT_SUFFIX = " -pre tree.",""
            