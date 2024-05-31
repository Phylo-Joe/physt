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

from log import LOG

def IqtreeEvaluateTreesCommand(msa_path: str, cores: int) -> str:
    iqtree_path = "iqtree2 "
    pass_msa = "-s " + msa_path
    pass_treefile = " -z initial_trees.treefile"
    no_search = " -n 0"
    parallel = " -nt " + str(cores)

    evaulate_tree_command = iqtree_path + pass_msa + pass_treefile + no_search + parallel
    evaulate_tree_command = evaulate_tree_command + " > /dev/null 2>&1"

    return evaulate_tree_command

def IqtreeLikelihoodAnalysis(msa_path: str, cores: int, iqtree_options: str) -> str:
    likelihood_command = ""

    iqtree_path = "iqtree2 "
    pass_msa = "-s " + msa_path
    pass_treefile = " -t initial_trees_best.treefile"
    parallel = " -nt " + str(cores)
    user_options = " " + iqtree_options

    likelihood_command = iqtree_path + pass_msa + pass_treefile + parallel + user_options       
    likelihood_command = likelihood_command + "-redo > /dev/null 2>&1"

    LOG.info(f'{likelihood_command}')

    return likelihood_command
